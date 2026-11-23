---
type: concept
title: LLM 的知識限制（幻覺、過時、無出處）
sources: [lewis2020, gao2023]
updated: 2026-11-23
---

# LLM 的知識限制

## 一句話白話定義
只靠「背在參數裡的知識」回答的語言模型，可能會編造答案、知識會過時，也說不出答案的根據。[src: lewis2020, p.1]

## 三個問題
- 幻覺（hallucination）：模型可能產生「幻覺」。[src: lewis2020, p.1]
- 難以更新：模型無法輕易擴充或修改記憶；純參數模型要再訓練才能跟上世界變化。[src: lewis2020, p.1; lewis2020, p.7]
- 無法追溯：模型難以說明預測依據，提供出處（provenance）仍是開放問題。[src: lewis2020, p.1]

## Survey 的歸納
- Gao et al. 把 LLM 的挑戰歸納為：幻覺、知識過時、推理過程不透明且無法追溯。[src: gao2023, p.1]
- 遇到超出訓練資料或需要最新資訊的問題時，LLM 特別容易產生「幻覺」。[src: gao2023, p.1]

## RAG 怎麼回應這些問題
- 外接檢索式記憶可以直接修改、擴充，取用的知識也能被檢查與解讀。[src: lewis2020, p.1]

- 引用外部知識能有效減少產生事實錯誤內容的問題，也能持續更新知識。[src: gao2023, p.1]

## 相關頁面
- [Gao et al. 2023](../sources/gao2023.md)
- [檢索增強生成（RAG）](rag.md)
- [Lewis et al. 2020](../sources/lewis2020.md)
