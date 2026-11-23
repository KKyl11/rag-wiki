---
type: concept
title: LLM Wiki
sources: [karpathy-llmwiki]
updated: 2026-11-23
---

# LLM Wiki

## 一句話白話定義
LLM Wiki 是讓 AI 幫你持續整理一份互相連結的筆記 wiki：每讀一篇新資料，就把重點整合進去，而不是每次提問才重新翻原始資料。[src: karpathy-llmwiki, §The core idea]

## 組成
- 三層：唯讀的原始資料（raw sources）、LLM 維護的 wiki、規定規則的 schema（如 AGENTS.md）。[src: karpathy-llmwiki, §Architecture]
- 兩個特殊檔：index.md（內容目錄）與 log.md（只能附加的時間紀錄）。[src: karpathy-llmwiki, §Indexing and logging]

## 操作
- Ingest、Query、Lint 三種操作；好的查詢答案可以寫回 wiki。[src: karpathy-llmwiki, §Operations]

## 本專案就是一個 LLM Wiki
- 本 wiki 依此架構建立：`raw/` 唯讀、`wiki/` 由 AI 維護、`AGENTS.md` 是 schema。[src: karpathy-llmwiki, §Architecture]

## 相關頁面
- [Karpathy LLM Wiki](../sources/karpathy-llmwiki.md)
- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
