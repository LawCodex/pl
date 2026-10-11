"""Dziennik Ustaw PDF -> Markdown body (text layer extracted with pypdf).

Heuristics:
  * page headers ("Dziennik Ustaw – 3 – Poz. 795", "©Kancelaria Sejmu s. 1/119", dates)
    are dropped; footnotes (block after an empty line at the page bottom starting with
    "1)" / "*)") are collected and appended at the end;
  * for a consolidated text announcement (tj=True) everything before the
    "Załącznik do obwieszczenia ..." header (the announcement itself) is dropped;
  * lines are re-flowed into paragraphs; a new paragraph starts at structural markers
    (Art., §, "1.", "1)", "a)", "–", headings such as "Rozdział 1", "DZIAŁ II", "Załącznik nr 1");
  * Polish line-end hyphenation is undone ("zobo-\\nwiązania" -> "zobowiązania",
    "społeczno-\\n-gospodarczy" -> "społeczno-gospodarczy");
  * superscript article numbers rendered by pypdf as "492[1]" become "492<sup>1</sup>".
Tables and forms in annexes cannot be reconstructed from the text layer; their text is
kept line by line.
"""
import re
import statistics

from pypdf import PdfReader

D = r"[–—-]"
HEADER_RES = [
    re.compile(r"^Dziennik Ustaw\s*" + D + r"\s*\d+\s*" + D + r"\s*Poz\.\s*\d+\s*$"),
    re.compile(r"^Dziennik Ustaw\s+Nr\s*\d+(\s*" + D + r"\s*\d+\s*" + D + r"\s*Poz\.\s*[\d\s,i" + D[1:-1] + r"]+)?\s*$"),
    re.compile(r"^" + D + r"\s*\d+\s*" + D + r"\s*$"),
    re.compile(r"^Poz\.\s*\d+([\s,i" + D[1:-1] + r"]+\d+)*\s*$"),
    re.compile(r"^RZECZYPOSPOLITEJ POLSKIEJ Warszawa, dnia \d{1,2} \S+ \d{4} r\.$"),
    re.compile(r"^©\s*Kancelaria Sejmu\s+s\.\s*\d+\s*/\s*\d+\s*$"),
    re.compile(r"^\d{4}-\d{2}-\d{2}\s*$"),
    re.compile(r"^DZIENNIK USTAW\s*$"),
    re.compile(r"^RZECZYPOSPOLITEJ POLSKIEJ\s*$"),
    re.compile(r"^Warszawa, dnia \d{1,2} \S+ \d{4} r\.\s*$"),
]

HEAD_WORDS = r"(?:KSIĘGA|Księga|CZĘŚĆ|Część|TYTUŁ|Tytuł|DZIAŁ|Dział|ROZDZIAŁ|Rozdział|ODDZIAŁ|Oddział|PODROZDZIAŁ|Podrozdział)"
HEAD_RE = re.compile(r"^" + HEAD_WORDS + r"\s+([IVXLCDM]+|\d+[a-z]?|[A-ZĄĆĘŁŃÓŚŹŻ]+|[a-ząćęłńóśźż]+)(\[\d+\]|<sup>\d+</sup>)?\.?\s*$")
HEAD_RANK = {"księga": 0, "część": 1, "tytuł": 2, "dział": 3, "rozdział": 4, "podrozdział": 5, "oddział": 5}
ANNEX_RE = re.compile(r"^(ZAŁĄCZNIK|Załącznik|ZAŁĄCZNIKI|Załączniki)(\s+(nr|Nr)\s+\S+)?(\s+do\b.*)?\s*$")
ART_RE = re.compile(r"^(Art\.\s*\d+[a-z]*(?:<sup>[^<]+</sup>)?\.)\s*(.*)$")
PARA_RE = re.compile(r"^§\s*\d+[a-z]*(?:<sup>[^<]+</sup>)?\.\s+\S")
UST_RE = re.compile(r"^\d+[a-z]*(?:<sup>[^<]+</sup>)?\.\s+[A-ZĄĆĘŁŃÓŚŹŻ(„\"]")
PKT_RE = re.compile(r"^\d+[a-z]*(?:<sup>[^<]+</sup>)?\)\s+\S")
LIT_RE = re.compile(r"^[a-z]{1,2}(?:<sup>[^<]+</sup>)?\)\s+\S")
TIRET_RE = re.compile(r"^[–—-]\s+\S")
FOOT_RE = re.compile(r"^(\d+|\*+)\)\s*\S")
NO_BREAK_AFTER = re.compile(r"(\b(art|ust|pkt|lit|poz|nr|Nr|Dz|U|z|w|i|oraz|do|r|t|str|tj|późn)\.?|§)\s*$")
SENT_END = re.compile(r"[.:;!?”\")]\s*$")


def sup(s):
    return re.sub(r"(?<=[0-9a-z])\[(\d+[a-z]?)\]", r"<sup>\1</sup>", s)


def md_escape(s):
    # keep our own <sup> tags; escape other markup characters
    s = s.replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_").replace("`", "\\`")
    s = s.replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"&lt;(/?)sup&gt;", r"<\1sup>", s)
    return s


def escape_line_start(s):
    s = re.sub(r"^(\d+)([.)])(\s)", r"\1\\\2\3", s)
    s = re.sub(r"^([-+#>|=])", r"\\\1", s)
    return s


def pdf_pages(path):
    out = []
    for page in PdfReader(path).pages:
        try:
            out.append(page.extract_text() or "")
        except Exception:  # noqa: BLE001
            out.append("")
    return out


def page_lines(pages, footnotes=True):
    """Yield (page_no, body_lines, footnote_lines)."""
    for n, txt in enumerate(pages):
        # control characters come from fonts without Unicode mapping (maps, drawings)
        txt = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd\ue000-\uf8ff]", "", txt)
        lines = [re.sub(r"[ \t\u00a0\u2000-\u200b\u202f\u205f\u3000]+", " ", ln).strip()
                 for ln in txt.replace("\r", "\n").split("\n")]
        # drop header lines at the top
        i = 0
        while i < len(lines) and i < 10:
            s = lines[i].strip()
            if not s or any(r.match(s) for r in HEADER_RES):
                i += 1
                continue
            break
        lines = lines[i:]
        # Kancelaria Sejmu copies: "Opracowano na podstawie: ..." side box on page 1
        side = []
        for j, ln in enumerate(lines):
            if ln.strip().startswith("Opracowano na"):
                side = [" ".join(x.strip() for x in lines[j:] if x.strip())]
                lines = lines[:j]
                break
        # footnotes: after the last blank line, a block starting with "1)" / "*)"
        foot = []
        for j in range(len(lines) - 1, 0, -1) if footnotes else ():
            if not lines[j].strip():
                rest = [ln for ln in lines[j + 1:] if ln.strip()]
                if rest and FOOT_RE.match(rest[0].strip()) and j > len(lines) * 0.3:
                    foot = rest
                    lines = lines[:j]
                break
        yield n, [ln.strip() for ln in lines if ln.strip()], side + [ln.strip() for ln in foot]


def join_lines(prev, nxt):
    """Join two lines of the same paragraph, undoing hyphenation."""
    m = re.search(r"(?<=[A-Za-zÀ-žĄĆĘŁŃÓŚŹŻąćęłńóśźż]) +-$", prev)
    if m and re.match(r"^[a-ząćęłńóśźż]", nxt):
        return prev[:m.start()] + nxt
    if re.search(r"[A-Za-zÀ-žĄĆĘŁŃÓŚŹŻąćęłńóśźż]-$", prev):
        if nxt.startswith("-"):
            return prev + nxt[1:]
        if re.match(r"^[a-ząćęłńóśźż]", nxt):
            return prev[:-1] + nxt
        return prev + nxt
    return prev + " " + nxt


TYPE_WORD = re.compile(r"^(USTAWA|ROZPORZĄDZENIE|DEKRET|OBWIESZCZENIE|KONSTYTUCJA)\b")


def trim_to_position(body, pos):
    """Old gazette issues: a position's PDF can contain the end of the previous act and the
    start of the next one.  Keep from the line "<pos>" (followed by the act type word) to the
    line "<pos+1>" followed by a type word."""
    start = None
    for i in range(len(body) - 1):
        if body[i].strip() == str(pos) and TYPE_WORD.match(body[i + 1]):
            start = i + 1
            break
    if start is None:
        return body
    for j in range(start + 1, len(body) - 1):
        if body[j].strip() == str(pos + 1) and TYPE_WORD.match(body[j + 1]):
            return body[start:j]
    return body[start:]


def convert(path, tj=False, pages=None, pos=None, ocr=False):
    """Convert a PDF (or a list of already extracted page texts, e.g. OCR output).
    pos: Dziennik Ustaw position of the document, used to cut neighbouring acts."""
    if pages is None:
        pages = pdf_pages(path)
    body, notes = [], []
    for _, lines, foot in page_lines(pages, footnotes=not ocr):
        body.extend(lines)
        notes.extend(foot)
    body = [sup(re.sub(r"\s{2,}", " ", ln)) for ln in body]
    if pos is not None:
        body = trim_to_position(body, pos)
    if tj:
        for i, ln in enumerate(body[:400]):
            if re.match(r"^Załącznik do obwieszczenia", ln):
                j = i
                while j < len(body) and j < i + 4 and not re.search(r"poz\.\s*\d+\s*\)\s*$", body[j]):
                    j += 1
                body = body[j + 1:] if j < i + 4 else body[i + 1:]
                break
    if not body:
        return ""
    widths = [len(ln) for ln in body if len(ln) > 20]
    typical = statistics.median(widths) if widths else 80
    short = typical * 0.7

    # pass 1: classify lines into blocks
    blocks = []  # (kind, text)  kind: head, art, para, annex
    cur = None
    annex = False
    head_types = []

    def flush():
        nonlocal cur
        if cur:
            blocks.append(cur)
        cur = None

    prev_line = ""
    i = 0
    while i < len(body):
        ln = body[i]
        m_head = HEAD_RE.match(ln)
        if m_head:
            flush()
            word = ln.split()[0].lower()
            title_bits = []
            k = i + 1
            # title lines: until the next marker
            while k < len(body) and k <= i + 3:
                nx = body[k]
                if (HEAD_RE.match(nx) or ART_RE.match(nx) or PARA_RE.match(nx) or ANNEX_RE.match(nx)
                        or UST_RE.match(nx) or PKT_RE.match(nx)):
                    break
                title_bits.append(nx)
                k += 1
                if len(nx) < short:
                    break
            title = ""
            for t in title_bits:
                title = join_lines(title, t) if title else t
            if word not in head_types:
                head_types.append(word)
            blocks.append(("head", word, ln + (" – " + title if title else "")))
            i = k
            prev_line = ""
            continue
        if ANNEX_RE.match(ln) and (not prev_line or SENT_END.search(prev_line) or len(prev_line) < short):
            flush()
            blocks.append(("annex", None, ln))
            annex = True
            i += 1
            prev_line = ""
            continue
        m_art = ART_RE.match(ln)
        new_para = False
        if m_art:
            flush()
            blocks.append(("art", None, m_art.group(1)))
            ln = m_art.group(2)
            if not ln:
                i += 1
                prev_line = ""
                continue
            new_para = True
        elif cur is None:
            new_para = True
        elif (PARA_RE.match(ln) or UST_RE.match(ln) or PKT_RE.match(ln) or LIT_RE.match(ln)
              or TIRET_RE.match(ln)) and not NO_BREAK_AFTER.search(prev_line):
            new_para = True
        elif len(prev_line) < short and (annex or (SENT_END.search(prev_line)
                                                   and re.match(r"^[A-ZĄĆĘŁŃÓŚŹŻ„(]", ln))):
            new_para = True
        if new_para:
            flush()
            cur = ("p", None, ln)
        else:
            cur = ("p", None, join_lines(cur[2], ln))
        prev_line = body[i]
        i += 1
    flush()

    # heading levels
    ranks = sorted(set(head_types), key=lambda w: HEAD_RANK.get(w.lower(), 9))
    level = {w: min(2 + n, 6) for n, w in enumerate(ranks)}
    art_level = 2 + len(ranks)
    out = []
    pending_art = None
    for kind, word, text in blocks:
        text = md_escape(text)
        if kind == "head":
            out.append("#" * level[word] + " " + text)
        elif kind == "annex":
            out.append("## " + text)
        elif kind == "art":
            if art_level <= 6:
                out.append("#" * art_level + " " + text)
            else:
                pending_art = f"**{text}**"
                continue
        else:
            text = escape_line_start(text)
            if pending_art:
                text = pending_art + " " + text
                pending_art = None
            out.append(text)
        if pending_art and kind != "art":
            out.insert(len(out) - 1, pending_art)
            pending_art = None
    if pending_art:
        out.append(pending_art)
    md = "\n\n".join(out)
    if notes:
        fn, cur_n = [], None
        for ln in notes:
            m = FOOT_RE.match(ln)
            if m:
                fn.append(ln)
            elif fn:
                fn[-1] = join_lines(fn[-1], ln)
            else:
                fn.append(ln)
        md += "\n\n---\n\nPrzypisy:\n\n" + "\n\n".join(escape_line_start(md_escape(sup(x))) for x in fn)
    return md


if __name__ == "__main__":
    import sys
    print(convert(sys.argv[1], tj=len(sys.argv) > 2))
