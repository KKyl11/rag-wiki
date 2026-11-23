"""出處檢查（graph 節點 G3 的程式檢查部分；逐頁稿節點內的小 loop 也用它）。

用法：python scripts/check_citations.py <run_dir> [--slides 3,6]
每一張 drafts/slide-NN.md 檢查：
  1. frontmatter 有 `wiki:` 出處（至少 1 頁），且每頁都存在
  2. 出處頁必須是 sources.md 檢索到的頁面（不能偷用沒檢索的頁面）
  3. frontmatter `evidence:` 的證據編號存在於 cards/
  4. 內文每個數字，都能在「被引用的 wiki 頁面」原文中找到
  5. 「教學比喻（非來源內容）」不得含數字
  --rules v2（預設）再加三項「往前移」的忠實度檢查（v1→v2，見 docs/workflow.md §8）：
  6. 限定詞保留：本頁用到的每個證據項目，其〔限定：…〕必須原樣出現在本頁
  7. 概括詞：「常、通常、總是、一定、所有、永遠、保證…」若出現在本頁、卻不在被引用的 wiki 頁，判為誇大
  8. 引號詞：本頁「」裡的詞（教學比喻框除外）必須出現在被引用的 wiki 頁
  --rules v1 重現 run-001 當時的規則
exit code：0 = PASS，1 = FAIL（輸出列出要退回的頁）
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ANALOGY_MARK, GENERALIZERS, number_found, numbers_in, parse_cards, parse_drafts, parse_sources, wiki_path  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--slides", default="")
    ap.add_argument("--rules", default="v2", choices=["v1", "v2"])
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    run = Path(a.run)
    only = {int(x) for x in a.slides.split(",") if x.strip()}
    pages, _ = parse_sources(run)
    cards = parse_cards(run)
    drafts = parse_drafts(run)
    if not drafts:
        print("FAIL：drafts/ 沒有任何 slide-NN.md")
        sys.exit(1)
    bad = {}
    checked = 0
    for d in drafts:
        if only and d["n"] not in only:
            continue
        checked += 1
        e = []
        wl = d["fm"].get("wiki") or []
        if not isinstance(wl, list) or not wl:
            e.append("沒有出處（frontmatter `wiki:` 是空的）")
            wl = []
        corpus = ""
        for w in wl:
            p = wiki_path(w)
            if not p.exists():
                e.append(f"引用的 wiki/{w} 不存在")
                continue
            if w.replace("wiki/", "") not in pages:
                e.append(f"引用的 wiki/{w} 不在 sources.md 檢索結果裡")
            corpus += "\n" + p.read_text(encoding="utf-8")
        for ev in d["fm"].get("evidence") or []:
            m = re.match(r"^([\w\-]+)#(E\d+)$", ev)
            if not m or m.group(1) not in cards or m.group(2) not in cards[m.group(1)]["items"]:
                e.append(f"證據編號 {ev} 不存在")
        body_lines = []
        for line in d["body"].splitlines():
            if ANALOGY_MARK in line:
                if re.search(r"\d", line.replace(ANALOGY_MARK, "")):
                    e.append(f"教學比喻含數字：{line.strip()[:50]}")
                continue
            body_lines.append(line)
        title = d["fm"].get("title", "")
        for num in numbers_in(title + "\n" + "\n".join(body_lines)):
            if corpus and not number_found(num, corpus):
                e.append(f"數字 {num} 在被引用的 wiki 頁面中找不到")
        if a.rules == "v2":
            text = title + "\n" + "\n".join(body_lines)
            plain_corpus = corpus
            for ev in d["fm"].get("evidence") or []:
                m = re.match(r"^([\w\-]+)#(E\d+)$", ev)
                if m and m.group(1) in cards:
                    for q in cards[m.group(1)]["quals"].get(m.group(2), []):
                        if q not in text:
                            e.append(f"限定詞遺失：用了 {ev}，但本頁沒有寫出它的限定「{q}」")
            for g in GENERALIZERS:
                if g in text and g not in plain_corpus:
                    e.append(f"概括詞「{g}」不在被引用的 wiki 頁（可能誇大）")
            for q in re.findall(r"「([^」]{1,30})」", text):
                if q not in plain_corpus:
                    e.append(f"引號詞「{q}」不在被引用的 wiki 頁（未標記的比喻或自創說法？）")
        if e:
            bad[d["n"]] = e
    print(f"檢查 {checked} 頁")
    if bad:
        print(f"FAIL：{len(bad)} 頁需退回逐頁稿 → {sorted(bad)}")
        for n, es in sorted(bad.items()):
            for x in es:
                print(f"- slide {n:02d}: {x}")
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
