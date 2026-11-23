"""覆蓋率關卡（graph 節點 G1、G2 的程式檢查部分）。

用法：
  python scripts/check_coverage.py <run_dir> --stage retrieve   # G1：相關 wiki 頁面 >= 3，否則 exit 2（停止整個 run）
  python scripts/check_coverage.py <run_dir> --stage cards      # G1b：每個來源都有證據卡、卡片只引用自己的來源與已檢索頁面
  python scripts/check_coverage.py <run_dir> --stage outline    # G2：8–15 頁、證據編號存在、每個來源至少被一張投影片用到
  --rules v2（預設）在 cards 階段多兩項（v1→v2 往前移的檢查，見 docs/workflow.md §8）：
     • 含數字的證據項目必須標〔限定：…〕（實驗條件／範圍／歸屬）
     • 每個限定詞必須原樣出現在該項目引用的 wiki 頁面
  --rules v1 重現 run-001 當時的規則
exit code：0 = PASS，1 = FAIL（退回），2 = STOP（資料不足，整個流程停下）
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import CITE_RE, QUAL_RE, WIKI_REF_RE, numbers_in, parse_cards, parse_frontmatter, parse_outline, parse_sources, wiki_path  # noqa: E402

MIN_PAGES = 3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--stage", required=True, choices=["retrieve", "cards", "outline"])
    ap.add_argument("--rules", default="v2", choices=["v1", "v2"])
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    run = Path(a.run)
    errs, info = [], []
    pages, keys = parse_sources(run)

    if a.stage == "retrieve":
        missing = [p for p in pages if not wiki_path(p).exists()]
        for p in missing:
            errs.append(f"sources.md 列出的頁面不存在：wiki/{p}")
        ok_pages = [p for p in pages if wiki_path(p).exists()]
        info.append(f"相關 wiki 頁面：{len(ok_pages)} 頁（門檻 {MIN_PAGES}）")
        # 來源清單必須等於這些頁面引用到的來源
        cited = set()
        for p in ok_pages:
            fm, _ = parse_frontmatter(wiki_path(p).read_text(encoding="utf-8"))
            cited |= set(fm.get("sources") or [])
        info.append(f"這些頁面引用到的來源：{sorted(cited)}")
        if set(keys) != cited:
            errs.append(f"sources.md 的「來源」清單 {sorted(keys)} 與頁面實際引用的來源 {sorted(cited)} 不一致")
        if len(ok_pages) < MIN_PAGES:
            print("\n".join(info))
            print(f"STOP：相關頁面少於 {MIN_PAGES} 頁，資料不足，不要硬湊。")
            sys.exit(2)

    elif a.stage == "cards":
        cards = parse_cards(run)
        for k in keys:
            if k not in cards:
                errs.append(f"來源 {k} 沒有證據卡（cards/{k}.md）")
            elif not cards[k]["items"]:
                errs.append(f"cards/{k}.md 沒有任何證據項目（格式：`- E1: ...`）")
        for k, c in cards.items():
            if k not in keys:
                errs.append(f"cards/{k}.md 的來源不在 sources.md 的來源清單")
            for eid, (claim, refs) in c["items"].items():
                if not refs:
                    errs.append(f"{k}#{eid} 沒有標 [wiki: 頁面]")
                for r in refs:
                    if r not in pages:
                        errs.append(f"{k}#{eid} 引用的 wiki/{r} 不在檢索結果 sources.md 裡（卡片只能用檢索到的頁面）")
                if a.rules == "v2":
                    bare = WIKI_REF_RE.sub("", CITE_RE.sub("", QUAL_RE.sub("", claim)))
                    quals = c["quals"].get(eid, [])
                    if numbers_in(bare) and not quals:
                        errs.append(f"{k}#{eid} 含數字但沒有標〔限定：…〕（實驗條件／範圍）")
                    wtext = "".join(wiki_path(r).read_text(encoding="utf-8") for r in refs if wiki_path(r).exists())
                    for q in quals:
                        if q not in wtext:
                            errs.append(f"{k}#{eid} 的限定詞「{q}」不在引用的 wiki 頁面裡")
                for inner in CITE_RE.findall(claim):
                    for part in inner.split(";"):
                        if part.split(",")[0].strip() != k:
                            errs.append(f"{k}#{eid} 混入其他來源：{part.strip()}（一張卡只能有一個來源）")
            info.append(f"cards/{k}.md：{len(c['items'])} 個證據項目")

    elif a.stage == "outline":
        cards = parse_cards(run)
        slides = parse_outline(run)
        info.append(f"大綱頁數：{len(slides)}")
        if not 8 <= len(slides) <= 15:
            errs.append(f"大綱 {len(slides)} 頁，不在 8–15 頁範圍")
        nums = [s["n"] for s in slides]
        if nums != list(range(1, len(slides) + 1)):
            errs.append(f"投影片編號不連續：{nums}")
        used_keys = set()
        for s in slides:
            for e in s["evidence"]:
                m = re.match(r"^([\w\-]+)#(E\d+)$", e)
                if not m:
                    errs.append(f"Slide {s['n']}：證據編號格式錯誤「{e}」（應為 key#E1）")
                    continue
                k, eid = m.groups()
                if k not in cards or eid not in cards[k]["items"]:
                    errs.append(f"Slide {s['n']}：證據 {e} 不存在")
                else:
                    used_keys.add(k)
            for w in s["wiki"]:
                if not wiki_path(w).exists():
                    errs.append(f"Slide {s['n']}：wiki/{w} 不存在")
        for k in keys:
            if k not in used_keys:
                errs.append(f"來源 {k} 沒有被任何一張投影片用到（課程 p.40：8 篇只用了 3 篇）")
        info.append(f"被用到的來源：{len(used_keys)}/{len(keys)}")

    print("\n".join(info))
    if errs:
        print(f"FAIL（{len(errs)}）")
        for e in errs:
            print(f"- {e}")
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
