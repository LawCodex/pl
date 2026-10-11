#!/usr/bin/env python3
"""Regenerate README.md from <raw>/manifest.json (written by convert.py)."""
import argparse
import collections
import datetime as dt
import json
import os

from fetch import DEFAULT_RAW

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.normpath(os.path.join(HERE, ".."))

TEMPLATE = """# LawCodex — Poland (Polska)

Polish legislation in force — the Constitution, codes (kodeksy), statutes (ustawy),
decrees with force of statute (dekrety) and regulations (rozporządzenia) published in
*Dziennik Ustaw Rzeczypospolitej Polskiej* — as Markdown, one file per act, in the original
Polish. Texts are the latest consolidated text (*tekst jednolity*) where one has been
announced.

Retrieved: {retrieved}.

## Contents

| Directory | Content | Files |
|---|---|---:|
| `konstytucja/` | Konstytucja Rzeczypospolitej Polskiej (1997) | {konstytucja} |
| `kodeksy/` | Codes (ustawy titled "Kodeks …": cywilny, karny, pracy, spółek handlowych, …) | {kodeksy} |
| `ustawy/<year>/` | Other statutes (ustawy) in force, by year of Dziennik Ustaw | {ustawy} |
| `dekrety/<year>/` | Decrees (dekrety) still in force | {dekrety} |
| `rozporzadzenia/<year>/` | Regulations (rozporządzenia) in force, by year (years with more than 900 files are split into `poz-NNNN-NNNN/` subdirectories) | {rozporzadzenia} |
| **Total** | | **{total}** |

Text basis of the {total} files:

| Text used | Files |
|---|---:|
| Latest *tekst jednolity* (consolidated text announced in Dziennik Ustaw), HTML | {tj_html} |
| Latest *tekst jednolity*, PDF (text layer extracted) | {tj_pdf} |
| *Tekst ujednolicony* (consolidated text prepared by the Kancelaria Sejmu, PDF) — acts amended but never re-announced | {u_pdf} |
| Text as published (act never amended / no consolidation), HTML | {orig_html} |
| Text as published, PDF (text layer extracted) | {orig_pdf} |
| Scanned PDF without text layer — **OCR** by LawCodex (Tesseract, Polish model), unverified | {ocr} |

Each file's front matter says which text was used (`text_version`, `consolidated_text`,
`source_text`, `text_format`) and, for consolidated texts, the date of the legal status
(`last_amended` = *stan prawny na dzień*).

## Not covered / known gaps

- **Acts without a usable text: {missing}** (listed in `MISSING.md`).
- **OCR texts ({ocr} files, `text_format: "pdf scan (OCR by LawCodex, unverified)"`).** For acts
  whose only text in the API is a scanned Dziennik Ustaw page without a text layer (most
  pre-1990 acts and many 1990s–2000s regulations never consolidated), the scan was OCR-ed
  with Tesseract 5 (`pol` model). Expect recognition errors (e.g. `§` read as `8`), lost
  layout (two-column pages, tables), and — for old gazette issues where one PDF page holds
  several positions — fragments of neighbouring acts at the start or end. Always check the
  official PDF linked in `source_text`.
- Acts with API status *akt objęty tekstem jednolitym* (amending acts whose content has been
  merged into another act's consolidated text), and records flagged in force but with status
  *uchylony* / *wygaśnięcie aktu*, are not published separately.
- Repealed and expired acts; *Monitor Polski* (MP) acts; international agreements, government
  statements (oświadczenia rządowe), announcements (obwieszczenia, other than as the source
  of consolidated texts), local law (dzienniki urzędowe województw).
- Acts in force whose latest consolidated text is not yet announced are given in that latest
  *tekst jednolity* (or, for never-consolidated acts, the Kancelaria Sejmu *tekst ujednolicony*,
  or the original text): amendments made after that date are not reflected.
- PDF extraction (all texts published from 2025 on — the API stopped providing HTML — and
  older texts) is heuristic: paragraphs and headings are reconstructed from the text layer,
  tables and forms (wzory) in annexes are reduced to their text lines, and occasional
  spurious spaces inside words may remain (artefacts of the PDF text layer). The HTML-based
  files keep tables (Markdown or HTML) and footnotes.
- Footnote markers in PDF-based files remain inline as in the official text (e.g. `cywilny1)`);
  the footnote texts are appended under *Przypisy*.

## Sources

- Sejm ELI API — <https://api.sejm.gov.pl/eli> (publisher `DU`, Dziennik Ustaw); act
  metadata, HTML texts (`/acts/DU/<year>/<pos>/text.html`) and PDFs.
  Selection: `GET /eli/acts/search?publisher=DU&type=<Ustawa|Dekret|Rozporządzenie>&inForce=1`.
- The same documents in ISAP: <https://isap.sejm.gov.pl/> (link in each file's front matter).

## Format

```markdown
---
title: "Ustawa z dnia 23 kwietnia 1964 r. - Kodeks cywilny"
identifier: "DU/1964/93"                # ELI of the act
official_citation: "Dz.U. 1964 nr 16 poz. 93"
type: code                              # constitution | code | act | decree | regulation
jurisdiction: pl
language: pl
date: 1964-04-23                        # date of the act
promulgated: 1964-05-18
entry_into_force: 1965-01-01
last_amended: 2026-05-19                # legal status date of the consolidated text
status: in_force
official_status: "akt posiada tekst jednolity"
text_version: "tekst jednolity"
consolidated_text: "Dz.U. 2026 poz. 795"
consolidated_text_eli: "DU/2026/795"
text_format: "pdf (text extracted)"
source: "https://api.sejm.gov.pl/eli/acts/DU/1964/93"
source_text: "https://api.sejm.gov.pl/eli/acts/DU/2026/795/text/I/D20260795.pdf"
isap: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU19640160093"
retrieved: {retrieved}
---
```

File names: `du-<year>-<position>-<slug of the title>.md` (Dziennik Ustaw year and position of
the act itself, not of its consolidated text). Hierarchy (księga, część, tytuł, dział,
rozdział, oddział) maps to headings; articles are headings (or bold labels below `######`);
paragraphs (§), ustępy, punkty, litery and tirety are paragraphs starting with their label.

## Licence

Under art. 4 of the Polish Copyright Act (*ustawa z dnia 4 lutego 1994 r. o prawie autorskim
i prawach pokrewnych*), normative acts and their official drafts are not subject to
copyright. The ELI API is an open public service of the Kancelaria Sejmu.

## Regenerating

```sh
pip install -r scripts/requirements.txt
cd scripts
python fetch.py all          # search + metadata + texts, cached in ../../_raw/pl
python ocr.py                # OCR fallback for scans (needs pdftoppm, tesseract, pol.traineddata)
python convert.py            # writes the Markdown tree and ../../_raw/pl/manifest.json
python readme.py             # this README and MISSING.md
```
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=DEFAULT_RAW)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--retrieved", default=dt.date.today().isoformat())
    a = ap.parse_args()
    with open(os.path.join(a.raw, "manifest.json"), encoding="utf-8") as f:
        man = json.load(f)
    ok = [m for m in man if "file" in m]
    c = collections.Counter(m["file"].split("/")[0] for m in ok)
    basis = collections.Counter()
    for m in ok:
        if m["kind"] == "ocr":
            basis["ocr"] += 1
        elif m["tj"]:
            basis["tj_" + m["kind"]] += 1
        elif m["label"] == "U":
            basis["u_pdf"] += 1
        else:
            basis["orig_" + m["kind"]] += 1
    missing = [m for m in man if "file" not in m]
    vals = {k: c.get(k, 0) for k in ("konstytucja", "kodeksy", "ustawy", "dekrety", "rozporzadzenia")}
    vals.update({k: basis.get(k, 0) for k in ("tj_html", "tj_pdf", "u_pdf", "orig_html", "orig_pdf", "ocr")})
    vals.update(total=len(ok), missing=len(missing), retrieved=a.retrieved)
    with open(os.path.join(a.out, "README.md"), "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(**vals))
    lines = ["# Acts in force without a usable text", "",
             "Selected acts (in force per the Sejm ELI API) for which no Markdown file could be produced.", "",
             "| ELI | Title | Reason |", "|---|---|---|"]
    for m in sorted(missing, key=lambda m: (m.get("year", 0), m.get("pos", 0))):
        t = (m.get("title") or "").replace("|", "\\|")
        lines.append(f"| [{m['eli']}](https://api.sejm.gov.pl/eli/acts/{m['eli']}) | {t} | {m.get('error', '')} |")
    with open(os.path.join(a.out, "MISSING.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(vals)


if __name__ == "__main__":
    main()
