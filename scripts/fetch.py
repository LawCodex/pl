#!/usr/bin/env python3
"""Fetch Polish legislation from the Sejm ELI API (Dziennik Ustaw) into a raw cache.

Phases (run in order; every phase is cached under --raw, default ../../_raw/pl):

  search  ELI search for every act flagged in force, per type -> search/<type>.json
  meta    full metadata for every selected act in force      -> meta/<year>/<pos>.json
          plus the metadata of its latest "tekst jednolity"  (same layout)
  texts   the text to convert (see text_candidates)          -> text/<year>/<pos>.(html|<T>.pdf)
          and the choice made                                -> text/<year>/<pos>.choice.json

Selection (see select_acts.py): Konstytucja, ustawy, dekrety and rozporządzenia whose
status is in force.  For every act the text used is the one of the most recent
consolidated text announcement ("obwieszczenie ... w sprawie ogłoszenia jednolitego
tekstu", reference "Inf. o tekście jednolitym") when one exists, otherwise the act's
own text (see text_candidates).

Usage: fetch.py [search|meta|texts|all] [--raw DIR] [--refresh] [--types ...]
Politeness: descriptive User-Agent, <= 4 concurrent connections, retries with backoff.
"""
import argparse
import concurrent.futures as cf
import json
import os
import sys
import threading
import time

import requests

from select_acts import selected_items

API = "https://api.sejm.gov.pl/eli"
UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
WORKERS = 4
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RAW = os.path.normpath(os.path.join(HERE, "..", "..", "_raw", "pl"))

_local = threading.local()


def session():
    s = getattr(_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers["User-Agent"] = UA
        _local.s = s
    return s


def get(url, tries=8):
    delay = 2
    for i in range(tries):
        try:
            r = session().get(url, timeout=300)
            if r.status_code == 200:
                return r
            if r.status_code in (404, 403):
                return None
            err = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            err = str(e)
        print(f"  retry {i+1} {url}: {err}", file=sys.stderr, flush=True)
        time.sleep(delay)
        delay = min(delay * 2, 120)
    print(f"  GIVING UP {url}", file=sys.stderr, flush=True)
    return None


def write_atomic(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".part"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)


def phase_search(raw, types, refresh=False):
    items = selected_items(raw, types, refresh=refresh)
    print(f"search: {len(items)} acts selected", flush=True)


def meta_path(raw, eli):
    _, y, p = eli.split("/")
    return os.path.join(raw, "meta", y, f"{p}.json")


def load_meta(raw, eli):
    p = meta_path(raw, eli)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return None


def fetch_meta(raw, eli):
    m = load_meta(raw, eli)
    if m is not None:
        return m
    r = get(f"{API}/acts/{eli}")
    if r is None:
        return None
    write_atomic(meta_path(raw, eli), r.content)
    return r.json()


def eli_key(eli):
    _, y, p = eli.split("/")
    return (int(y), int(p))


def latest_tj(meta):
    """ELI of the most recent consolidated-text announcement for this act, or None."""
    refs = (meta.get("references") or {}).get("Inf. o tekście jednolitym") or []
    elis = [r["id"] for r in refs if r.get("id", "").startswith("DU/")]
    if not elis:
        return None
    return max(elis, key=eli_key)


def run_pool(fn, items, label):
    done = 0
    with cf.ThreadPoolExecutor(WORKERS) as ex:
        for _ in ex.map(fn, items):
            done += 1
            if done % 500 == 0:
                print(f"{label}: {done}/{len(items)}", flush=True)
    print(f"{label}: {done}/{len(items)} done", flush=True)


def phase_meta(raw, types):
    items = selected_items(raw, types)
    print(f"meta: {len(items)} selected acts", flush=True)

    def one(it):
        m = fetch_meta(raw, it["ELI"])
        if m is None:
            return
        tj = latest_tj(m)
        if tj:
            fetch_meta(raw, tj)

    run_pool(one, items, "meta")


def text_candidates(raw, act_meta):
    """Ordered list of (source_meta, kind, label, url, local_path) to try.

    1. latest consolidated text announcement (tekst jednolity): HTML, else official PDF
       (I/O; T = Kancelaria Sejmu copy when the official scan has no text layer);
    2. otherwise the act itself: "tekst ujednolicony" PDF (U, consolidated by Kancelaria
       Sejmu, only exists for amended acts), else HTML, else the published PDF (I/O/T).
    """
    out = []

    def add_pdfs(m, order):
        names = {t["type"]: t["fileName"] for t in (m.get("texts") or [])}
        _, y, p = m["ELI"].split("/")
        seen = set()
        for t in order:
            if t in names and names[t] not in seen:
                seen.add(names[t])
                out.append((m, "pdf", t, f"{API}/acts/{m['ELI']}/text/{t}/{names[t]}",
                            os.path.join(raw, "text", y, f"{p}.{t}.pdf")))

    def add_html(m):
        if m.get("textHTML"):
            _, y, p = m["ELI"].split("/")
            out.append((m, "html", "H", f"{API}/acts/{m['ELI']}/text.html",
                        os.path.join(raw, "text", y, f"{p}.html")))

    tj = latest_tj(act_meta)
    tm = load_meta(raw, tj) if tj else None
    if tm is not None:
        add_html(tm)
        add_pdfs(tm, ("I", "O", "T"))
    add_pdfs(act_meta, ("U",))
    add_html(act_meta)
    add_pdfs(act_meta, ("I", "O", "T"))
    return out


def pdf_has_text(path, pages=3):
    try:
        from pypdf import PdfReader
        r = PdfReader(path)
        txt = "".join((r.pages[i].extract_text() or "") for i in range(min(pages, len(r.pages))))
        return len(txt.strip()) > 50
    except Exception as e:  # noqa: BLE001
        print(f"  bad pdf {path}: {e}", file=sys.stderr)
        return False


def choice_path(raw, eli):
    _, y, p = eli.split("/")
    return os.path.join(raw, "text", y, f"{p}.choice.json")


def phase_texts(raw, types):
    items = selected_items(raw, types)
    todo = [it for it in items if not os.path.exists(choice_path(raw, it["ELI"]))]
    print(f"texts: {len(todo)} acts to resolve", flush=True)

    def one(it):
        m = load_meta(raw, it["ELI"])
        if m is None:
            return
        choice = None
        for src, kind, label, url, path in text_candidates(raw, m):
            if not os.path.exists(path):
                r = get(url)
                if r is None or not r.content:
                    continue
                write_atomic(path, r.content)
            if kind == "html" or pdf_has_text(path):
                choice = {"source_eli": src["ELI"], "kind": kind, "label": label, "url": url,
                          "path": os.path.relpath(path, raw)}
                break
        if choice is None:
            choice = {"source_eli": None, "kind": None}
            print(f"  no usable text for {it['ELI']}", file=sys.stderr, flush=True)
        write_atomic(choice_path(raw, it["ELI"]), json.dumps(choice, ensure_ascii=False).encode())

    run_pool(one, todo, "texts")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phase", nargs="?", default="all", choices=["search", "meta", "texts", "all"])
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--refresh", action="store_true", help="re-run the in-force search")
    ap.add_argument("--types", default="all", help="comma list: konstytucja,ustawa,dekret,rozporzadzenie")
    a = ap.parse_args()
    types = None if a.types == "all" else set(a.types.split(","))
    if a.phase in ("search", "all"):
        phase_search(a.raw, types, a.refresh)
    if a.phase in ("meta", "all"):
        phase_meta(a.raw, types)
    if a.phase in ("texts", "all"):
        phase_texts(a.raw, types)


if __name__ == "__main__":
    main()
