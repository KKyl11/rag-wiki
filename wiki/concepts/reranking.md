---
type: concept
title: 重新排序（reranking）
sources: [gao2023, liu2023, anthropic2024]
updated: 2026-11-23
---

# 重新排序（reranking）

## 一句話白話定義
Reranking 是在初步檢索之後，再用更仔細的方法把候選片段重新排名，只留下最相關的幾段。[src: gao2023, p.10]

## 說明
- Reranking 把最相關的片段排到前面、縮小文件池，同時有「增強」與「過濾」兩種作用。[src: gao2023, p.10]
- 可以用規則（多樣性、相關性、MRR 等指標），也可以用模型（BERT 系列、Cohere rerank、bge-reranker、通用 LLM）。[src: gao2023, p.10]
- Advanced RAG 會把最相關的內容移到 prompt 的邊緣（開頭或結尾）。[src: gao2023, p.4]
- Liu et al. 發現模型較會使用輸入開頭或結尾的資訊，因此建議用 reranking 把相關資訊推到輸入開頭，或截短檢索清單。[src: liu2023, p.10]
- Anthropic 的設定：先檢索 top 150，用 Cohere reranker 評分後取 top 20；搭配 Contextual Retrieval 讓 top-20 檢索失敗率降低 67%（5.7% → 1.9%）。[src: anthropic2024, §Further boosting performance with Reranking; anthropic2024, §Performance improvements]
- 代價：多一個執行步驟，必然增加一些延遲；重排越多越準但越慢越貴。[src: anthropic2024, §Cost and latency considerations]

## 相關頁面
- [Contextual Retrieval](contextual-retrieval.md)
- [Lost in the Middle](lost-in-the-middle.md)
- [RAG 三種範式](rag-paradigms.md)
- [Gao et al. 2023](../sources/gao2023.md)
