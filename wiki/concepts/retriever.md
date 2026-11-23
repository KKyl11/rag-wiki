---
type: concept
title: 檢索器（retriever）：dense 檢索與 BM25
sources: [lewis2020, gao2023, anthropic2024]
updated: 2026-11-23
---

# 檢索器（retriever）

## 一句話白話定義
檢索器是 RAG 裡負責「從一大堆資料中挑出跟問題最相關的幾段」的元件。[src: lewis2020, p.2]

## Dense 檢索（向量檢索）
- RAG 原始論文用 DPR：文件與查詢分別經 BERT-base 編碼成向量（embedding），用最大內積搜尋（MIPS）找 top-k。[src: lewis2020, p.3]
- 所有片段事先算好 embedding，用 FAISS 建索引加速搜尋。[src: lewis2020, p.4]

- 檢索靠計算問題與片段 embedding 的相似度（例如 cosine similarity），embedding 模型的語意表達能力是關鍵。[src: gao2023, p.9]

## BM25（字詞重疊式檢索）
- Lewis et al. 把 dense 檢索器換成 BM25 做比較：FEVER 上 BM25 最好，其他任務 dense 檢索較好，開放領域問答尤其明顯。[src: lewis2020, p.7]

- Gao et al. 把 BM25 歸為 sparse 編碼器、BERT 類模型歸為 dense 檢索器；兩者捕捉不同的相關性特徵，可以混合（hybrid）互補。[src: gao2023, p.9]

- Anthropic 的例子：查「Error code TS-999」時，embedding 可能只找到一般錯誤碼的內容，BM25 則能精確比對「TS-999」。[src: anthropic2024, §A primer on RAG: scaling to larger knowledge bases]
- 混合做法：BM25 與 embedding 各取 top 片段，用 rank fusion 合併去重。[src: anthropic2024, §A primer on RAG: scaling to larger knowledge bases]

## 檢索準確度
- FEVER 中，top-1 文件來自正確文章的比例為 71%，top-10 中有正確文章的比例為 90%。[src: lewis2020, p.7]

- Anthropic 實驗中，Embeddings＋BM25 比只用 embeddings 好。[src: anthropic2024, §Conclusion]

## 相關頁面
- [Contextual Retrieval](contextual-retrieval.md)
- [Gao et al. 2023](../sources/gao2023.md)
- [檢索增強生成（RAG）](rag.md)
- [切塊（chunking）](chunking.md)
- [Lewis et al. 2020](../sources/lewis2020.md)
