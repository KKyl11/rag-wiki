"""渲染 HTML（graph 節點 N5）：把「已通過」的逐頁稿轉成單一檔案的 deck.html。

用法：python scripts/render_deck.py <run_dir> [--title 簡報標題]
規則（課程 p.44）：渲染節點不能改任何一個字。本腳本只做「markdown 語法 → HTML 標籤」的轉換，
文字原封不動；版面問題只能改 scripts/deck_template.html 的 CSS，字太多要退回逐頁稿。

支援的逐頁稿語法：
  ### 小標、- 條列、1. 編號、段落、**粗體**、`code`、| 表格 |、
  > 🎓 教學比喻（非來源內容）：...（比喻框）、> ⚖️ ...（兩說並陳框）、> 其他（重點框）、
  ```flow  每行「A → B → C」畫成流程方塊；
  ```quiz  每行「Q: 問題 || A: 答案」畫成小測驗（答案按 a 鍵或點擊顯示）
"""
import argparse
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, parse_drafts  # noqa: E402

TEMPLATE = ROOT / "scripts" / "deck_template.html"


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    return s


def render_body(md):
    out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        s = lines[i].rstrip()
        if not s.strip():
            i += 1
            continue
        if s.startswith("```"):
            kind = s[3:].strip()
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            if kind == "flow":
                for row in block:
                    steps = [x.strip() for x in row.split("→") if x.strip()]
                    parts = []
                    for j, st in enumerate(steps):
                        parts.append(f'<div class="step">{inline(st)}</div>')
                        if j < len(steps) - 1:
                            parts.append('<div class="arrow" aria-hidden="true">→</div>')
                    out.append(f'<div class="flow">{"".join(parts)}</div>')
            elif kind == "quiz":
                out.append('<ol class="quiz">')
                for row in block:
                    if "||" in row:
                        q, a = row.split("||", 1)
                        q = re.sub(r"^\s*Q[:：]\s*", "", q).strip()
                        a = re.sub(r"^\s*A[:：]\s*", "", a).strip()
                        out.append(f'<li><span class="q">{inline(q)}</span>'
                                   f'<span class="a">{inline(a)}</span></li>')
                out.append("</ol>")
            else:
                out.append("<pre>" + html.escape("\n".join(block)) + "</pre>")
            continue
        if s.startswith("### "):
            out.append(f"<h3>{inline(s[4:])}</h3>")
            i += 1
            continue
        if s.startswith(">"):
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i].lstrip(">").strip())
                i += 1
            text = " ".join(x for x in q if x)
            cls = "analogy" if "教學比喻" in text else ("debate" if "⚖️" in text else "callout")
            out.append(f'<div class="box {cls}">{inline(text)}</div>')
            continue
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            h = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append(f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")
            continue
        if re.match(r"^\s*[-*] ", s) or re.match(r"^\s*\d+\. ", s):
            ordered = bool(re.match(r"^\s*\d+\. ", s))
            tag = "ol" if ordered else "ul"
            items = []
            while i < len(lines) and (re.match(r"^\s*[-*] ", lines[i]) or re.match(r"^\s*\d+\. ", lines[i])):
                items.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", lines[i]))
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(\s*[-*] |\s*\d+\. |>|\||```|### )", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--title", default="RAG 是什麼？讓 AI 先查資料再回答")
    a = ap.parse_args()
    run = Path(a.run)
    drafts = parse_drafts(run)
    total = len(drafts)
    sections = []
    for d in drafts:
        fm = d["fm"]
        wiki = fm.get("wiki") or []
        layout = fm.get("layout", "content")
        kicker = fm.get("section", "")
        links = " · ".join(f'<span>{html.escape(w)}</span>' for w in wiki)
        sections.append(
            f'<section class="slide layout-{html.escape(layout)}" data-n="{d["n"]}" data-wiki="{html.escape(",".join(wiki))}">\n'
            f'  <div class="content">\n'
            + (f'    <div class="kicker">{inline(kicker)}</div>\n' if kicker else "")
            + f'    <h2>{inline(fm.get("title", ""))}</h2>\n'
            f'    <div class="body">\n{render_body(d["body"])}\n    </div>\n'
            f'  </div>\n'
            f'  <footer><div class="wiki">📚 Wiki：{links}</div><div class="pageno">{d["n"]} / {total}</div></footer>\n'
            f'</section>'
        )
    tpl = TEMPLATE.read_text(encoding="utf-8")
    out = tpl.replace("{{TITLE}}", html.escape(a.title)).replace("{{SLIDES}}", "\n".join(sections))
    (run / "deck.html").write_text(out, encoding="utf-8")
    print(f"wrote {run / 'deck.html'}：{total} 頁")


if __name__ == "__main__":
    main()
