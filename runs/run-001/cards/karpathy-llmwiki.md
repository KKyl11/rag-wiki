---
source: karpathy-llmwiki
wiki_pages: [sources/karpathy-llmwiki.md, concepts/llm-wiki.md, comparisons/rag-vs-llm-wiki.md]
---
# 證據卡：karpathy-llmwiki（LLM Wiki）
- E1: RAG 每次提問都從原始文件重新拼湊知識，沒有累積。[wiki: comparisons/rag-vs-llm-wiki.md] [src: karpathy-llmwiki, §The core idea]
- E2: LLM Wiki：加入來源時就整合進 wiki（更新相關頁面、標註矛盾），知識編譯一次、持續更新，越用越豐富。[wiki: comparisons/rag-vs-llm-wiki.md] [src: karpathy-llmwiki, §The core idea]
- E3: 三層架構：唯讀的原始資料（raw sources）、LLM 維護的 wiki、規定規則的 schema（如 AGENTS.md）。[wiki: concepts/llm-wiki.md] [src: karpathy-llmwiki, §Architecture]
- E4: 找資料的方式：先讀 index 找頁面再深入；中等規模不需要 embedding 基礎設施。[wiki: comparisons/rag-vs-llm-wiki.md] [src: karpathy-llmwiki, §Indexing and logging]
- E5: 分工：LLM 負責所有維護工作，人負責挑來源與提問。[wiki: comparisons/rag-vs-llm-wiki.md] [src: karpathy-llmwiki, §The core idea]
