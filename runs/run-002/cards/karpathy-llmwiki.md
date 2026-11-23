---
source: karpathy-llmwiki
wiki_pages: [sources/karpathy-llmwiki.md, concepts/llm-wiki.md, comparisons/rag-vs-llm-wiki.md]
---
# 證據卡：karpathy-llmwiki（LLM Wiki）— v2
- E1: RAG 查詢時才檢索相關片段並生成，每次從頭重新發現，沒有累積。〔限定：Karpathy〕[wiki: comparisons/rag-vs-llm-wiki.md] [src: karpathy-llmwiki, §The core idea]
- E2: LLM Wiki：加入來源時就整合進 wiki，編譯一次、持續更新；交叉引用與矛盾標註已做好，越用越豐富。[wiki: comparisons/rag-vs-llm-wiki.md] [src: karpathy-llmwiki, §The core idea]
- E3: 三層：唯讀的原始資料（raw sources）、LLM 維護的 wiki、規定規則的 schema（如 AGENTS.md）。[wiki: concepts/llm-wiki.md] [src: karpathy-llmwiki, §Architecture]
- E4: 怎麼找資料：先讀 index 找頁面再深入；中等規模不需要 embedding 基礎設施。〔限定：中等規模〕[wiki: comparisons/rag-vs-llm-wiki.md] [src: karpathy-llmwiki, §Indexing and logging]
- E5: LLM 負責所有維護工作，人負責挑來源與提問。[wiki: comparisons/rag-vs-llm-wiki.md] [src: karpathy-llmwiki, §The core idea]
