"""統計 runs/run-NNN/report.md：每個節點／關卡失敗幾次、退回幾次、大圈還是小圈。

用法：python scripts/report_stats.py runs/run-001 [runs/run-002 ...]
解析 report.md 的表格列：| # | 輪次 | 節點 | 檢查項目 | 結果 | 失敗原因 | 退回到 |
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# 節點在 graph 中的順序，用來判斷「退回跨過幾個節點」（大圈 vs 小圈）
ORDER = ["N1", "G1", "N2", "G1b", "N3", "G2", "N4", "G3", "N5", "G4", "N6"]


def node_key(s):
    m = re.match(r"\s*(G1b|G\d|N\d)", s)
    return m.group(1) if m else s.strip()


def parse(run):
    rows = []
    for line in (Path(run) / "report.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and cells[0].isdigit():
            rows.append(dict(zip(["n", "round", "node", "check", "result", "reason", "back"], cells)))
    return rows


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    for run in sys.argv[1:]:
        rows = parse(run)
        fails = [r for r in rows if "FAIL" in r["result"]]
        by_node = Counter(node_key(r["node"]) for r in fails)
        kinds = defaultdict(list)
        big = small = 0
        for r in fails:
            src = node_key(r["node"])
            # 從退回文字裡找出目標節點，取最遠的那個
            m = re.findall(r"N\d", r["back"])
            if src in ORDER and m:
                far = min(ORDER.index(x) for x in m if x in ORDER)
                gap = ORDER.index(src) - far
                if gap >= 3:
                    big += 1
                else:
                    small += 1
            kinds[src].append(r["reason"][:80])
        print(f"## {run}")
        print(f"- 表格列數：{len(rows)}；失敗：{len(fails)}")
        print(f"- 失敗次數（依節點）：{dict(by_node.most_common())}")
        print(f"- 退回：小圈（退回 1–2 個節點）{small} 次、大圈（跨 3 個以上節點）{big} 次")
        brakes = [r for r in rows if "剎車" in r["back"]]
        print(f"- 觸發剎車：{len(brakes)} 次")
        for k, v in kinds.items():
            for x in v:
                print(f"  - {k}: {x}")
        print()


if __name__ == "__main__":
    main()
