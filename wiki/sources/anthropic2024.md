---
type: source
key: anthropic2024
title: Introducing Contextual Retrieval（Anthropic, 2024）
url: https://www.anthropic.com/news/contextual-retrieval
raw: raw/anthropic2024.md
sources: [anthropic2024]
updated: 2026-11-23
---

# Anthropic 2024 — Introducing Contextual Retrieval

## 書目
- Anthropic 官方文章，2024-09-19 發布，抓取日期 2026-11-23。[src: anthropic2024, §Introducing Contextual Retrieval]

## 一句話摘要
傳統 RAG 切塊時會把片段的上下文弄丟；Contextual Retrieval 在每個片段前面加上一小段說明它出自哪裡的脈絡，再建 embedding 與 BM25 索引，大幅減少檢索失敗。[src: anthropic2024, §Introducing Contextual Retrieval]

## 什麼時候不需要 RAG
- 知識庫小於 200,000 tokens（約 500 頁）時，可以直接把整個知識庫放進 prompt，不需要 RAG。[src: anthropic2024, §A note on simply using a longer prompt]
- Prompt caching 讓這種做法更快、更省：延遲降低 2 倍以上、成本最多降低 90%。[src: anthropic2024, §A note on simply using a longer prompt]

## RAG 入門（文章的說明）
- 前處理：把知識庫切成通常不超過幾百 tokens 的片段，用 embedding 模型轉成向量，存進可依語意相似度搜尋的向量資料庫。[src: anthropic2024, §A primer on RAG: scaling to larger knowledge bases]
- 執行時，用向量資料庫找出與查詢最相關的片段，加進送給生成模型的 prompt。[src: anthropic2024, §A primer on RAG: scaling to larger knowledge bases]
- Embedding 擅長語意關係，但可能漏掉精確比對；BM25 用字詞比對找精確詞句，適合含獨特代碼或技術詞的查詢，例如「Error code TS-999」。[src: anthropic2024, §A primer on RAG: scaling to larger knowledge bases]
- 結合 BM25 與 embedding：各自找出 top 片段，用 rank fusion 合併去重，再把 top-K 片段放進 prompt。[src: anthropic2024, §A primer on RAG: scaling to larger knowledge bases]

## 問題：切塊會丟失上下文
- 例子：問「ACME 公司 2023 年第二季營收成長多少？」，相關片段只寫「公司營收比上一季成長 3%」，沒說是哪家公司、哪個時期，因此難以被正確檢索與使用。[src: anthropic2024, §The context conundrum in traditional RAG]

## 做法
- 在每個片段建 embedding（Contextual Embeddings）與 BM25 索引（Contextual BM25）之前，先在前面加上說明該片段的脈絡。[src: anthropic2024, §Introducing Contextual Retrieval]
- 脈絡由 Claude 3 Haiku 讀整份文件與該片段後生成，通常 50–100 tokens。[src: anthropic2024, §Implementing Contextual Retrieval]
- 利用 prompt caching，生成脈絡片段的一次性成本是每百萬文件 tokens 1.02 美元。[src: anthropic2024, §Using Prompt Caching to reduce the costs of Contextual Retrieval]

## 結果（top-20 片段的檢索失敗率，1 − recall@20）
- 只用 Contextual Embeddings：失敗率降低 35%（5.7% → 3.7%）。[src: anthropic2024, §Performance improvements]
- Contextual Embeddings ＋ Contextual BM25：失敗率降低 49%（5.7% → 2.9%）。[src: anthropic2024, §Performance improvements]
- 再加上 reranking：失敗率降低 67%（5.7% → 1.9%）。[src: anthropic2024, §Performance improvements]
- 實驗涵蓋程式碼庫、小說、ArXiv 論文、科學論文等領域；圖表是最佳 embedding 設定（Gemini Text 004）下各領域的平均。[src: anthropic2024, §Methodology]

## Reranking 設定
- 先初步檢索 top 150 個片段，用 reranking 模型（測試用 Cohere reranker）評分，再取 top 20 放進模型。[src: anthropic2024, §Further boosting performance with Reranking]
- 代價：reranking 在執行時多一個步驟，必然增加一些延遲；重排越多片段效果越好，但延遲與成本越高。[src: anthropic2024, §Cost and latency considerations]

## 結論清單
- Embeddings＋BM25 比只用 embeddings 好；放 top-20 片段比 top-10 或 top-5 好；加脈絡大幅提升檢索準確度；有 reranking 比沒有好；這些好處可以疊加。[src: anthropic2024, §Conclusion]
- 片段數量的取捨：放越多片段越可能包含相關資訊，但資訊太多也會讓模型分心；他們測 5、10、20 片段，20 最好。[src: anthropic2024, §Implementation considerations]

## 相關頁面
- [Contextual Retrieval](../concepts/contextual-retrieval.md)
- [檢索器（retriever）](../concepts/retriever.md)
- [重新排序（reranking）](../concepts/reranking.md)
