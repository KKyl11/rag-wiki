"""把網頁 HTML 轉成 markdown 存進 raw/（只用標準函式庫）。

用法：python -I scripts/html_to_md.py <input.html> <output.md> <原始網址> [起始標題文字] [結束標題文字]
- 只保留 <article> 內、從「起始標題」到「結束標題」之前的內容
- 檔頭寫入原始網址與抓取日期（需求 Q10）
"""
import datetime
import html
import re
import sys
from html.parser import HTMLParser

BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "pre", "tr", "blockquote", "figcaption"}
SKIP = {"script", "style", "svg", "nav", "footer", "button", "noscript"}


class MD(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.buf = [], []
        self.skip = 0
        self.in_article = False
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            self.in_article = True
        if tag in SKIP:
            self.skip += 1
        self.stack.append(tag)
        if tag in BLOCK:
            self.flush()
        if tag in ("td", "th"):
            self.buf.append(" | ")
        if tag == "br":
            self.buf.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if tag in BLOCK:
            prefix = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "li": "- ", "blockquote": "> "}.get(tag, "")
            self.flush(prefix)
        if tag == "article":
            self.flush()
            self.in_article = False
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if self.in_article and not self.skip:
            self.buf.append(data)

    def flush(self, prefix=""):
        text = re.sub(r"[ \t\r\f\v]+", " ", "".join(self.buf)).strip()
        self.buf = []
        if text:
            self.out.append(prefix + text)


def main():
    src, dst, url = sys.argv[1:4]
    start = sys.argv[4] if len(sys.argv) > 4 else None
    end = sys.argv[5] if len(sys.argv) > 5 else None
    p = MD()
    p.feed(open(src, encoding="utf-8").read())
    lines = p.out
    if start:
        idx = [i for i, l in enumerate(lines) if l.lstrip("# ").strip() == start and l.startswith("#")]
        lines = lines[idx[0]:] if idx else lines
    if end:
        idx = [i for i, l in enumerate(lines) if l.lstrip("# ").strip() == end and l.startswith("#")]
        lines = lines[: idx[0]] if idx else lines
    # 去除重複的連續行
    dedup = []
    for l in lines:
        if not dedup or dedup[-1] != l:
            dedup.append(l)
    header = (
        f"---\nsource_url: {url}\nfetched: {datetime.date.today().isoformat()}\n"
        f"converted_by: scripts/html_to_md.py (stdlib HTMLParser)\n---\n\n"
    )
    open(dst, "w", encoding="utf-8").write(header + "\n\n".join(html.unescape(l) for l in dedup) + "\n")
    print(f"wrote {dst}: {len(dedup)} blocks")


if __name__ == "__main__":
    main()
