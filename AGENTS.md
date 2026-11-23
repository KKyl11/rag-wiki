# AGENTS.md — RAG LLM Wiki 維護手冊

> 本檔是 Karpathy LLM Wiki 架構中的「schema」層。Claude Code 透過 `CLAUDE.md` 的 `@AGENTS.md` 讀取本檔；其他 agent 直接讀本檔。
> 需求來源：`docs/requirements.md`（R1–R18），對照表：`docs/requirements-check.md`。

## 1. 這個 Wiki 是什麼、給誰看（R1）
- 主題：RAG（Retrieval-Augmented Generation，檢索增強生成）與其進階變形、限制，以及 LLM Wiki 本身。
- 主要讀者：**之後要用 Wiki 做簡報的 AI agent** 與作者本人。頁面要精確、每句可追溯，不必白話。
- 下游簡報的讀者：**完全不懂 RAG 的大學生**。
- 白話化、比喻、教學順序屬於**簡報階段**（見 `.claude/skills/topic-slides/SKILL.md`），不寫進 Wiki 正文。

## 2. 三層架構與權限（R10）
| 層 | 路徑 | 誰可以改 |
|---|---|---|
| Raw sources | `raw/` | **唯讀**。只有使用者新增檔案；AI 不得修改或刪除。 |
| Wiki | `wiki/` | AI 全權維護。 |
| Schema | `AGENTS.md` | AI 提議、使用者確認後才改。 |
- 論文存 arXiv 原始 PDF（`raw/<key>.pdf`）；網頁存成 markdown（`raw/<key>.md`），檔頭必須有 `source_url` 與 `fetched` 日期。
- `raw/` 不放個資或機密文件。
- 打包繳交時，PDF 若太大可排除在 zip 外，但 `README.md` 必須列出每篇的原始連結。

## 3. 頁面類型與 frontmatter（R2）
| type | 路徑 | 內容 |
|---|---|---|
| `source` | `wiki/sources/<key>.md` | 每篇來源一頁：書目、一句話摘要、核心主張、關鍵數字（附頁碼）、限制、相關概念連結 |
| `concept` | `wiki/concepts/<slug>.md` | 一個概念一頁：**一句話白話定義**、說明、關鍵數字、與其他概念的關係 |
| `comparison` | `wiki/comparisons/<slug>.md` | 兩個以上做法的比較（建議用表格） |
| — | `wiki/index.md`, `wiki/log.md` | 目錄與時間線（見 §7） |

每個 `source`／`concept`／`comparison` 頁開頭必須有 YAML frontmatter：
```yaml
---
type: concept            # source | concept | comparison
title: 檢索增強生成（RAG）
sources: [lewis2020, gao2023]   # 本頁引用到的所有來源 key
updated: 2026-11-23
---
```
`source` 頁另加 `key`、`url`、`raw`（raw 檔路徑）。不做人物頁。檔名用小寫英文與連字號。

## 4. 語言（R3）
- 繁體中文（台灣用語）。專有名詞第一次出現寫「中文（English）」，之後可直接用英文。
- 直接引文保留英文原句、加引號，**每則 ≤25 個英文字**；其餘一律中文轉述。

## 5. 出處規則（R4）
- 格式：PDF 用 `[src: <key>, p.<N>]`，N 是 **PDF 檔的實體頁序（第 1 頁起算）**，不是期刊頁碼；網頁用 `[src: <key>, §<小節標題>]`。
- **每個段落、每個條列項、每個表格資料列**至少一個出處。標題、frontmatter、程式碼區塊除外。
- **所有數字**（百分比、數量、年份以外的實驗數值）必須在同一句或同一列附出處與頁碼／小節。
- 只寫來源真的有的內容；找不到出處的句子就刪掉，不要用模型自己的知識補。
- 來源 key 必須對應到 `wiki/sources/<key>.md`。目前的 key：

| key | 來源 |
|---|---|
| lewis2020 | Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks（arXiv 2005.11401） |
| gao2023 | Gao et al., Retrieval-Augmented Generation for Large Language Models: A Survey（arXiv 2312.10997） |
| liu2023 | Liu et al., Lost in the Middle: How Language Models Use Long Contexts（arXiv 2307.03172） |
| asai2023 | Asai et al., Self-RAG（arXiv 2310.11511） |
| edge2024 | Edge et al., From Local to Global: A Graph RAG Approach（arXiv 2404.16130） |
| anthropic2024 | Anthropic, Introducing Contextual Retrieval（網頁） |
| karpathy-llmwiki | Karpathy, LLM Wiki（gist） |

## 6. 矛盾處理（R5）
- 不由 AI 擅自裁決哪一方正確。在相關概念頁加：
  ```
  > ⚖️ 矛盾：<主題>
  > - A 說法…… [src: a, p.N]
  > - B 說法…… [src: b, p.M]
  > - 可能原因：……（年代／實驗設定／定義不同）
  ```
- 矛盾區塊必須引用**至少兩個不同來源**；同時在 `log.md` 記一筆 `contradiction`。
- 簡報若用到有矛盾的主題，要呈現兩種說法。

## 7. index.md 與 log.md
- `wiki/index.md`：依類別（Sources / Concepts / Comparisons）列出**每一頁**，格式 `- [標題](相對路徑) — 一句話摘要`。每次 ingest 都更新。
- `wiki/log.md`：只能附加（append-only），每筆開頭固定格式 `## [YYYY-MM-DD] <ingest|lint|query|contradiction|fix> | <標題>`，下方列出新增／修改的頁面。

## 8. 工作流程

### 8.1 Ingest（R6、R9）：一次一篇
1. 讀 `raw/<key>`（PDF 先轉文字，記下實體頁碼）。
2. 建立 `wiki/sources/<key>.md`。
3. 更新或新增受影響的 concept／comparison 頁（一篇可能動到多頁）；新數字一律附頁碼。
4. 與既有頁面比對；有衝突就依 §6 標註。
5. 更新 `index.md`，在 `log.md` 附加一筆 ingest。
6. 執行 `python scripts/lint_wiki.py`，沒有 error 才 commit：`ingest(<key>): <摘要>`。
- 順序：lewis2020 → gao2023 → liu2023 → asai2023 → edge2024 → anthropic2024 → karpathy-llmwiki。

### 8.2 Query
先讀 `index.md` 找相關頁面，再讀頁面作答並附出處；有長期價值的答案（比較、分析）可寫回 wiki 成新頁並更新 index/log。

### 8.3 Lint（R8）
`python scripts/lint_wiki.py` 檢查：(a) 斷的內部連結 (b) 孤兒頁（沒有其他 wiki 頁連入；index/log 除外）(c) 沒有出處的段落／條列／表格列 (d) 出處 key 不存在 (e) 頁面未列入 `index.md` (f) 矛盾區塊少於兩個來源 (g) frontmatter 缺 `type`/`sources`/`updated`；另加 (h)「教學比喻」行含數字 (i) 本檔超過 12,000 字元 (j) 區塊裡的數字在所引用的 raw 頁面找不到。結果寫入 `docs/lint-report.md`。error 必須修到 0。
- 數字一律保留原文的單位與寫法（例：寫 `$314 million`，不要換算成「3.14 億美元」），否則 (j) 無法驗證。
- 修改 lint 後要跑 `python scripts/test_lint.py`（故意埋錯，確認每一項都抓得到）。

### 8.4 產出簡報（R7、R14）
用 skill `.claude/skills/topic-slides/SKILL.md`（`/topic-slides <主題>`）。流程圖與節點規則見 `docs/workflow.md`。要點：
- 簡報**只能使用 wiki 內容**；資料不足（相關頁面 < 3）就停下，不硬湊。
- 8–15 頁，每頁頁尾標對應的 wiki 頁面。
- 比喻優先用來源原有的；自創比喻必須標「教學比喻（非來源內容）」，且不得含事實或數字。

## 9. 驗證與審查（R12、R13）
- 「檢查一下」不算驗證。能用程式檢查的，都寫成 `scripts/` 裡的腳本，**以腳本 exit code 判定通過與否**。
- AI 審查（忠實度、覆蓋率）一律交給**新的 subagent**，只給「成品＋被引用的 wiki 頁面」，不給生成過程、不給先前對話。不要叫生成者審自己的作品。

## 10. 剎車（R15）
- 每個 loop 最多 3 輪。改滿 3 輪仍不過：在 report 記錄未通過項目，以目前最佳版本繼續，不無限重來。
- 每一輪只修檢查報告列出的問題，不順手改別的。

## 11. git 與紀錄（R11、R17）
- git 就是檢查紀錄。每個有意義的步驟都 commit，訊息格式 `<階段>: <節點> [roundN] - <做了什麼>`，例：`run1: drafts round2 - fix p6 faithfulness`。
- report 中的失敗與退回必須是真實發生的；不捏造錯誤、不隱藏錯誤。

## 12. 本檔維護（R16、R18）
- `CLAUDE.md` 只有一行 `@AGENTS.md`；規則只維護在本檔。
- 本檔保持在 12,000 字元以內，流程細節放 skill 與 `docs/workflow.md`。
