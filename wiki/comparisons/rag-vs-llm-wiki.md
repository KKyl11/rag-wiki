---
type: comparison
title: RAG vs LLM Wiki
sources: [karpathy-llmwiki, lewis2020, gao2023]
updated: 2026-11-23
---

# RAG vs LLM Wiki

## 一句話白話定義
RAG 是「每次被問才去翻原始資料」；LLM Wiki 是「平常就把讀過的資料整理成筆記，被問時先查筆記」。[src: karpathy-llmwiki, §The core idea]

## 比較
| 面向 | RAG | LLM Wiki |
|---|---|---|
| 何時整理知識 | 查詢時才檢索相關片段並生成 [src: karpathy-llmwiki, §The core idea] | 加入來源時就整合進 wiki，編譯一次、持續更新 [src: karpathy-llmwiki, §The core idea] |
| 知識會不會累積 | 每次從頭重新發現，沒有累積 [src: karpathy-llmwiki, §The core idea] | 交叉引用與矛盾標註已做好，越用越豐富 [src: karpathy-llmwiki, §The core idea] |
| 知識存在哪 | 切塊後的向量索引 [src: gao2023, p.3] | 互相連結的 markdown 頁面＋index.md [src: karpathy-llmwiki, §Indexing and logging] |
| 怎麼找資料 | 依 embedding 相似度取 top-K 片段 [src: gao2023, p.3] | 先讀 index 找頁面再深入；中等規模不需要 embedding 基礎設施 [src: karpathy-llmwiki, §Indexing and logging] |
| 誰來維護 | 換掉索引即可更新知識 [src: lewis2020, p.8] | LLM 負責所有維護工作，人負責挑來源與提問 [src: karpathy-llmwiki, §The core idea] |

## 兩者的關係
- Karpathy 明確把 LLM Wiki 定位成與 RAG 不同的做法：不只在查詢時從原始文件檢索，而是持續建立並維護 wiki。[src: karpathy-llmwiki, §The core idea]
- 規模變大時，Karpathy 也建議替 wiki 加上搜尋工具，例如 BM25／向量混合搜尋的 qmd。[src: karpathy-llmwiki, §Optional: CLI tools]
- 在 LLM Wiki 上做 Query 時，LLM 先搜尋相關頁面、讀取後綜合出附出處的答案；答案可以是 markdown 頁、比較表，也可以是簡報（Marp）。[src: karpathy-llmwiki, §Operations]

## 相關頁面
- [LLM Wiki](../concepts/llm-wiki.md)
- [檢索增強生成（RAG）](../concepts/rag.md)
- [Karpathy LLM Wiki](../sources/karpathy-llmwiki.md)
