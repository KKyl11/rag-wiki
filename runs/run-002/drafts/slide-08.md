---
slide: 8
title: 進階 1：Contextual Retrieval——替片段補上下文
section: 進階變形
layout: content
evidence: [anthropic2024#E1, anthropic2024#E2, anthropic2024#E3, anthropic2024#E7, gao2023#E12]
wiki: [concepts/contextual-retrieval.md, concepts/reranking.md]
---
Contextual Retrieval：先替每個片段補一句說明，再拿去建索引。

- **問題**（例子）：片段「公司營收比上一季成長 3%」沒說是哪家公司、哪一季。
- **做法**：用 Claude 讀整份文件與片段，生成 50–100 tokens 的說明加在片段前面，再建 embedding 與 BM25 索引。
- **可再疊加 reranking**：初步檢索後重新排名，把最相關的片段排到前面。

| 做法（top-20 檢索失敗率：相關文件沒出現在前 20 個片段裡的比例；降幅是和基準比的相對降幅） | 失敗率 |
|---|---|
| 基準 | 5.7% |
| Contextual Embeddings（單獨使用） | 3.7%（降 35%） |
| Contextual Embeddings ＋ Contextual BM25 | 2.9%（降 49%） |
| 再 ＋ Reranking | 1.9%（降 67%） |
