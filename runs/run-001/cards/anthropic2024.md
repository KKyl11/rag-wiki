---
source: anthropic2024
wiki_pages: [sources/anthropic2024.md, concepts/contextual-retrieval.md, concepts/retriever.md, comparisons/rag-vs-long-context.md, concepts/reranking.md]
---
# 證據卡：anthropic2024（Contextual Retrieval）
- E1: 切塊的問題：片段「公司營收比上一季成長 3%」沒說是哪家公司、哪一季，難以被正確檢索。[wiki: concepts/contextual-retrieval.md] [src: anthropic2024, §The context conundrum in traditional RAG]
- E2: Contextual Retrieval：用 Claude 讀整份文件與片段，生成 50–100 tokens 的說明加在片段前面，再建 embedding 與 BM25 索引。[wiki: concepts/contextual-retrieval.md] [src: anthropic2024, §Implementing Contextual Retrieval]
- E3: top-20 檢索失敗率：基準 5.7%；Contextual Embeddings 3.7%（降 35%）；再加 Contextual BM25 2.9%（降 49%）；再加 Reranking 1.9%（降 67%）。[wiki: concepts/contextual-retrieval.md] [src: anthropic2024, §Performance improvements]
- E4: 查「Error code TS-999」時，embedding 可能只找到一般錯誤碼的內容，BM25 則能精確比對「TS-999」。[wiki: concepts/retriever.md] [src: anthropic2024, §A primer on RAG: scaling to larger knowledge bases]
- E5: 知識庫小於 200,000 tokens（約 500 頁）時，可以直接全部放進 prompt，不需要 RAG。[wiki: comparisons/rag-vs-long-context.md] [src: anthropic2024, §A note on simply using a longer prompt]
- E6: 放越多片段越可能包含相關資訊，但資訊太多會讓模型分心；在 5、10、20 片段中，20 最好。[wiki: comparisons/rag-vs-long-context.md] [src: anthropic2024, §Implementation considerations]
