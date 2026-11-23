# 繳交內容（可直接複製貼上到表單）

> 每一項後面的「證據」是本專案（`rag-wiki/`）內的檔案路徑。

> **公開連結**
> - 教學簡報：https://kkyl11.github.io/rag-wiki/deck.html
> - LLM Wiki（目錄）：https://github.com/KKyl11/rag-wiki/blob/main/wiki/index.md
> - 專案 repo：https://github.com/KKyl11/rag-wiki
> - 流程圖（GitHub 會直接渲染 Mermaid）：https://github.com/KKyl11/rag-wiki/blob/main/docs/workflow.md
> - 執行紀錄：https://github.com/KKyl11/rag-wiki/blob/main/runs/run-001/report.md 、 https://github.com/KKyl11/rag-wiki/blob/main/runs/run-002/report.md
> - 反思：https://github.com/KKyl11/rag-wiki/blob/main/docs/reflection.md
> - 公開版不含課程簡報 PDF 與 raw/ 原始資料副本；完整 commit 歷史在 docs/git-log.md


---

## 1. LLM Wiki 主題與簡短介紹

**主題：RAG（Retrieval-Augmented Generation，檢索增強生成）**

這個 Wiki 整理「讓 AI 先查資料再回答」的 RAG 技術，涵蓋以下內容：
- 為什麼需要 RAG：LLM 會幻覺、知識過時、無法追溯出處
- 基本流程：切塊 → 嵌入 → 檢索 → 生成
- 進階變形：Self-RAG、GraphRAG、Contextual Retrieval
- 限制與爭議：Lost in the Middle、長上下文 vs RAG
- RAG 和 LLM Wiki 本身的差別

建立方式依 Karpathy 的 LLM Wiki 架構（raw／wiki／schema 三層），並採用「先討論、後生成」：
1. AI 先讀課程簡報，列出 10 個釐清問題，每題附建議答案。
2. 等我回覆「照預設」之後，才建立 `AGENTS.md` 和資料夾。
3. 把需求摘要（R1–R18）逐條對照 `AGENTS.md`，找到 2 處缺漏並補上。
4. 一次 ingest 一篇、每篇各 commit 一次，共 7 篇（5 篇論文＋2 篇網頁）。

成果：
- 共 22 頁：7 個來源頁、12 個概念頁、3 個比較頁。
- 每一段都附頁碼出處；資料互相矛盾的地方用 ⚖️ 並陳兩說。
- lint 除了檢查結構，還會**逐一驗證 wiki 裡的每個數字確實出現在原始 PDF 的那一頁**。

證據：`docs/discussion.md`、`docs/requirements.md`、`docs/requirements-check.md`、`AGENTS.md`、`wiki/log.md`、`git log`

## 2. LLM Wiki 連結或成果

- Wiki 目錄：`wiki/index.md`（22 頁）— https://github.com/KKyl11/rag-wiki/blob/main/wiki/index.md
- Wiki 時間線：`wiki/log.md`（7 次 ingest、1 次 contradiction、lint、query 寫回）
- Lint 結果：`docs/lint-report.md`（PASS，0 error）
- Lint 歷程：`docs/lint-history.md`。第一次 lint 全過，但 `scripts/test_lint.py` 故意埋錯後，發現 lint 自己有漏洞（相關頁面豁免太寬）。新增「數字對照原文」檢查後，又抓到 wiki 裡 3 個單位換算錯誤（例如把 `$314 million` 寫成「3.14 億」，原文找不到這個寫法）。
- 原始資料：`raw/`（5 篇 arXiv PDF、2 篇網頁 markdown，檔頭附原始網址）

## 3. 教學 HTML 簡報連結

- 簡報：https://kkyl11.github.io/rag-wiki/deck.html （檔案：`deck.html`，共 15 頁，是 run-002 的成品）
  - 單一檔案，用瀏覽器直接打開即可。
  - ← → 翻頁；按 A 顯示小測驗答案；按 F 全螢幕。
  - 每頁頁尾標出用到的 wiki 頁面，右下角有頁碼。
- 教學結構：開場問題 → LLM 為什麼會答錯或過時 → 核心概念（參數 vs 非參數記憶，附來源原有的比喻）→ 流程（索引 → 檢索 → 生成、切塊、嵌入與檢索）→ 具體例子（換索引實驗）→ 進階（Contextual Retrieval、Self-RAG、GraphRAG）→ RAG 也會答錯 → Lost in the Middle（⚖️ 兩說並陳）→ 長上下文爭議 → RAG vs LLM Wiki → 回顧＋小測驗 → 參考資料
- 每頁截圖：`runs/run-002/screenshots/`

## 4. loop / graph 的流程圖或文字說明

完整說明在 `docs/workflow.md`，包含 Mermaid 流程圖、每個節點的規格表與設計理由。

**流程**：檢索 wiki（N1）→ 覆蓋率關卡（G1，相關頁少於 3 頁就停）→ 證據卡（N2，每個來源一張、平行）→ 卡片關卡（G1b）→ 大綱（N3）→ 大綱檢查（G2：腳本＋獨立 AI 審查）→ 逐頁稿（N4）→ 忠實度檢查（G3：腳本＋獨立 AI 審查）→ 渲染 HTML（N5）→ 渲染檢查（G4：headless Chrome 量測＋獨立覆蓋率審查）→ 交件（N6）

**哪些步驟會重複**
- N4 逐頁稿：寫 → `check_citations` → 修，最多 2 輪。
- N5 渲染：渲染 → 量測溢出 → 調 CSS，最多 3 輪。
- 每個關卡最多退回 3 輪（剎車）。

**哪裡要檢查或重新生成**（退回路線都事先畫好）
- 錯在哪一頁，只退那一頁回 N4。
- 證據卡本身缺內容，退回 N2。
- 字太多，退回 N4 縮短；版面問題留在 N5 改 CSS。
- 缺子題，退回 N1。

**為什麼這樣設計**
- 各階段的標準完全不同，所以拆成 graph，不用單一 loop。
- 每個關卡緊接在產生錯誤的節點後面，讓「小圈」快速修正，「大圈」很少發生。
- 每一關只能看規定的輸入：證據卡只看一個來源；逐頁稿只看自己的卡片；渲染不能改字。
- 能用程式判斷的都交給腳本，以 exit code 判定；只有意思層次的問題交給獨立 subagent，而且只給它成品和來源。
- 誠實的取捨：課程中的「人工確認大綱」因截止時間改成 AI 大綱審查，加上使用者交件前的最終驗收。

證據：`docs/workflow.md`、`.claude/skills/topic-slides/SKILL.md`（`/topic-slides` 可重複呼叫）、`.claude/skills/topic-slides/reviewers/`、`scripts/`

## 5. 一次實際執行的結果或檢查紀錄

實際執行了兩次，每次都逐關記錄。

**run-001（workflow v1）**：`runs/run-001/report.md`，共 19 列紀錄、6 次失敗。
- G2 大綱被退 1 次：一頁塞了三個新概念。
- G3 忠實度連續 3 輪失敗：
  - 第 1 輪：15 頁中退回 4 頁（拿掉限定詞、加「常」、未標記的比喻、用了卡片以外的內容）。
  - 第 2 輪：退回 1 頁（拿掉「Naive RAG」限定）。
  - 第 3 輪：仍退回 1 頁（自行歸類），**觸發剎車**，記為未通過項目，帶到 run-002。
- N5 渲染溢出 2 次，調 CSS 解決。
- G4 覆蓋率審查 PASS，但順帶發現一個 G3 漏掉的「＋」符號問題。

**run-002（workflow v2）**：`runs/run-002/report.md`
- G3 第 1 輪：15 頁中退回 3 頁。
- G3 第 2 輪：退回 1 頁。
- 第 3 輪：**通過，15/15 頁**。
- 0 次大圈，0 次剎車。
- 渲染溢出 1 次，依 graph 退回 N4 縮短文字。

每一步都有 commit，可用 `git log --oneline --grep=run1` 和 `--grep=run2` 查看。腳本的完整輸出在 `runs/*/checks/`，AI 審查原文在 `runs/*/reviews/`。

## 6. 反思：哪個節點最常出錯？你如何調整檢查流程？

完整內容見 `docs/reflection.md`，v1 → v2 的修改紀錄見 `docs/workflow.md` §8。

**最常出錯的節點：G3 忠實度**（run-001 失敗 3 次、run-002 失敗 2 次）。但錯誤其實**產生在 N4 逐頁稿**：為了讓零基礎讀者看懂而簡化句子時，常見這幾種錯：
- 拿掉限定詞，例如把「Naive RAG 的問題」寫成「RAG 的問題」，或拿掉「兩個資料集的實驗」
- 加上概括詞，例如「常」
- 用了沒標記的比喻
- 自己幫 wiki 做歸類

v1 的腳本只檢查數字和出處，這些錯都要等到最後的 AI 審查才發現，每一輪都要重開一個審查者。

**把檢查往前移到哪裡**
- **N2 證據卡**：含數字的證據必須標 `〔限定：…〕`，限定詞要原樣出現在 wiki。
- **N4 寫稿的小 loop**：腳本檢查三件事：用到的證據的限定詞有沒有寫出來；有沒有 wiki 裡沒有的概括詞（常、總是、保證…）；「」引號裡的詞是否出現在 wiki。

**有沒有因此修改 workflow？** 有，改成 v2。graph 的節點和退回路線不變，只改檢查的位置。理由是課程 p.26：錯誤要在離源頭最近的地方被抓到。

**驗證效果**
- 回測：用 v2 檢查跑 run-001 的第一版逐頁稿，能提早抓到 G3 第 1 輪退回 4 頁中的 3 頁。
- 突變測試：故意拿掉限定詞，腳本確實會 FAIL。
- run-002 的失敗次數從 6 次降到 3 次，大圈從 1 次降到 0 次，剎車從 1 次降到 0 次；run-001 的那幾類錯沒有再出現。

**沒解決的部分**：「自行歸類」「拿掉歸屬」這種意思層次的錯，字串比對抓不到，仍然要靠 G3 的獨立 AI 審查。往前移的效果是讓 AI 審查只處理真正需要判斷的問題。
