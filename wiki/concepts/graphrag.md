---
type: concept
title: GraphRAG（圖譜式 RAG）
sources: [edge2024]
updated: 2026-11-23
---

# GraphRAG

## 一句話白話定義
GraphRAG 先把所有文件整理成「誰和誰有關係」的知識圖，並替每一群相關的東西寫好摘要，用來回答需要看完整份資料才答得出的大問題。[src: edge2024, p.2]

## 為什麼需要
- 一般（vector）RAG 只取回少數與問題相似的片段，適合答案集中在少數紀錄的問題。[src: edge2024, p.2]
- 「資料集的主要主題是什麼？」這類全域問題需要理解整個語料，一般 RAG 會失敗。[src: edge2024, p.1]

## 怎麼做
1. 用 LLM 從文件抽出實體與關係，建成知識圖。[src: edge2024, p.2]
2. 把圖分成階層式群集，由下而上替每個群集寫摘要。[src: edge2024, p.2]
3. 回答時每份摘要各自產生部分答案（map），再合成最終答案（reduce）。[src: edge2024, p.2]

## 效果與代價
- 這類問題沒有標準答案，因此論文用 LLM 當評審，兩兩比較兩個系統的答案，用「勝率」表示。[src: edge2024, p.2]
- 全面性勝率對 vector RAG 為 72–83%（Podcast）與 72–80%（新聞）。[src: edge2024, p.9]
- vector RAG 的答案則最直接。[src: edge2024, p.9]
- 用最高層摘要回答時，比直接摘要原文少用超過 97% 的 tokens。[src: edge2024, p.10]

## 相關頁面
- [Edge et al. 2024](../sources/edge2024.md)
- [檢索增強生成（RAG）](rag.md)
