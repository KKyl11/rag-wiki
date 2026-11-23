---
type: comparison
title: RAG vs fine-tuning
sources: [gao2023]
updated: 2026-11-23
---

# RAG vs fine-tuning（微調）

## 一句話白話定義
RAG 像給模型一本量身訂做的課本隨時翻查；fine-tuning 像學生花時間把知識內化進腦中。[src: gao2023, p.5]

## 來源原有的比喻
- Gao et al. 把 RAG 比作給模型一本量身訂做的教科書來查資料，把 fine-tuning 比作學生隨時間把知識內化。[src: gao2023, p.5]

## 比較
| 面向 | RAG | Fine-tuning |
|---|---|---|
| 知識更新 | 可即時更新 [src: gao2023, p.5] | 較靜態，更新要重新訓練 [src: gao2023, p.5] |
| 擅長 | 精確查找資訊、利用外部知識，可解釋性高 [src: gao2023, p.5] | 複製特定結構、風格或格式，深度客製行為 [src: gao2023, p.5] |
| 代價 | 延遲較高，資料檢索有倫理考量 [src: gao2023, p.5] | 資料準備與訓練需要大量運算 [src: gao2023, p.5] |

- 論文引述的研究：知識密集任務上，RAG 一致優於非監督式 fine-tuning；LLM 很難透過非監督式 fine-tuning 學到新事實。[src: gao2023, p.5]
- 兩者不互斥，可以互補，合併使用有時效果最好。[src: gao2023, p.5]

## 相關頁面
- [檢索增強生成（RAG）](../concepts/rag.md)
- [Gao et al. 2023](../sources/gao2023.md)
