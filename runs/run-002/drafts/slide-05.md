---
slide: 5
title: 第一步拆開看：切塊（chunking）
section: 流程
layout: content
evidence: [gao2023#E4, lewis2020#E9]
wiki: [concepts/chunking.md]
---
- **為什麼要切？** 把長文件切成一小段一小段，檢索器才能一段一段比對、挑選。
- **RAG 原始論文的做法**：每篇 Wikipedia 文章切成不重疊的 100 字片段，共 21M 段。
- **最常見的做法**：以固定 token 數切分，例如 100、256、512。

| | 切大塊 | 切小塊 |
|---|---|---|
| 好處 | 保留較多脈絡 | 雜訊少 |
| 代價 | 雜訊多、處理時間與成本較高 | 可能傳達不了必要的脈絡 |
