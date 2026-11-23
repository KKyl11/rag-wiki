---
slide: 3
title: 核心概念：背在腦中 vs 隨時翻課本
section: 概念
layout: content
evidence: [lewis2020#E1, lewis2020#E4, lewis2020#E5, gao2023#E7]
wiki: [concepts/parametric-vs-nonparametric-memory.md, comparisons/rag-vs-fine-tuning.md]
---
| | 參數記憶（背在腦中） | 非參數記憶（可以翻的資料） |
|---|---|---|
| 存在哪裡 | 模型參數 | 外部文件索引（例如 Wikipedia） |
| 怎麼更新 | 需要再訓練 | 替換索引即可 |
| 看得懂嗎 | 難以說明預測依據 | 由原始文字構成，人可讀也可改 |

RAG 把兩者結合：模型本身的能力，加上一份可以翻的外部資料。

> 來源原有的比喻（Gao et al.）：RAG 像給模型一本**量身訂做的課本**隨時翻查；fine-tuning（微調）則像學生花時間把知識內化進腦中。
