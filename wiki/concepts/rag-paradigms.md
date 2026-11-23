---
type: concept
title: RAG 三種範式（Naive / Advanced / Modular）與基本流程
sources: [gao2023, asai2023]
updated: 2026-11-23
---

# RAG 三種範式與基本流程

## 一句話白話定義
最基本的 RAG 只有三步：先把資料切塊建索引，再找出跟問題最像的幾塊，最後把問題和這幾塊一起交給 LLM 回答。[src: gao2023, p.3]

## 基本流程（Naive RAG）
1. 索引（indexing）：把 PDF、HTML 等原始資料清理成純文字，切成小塊，用 embedding 模型編碼成向量，存進向量資料庫。[src: gao2023, p.3]
2. 檢索（retrieval）：用同一個編碼模型把問題轉成向量，算出與各片段的相似度，取最相似的 top-K 片段。[src: gao2023, p.3]
3. 生成（generation）：把問題與選出的片段組成 prompt，交給 LLM 生成答案。[src: gao2023, p.3]

## 三種範式
| 範式 | 特色 |
|---|---|
| Naive RAG | 傳統的「Retrieve-Read」流程：索引、檢索、生成 [src: gao2023, p.3] |
| Advanced RAG | 加上檢索前（優化索引、改寫查詢）與檢索後（reranking、壓縮脈絡）的策略 [src: gao2023, p.3-4] |
| Modular RAG | 可新增、替換、重組模組，不限於「先檢索再生成」，包含迭代與自適應檢索 [src: gao2023, p.4] |

- 自適應檢索的例子包含 FLARE 與 Self-RAG：依情境判斷是否需要檢索。見 [Self-RAG](self-rag.md)。[src: gao2023, p.5]

## Naive RAG 的問題
- 檢索可能選到不相關片段、漏掉關鍵資訊；生成可能出現檢索內容不支持的幻覺；整合多段資訊可能不連貫或重複。[src: gao2023, p.3]

- Self-RAG 指出 Naive 式「固定檢索一定數量段落」的問題：不管需要與否都檢索，可能產生沒幫助的回答。[src: asai2023, p.1]

## 相關頁面
- [Asai et al. 2023](../sources/asai2023.md)
- [檢索增強生成（RAG）](rag.md)
- [重新排序（reranking）](reranking.md)
- [Gao et al. 2023](../sources/gao2023.md)
