# 需求摘要（由 docs/discussion.md 整理，使用者回覆「照預設」= 全部確認）

來源標記：D = 討論題號（docs/discussion.md），T = 任務全程規則，C = 課程簡報頁碼。

| ID | 需求 | 來源 |
|---|---|---|
| R1 | Wiki 讀者是「之後做簡報的 AI agent」與作者本人：頁面精確、可引用。簡報讀者才是零基礎大學生，白話化在簡報階段做。 | D-Q1 |
| R2 | 頁面類型：`wiki/sources/`（每來源一頁：書目、核心主張、關鍵數字＋頁碼、限制）、`wiki/concepts/`、`wiki/comparisons/`，加 `index.md`、`log.md`；不做人物頁。 | D-Q2 |
| R3 | 語言：繁體中文（台灣用語）；專有名詞首次出現「中文（English）」；直接引文保留英文、每則 ≤25 英文字，其餘中文轉述。 | D-Q3 |
| R4 | 出處：每段落／條列項至少一個 `[src: key, p.N]`（PDF 頁碼）或 `[src: key, §小節]`（網頁）；所有數字必須有出處且附頁碼／小節。 | D-Q4 |
| R5 | 矛盾：不擅自裁決；概念頁用 `> ⚖️ 矛盾：` 區塊並列兩方說法與出處、註明可能原因；記入 `log.md`；簡報若用到要呈現兩說。 | D-Q5 |
| R6 | 一次 ingest 一篇，順序 lewis2020 → gao2023 → liu2023 → asai2023 → edge2024 → anthropic2024 → karpathy-llmwiki；每篇更新 wiki、`index.md`、`log.md` 並 commit。 | D-Q6, C-p.35 |
| R7 | 下游產出是 8–15 頁教學 HTML 簡報，每頁頁尾標 wiki 頁面；概念頁要有「一句話白話定義」；比喻優先用來源原有，自創比喻標「教學比喻（非來源內容）」且不含事實主張。 | D-Q7 |
| R8 | lint 檢查：(a) 斷連結 (b) 孤兒頁 (c) 無出處段落 (d) 出處 key 不存在 (e) 未列入 index (f) 矛盾區塊缺兩方出處 (g) frontmatter 缺 `type`/`sources`/`updated`。 | D-Q8 |
| R9 | Ingest 7 篇：lewis2020、gao2023、liu2023、asai2023、edge2024、anthropic2024、karpathy-llmwiki。 | D-Q9 |
| R10 | raw/：論文存原始 PDF；網頁轉 markdown、檔頭留原網址與抓取日期；raw/ 唯讀，AI 只改 wiki/；打包時大 PDF 可排除並列連結。 | D-Q10 |
| R11 | git 就是檢查紀錄：每個有意義的步驟 commit，訊息看得出階段／節點／輪次。 | T-2, C-p.14 |
| R12 | 「檢查一下」不算驗證：能程式檢查的都寫成 `scripts/` 腳本，以腳本結果判定。 | T-3, C-p.14, p.22 |
| R13 | AI 審查（忠實度、覆蓋率）交給新的 subagent，只給成品＋被引用 wiki 頁，不給生成過程。 | T-4, C-p.22 |
| R14 | 簡報只能用 wiki 內容，不用模型自身知識硬湊，不編造數字或引用；資料不足就停。 | T-5, C-p.23 |
| R15 | 剎車：每個 loop 最多 3 輪，改滿仍不過就記錄並以最佳版本繼續。 | T-6, C-p.23 |
| R16 | `CLAUDE.md` 只寫一行 `@AGENTS.md`，規則統一寫在 `AGENTS.md`。 | T-7, C-p.15, p.34 |
| R17 | 誠實紀錄：report 裡的失敗與退回必須真實，不捏造、不隱藏。 | T-8 |
| R18 | 規則檔別寫太長（≤12,000 字元），細節拆到 skill。 | C-p.34 |
