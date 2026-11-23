---
slide: 12
title: 爭議：模型讀得下整本書，還需要 RAG 嗎？
section: 限制與爭議
layout: content
evidence: [anthropic2024#E5, gao2023#E9, gao2023#E10, gao2023#E8, liu2023#E3]
wiki: [comparisons/rag-vs-long-context.md, comparisons/rag-vs-fine-tuning.md, concepts/lost-in-the-middle.md]
---
現在的 LLM 能處理超過 200,000 tokens 的脈絡，引發「還需不需要 RAG」的討論。

### 可以不用 RAG 的時候
- 知識庫小於 200,000 tokens（約 500 頁）時，可以直接把整個知識庫放進 prompt。

### RAG 仍有價值的理由
- 一次塞大量脈絡會明顯拖慢推理速度。
- RAG 能找到原始出處讓人驗證；只靠長上下文的生成像黑盒子。
- 讀得下不等於讀得好：擴充脈絡長度的模型也有中間迷失現象。

> 和 fine-tuning 的關係：兩者不互斥，可以互補。
