---
type: concept
title: Self-RAG（自我反思式 RAG）
sources: [asai2023, gao2023]
updated: 2026-11-23
---

# Self-RAG（Self-Reflective Retrieval-Augmented Generation）

## 一句話白話定義
Self-RAG 讓模型自己判斷「這題需不需要查資料」，查了之後再自己檢查「找到的資料有沒有用、我寫的有沒有根據」。[src: asai2023, p.1]

## 和傳統 RAG 的差別
| 面向 | 傳統 RAG | Self-RAG |
|---|---|---|
| 何時檢索 | 不論需要與否，固定檢索一定數量段落 [src: asai2023, p.1] | 模型判斷需要時才檢索 [src: asai2023, p.1] |
| 檢查品質 | 不會回頭檢查生成品質 [src: asai2023, p.2] | 用批判標記評估相關性、支持度、有用度 [src: asai2023, p.4] |
| 引用 | 輸出不保證與段落一致 [src: asai2023, p.1] | 每段附引用與「是否被支持」的自我評估 [src: asai2023, p.2] |

## 反思標記（reflection tokens）
- Retrieve：要不要檢索（yes / no / continue）。[src: asai2023, p.4]
- ISREL：段落是否與問題相關（relevant / irrelevant）。[src: asai2023, p.4]
- ISSUP：輸出是否被段落支持（fully / partially / no support）。[src: asai2023, p.4]
- ISUSE：回答是否有用（5 到 1 分）。[src: asai2023, p.4]

## 在 RAG 演進中的位置
- Gao et al. 把 Self-RAG 列為 Modular RAG 中「自適應檢索」的例子：依情境判斷是否需要檢索。[src: gao2023, p.5]

## 相關頁面
- [Asai et al. 2023](../sources/asai2023.md)
- [RAG 三種範式](rag-paradigms.md)
