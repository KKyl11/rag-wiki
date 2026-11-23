---
slide: 8
title: 進階 1：Contextual Retrieval——替片段補上下文
section: 進階變形
layout: content
evidence: [gao2023#E6, anthropic2024#E1, anthropic2024#E2, anthropic2024#E3, gao2023#E12]
wiki: [concepts/rag-paradigms.md, concepts/contextual-retrieval.md, concepts/reranking.md]
---
RAG 從最基本的 Naive RAG，演進到加入各種優化的 Advanced RAG 與 Modular RAG。以下是改良「檢索」的一個例子：

- **問題**：切塊後，片段「公司營收比上一季成長 3%」沒說是哪家公司、哪一季，很難被正確找到。
- **做法**：讓 Claude 讀整份文件與片段，生成 50–100 tokens 的說明加在片段前面，再建 embedding 與 BM25 索引。
- **再加 reranking**：初步檢索後重新排名，把最相關的片段排到前面。

| 做法（top-20 片段的檢索失敗率） | 失敗率 |
|---|---|
| 一般做法 | 5.7% |
| ＋ Contextual Embeddings | 3.7%（降 35%） |
| ＋ Contextual BM25 | 2.9%（降 49%） |
| ＋ Reranking | 1.9%（降 67%） |
