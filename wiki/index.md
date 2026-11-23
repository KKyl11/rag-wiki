# RAG Wiki — Index

> 依類別列出 wiki 的每一頁。格式：`- [標題](路徑) — 一句話摘要`。每次 ingest 更新。

## Sources

- [Lewis et al. 2020 — RAG 原始論文](sources/lewis2020.md) — 提出 RAG：預訓練生成器＋可檢索的 Wikipedia 向量索引，一起微調
- [Gao et al. 2023 — RAG Survey](sources/gao2023.md) — 三種範式、檢索／生成／增強技術、評估與挑戰
- [Liu et al. 2023 — Lost in the Middle](sources/liu2023.md) — 相關資訊在長輸入中間時表現下降，呈 U 形曲線
- [Asai et al. 2023 — Self-RAG](sources/asai2023.md) — 模型自己決定何時檢索，用反思標記自我批判
- [Edge et al. 2024 — GraphRAG](sources/edge2024.md) — 知識圖＋群集摘要，回答整份語料的全域問題
- [Anthropic 2024 — Introducing Contextual Retrieval](sources/anthropic2024.md) — 替片段補脈絡＋BM25＋reranking，檢索失敗率最多降 67%
- [Karpathy — LLM Wiki](sources/karpathy-llmwiki.md) — 讓 LLM 持續維護互相連結的 wiki，知識編譯一次、持續更新

## Concepts

- [檢索增強生成（RAG）](concepts/rag.md) — 先檢索相關段落、再根據段落生成答案
- [參數記憶 vs 非參數記憶](concepts/parametric-vs-nonparametric-memory.md) — 模型背在參數裡的知識 vs 可替換的外部索引
- [檢索器（retriever）](concepts/retriever.md) — 挑出最相關段落的元件；dense 檢索與 BM25
- [切塊（chunking）](concepts/chunking.md) — 把長文件切成小段以便檢索
- [LLM 的知識限制](concepts/llm-knowledge-limits.md) — 幻覺、難以更新、無法追溯出處
- [RAG 三種範式與基本流程](concepts/rag-paradigms.md) — Naive（索引→檢索→生成）、Advanced、Modular
- [重新排序（reranking）](concepts/reranking.md) — 初步檢索後再精排，只留最相關片段
- [Lost in the Middle（中間迷失）](concepts/lost-in-the-middle.md) — 模型較會用開頭與結尾的資訊；對 RAG 的意義
- [Self-RAG（自我反思式 RAG）](concepts/self-rag.md) — 按需檢索＋Retrieve/ISREL/ISSUP/ISUSE 四種反思標記
- [GraphRAG（圖譜式 RAG）](concepts/graphrag.md) — 建知識圖、群集摘要、map-reduce 回答
- [Contextual Retrieval（情境化檢索）](concepts/contextual-retrieval.md) — 建索引前替每個片段加上 50–100 tokens 的脈絡說明
- [LLM Wiki](concepts/llm-wiki.md) — raw／wiki／schema 三層；ingest、query、lint 三操作

## Comparisons

- [RAG vs fine-tuning](comparisons/rag-vs-fine-tuning.md) — 翻課本 vs 內化知識：更新、擅長、代價
- [RAG vs 長上下文](comparisons/rag-vs-long-context.md) — 能塞進 prompt 為何還要 RAG
- [RAG vs LLM Wiki](comparisons/rag-vs-llm-wiki.md) — 查詢時才檢索 vs 平時就整理成 wiki
