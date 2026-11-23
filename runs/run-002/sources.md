# N1 檢索結果（run-002，workflow v2）：RAG 是什麼？讓 AI 先查資料再回答

- 主題：RAG（給完全不懂 RAG 的大學生）
- 做法：讀 `wiki/index.md`，依建議教學結構（問題→概念→流程→例子→進階→限制→比較）挑頁面；只看 wiki，不讀 raw/。

## 相關頁面
- wiki/concepts/rag.md — 核心定義、元件、為什麼需要
- wiki/concepts/llm-knowledge-limits.md — 「LLM 為什麼會答錯或過時」
- wiki/concepts/parametric-vs-nonparametric-memory.md — 核心概念的比較表、換索引更新知識
- wiki/concepts/rag-paradigms.md — 運作流程（索引→檢索→生成）、三種範式
- wiki/concepts/chunking.md — 流程中的切塊
- wiki/concepts/retriever.md — 流程中的嵌入與檢索、BM25
- wiki/concepts/reranking.md — 進階：重新排序
- wiki/concepts/contextual-retrieval.md — 進階變形：Contextual Retrieval
- wiki/concepts/self-rag.md — 進階變形：Self-RAG
- wiki/concepts/graphrag.md — 進階變形：GraphRAG
- wiki/concepts/lost-in-the-middle.md — 限制：Lost in the Middle
- wiki/comparisons/rag-vs-long-context.md — 爭議：長上下文 vs RAG（含 ⚖️ 矛盾）
- wiki/comparisons/rag-vs-fine-tuning.md — 比較與來源原有比喻（課本）
- wiki/comparisons/rag-vs-llm-wiki.md — 呼應本作業：RAG vs LLM Wiki
- wiki/concepts/llm-wiki.md — LLM Wiki 架構
- wiki/sources/lewis2020.md — 原始論文：具體例子（換索引、人工評估）
- wiki/sources/gao2023.md — Survey：流程、缺點、比較
- wiki/sources/liu2023.md — Lost in the Middle 實驗數字
- wiki/sources/asai2023.md — Self-RAG 細節
- wiki/sources/edge2024.md — GraphRAG 細節
- wiki/sources/anthropic2024.md — Contextual Retrieval 細節、何時不需要 RAG
- wiki/sources/karpathy-llmwiki.md — LLM Wiki 原文

## 來源
- lewis2020
- gao2023
- liu2023
- asai2023
- edge2024
- anthropic2024
- karpathy-llmwiki
