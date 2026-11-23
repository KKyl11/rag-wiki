# Lint 執行歷程（階段 3）

最終結果：[`docs/lint-report.md`](lint-report.md)（由 `python scripts/lint_wiki.py` 自動產生）。
修正前的失敗報告存檔：[`docs/lint-report-before-fix.md`](lint-report-before-fix.md)。

| # | 時間點 | 指令 | 結果 | 問題 | 處理 |
|---|---|---|---|---|---|
| 1 | ingest lewis2020 後 | `lint_wiki.py` | FAIL 1 error | (a) `index.md` 的格式範例 `` `[標題](路徑)` `` 被當成斷連結——**lint 腳本誤判** | lint 改為忽略行內程式碼 → PASS |
| 2–6 | ingest gao2023、liu2023、asai2023、edge2024、anthropic2024 後 | `lint_wiki.py` | 每次 PASS | — | — |
| 7 | ingest karpathy-llmwiki 後 | `lint_wiki.py` | PASS（22 頁） | 但 PASS 不代表 lint 有用 → 寫 `scripts/test_lint.py` 故意埋錯測試 lint | — |
| 8 | lint 自我測試 | `test_lint.py` | **11/12**，(c) 沒抓到 | 「相關頁面」標題底下的所有內容都被豁免出處檢查，**沒出處的句子可以藏在那裡** | 豁免範圍縮小為「只有純連結的條列項」→ 12/12 |
| 9 | 加入 (j) 數字對照 raw | `lint_wiki.py` | **FAIL 14 error** | 10 個是 lint 誤判（日期 `2023-10-17` 被拆成數字、`1.` 條列編號、英文數字詞 "ten"）；**3 個是 wiki 真的寫錯形式**：`3.14 億美元`（原文 `$314 million`）、`100 萬 tokens`（原文 `1 million`）、`2018 年 12 月`（原文 `December 2018`）——單位換算後的數字在原文找不到，無法機械驗證 | lint 排除日期／條列編號、加入英文數字詞；wiki 改回原文寫法 → PASS |
| 10 | 最終 | `lint_wiki.py`、`test_lint.py` | **PASS 0 error**；自我測試 **13/13** | — | — |

## 學到的事
- lint 第一次全過時，其實有一個漏洞（相關頁面豁免）沒被發現——**要先證明檢查會失敗，PASS 才有意義**。
- 數字換算（億、萬、月份）是「看起來沒錯、但無法驗證」的高風險點。規則：wiki 與簡報的數字一律保留原文單位。這條規則之後也套用到簡報（見 `docs/workflow.md`）。
