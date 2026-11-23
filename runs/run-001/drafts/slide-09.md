---
slide: 9
title: 進階 2：Self-RAG 與 GraphRAG
section: 進階變形
layout: content
evidence: [asai2023#E1, asai2023#E2, edge2024#E1, edge2024#E2, edge2024#E3]
wiki: [concepts/self-rag.md, concepts/graphrag.md]
---
### Self-RAG：需要時才查，查完自己檢查
- **解決什麼**：傳統 RAG 不管需不需要，都固定檢索一定數量的段落。
- **做法**：模型自己判斷要不要檢索，並用「反思標記」評估找到的段落是否相關、自己寫的內容有沒有被段落支持。

### GraphRAG：回答「整份資料在講什麼」
- **解決什麼**：「資料集的主要主題是什麼？」這類全域問題，一般 RAG 會失敗。
- **做法**：先用 LLM 把文件建成知識圖、替每群相關內容寫摘要，回答時再彙整這些摘要。
- **結果**（兩個資料集的實驗）：在「全面性」上，GraphRAG 對一般 RAG 的勝率為 72–83%（Podcast）與 72–80%（新聞）；一般 RAG 的答案則最直接。
