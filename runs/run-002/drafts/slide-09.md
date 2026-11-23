---
slide: 9
title: 進階 2：Self-RAG 與 GraphRAG
section: 進階變形
layout: content
evidence: [asai2023#E1, asai2023#E2, edge2024#E1, edge2024#E2, edge2024#E3, edge2024#E5]
wiki: [concepts/self-rag.md, concepts/graphrag.md]
---
### Self-RAG：需要時才查，查完自己檢查
- **解決什麼**：傳統 RAG 不論需要與否，都固定檢索一定數量段落。
- **做法**：模型判斷需要時才檢索，並用反思標記評估段落的相關性、輸出是否被段落支持、回答是否有用。

### GraphRAG：回答關於整份資料的全域問題
- **解決什麼**：「資料集的主要主題是什麼？」這類全域問題，一般 RAG 會失敗。
- **做法**：用 LLM 把文件建成知識圖、替各群集寫摘要，回答時每份摘要先各自產生部分答案，再合成最終答案。
- **結果**：論文用 LLM 當評審兩兩比較；全面性勝率對 vector RAG 為 72–83%（Podcast）與 72–80%（新聞），vector RAG 的答案則最直接。
