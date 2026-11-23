---
slide: 14
title: 重點回顧＋小測驗
section: 回顧
layout: content
evidence: [lewis2020#E2, gao2023#E3, liu2023#E1, karpathy-llmwiki#E2]
wiki: [concepts/rag.md, concepts/rag-paradigms.md, concepts/lost-in-the-middle.md, comparisons/rag-vs-llm-wiki.md]
---
- RAG：先去資料庫找相關段落，再根據找到的內容寫答案。
- 最基本的 Naive RAG 流程：索引 → 檢索 → 生成。
- 相關資訊放在長輸入的中間時，模型表現最差。

```quiz
Q: 最基本的 Naive RAG 有哪三個步驟？ || A: 索引、檢索、生成
Q: 想讓 RAG 知道新的事，需要重新訓練模型嗎？ || A: 不用，換掉索引就能更新知識
Q: 關鍵資訊放在長輸入的哪裡，模型表現最差？ || A: 中間（Lost in the Middle）
Q: RAG 和 LLM Wiki 在何時整理知識上有什麼不同？ || A: RAG 查詢時才檢索；LLM Wiki 加入來源時就整合進 wiki
```
