---
type: concept
title: 檢索增強生成（RAG）
sources: [lewis2020, gao2023, asai2023, edge2024, anthropic2024, karpathy-llmwiki]
updated: 2026-11-23
---

# 檢索增強生成（Retrieval-Augmented Generation, RAG）

## 一句話白話定義
RAG 就是讓語言模型「先去資料庫找相關段落，再根據找到的內容寫答案」。[src: lewis2020, p.2]

## 定義
- Lewis et al. 把 RAG 定義為結合「預訓練參數記憶」與「非參數記憶」來生成語言的模型。[src: lewis2020, p.1]
- 模型用輸入序列 x 檢索文字文件 z，再把 z 當成額外脈絡來生成目標序列 y。[src: lewis2020, p.2]

- Gao et al. 的描述：RAG 透過語意相似度從外部知識庫檢索相關文件片段，藉此減少產生事實錯誤內容的問題。[src: gao2023, p.1]

## 組成元件
- 檢索器（retriever）：給定查詢 x，回傳最相關的 top-K 段文字。見 [檢索器](retriever.md)。[src: lewis2020, p.2]
- 生成器（generator）：根據查詢、檢索到的段落、以及已生成的字，產生下一個字。[src: lewis2020, p.2-3]
- 知識庫：原始論文用 Wikipedia，切成 100 字片段後建立向量索引。見 [切塊](chunking.md)。[src: lewis2020, p.4]

## 典型流程
- 索引 → 檢索 → 生成三步，詳見 [RAG 三種範式與基本流程](rag-paradigms.md)。[src: gao2023, p.3]

## 為什麼要 RAG
- 純參數模型難以更新知識、難以說明依據、會產生幻覺；外接檢索式記憶可以直接修改、擴充，也能被檢查。見 [LLM 的知識限制](llm-knowledge-limits.md)。[src: lewis2020, p.1]
- 換掉索引就能更新知識，不必重新訓練模型。[src: lewis2020, p.8]

- RAG 與 fine-tuning、長上下文的比較，見 [RAG vs fine-tuning](../comparisons/rag-vs-fine-tuning.md)、[RAG vs 長上下文](../comparisons/rag-vs-long-context.md)。[src: gao2023, p.5; gao2023, p.14]

## 進階變形
- [Self-RAG](self-rag.md)：模型自己決定何時檢索，並自我批判輸出。[src: asai2023, p.1]

- [GraphRAG](graphrag.md)：先把文件建成知識圖與群集摘要，回答需要看完整份資料的全域問題。[src: edge2024, p.1]

- [Contextual Retrieval](contextual-retrieval.md)：替每個片段補上脈絡再建索引，減少檢索失敗。[src: anthropic2024, §Introducing Contextual Retrieval]

## 與 LLM Wiki 的對照
- Karpathy 指出 RAG 在每次提問時都從原始文件重新拼湊知識、沒有累積，並提出 LLM Wiki 作為不同做法。見 [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)。[src: karpathy-llmwiki, §The core idea]

## 相關頁面
- [Gao et al. 2023](../sources/gao2023.md)
- [Lewis et al. 2020](../sources/lewis2020.md)
- [參數記憶 vs 非參數記憶](parametric-vs-nonparametric-memory.md)
