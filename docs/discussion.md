# 先討論：建立 RAG LLM Wiki 前的需求釐清

> 這份文件是「先討論、後生成」（課程第 29–33 頁）的證據。
> 流程：AI 先讀課程簡報 → 確認 7 篇候選資料連結有效 → 列出 10 個釐清問題＋建議答案 → **停下等使用者回覆** → 收到回覆後才建立任何 Wiki 檔案。
> 日期：2026-11-23

## 討論前的準備

- 已讀完 `docs/course-slides.pdf`（53 頁），採用的觀念：loop 五件事與剎車（p.21–23）、大圈小圈（p.26）、先討論再建 Wiki（p.29–35）、Loop 版／Graph 版簡報流程（p.41–47）。
- 7 篇候選資料連結全部以 `curl` 確認回應 HTTP 200（arXiv abs 頁標題以 `citation_title` meta 核對）。

## AI 提出的問題與建議答案

**Q1. 這個 Wiki 是給誰看的？**
建議：Wiki 的主要讀者是「之後要用 Wiki 做簡報的 AI agent」與我本人，所以頁面要精確、可被引用；「完全不懂 RAG 的大學生」是**簡報**的讀者，白話化在簡報階段才做。

**Q2. 要哪些頁面類型？**
建議 4 類：
- `wiki/sources/`：每篇來源一頁（書目、核心主張、關鍵數字＋頁碼、限制）
- `wiki/concepts/`：概念頁（RAG、chunking、embedding、retriever、reranking、Self-RAG、GraphRAG、Contextual Retrieval、Lost in the Middle、LLM Wiki…）
- `wiki/comparisons/`：比較頁（RAG vs 長上下文、RAG vs fine-tuning、RAG vs LLM Wiki）
- 另有 `index.md`、`log.md`；不做人物頁。

**Q3. 用什麼語言？**
建議：繁體中文（台灣用語），專有名詞首次出現寫成「檢索器（retriever）」，之後可直接用英文；直接引文保留英文原句、每則 ≤25 個英文字，其餘一律中文轉述。

**Q4. 出處要多細？**
建議：每個段落／條列項至少一個出處，格式 `[src: lewis2020, p.3]`；PDF 標頁碼，網頁標小節標題。**所有數字都必須有出處且附頁碼／小節。**

**Q5. 資料互相矛盾怎麼辦？**
建議：不由 AI 擅自裁決。在概念頁加 `> ⚖️ 矛盾：` 區塊，並列兩方說法與出處、註明可能原因（年代、實驗設定不同），並記入 `log.md`；簡報若用到要呈現兩種說法。

**Q6. 一次一篇還是批次 ingest？**
建議：一次一篇，每篇 ingest 後更新 wiki、`index.md`、`log.md` 並 commit（課程 p.35）。順序由基礎到進階：Lewis 2020 → Survey → Lost in the Middle → Self-RAG → GraphRAG → Contextual Retrieval → Karpathy gist。

**Q7. 之後要產出什麼？**
建議：8–15 頁教學 HTML 簡報，每頁頁尾標對應 wiki 頁面。因此概念頁要有「一句話白話定義」；比喻優先用來源原有的（例：Survey 把 RAG 比作給模型一本量身訂做的課本），若需自創比喻要標「教學比喻（非來源內容）」且比喻內不得含事實主張。

**Q8. lint 要檢查什麼？**
建議 `scripts/lint_wiki.py` 檢查：(a) 斷的內部連結 (b) 孤兒頁 (c) 沒有出處的段落 (d) 出處 key 不在來源清單 (e) 頁面未列入 `index.md` (f) 矛盾區塊缺兩方出處 (g) frontmatter 缺 `type`／`sources`／`updated`。

**Q9. 要 ingest 哪些資料？**
建議 7 篇全收（皆已確認有效），超過最低 5 篇，讓覆蓋率關卡有餘裕，也支撐「RAG vs LLM Wiki」那頁：

| key | 資料 | 形式 |
|---|---|---|
| lewis2020 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks（arXiv 2005.11401） | PDF |
| gao2023 | Retrieval-Augmented Generation for Large Language Models: A Survey（arXiv 2312.10997） | PDF |
| liu2023 | Lost in the Middle: How Language Models Use Long Contexts（arXiv 2307.03172） | PDF |
| asai2023 | Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection（arXiv 2310.11511） | PDF |
| edge2024 | From Local to Global: A Graph RAG Approach to Query-Focused Summarization（arXiv 2404.16130） | PDF |
| anthropic2024 | Anthropic, "Introducing Contextual Retrieval" | 網頁→md |
| karpathy-llmwiki | Karpathy, `llm-wiki.md` gist | 網頁→md |

**Q10. raw/ 原始資料怎麼保存？**
建議：論文存 arXiv 原始 PDF；網頁轉 markdown，檔頭保留原網址與抓取日期；`raw/` 唯讀不修改，AI 只改 `wiki/`；打包時 PDF 若太大可排除並在 README 列原始連結。

## 使用者回覆（原文）

> 照預設

## 結論

10 題全部採用建議答案。下一步：依此寫 `docs/requirements.md`，再生成 `AGENTS.md`，並以 `docs/requirements-check.md` 逐條對照。
