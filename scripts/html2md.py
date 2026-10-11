"""Sejm ELI act HTML (text.html) -> Markdown body.

The HTML is structured as <section> parts ("Treść ustawy", "Załącznik ...") containing
nested <div class="unit unit_XXX"> elements:
  with-title units  (book, part, titl, bran=dział, chpt=rozdział, schp=oddział, ...) -> headings
  unit_arti         -> article heading
  other units       (para=§, pass=ust., pint=pkt, lett=lit., tire=tiret ...) -> paragraphs
Footnotes (gloss-link tooltips) become Markdown footnotes.
"""
import re

from lxml import etree, html as lhtml

WS = re.compile(r"[ \t\r\n   ]+")
BLOCK_TAGS = {"div", "p", "table", "section", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6", "br"}


def classes(el):
    return set((el.get("class") or "").split())


def norm(s):
    return WS.sub(" ", s or "").strip()


def md_escape(s):
    s = s.replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_").replace("`", "\\`")
    s = s.replace("<", "&lt;").replace(">", "&gt;")
    return s


def escape_line_start(s):
    """Prevent Markdown list/heading/quote interpretation at paragraph start."""
    s = re.sub(r"^(\d+)([.)])(\s)", r"\1\\\2\3", s)
    s = re.sub(r"^([-+#>|=])", r"\\\1", s)
    return s


class Ctx:
    """Footnotes keep their official numbers (the text refers to "odnośnik N")."""

    def __init__(self):
        self.notes = {}  # key -> text
        self.order = []

    def note(self, num, text):
        num = re.sub(r"[^0-9a-zA-Z*]", "", num) or str(len(self.order) + 1)
        num = num.replace("*", "x")
        key, i = num, 1
        while key in self.notes and self.notes[key] != text:
            i += 1
            key = f"{num}-{i}"
        if key not in self.notes:
            self.notes[key] = text
            self.order.append(key)
        return f"[^{key}]"


def inline(el, ctx, skip_heading=False):
    """Inline text of an element (Markdown-escaped, sup/sub kept as HTML)."""
    parts = []

    def walk(e, top=False):
        tag = e.tag if isinstance(e.tag, str) else ""
        tag = tag.lower()
        cl = classes(e) if tag else set()
        if tag in ("script", "style"):
            pass
        elif "gloss-link" in cl:
            tip = e.xpath(".//*[contains(@class,'pro-gloss-inner')]")
            txt = norm(tip[0].text_content()) if tip else ""
            sup = e.xpath("./sup")
            num = norm(sup[0].text_content()) if sup else ""
            parts.append(ctx.note(num, md_escape(txt)) if txt else "")
        elif tag in ("sup", "sub"):
            parts.append(f"<{tag}>{md_escape(norm(e.text_content()))}</{tag}>")
        elif tag == "img":
            alt = e.get("alt") or ""
            src = e.get("src") or ""
            if src.startswith("data:"):
                parts.append(f"[obraz{': ' + alt if alt else ''}]")
            else:
                parts.append(f"![{md_escape(alt)}]({src})")
        elif tag == "br":
            parts.append(" ")
        else:
            if e.text and tag:
                parts.append(md_escape(e.text))
            for c in e:
                walk(c)
                if c.tail:
                    parts.append(md_escape(c.tail))
            if tag in BLOCK_TAGS:
                parts.append(" ")
            return
        # leaf handled; tail handled by parent

    walk(el, True)
    return norm("".join(parts))


def table_md(tbl, ctx):
    """Render a table that contains no nested table."""
    rows = tbl.xpath("./tr|./thead/tr|./tbody/tr|./tfoot/tr")
    cells = [r.xpath("./td|./th") for r in rows]
    complex_ = any((c.get("rowspan") not in (None, "1")) or (c.get("colspan") not in (None, "1"))
                   for r in cells for c in r)
    texts = [[inline(c, ctx) for c in r] for r in cells]
    keep = [i for i, r in enumerate(texts) if any(r)]
    if not keep:
        return ""
    if not complex_:
        data = [texts[i] for i in keep]
        w = max(len(r) for r in data)
        data = [r + [""] * (w - len(r)) for r in data]
        cols = [j for j in range(w) if any(r[j] for r in data)]
        data = [[r[j] for j in cols] for r in data]
        if len(cols) == 1:
            return "\n\n".join(r[0] for r in data if r[0])
        out = []
        for i, r in enumerate(data):
            out.append("| " + " | ".join(x.replace("|", "\\|") for x in r) + " |")
            if i == 0:
                out.append("|" + "---|" * len(cols))
        return "\n".join(out)
    out = ["<table>"]
    for i in keep:
        cs = []
        for c, t in zip(cells[i], texts[i]):
            attrs = "".join(f' {a}="{c.get(a)}"' for a in ("rowspan", "colspan") if c.get(a) not in (None, "1"))
            tag = c.tag.lower()
            cs.append(f"<{tag}{attrs}>{t}</{tag}>")
        out.append("<tr>" + "".join(cs) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


class Renderer:
    def __init__(self):
        self.ctx = Ctx()
        self.out = []

    def para(self, text, quote=0):
        text = text.strip()
        if not text:
            return
        text = escape_line_start(text)
        if quote:
            text = "\n".join(("> " * quote) + ln for ln in text.split("\n"))
        self.out.append(text)

    def heading(self, level, text, quote=0):
        text = text.strip()
        if not text:
            return
        if level <= 6 and not quote:
            self.out.append("#" * level + " " + text)
        else:
            self.para(f"**{text}**", quote)

    def unit_label(self, unit):
        """Label of a unit: its <h3> plus <p> siblings (the HTML parser moves the <P>
        elements of the original <h3><P>..</P></h3> out of the heading)."""
        bits = []
        for c in unit:
            if not isinstance(c.tag, str):
                continue
            tag = c.tag.lower()
            if tag == "h3":
                ps = c.xpath("./p")
                for x in (ps or [c]):
                    t = inline(x, self.ctx)
                    if t:
                        bits.append(t)
            elif tag == "p":
                t = inline(c, self.ctx)
                if t:
                    bits.append(t)
            elif "unit-inner" in classes(c):
                break
        return " – ".join(bits)

    def content(self, container, depth, quote, pending_label="", children=None):
        """Render children of a unit-inner / block. Returns leftover pending label."""
        for c in (container if children is None else children):
            if not isinstance(c.tag, str):
                continue
            tag = c.tag.lower()
            cl = classes(c)
            if "unit" in cl:
                if pending_label:
                    self.para(pending_label, quote)
                    pending_label = ""
                self.unit(c, depth, quote)
            elif "cite-box" in cl:
                if pending_label:
                    self.para(pending_label, quote)
                    pending_label = ""
                body = c.xpath("./*[contains(@class,'cite-body')]")
                opn = "„"
                start = len(self.out)
                for b in body:
                    self.content(b, depth, quote + 1)
                trailer = c.xpath("./*[contains(@class,'trailer')]")
                ttxt = inline(trailer[0], self.ctx) if trailer else ""
                if len(self.out) > start:
                    first = self.out[start]
                    m = re.match(r"^((?:> )+)(#+ )?", first)
                    pre = m.group(0) if m else ""
                    self.out[start] = pre + opn + first[len(pre):]
                    self.out[-1] = self.out[-1] + "”" + (ttxt if ttxt else "")
            elif tag == "table" and c.xpath(".//table"):
                # layout table wrapping data tables / text: render its cells' content
                if pending_label:
                    self.para(pending_label, quote)
                    pending_label = ""
                for cell in c.xpath("./tr/td|./tr/th|./tbody/tr/td|./thead/tr/td|./tbody/tr/th"):
                    self.content(cell, depth, quote)
            elif tag == "table":
                if pending_label:
                    self.para(pending_label, quote)
                    pending_label = ""
                t = table_md(c, self.ctx)
                if t:
                    if quote:
                        t = "\n".join("> " * quote + ln for ln in t.split("\n"))
                    self.out.append(t)
            elif tag in ("ul", "ol"):
                if pending_label:
                    self.para(pending_label, quote)
                    pending_label = ""
                for li in c:
                    if not isinstance(li.tag, str):
                        continue
                    kids = [k for k in li if isinstance(k.tag, str)]
                    lab = ""
                    if kids and len(kids[0]) == 0 and len(norm(kids[0].text_content())) <= 4:
                        lab = md_escape(norm(kids[0].text_content()))
                        kids = kids[1:]
                    if not kids:
                        if lab or norm(li.text_content()):
                            self.para(lab or inline(li, self.ctx), quote)
                        continue
                    left = self.content(li, depth, quote, lab, children=kids)
                    if left:
                        self.para(left, quote)
            elif tag == "h2" and c.xpath(".//div[contains(concat(' ',@class,' '),' unit ')]"):
                # malformed HTML: the parser swallowed the body into the part heading
                pending_label = self.content(c, depth, quote, pending_label)
            elif tag in ("h3", "h2") or (tag == "p" and "unit" in classes(container)):
                continue
            elif c.xpath(".//*[contains(concat(' ',@class,' '),' unit ')]|.//table|.//*[contains(@class,'cite-box')]"):
                pending_label = self.content(c, depth, quote, pending_label)
            else:
                txt = inline(c, self.ctx)
                if txt:
                    self.para((pending_label + " " + txt).strip() if pending_label else txt, quote)
                    pending_label = ""
        return pending_label

    def unit(self, u, depth, quote):
        cl = classes(u)
        inner = u.xpath("./*[contains(@class,'unit-inner')]")
        label = self.unit_label(u)
        if "with-title" in cl:
            self.heading(min(depth + 2, 7), label, quote)
            for i in inner:
                self.content(i, depth + 1, quote)
            return
        if "unit_arti" in cl and not quote:
            lvl = depth + 2
            if lvl <= 6:
                self.heading(lvl, label.replace("**", ""))
                left = ""
            else:
                left = f"**{label}**"
            for i in inner:
                left = self.content(i, depth + 1, quote, left)
            if left:
                self.para(left)
            return
        left = label
        for i in inner:
            left = self.content(i, depth, quote, left)
        if left:
            self.para(left, quote)

    def render(self, root, skip_first_part=False):
        sections = root.xpath("//div[@class='parts']/section") or root.xpath("//section")
        if skip_first_part and len(sections) > 1:
            sections = sections[1:]
        multi = len(sections) > 1
        for s in sections:
            part = s.xpath(".//div[contains(@class,'part')]")[0] if s.xpath(".//div[contains(@class,'part')]") else s
            h2 = part.xpath("./h2")
            if h2 and h2[0].xpath(".//div[contains(concat(' ',@class,' '),' unit ')]"):
                sp = h2[0].xpath("./span")
                title = norm(sp[0].text_content()) if sp else ""
            else:
                title = inline(h2[0], self.ctx) if h2 else ""
            base = 0
            if title and not title.startswith("Treść") and not re.match(r"^(Załącznik +- +)?Tekst jednolity", title):
                self.out.append("## " + title)
                base = 1
            elif title and re.match(r"^Załącznik +- +Tekst jednolity", title):
                # the consolidated text itself: keep any footnote of its header
                fn = re.findall(r"\[\^\d+\]", title)
                if fn:
                    self.out.append("Tekst jednolity" + "".join(fn))
            blocks = part.xpath("./div[contains(@class,'block')]")
            if not blocks or (h2 and h2[0].xpath(".//div[contains(concat(' ',@class,' '),' unit ')]")):
                blocks = [part]
            for block in blocks:
                self.content(block, base, 0)
        if not self.out:
            blocks = root.xpath("//div[contains(concat(' ',@class,' '),' block ')]"
                                "[not(ancestor::div[contains(concat(' ',@class,' '),' block ')])]")
            if skip_first_part and len(blocks) > 1:
                blocks = blocks[1:]
            for block in blocks:
                self.content(block, 0, 0)
        md = "\n\n".join(self.out)
        if self.ctx.notes:
            md += "\n\n---\n\n" + "\n".join(f"[^{k}]: {self.ctx.notes[k]}" for k in self.ctx.order)
        return md


def convert(data, skip_first_part=False):
    if isinstance(data, bytes):
        data = data.decode("utf-8", errors="replace")
    md = _convert(lhtml.document_fromstring(data), skip_first_part)
    if len(md.strip()) < 20:
        # libxml2 re-nests the document when block elements sit inside inline ones (e.g. a
        # footnote list inside the <h1> title); BeautifulSoup keeps the nesting as written
        from lxml.html import soupparser
        md = _convert(soupparser.fromstring(data), skip_first_part)
    return md


def _convert(root, skip_first_part):
    for bad in root.xpath("//div[@id='toc']|//script|//style|//h1"):
        bad.getparent().remove(bad)
    return Renderer().render(root, skip_first_part)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1], "rb") as f:
        print(convert(f.read(), skip_first_part=len(sys.argv) > 2))
