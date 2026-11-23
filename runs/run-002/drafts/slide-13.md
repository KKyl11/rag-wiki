---
slide: 13
title: RAG vs LLM Wiki（這份作業就是 LLM Wiki）
section: 比較
layout: content
evidence: [karpathy-llmwiki#E1, karpathy-llmwiki#E2, karpathy-llmwiki#E3, karpathy-llmwiki#E4, karpathy-llmwiki#E5]
wiki: [comparisons/rag-vs-llm-wiki.md, concepts/llm-wiki.md]
---
Karpathy 把 LLM Wiki 定位成與 RAG 不同的做法：

| | RAG | LLM Wiki |
|---|---|---|
| 何時整理知識 | 查詢時才檢索相關片段 | 加入來源時就整合進 wiki |
| 知識會累積嗎 | 每次從頭重新發現，沒有累積 | 編譯一次、持續更新，越用越豐富 |
| 怎麼找資料 | 依 embedding 相似度取 top-K 片段 | 先讀 index 找頁面再深入（中等規模不需要 embedding 基礎設施） |
| 怎麼更新／維護 | 換掉索引即可更新知識 | LLM 負責維護，人負責挑來源與提問 |

- 三層架構：唯讀的原始資料、LLM 維護的 wiki、規定規則的 schema（本作業的 `AGENTS.md`）。
