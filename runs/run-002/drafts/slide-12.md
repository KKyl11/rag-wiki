---
slide: 12
title: 爭議：模型讀得下整本書，還需要 RAG 嗎？
section: 限制與爭議
layout: content
evidence: [anthropic2024#E5, gao2023#E9, gao2023#E10, liu2023#E3, gao2023#E8]
wiki: [comparisons/rag-vs-long-context.md, comparisons/rag-vs-fine-tuning.md, concepts/lost-in-the-middle.md]
---
LLM 現在能處理超過 200,000 tokens 的脈絡，過去靠 RAG 的長文件問答，現在可以把整份文件直接放進 prompt。

### 可以不用 RAG 的時候
- Anthropic 的建議：知識庫小於 200,000 tokens（約 500 頁）時，可以直接全部放進 prompt。

### Gao et al. 認為 RAG 仍需要的理由
- 一次給大量脈絡會明顯拖慢推理速度。
- RAG 能找到原始出處讓使用者驗證；只靠長上下文的生成像黑盒子。

另外，Liu et al. 發現擴充脈絡長度的模型也有 Lost in the Middle 現象（見上一頁）。

> 另一個比較：RAG 擅長精確查找、可即時更新；fine-tuning 擅長複製特定結構、風格或格式。兩者不互斥，可以互補。
