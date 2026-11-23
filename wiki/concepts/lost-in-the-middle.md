---
type: concept
title: Lost in the Middle（中間迷失）
sources: [liu2023, gao2023]
updated: 2026-11-23
---

# Lost in the Middle（中間迷失）

## 一句話白話定義
語言模型讀長輸入時，比較記得開頭和結尾，放在中間的關鍵資訊容易被忽略。[src: liu2023, p.1]

## 說明
- 表現隨相關資訊位置呈 U 形：開頭（primacy bias）與結尾（recency bias）最好，中間最差。[src: liu2023, p.1]
- 嚴重時，關鍵文件放在中間的表現比完全不給文件還差：GPT-3.5-Turbo 在 20、30 篇文件設定的最差情況低於 closed-book 的 56.1%。[src: liu2023, p.5]
- 即使是擴充脈絡長度的模型也有這個現象。[src: liu2023, p.1]
- Gao et al. 也把它列為 RAG 的問題：多餘資訊會干擾生成，過長脈絡會導致「Lost in the middle」。[src: gao2023, p.10]

## 對 RAG 的意義
- 不是檢索越多越好：模型表現遠在檢索器 recall 飽和前就飽和。[src: liu2023, p.10]
- 對策方向：reranking 把相關片段放到最前面、或截短檢索清單。見 [重新排序](reranking.md)。[src: liu2023, p.10]

## 相關頁面
- [Liu et al. 2023](../sources/liu2023.md)
- [RAG vs 長上下文](../comparisons/rag-vs-long-context.md)
