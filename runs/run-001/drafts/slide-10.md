---
slide: 10
title: RAG 也會答錯
section: 限制
layout: content
evidence: [gao2023#E13, lewis2020#E11, lewis2020#E12]
wiki: [concepts/rag-paradigms.md, sources/lewis2020.md]
---
最基本的 RAG（Naive RAG）可能在這兩個地方出錯：

- **檢索**：可能選到不相關的片段，或漏掉關鍵資訊。
- **生成**：可能產生檢索內容不支持的幻覺；整合多段資訊時也可能不連貫或重複。

RAG 原始論文也指出另一個限制：

- **資料本身**：Wikipedia 或任何外部知識來源，都不可能完全正確、完全沒有偏誤。

> 原始論文作者認為，以 Wikipedia 為依據能讓模型較少「幻覺」；但同一篇論文也承認，外部知識來源不可能完全正確。
