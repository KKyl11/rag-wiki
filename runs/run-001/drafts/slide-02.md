---
slide: 2
title: LLM 為什麼會答錯或過時？
section: 問題
layout: content
evidence: [lewis2020#E3, gao2023#E1, gao2023#E2]
wiki: [concepts/llm-knowledge-limits.md]
---
只靠「背在參數裡的知識」回答的語言模型，有三個問題：

- **幻覺（hallucination）**：模型可能編造答案；遇到超出訓練資料、或需要最新資訊的問題時特別容易發生。
- **過時**：模型無法輕易擴充或修改記憶，要跟上世界變化得再訓練。
- **無法追溯**：模型難以說明答案的依據，說不出出處。

> 解法方向：引用外部知識，能有效減少事實錯誤的內容，也能持續更新知識。
