# RAG Wiki — Log

> append-only。每筆格式：`## [YYYY-MM-DD] <ingest|lint|query|contradiction|fix> | <標題>`

## [2026-11-23] init | 建立 wiki 架構
- 依 docs/discussion.md（使用者回覆「照預設」）與 docs/requirements.md 建立 AGENTS.md、CLAUDE.md、raw/、wiki/index.md、wiki/log.md

## [2026-11-23] ingest | lewis2020 — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- 新增：sources/lewis2020.md、concepts/rag.md、concepts/parametric-vs-nonparametric-memory.md、concepts/retriever.md、concepts/chunking.md、concepts/llm-knowledge-limits.md
- 發現：論文內部數字不一致（p.6 內文 17% vs p.8 Table 4 的 11.7%／17.7%），已在 source 頁註記、簡報禁用
- lint：第一次 FAIL 1 error（index.md 的格式範例 `[標題](路徑)` 被當成斷連結，是 lint 腳本誤判）→ 修 lint_wiki.py 忽略行內程式碼 → PASS

## [2026-11-23] ingest | gao2023 — Retrieval-Augmented Generation for Large Language Models: A Survey
- 新增：sources/gao2023.md、concepts/rag-paradigms.md、concepts/reranking.md、comparisons/rag-vs-fine-tuning.md、comparisons/rag-vs-long-context.md
- 更新：concepts/rag.md、concepts/chunking.md、concepts/retriever.md、concepts/llm-knowledge-limits.md
- 待追蹤：gao2023 p.10 說過長脈絡會造成 Lost in the middle、p.14 引述「加入不相關文件反而提升準確率 30% 以上」——等 liu2023、anthropic2024 ingest 後判斷是否構成矛盾
- lint：PASS（0 error）

## [2026-11-23] ingest | liu2023 — Lost in the Middle: How Language Models Use Long Contexts
- 新增：sources/liu2023.md、concepts/lost-in-the-middle.md
- 更新：comparisons/rag-vs-long-context.md、concepts/reranking.md、sources/gao2023.md（加連結）

## [2026-11-23] contradiction | 多放文件到脈絡是好是壞（liu2023 vs gao2023 引述的 Cuconasu）
- 標註於 comparisons/rag-vs-long-context.md 的 ⚖️ 區塊；不裁決，註明實驗設定不同、Cuconasu 原文未收錄
- lint：PASS（0 error）

## [2026-11-23] ingest | asai2023 — Self-RAG
- 新增：sources/asai2023.md、concepts/self-rag.md
- 更新：concepts/rag-paradigms.md（連到 Self-RAG）、concepts/rag.md（新增「進階變形」）
- 註記：Table 2 在 PDF 轉文字後欄位錯亂，數字無法可靠對應欄位，因此只收錄內文明確寫出的結論，不收表格數字
- lint：PASS（0 error）

## [2026-11-23] ingest | edge2024 — From Local to Global: A GraphRAG Approach
- 新增：sources/edge2024.md、concepts/graphrag.md
- 更新：concepts/rag.md（進階變形）、concepts/chunking.md（600-token＋100 重疊）
- lint：PASS（0 error）

## [2026-11-23] ingest | anthropic2024 — Introducing Contextual Retrieval
- 新增：sources/anthropic2024.md、concepts/contextual-retrieval.md
- 更新：concepts/rag.md、concepts/chunking.md、concepts/retriever.md、concepts/reranking.md、comparisons/rag-vs-long-context.md
- 比對：「片段數量」與 liu2023 不衝突（Anthropic 只比到 20 片段，liu2023 說超過 20 篇效益很小），不另立矛盾區塊
- lint：PASS（0 error）

## [2026-11-23] ingest | karpathy-llmwiki — LLM Wiki (gist)
- 新增：sources/karpathy-llmwiki.md、concepts/llm-wiki.md、comparisons/rag-vs-llm-wiki.md
- 更新：concepts/rag.md（與 LLM Wiki 的對照）
- 自我修正：rag-vs-llm-wiki 初稿有一句「本作業的簡報流程就是以 wiki 為知識庫的 RAG」是我的推論、來源沒有寫，改成只寫 §Operations 的原意
- lint：PASS（0 error）

## [2026-11-23] lint | 全面 lint＋lint 自我測試
- test_lint.py 抓到 lint 漏洞：「相關頁面」底下全部豁免出處 → 縮小為只豁免純連結條列
- 新增 (j) 數字對照 raw：第一次 FAIL 14（10 個 lint 誤判、3 個 wiki 換算單位後無法驗證）→ 修正
- 修正頁面：concepts/contextual-retrieval.md、sources/edge2024.md、sources/lewis2020.md（數字改回原文寫法）
- 詳見 docs/lint-history.md；最終 PASS 0 error，自我測試 13/13

## [2026-11-23] query | run-001 覆蓋率審查發現的缺口寫回 wiki
- 起因：runs/run-001/reviews/coverage-round1.md 指出簡報沒說明「檢索失敗率」的意思、「勝率」由誰評；這兩點 raw 有但 wiki 沒寫，簡報因此無法使用
- 更新：concepts/contextual-retrieval.md（失敗率定義、降幅是相對降幅、哪幾列是疊加）、concepts/graphrag.md（LLM 當評審）
- 依 Karpathy LLM Wiki 的 Query 操作：有價值的查詢結果寫回 wiki
