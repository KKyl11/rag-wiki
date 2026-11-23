---
type: concept
title: Contextual Retrieval（情境化檢索）
sources: [anthropic2024]
updated: 2026-11-23
---

# Contextual Retrieval

## 一句話白話定義
切塊後的片段常常「看不出在講誰」；Contextual Retrieval 先替每個片段補一句「這段出自哪裡、在講什麼」，再拿去建索引。[src: anthropic2024, §Introducing Contextual Retrieval]

## 要解決的問題
- 傳統 RAG 編碼時會移除上下文，常導致找不到相關資訊。[src: anthropic2024, §Introducing Contextual Retrieval]
- 例子：片段「公司營收比上一季成長 3%」沒說是哪家公司、哪一季。[src: anthropic2024, §The context conundrum in traditional RAG]

## 做法
- 用 Claude 讀整份文件與片段，生成 50–100 tokens 的說明，加在片段前面，再建 embedding（Contextual Embeddings）與 BM25 索引（Contextual BM25）。[src: anthropic2024, §Implementing Contextual Retrieval]
- 改寫後的例子：在原片段前加上「這段出自 ACME 公司 2023 年第二季的 SEC 申報；上一季營收為 $314 million」。[src: anthropic2024, §Introducing Contextual Retrieval]

## 效果（top-20 檢索失敗率）
- 失敗率的意思：相關文件沒有出現在前 20 個片段裡的比例（1 minus recall@20）。[src: anthropic2024, §Methodology]
- 下表的降幅是和基準比的相對降幅；Contextual Embeddings 那一列是單獨使用，後兩列才是逐項疊加。[src: anthropic2024, §Performance improvements]

| 做法 | 失敗率 | 降幅 |
|---|---|---|
| 一般做法（基準） | 5.7% [src: anthropic2024, §Performance improvements] | — |
| Contextual Embeddings | 3.7% [src: anthropic2024, §Performance improvements] | 35% [src: anthropic2024, §Performance improvements] |
| ＋ Contextual BM25 | 2.9% [src: anthropic2024, §Performance improvements] | 49% [src: anthropic2024, §Performance improvements] |
| ＋ Reranking | 1.9% [src: anthropic2024, §Performance improvements] | 67% [src: anthropic2024, §Performance improvements] |

## 相關頁面
- [Anthropic 2024](../sources/anthropic2024.md)
- [切塊（chunking）](chunking.md)
- [檢索器（retriever）](retriever.md)
