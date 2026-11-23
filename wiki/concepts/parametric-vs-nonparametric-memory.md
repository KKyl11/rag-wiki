---
type: concept
title: 參數記憶 vs 非參數記憶
sources: [lewis2020]
updated: 2026-11-23
---

# 參數記憶（parametric memory）vs 非參數記憶（non-parametric memory）

## 一句話白話定義
參數記憶是模型「背在腦子裡」的知識；非參數記憶是模型「可以翻的外部資料」。[src: lewis2020, p.1]

## 說明
| 項目 | 參數記憶 | 非參數記憶 |
|---|---|---|
| 存在哪裡 | 模型參數（RAG 論文中是 BART 生成器）[src: lewis2020, p.3] | 外部文件索引（RAG 論文中是 Wikipedia 的 dense 向量索引）[src: lewis2020, p.3] |
| 怎麼更新 | 需要再訓練 [src: lewis2020, p.7] | 替換索引即可（hot-swapping）[src: lewis2020, p.8] |
| 可解釋性 | 難以說明預測依據 [src: lewis2020, p.1] | 由原始文字構成，人可讀也可改 [src: lewis2020, p.9] |

- 兩者會合作：Jeopardy 例子中，檢索到的文件引導生成，生成器再補完存在參數裡的書名。[src: lewis2020, p.6]
- 換索引實驗：索引年份對上時答對約七成（70%、68%），對不上時只剩 12% 與 4%。[src: lewis2020, p.8]

## 相關頁面
- [檢索增強生成（RAG）](rag.md)
- [Lewis et al. 2020](../sources/lewis2020.md)
