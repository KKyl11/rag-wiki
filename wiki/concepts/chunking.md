---
type: concept
title: 切塊（chunking）
sources: [lewis2020, gao2023, edge2024, anthropic2024]
updated: 2026-11-23
---

# 切塊（chunking）

## 一句話白話定義
切塊是把長文件切成一小段一小段，讓檢索器可以一段一段比對、挑選。[src: lewis2020, p.4]

## 說明
- RAG 原始論文把每篇 Wikipedia 文章切成不重疊的 100 字片段，共 21M 段，每段算一個 embedding。[src: lewis2020, p.4]
- 最常見的做法是以固定 token 數切分，例如 100、256、512。[src: gao2023, p.8]
- 取捨：大塊能保留較多脈絡，但雜訊多、處理時間與成本較高；小塊雜訊少，但可能傳達不了必要的脈絡。[src: gao2023, p.8]
- 固定長度切分可能把句子切斷，因此有遞迴切分、滑動視窗、Small2Big（用句子檢索、回傳前後句當脈絡）等改良。[src: gao2023, p.8]
- 片段可以附加 metadata（頁碼、檔名、作者、時間戳），檢索時用來過濾範圍。[src: gao2023, p.8]
- GraphRAG 的實驗把語料切成 600-token 片段，片段之間重疊 100 tokens。[src: edge2024, p.8]
- Anthropic 的說明：片段通常不超過幾百 tokens。[src: anthropic2024, §A primer on RAG: scaling to larger knowledge bases]
- 切塊的副作用：單一片段可能缺乏足夠脈絡（例如沒寫是哪家公司、哪一季），因而難以被正確檢索；Contextual Retrieval 就是為此提出。見 [Contextual Retrieval](contextual-retrieval.md)。[src: anthropic2024, §The context conundrum in traditional RAG]
- 片段大小、邊界、重疊的選擇都會影響檢索表現。[src: anthropic2024, §Implementation considerations]

## 相關頁面
- [檢索器（retriever）](retriever.md)
- [檢索增強生成（RAG）](rag.md)
