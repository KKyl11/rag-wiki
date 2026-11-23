---
name: topic-slides
description: 只用本專案 wiki/ 的內容，把一個主題做成 8–15 頁的教學 HTML 簡報。依 docs/workflow.md 的 graph 執行（檢索→覆蓋率→證據卡→大綱→逐頁稿→忠實度→渲染→渲染檢查），每關用 scripts/ 的腳本與獨立 subagent 檢查，狀態寫在 runs/run-NNN/。使用者說「/topic-slides <主題>」或要用 wiki 做簡報時使用。
---

# /topic-slides <主題>

流程圖、每個節點的輸入輸出與退回路線：`docs/workflow.md`（**先讀**）。本檔是執行用的檢查表。

## 🎯 目標
只用 `wiki/` 的內容，產出讓**完全不懂該主題的大學生**看得懂的教學 HTML 簡報（8–15 頁）。

## 🚧 限制
- 只能用 wiki；不能讀 `raw/` 補內容，不能用模型自己的知識硬湊，不能編數字。
- 數字一律照 wiki 原樣寫（含單位與寫法，例如 `$314 million`、`200,000 tokens`）。
- 自創比喻必須寫成 `> 🎓 教學比喻（非來源內容）：...`，且不得含數字或事實主張。
- 有 ⚖️ 矛盾標註的主題，簡報要並陳兩說。
- 渲染不能改字；版面問題只能改 `scripts/deck_template.html` 的 CSS。

## ✅ 完成標準（全部以腳本 exit code 或獨立審查結果判定）
| 關卡 | 指令／審查 |
|---|---|
| G1 | `python scripts/check_coverage.py runs/run-NNN --stage retrieve`（exit 2 = 停） |
| G1b | `python scripts/check_coverage.py runs/run-NNN --stage cards` |
| G2 | `python scripts/check_coverage.py runs/run-NNN --stage outline` ＋ subagent：`reviewers/outline.md` |
| G3 | `python scripts/check_citations.py runs/run-NNN` ＋ subagent：`reviewers/faithfulness.md` |
| G4 | `python scripts/check_deck.py runs/run-NNN --screenshots` ＋ subagent：`reviewers/coverage.md` |

## 🛑 停止條件
- 相關 wiki 頁面 < 3 → 停下回報「資料不足」。
- 每個關卡最多 3 輪；N4 小 loop 最多 2 輪；N5 小 loop 最多 3 輪。改滿仍不過 → 記錄在 `report.md`，以最佳版本繼續。
- 全過 → 交件，請使用者最終驗收。

## ⏰ 觸發
使用者輸入 `/topic-slides <主題>`，或要求用 wiki 做某主題的簡報。

## 執行步驟
1. 建 `runs/run-NNN/`（NNN 為下一個編號）與 `report.md`（表頭見下）。
2. **N1**：讀 `wiki/index.md`，選出相關頁面寫入 `sources.md`：
   ```
   ## 相關頁面
   - wiki/concepts/rag.md — 選頁理由
   ## 來源
   - lewis2020
   ```
   「來源」必須等於這些頁面 frontmatter `sources` 的聯集。→ **G1**。
3. **N2**：每個來源開一張 `cards/<key>.md`（只看與該來源有關的頁面，只收引用該來源的內容）：
   ```
   ---
   source: lewis2020
   wiki_pages: [sources/lewis2020.md, concepts/rag.md]
   ---
   - E1: 主張（照 wiki 原文數字） 〔限定：實驗條件／範圍／歸屬〕 [wiki: sources/lewis2020.md] [src: lewis2020, p.6]
   ```
   **v2**：含數字的項目必須標〔限定：…〕，限定詞要**原樣**取自 wiki（例：「Naive RAG」「作者認為」「Podcast／新聞」）；主張屬於某變體、某實驗或某人看法時也要標。
   → **G1b**。
4. **N3**：寫 `outline.md`（教學結構見下）：
   ```
   ## Slide 3: 標題
   - 教學目標: 學生看完能說出……
   - evidence: lewis2020#E1, gao2023#E2
   - wiki: concepts/llm-knowledge-limits.md
   ```
   → **G2**（腳本＋開新 subagent，只給 `outline.md` 與 `cards/`，用 `reviewers/outline.md` 的指示）。
5. **N4**：每頁寫 `drafts/slide-NN.md`，只能用該頁大綱與對應卡片：
   ```
   ---
   slide: 3
   title: LLM 為什麼會答錯或過時？
   section: 問題
   layout: content        # cover | content
   evidence: [lewis2020#E1]
   wiki: [concepts/llm-knowledge-limits.md]
   ---
   - 條列……
   ```
   可用語法：`### 小標`、條列、`**粗體**`、表格、`> 重點`、`> 🎓 教學比喻（非來源內容）：`、`> ⚖️ 兩說並陳`、```` ```flow ````（`A → B → C`）、```` ```quiz ````（`Q: … || A: …`）。
   每頁寫完跑 `check_citations.py --slides N`（v2：另查限定詞保留、概括詞、引號詞），最多修 2 輪。
   寫稿守則（v2，來自 run-001 的失敗）：用到帶〔限定〕的證據就寫出限定詞；不要加「常、總是、一定、保證」等概括詞；自己的說法不要加「」；不要自己把 wiki 的並列項目重新歸類；表格的「＋」「→」要符合 wiki 原意。→ **G3**（腳本＋開新 subagent，只給逐頁稿與被引用 wiki 頁）。
6. **N5**：`python scripts/render_deck.py runs/run-NNN`，再跑 `check_deck.py --screenshots`，看截圖調 CSS（最多 3 輪）。→ **G4**（腳本＋開新 subagent 審覆蓋率，只給 deck 文字與被引用 wiki 頁）。
7. **N6**：`report.md` 寫總結，請使用者驗收。

## 建議教學結構（零基礎讀者）
開場問題 → LLM 為什麼會答錯或過時 → 核心概念（比喻＋圖解）→ 運作流程（切塊、嵌入、檢索、生成）→ 具體例子 → 進階變形 → 限制與爭議 → 與相關做法比較 → 重點回顧＋小測驗 → 參考資料。

## report.md 格式
```
| # | 輪次 | 節點 | 檢查項目 | 結果 | 失敗原因 | 退回到 |
|---|---|---|---|---|---|---|
```
每通過或失敗一個關卡就加一列；腳本完整輸出存到 `checks/`，AI 審查存到 `reviews/`；每個節點、每輪修正都 commit：`runN: <節點> roundK - <做了什麼>`。
