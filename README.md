# LawCodex — Poland (Polska)

Polish legislation in force — the Constitution, codes (kodeksy), statutes (ustawy),
decrees with force of statute (dekrety) and regulations (rozporządzenia) published in
*Dziennik Ustaw Rzeczypospolitej Polskiej* — as Markdown, one file per act, in the original
Polish. Texts are the latest consolidated text (*tekst jednolity*) where one has been
announced.

Retrieved: 2026-10-11.

## Contents

| Directory | Content | Files |
|---|---|---:|
| `konstytucja/` | Konstytucja Rzeczypospolitej Polskiej (1997) | 1 |
| `kodeksy/` | Codes (ustawy titled "Kodeks …": cywilny, karny, pracy, spółek handlowych, …) | 14 |
| `ustawy/<year>/` | Other statutes (ustawy) in force, by year of Dziennik Ustaw | 4764 |
| `dekrety/<year>/` | Decrees (dekrety) still in force | 84 |
| `rozporzadzenia/<year>/` | Regulations (rozporządzenia) in force, by year (years with more than 900 files are split into `poz-NNNN-NNNN/` subdirectories) | 16410 |
| **Total** | | **21273** |

Text basis of the 21273 files:

| Text used | Files |
|---|---:|
| Latest *tekst jednolity* (consolidated text announced in Dziennik Ustaw), HTML | 1748 |
| Latest *tekst jednolity*, PDF (text layer extracted) | 892 |
| *Tekst ujednolicony* (consolidated text prepared by the Kancelaria Sejmu, PDF) — acts amended but never re-announced | 559 |
| Text as published (act never amended / no consolidation), HTML | 10274 |
| Text as published, PDF (text layer extracted) | 4189 |
| Scanned PDF without text layer — **OCR** by LawCodex (Tesseract, Polish model), unverified | 3611 |

Each file's front matter says which text was used (`text_version`, `consolidated_text`,
`source_text`, `text_format`) and, for consolidated texts, the date of the legal status
(`last_amended` = *stan prawny na dzień*).

## Not covered / known gaps

- **Acts without a usable text: 3** (listed in `MISSING.md`).
- **OCR texts (3611 files, `text_format: "pdf scan (OCR by LawCodex, unverified)"`).** For acts
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
retrieved: 2026-10-11
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
