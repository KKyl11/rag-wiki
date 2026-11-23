---
source: lewis2020
wiki_pages: [sources/lewis2020.md, concepts/rag.md, concepts/llm-knowledge-limits.md, concepts/parametric-vs-nonparametric-memory.md, concepts/retriever.md, concepts/chunking.md]
---
# 證據卡：lewis2020（RAG 原始論文）
- E1: RAG 結合「預訓練參數記憶」與「非參數記憶」來生成語言。[wiki: concepts/rag.md] [src: lewis2020, p.1]
- E2: 模型用輸入 x 檢索文件 z，再把 z 當成額外脈絡來生成輸出 y；檢索器取 top-K 段文字，生成器根據查詢與段落產生答案。[wiki: concepts/rag.md] [src: lewis2020, p.2]
- E3: 純參數模型的問題：難以擴充或修改記憶、難以說明預測依據、會產生「幻覺」。[wiki: concepts/llm-knowledge-limits.md] [src: lewis2020, p.1]
- E4: 參數記憶存在模型參數裡（BART 生成器），更新要再訓練；非參數記憶是外部文件索引（Wikipedia 向量索引），替換索引即可更新。[wiki: concepts/parametric-vs-nonparametric-memory.md] [src: lewis2020, p.3]
- E5: 記憶由原始文字構成，人可讀也可改（human-readable、human-writable）。[wiki: concepts/parametric-vs-nonparametric-memory.md] [src: lewis2020, p.9]
- E6: 換索引實驗：82 位在 2016 到 2018 年間換人的世界領袖，用「Who is {position}?」提問。[wiki: sources/lewis2020.md] [src: lewis2020, p.7-8]
- E7: 用 2016 索引問 2016 領袖答對 70%；用 2018 索引問 2018 領袖答對 68%；索引與年份不對時只剩 12% 與 4%。[wiki: sources/lewis2020.md] [src: lewis2020, p.8]
- E8: Jeopardy 出題人工評估（452 組）：認為 BART 較符合事實的只有 7.1%，認為 RAG 較符合事實的有 42.7%。[wiki: sources/lewis2020.md] [src: lewis2020, p.6]
- E9: 知識庫：每篇 Wikipedia 文章切成不重疊的 100 字片段，共 21M 段，每段算一個 embedding。[wiki: concepts/chunking.md] [src: lewis2020, p.4]
- E10: 檢索器 DPR 把文件與查詢各自編碼成向量（embedding），用最大內積搜尋（MIPS）找 top-k。[wiki: concepts/retriever.md] [src: lewis2020, p.3]
- E12: 作者認為以 Wikipedia 為依據讓模型較少「幻覺」、較符合事實。[wiki: sources/lewis2020.md] [src: lewis2020, p.10]
- E11: 限制：Wikipedia 或任何外部知識來源都不可能完全正確、完全沒有偏誤。[wiki: sources/lewis2020.md] [src: lewis2020, p.10]
