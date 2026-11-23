# N3 大綱（round 2）：RAG 是什麼？讓 AI 先查資料再回答

- 讀者：完全不懂 RAG 的大學生
- 結構：封面＋開場問題 → 問題 → 核心概念 → 流程（總覽、切塊、嵌入與檢索）→ 例子 → 進階 → 限制與爭議 → 比較（呼應作業）→ 回顧＋測驗 → 參考資料
- 只用 cards/ 的證據；每頁的 wiki 欄位＝頁尾出處
- round 2 修改（依 reviews/outline-round1.md）：[必改] 舊 Slide 6 拆成「切塊」「嵌入與檢索」兩頁並補 lewis2020#E10；封面與開場合併；開場改用 gao2023#E1 不劇透例子；新增「RAG 也會答錯」頁用上 gao2023#E13、lewis2020#E11；Slide 9 拿掉反思標記細節；限制頁加入 liu2023#E6；爭議頁聚焦「何時不需要 RAG」；進階頁用 gao2023#E6 當框架；例子頁拿掉 lewis2020#E8
- round 2 之後（依 reviews/outline-round2.md 建議）：Slide 12 補 liu2023#E3、Slide 13 補 karpathy-llmwiki#E5

## Slide 1: RAG 是什麼？讓 AI 先查資料再回答
- 教學目標: 用一個問題開場，並用白話一句話知道 RAG 在做什麼（先找文件，再根據文件回答）
- evidence: lewis2020#E2, gao2023#E1
- wiki: concepts/rag.md, concepts/llm-knowledge-limits.md

## Slide 2: LLM 為什麼會答錯或過時？
- 教學目標: 說出只靠模型內部知識的三個問題：幻覺、過時、無法追溯
- evidence: lewis2020#E3, gao2023#E1, gao2023#E2
- wiki: concepts/llm-knowledge-limits.md

## Slide 3: 核心概念：背在腦中 vs 隨時翻課本
- 教學目標: 理解參數記憶與非參數記憶的差別，RAG 把兩者結合；fine-tuning 第一次出現時附白話說明
- evidence: lewis2020#E1, lewis2020#E4, lewis2020#E5, gao2023#E7
- wiki: concepts/parametric-vs-nonparametric-memory.md, comparisons/rag-vs-fine-tuning.md

## Slide 4: RAG 怎麼運作：索引 → 檢索 → 生成
- 教學目標: 能說出 RAG 的三步流程（embedding 只給一句白話，細節留到 Slide 6）
- evidence: gao2023#E3, lewis2020#E2
- wiki: concepts/rag-paradigms.md, concepts/rag.md

## Slide 5: 第一步拆開看：切塊
- 教學目標: 理解為什麼要切塊，以及切大切小的取捨
- evidence: gao2023#E4, lewis2020#E9
- wiki: concepts/chunking.md

## Slide 6: 第二步拆開看：嵌入與檢索
- 教學目標: 理解 embedding（文字變向量、找最像的 top-k），以及 BM25 精確比對的互補
- evidence: lewis2020#E10, gao2023#E5, anthropic2024#E4
- wiki: concepts/retriever.md

## Slide 7: 具體例子：換一本「課本」，答案就跟著更新
- 教學目標: 用原始論文的換索引實驗看懂 RAG 的好處
- evidence: lewis2020#E6, lewis2020#E7
- wiki: sources/lewis2020.md

## Slide 8: 進階 1：Contextual Retrieval——替片段補上下文
- 教學目標: 知道 RAG 從 Naive 演進到 Advanced／Modular；理解切塊會丟失上下文，以及補脈絡＋BM25＋reranking 的效果
- evidence: gao2023#E6, anthropic2024#E1, anthropic2024#E2, anthropic2024#E3, gao2023#E12
- wiki: concepts/rag-paradigms.md, concepts/contextual-retrieval.md, concepts/reranking.md

## Slide 9: 進階 2：Self-RAG 與 GraphRAG
- 教學目標: 知道兩種變形各自解決什麼問題（各一句做法）
- evidence: asai2023#E1, asai2023#E2, edge2024#E1, edge2024#E2, edge2024#E3
- wiki: concepts/self-rag.md, concepts/graphrag.md

## Slide 10: RAG 也會答錯
- 教學目標: 避免誤以為 RAG 能完全消除幻覺——檢索可能找錯、生成可能沒照資料、資料本身也可能有錯
- evidence: gao2023#E13, lewis2020#E11, lewis2020#E12
- wiki: concepts/rag-paradigms.md, sources/lewis2020.md

## Slide 11: 限制：資料塞越多越好嗎？（Lost in the Middle）
- 教學目標: 理解中間迷失（closed-book 要白話說明），並看到「多放文件」的兩種說法
- evidence: liu2023#E1, liu2023#E2, liu2023#E4, liu2023#E6, gao2023#E11, anthropic2024#E6
- wiki: concepts/lost-in-the-middle.md, comparisons/rag-vs-long-context.md, sources/liu2023.md

## Slide 12: 爭議：模型讀得下整本書，還需要 RAG 嗎？
- 教學目標: 知道什麼時候不需要 RAG、什麼時候 RAG 仍有價值；fine-tuning 只一句「可互補」
- evidence: anthropic2024#E5, gao2023#E9, gao2023#E10, gao2023#E8, liu2023#E3
- wiki: comparisons/rag-vs-long-context.md, comparisons/rag-vs-fine-tuning.md, concepts/lost-in-the-middle.md

## Slide 13: RAG vs LLM Wiki（這份作業就是 LLM Wiki）
- 教學目標: 比較「查詢時才檢索」與「平時就整理成 wiki」
- evidence: karpathy-llmwiki#E1, karpathy-llmwiki#E2, karpathy-llmwiki#E3, karpathy-llmwiki#E4, karpathy-llmwiki#E5
- wiki: comparisons/rag-vs-llm-wiki.md, concepts/llm-wiki.md

## Slide 14: 重點回顧＋小測驗
- 教學目標: 自我檢查是否記得核心概念
- evidence: lewis2020#E2, gao2023#E3, liu2023#E1, karpathy-llmwiki#E1
- wiki: concepts/rag.md, concepts/rag-paradigms.md, concepts/lost-in-the-middle.md, comparisons/rag-vs-llm-wiki.md

## Slide 15: 參考資料
- 教學目標: 知道每個內容的原始出處
- evidence: lewis2020#E1, gao2023#E6, liu2023#E1, asai2023#E2, edge2024#E2, anthropic2024#E2, karpathy-llmwiki#E3
- wiki: sources/lewis2020.md, sources/gao2023.md, sources/liu2023.md, sources/asai2023.md, sources/edge2024.md, sources/anthropic2024.md, sources/karpathy-llmwiki.md
