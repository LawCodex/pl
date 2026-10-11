#!/usr/bin/env python3
"""OCR fallback for acts whose only available text is a scanned PDF without a text layer.

For every act whose <raw>/text/<y>/<p>.choice.json has kind=null (see fetch.py), the
scanned PDF (I, else O, else T) is rasterised with pdftoppm (300 dpi, greyscale) and
read with Tesseract using the Polish model (pol.traineddata, from
https://github.com/tesseract-ocr/tessdata, expected in <raw>/tessdata/).  Page texts are
saved to <raw>/ocr/<y>/<p>.json and the choice file is updated to kind="ocr".

Requires the poppler `pdftoppm` and `tesseract` binaries.
Usage: ocr.py [--raw DIR] [--workers N]
"""
import argparse
import concurrent.futures as cf
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

from fetch import API, DEFAULT_RAW, load_meta


def ocr_pdf(pdf, tessdata, workdir):
    subprocess.run(["pdftoppm", "-r", "300", "-gray", "-png", pdf, os.path.join(workdir, "p")],
                   check=True, capture_output=True)
    pages = []
    for img in sorted(glob.glob(os.path.join(workdir, "p-*.png")),
                      key=lambda f: int(f.rsplit("-", 1)[1].split(".")[0])):
        r = subprocess.run(["tesseract", img, "-", "-l", "pol", "--tessdata-dir", tessdata, "--psm", "3"],
                           capture_output=True, text=True, env={**os.environ, "OMP_THREAD_LIMIT": "1"})
        pages.append(r.stdout)
        os.remove(img)
    return pages


def one(raw, choice_file):
    with open(choice_file, encoding="utf-8") as f:
        ch = json.load(f)
    if ch.get("kind"):
        return None
    base = choice_file[: -len(".choice.json")]
    y, p = base.split(os.sep)[-2:]
    eli = f"DU/{y}/{p}"
    meta = load_meta(raw, eli)
    names = {t["type"]: t["fileName"] for t in (meta or {}).get("texts", [])}
    for label in ("I", "O", "T"):
        pdf = f"{base}.{label}.pdf"
        if os.path.exists(pdf) and label in names:
            break
    else:
        return f"{eli}: no pdf"
    out = os.path.join(raw, "ocr", y, f"{p}.json")
    if not os.path.exists(out):
        work = tempfile.mkdtemp(dir=os.path.join(raw, "ocr-tmp"))
        try:
            pages = ocr_pdf(pdf, os.path.join(raw, "tessdata"), work)
        finally:
            shutil.rmtree(work, ignore_errors=True)
        if sum(len(x.strip()) for x in pages) < 50:
            return f"{eli}: OCR produced no text"
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(pages, f, ensure_ascii=False)
    ch = {"source_eli": eli, "kind": "ocr", "label": label,
          "url": f"{API}/acts/{eli}/text/{label}/{names[label]}", "path": os.path.relpath(out, raw)}
    with open(choice_file, "w", encoding="utf-8") as f:
        json.dump(ch, f, ensure_ascii=False)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    os.makedirs(os.path.join(a.raw, "ocr-tmp"), exist_ok=True)
    todo = []
    for c in glob.glob(os.path.join(a.raw, "text", "*", "*.choice.json")):
        with open(c, encoding="utf-8") as f:
            if not json.load(f).get("kind"):
                todo.append(c)
    print(f"ocr: {len(todo)} acts", flush=True)
    with cf.ProcessPoolExecutor(a.workers) as ex:
        for n, err in enumerate(ex.map(one, [a.raw] * len(todo), todo), 1):
            if err:
                print("  " + err, file=sys.stderr, flush=True)
            if n % 100 == 0:
                print(f"ocr: {n}/{len(todo)}", flush=True)
    print("ocr done", flush=True)


if __name__ == "__main__":
    main()
