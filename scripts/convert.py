#!/usr/bin/env python3
"""Convert the cached Sejm ELI texts (HTML or PDF) into LawCodex Markdown.

Usage: convert.py [--raw DIR] [--out DIR] [--types ...] [--only ELI ...] [--retrieved YYYY-MM-DD]

Reads <raw>/search, <raw>/meta and <raw>/text (produced by fetch.py) and writes
  konstytucja/du-1997-483-konstytucja-rzeczypospolitej-polskiej.md
  kodeksy/du-<year>-<pos>-<slug>.md
  ustawy/<year>/du-<year>-<pos>-<slug>.md
  dekrety/<year>/...
  rozporzadzenia/<year>/[<shard>/]du-<year>-<pos>-<slug>.md
A manifest of everything written (and every act without usable text) goes to
<raw>/manifest.json, used by readme.py.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import sys
import unicodedata

from select_acts import selected_items, category
from fetch import load_meta, DEFAULT_RAW, choice_path
import html2md
import pdf2md

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.normpath(os.path.join(HERE, ".."))
MAX_PER_DIR = 900

TRANS = str.maketrans({"ł": "l", "Ł": "L", "–": "-", "—": "-"})


def slugify(s, maxlen=80):
    s = s.translate(TRANS)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s


DATE_RE = re.compile(r"\bz dnia \d{1,2}\s+\S+\s+\d{4}\s*r\.?\s*", re.I)


def short_title(title):
    """Part of the title after the 'z dnia ... r.' date (e.g. 'Kodeks cywilny', 'o podatku ...')."""
    m = DATE_RE.search(title)
    t = title[m.end():] if m else title
    t = re.sub(r"^[\s\-–—]+", "", t).strip().rstrip(".")
    return t or title


def is_code(title):
    st = short_title(title)
    return bool(re.match(r"^Kodeks\b", st)) and title.lower().startswith("ustawa")


def yaml_str(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def front_matter(fields):
    lines = ["---"]
    for k, v in fields.items():
        if v is None or v == "":
            continue
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            lines.append(f"{k}: {v}")
        elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(v)) or re.fullmatch(r"[a-z_]+", str(v)):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {yaml_str(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def target_dir(cat, meta, title):
    y = str(meta["year"])
    if cat == "konstytucja":
        return "konstytucja"
    if cat == "ustawa" and is_code(title):
        return "kodeksy"
    base = {"ustawa": "ustawy", "dekret": "dekrety", "rozporzadzenie": "rozporzadzenia"}[cat]
    return os.path.join(base, y)


def doc_type(cat, title):
    if cat == "konstytucja":
        return "constitution"
    if cat == "ustawa":
        return "code" if is_code(title) else "act"
    return {"dekret": "decree", "rozporzadzenie": "regulation"}[cat]


def build(raw, it, retrieved):
    eli = it["ELI"]
    meta = load_meta(raw, eli)
    if meta is None:
        return {"eli": eli, "error": "no metadata"}
    cp = choice_path(raw, eli)
    if not os.path.exists(cp):
        return {"eli": eli, "error": "text not fetched"}
    with open(cp, encoding="utf-8") as f:
        choice = json.load(f)
    cat = category(it)
    title = re.sub(r"\s+", " ", meta["title"]).strip().rstrip(".") if meta.get("title") else eli
    info = {"eli": eli, "cat": cat, "title": title, "year": meta["year"], "pos": meta["pos"],
            "status": meta.get("status")}
    if not choice.get("kind"):
        info["error"] = "no usable text (scanned PDF without text layer, OCR failed)"
        return info
    src_eli = choice["source_eli"]
    path = os.path.join(raw, choice["path"])
    is_tj = src_eli != eli
    try:
        if choice["kind"] == "html":
            with open(path, "rb") as f:
                body = html2md.convert(f.read(), skip_first_part=is_tj)
        elif choice["kind"] == "ocr":
            with open(path, encoding="utf-8") as f:
                pages = [re.sub(r"(?m)(^|\s|„)\$ ?(?=\d)", r"\1§ ", pg) for pg in json.load(f)]
            # OCR reads "§" as "8" at the start of a paragraph: "8 2. 1. Funkcjonariuszowi"
            pages = [re.sub(r"(?m)^(„?)8 (\d+[a-z]?\. )", r"\1§ \2", pg) for pg in pages]
            body = pdf2md.convert(None, tj=is_tj, pages=pages, ocr=True, pos=int(src_eli.split("/")[2]))
        else:
            body = pdf2md.convert(path, tj=is_tj, pos=int(src_eli.split("/")[2]))
    except Exception as e:  # noqa: BLE001
        info["error"] = f"conversion failed: {e!r}"
        return info
    if len(body.strip()) < 20:
        info["error"] = "empty text after conversion"
        return info

    src_meta = load_meta(raw, src_eli) if is_tj else meta
    if cat == "konstytucja":
        h1 = "Konstytucja Rzeczypospolitej Polskiej"
    else:
        h1 = title
    if is_tj:
        version = "tekst jednolity"
        consolidated = src_meta.get("legalStatusDate") or src_meta.get("announcementDate")
    elif choice["label"] == "U":
        version = "tekst ujednolicony (Kancelaria Sejmu)"
        consolidated = None
    else:
        version = "tekst ogłoszony (original)"
        consolidated = None
    fm = {
        "title": h1 if cat == "konstytucja" else title,
        "identifier": eli,
        "official_citation": meta.get("displayAddress"),
        "type": doc_type(cat, title),
        "jurisdiction": "pl",
        "language": "pl",
        "date": meta.get("announcementDate"),
        "promulgated": meta.get("promulgation"),
        "entry_into_force": meta.get("entryIntoForce"),
        "last_amended": consolidated,
        "status": "in_force",
        "official_status": meta.get("status"),
        "text_version": version,
        "consolidated_text": src_meta.get("displayAddress") if is_tj else None,
        "consolidated_text_eli": src_eli if is_tj else None,
        "text_format": {"html": "html", "ocr": "pdf scan (OCR by LawCodex, unverified)"}.get(
            choice["kind"], "pdf (text extracted)"),
        "source": f"https://api.sejm.gov.pl/eli/acts/{eli}",
        "source_text": choice["url"],
        "isap": f"https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id={meta['address']}" if meta.get("address") else None,
        "retrieved": retrieved,
    }
    md = front_matter(fm) + f"\n# {h1}\n\n" + body.strip() + "\n"
    info.update({"dir": target_dir(cat, meta, title), "md": md, "kind": choice["kind"],
                 "label": choice["label"], "tj": is_tj})
    return info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--types", default="all")
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--retrieved", default=dt.date.today().isoformat())
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    types = None if a.types == "all" else set(a.types.split(","))
    items = selected_items(a.raw, types)
    if a.only:
        items = [i for i in items if i["ELI"] in set(a.only)]

    results = []
    with cf.ProcessPoolExecutor(a.workers) as ex:
        futs = [ex.submit(build, a.raw, it, a.retrieved) for it in items]
        for n, f in enumerate(cf.as_completed(futs), 1):
            results.append(f.result())
            if n % 1000 == 0:
                print(f"converted {n}/{len(items)}", flush=True)

    # shard big directories
    by_dir = {}
    for r in results:
        if "md" in r:
            by_dir.setdefault(r["dir"], []).append(r)
    manifest = []
    for d, rs in by_dir.items():
        rs.sort(key=lambda r: r["pos"])
        shard = len(rs) > MAX_PER_DIR
        for r in rs:
            sub = d
            if shard:
                lo = r["pos"] // 500 * 500
                sub = os.path.join(d, f"poz-{lo:04d}-{lo + 499:04d}")
            slug = "konstytucja-rzeczypospolitej-polskiej" if r["cat"] == "konstytucja" else slugify(short_title(r["title"]))
            name = f"du-{r['year']}-{r['pos']}-{slug}".rstrip("-") + ".md"
            rel = os.path.join(sub, name)
            p = os.path.join(a.out, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(r["md"])
            manifest.append({k: v for k, v in r.items() if k != "md"} | {"file": rel})
    for r in results:
        if "md" not in r:
            manifest.append(r)
            print(f"SKIP {r['eli']}: {r.get('error')}", file=sys.stderr)
    mp = os.path.join(a.raw, "manifest.json" if not a.only else "manifest-only.json")
    with open(mp, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=0)
    ok = sum(1 for m in manifest if "file" in m)
    print(f"written {ok}, skipped {len(manifest) - ok}")


if __name__ == "__main__":
    main()
