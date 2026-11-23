---
slide: 14
title: 重點回顧＋小測驗
section: 回顧
layout: content
evidence: [lewis2020#E2, gao2023#E3, liu2023#E1, karpathy-llmwiki#E1]
wiki: [concepts/rag.md, concepts/rag-paradigms.md, concepts/lost-in-the-middle.md, comparisons/rag-vs-llm-wiki.md]
---
- RAG＝先去資料庫找相關段落，再根據找到的內容寫答案。
- 流程：索引 → 檢索 → 生成。
- 資料不是塞越多越好：放在中間的關鍵資訊容易被忽略。

```quiz
Q: RAG 的三個步驟是什麼？ || A: 索引、檢索、生成
Q: 想讓 RAG 知道新的事，一定要重新訓練模型嗎？ || A: 不用，換掉索引就能更新知識
Q: 關鍵資訊放在長輸入的哪裡，模型最容易忽略？ || A: 中間（Lost in the Middle）
Q: RAG 和 LLM Wiki 最大的差別是什麼？ || A: RAG 被問時才檢索；LLM Wiki 加入資料時就整理成 wiki
```
