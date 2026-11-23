---
type: source
key: lewis2020
title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks（Lewis et al., 2020）
url: https://arxiv.org/abs/2005.11401
raw: raw/lewis2020.pdf
sources: [lewis2020]
updated: 2026-11-23
---

# Lewis et al. 2020 — RAG 原始論文

## 書目
- Patrick Lewis 等人（Facebook AI Research、University College London、New York University），arXiv 2005.11401v4，2021-04-12 版。[src: lewis2020, p.1]

## 一句話摘要
提出「檢索增強生成（retrieval-augmented generation, RAG）」：把預訓練的生成模型（參數記憶）接上一個可檢索的 Wikipedia 向量索引（非參數記憶），一起微調，用在需要大量知識的任務上。[src: lewis2020, p.1]

## 要解決的問題
- 大型預訓練語言模型能把事實知識存在參數裡，但「精確存取與操作知識」的能力有限，在知識密集型任務上落後專門架構。[src: lewis2020, p.1]
- 這類模型難以擴充或修改記憶、難以說明預測的依據，而且會產生「幻覺（hallucinations）」。[src: lewis2020, p.1]
- 提供決策出處（provenance）與更新世界知識，仍是未解問題。[src: lewis2020, p.1]

## 核心做法
- 兩個元件：檢索器（retriever）根據輸入 x 找出 top-K 篇文件 z；生成器（generator）根據 x 與 z 生成輸出 y。[src: lewis2020, p.2]
- 檢索器採用 DPR（Dense Passage Retriever），是雙編碼器（bi-encoder）：文件與查詢各自用 BERT-base 編碼成向量，用最大內積搜尋（MIPS）找最相關文件。[src: lewis2020, p.3]
- 生成器採用 BART-large，是有 400M 參數的預訓練 seq2seq transformer；輸入 x 與檢索到的內容 z 直接串接後送進 BART。[src: lewis2020, p.3]
- 論文把文件索引稱為「非參數記憶」，把 BART 生成器的參數稱為「參數記憶」。[src: lewis2020, p.3]
- 兩種變形：RAG-Sequence 整段輸出用同一篇文件；RAG-Token 每個 token 可以依據不同文件，因此能組合多篇文件的內容。[src: lewis2020, p.3]
- 訓練時不告訴模型「該檢索哪篇文件」，檢索器與生成器一起端到端訓練；文件編碼器與索引固定不動，只微調查詢編碼器與 BART。[src: lewis2020, p.3-4]

## 實驗設定（知識庫怎麼建）
- 知識來源是 December 2018 的 Wikipedia 備份，每篇文章切成不重疊的 100 字（word）片段，共 21M 篇文件。[src: lewis2020, p.4]
- 每個片段用文件編碼器算出 embedding，再用 FAISS 建立 MIPS 索引以加速檢索。[src: lewis2020, p.4]
- 訓練時每個查詢檢索 top-k 篇，k 取 5 或 10。[src: lewis2020, p.4]

## 關鍵結果（數字）
- 在 Natural Questions、WebQuestions、CuratedTrec 三個開放領域問答任務達到當時最佳（state of the art）。[src: lewis2020, p.1]
- 即使正確答案不在任何檢索到的文件中，RAG 在 NQ 上仍有 11.8% 答對；抽取式模型在這種情況下是 0%。[src: lewis2020, p.6]
- MS-MARCO 生成任務上，RAG-Sequence 比 BART 高 2.6 個 Bleu 點與 2.6 個 Rouge-L 點。[src: lewis2020, p.6]
- Jeopardy 出題的人工評估（452 組）：認為 BART 較符合事實的只有 7.1%，認為 RAG 較符合事實的有 42.7%。[src: lewis2020, p.6]
- FEVER 三分類事實查核：與使用檢索監督的最佳複雜系統差距在 4.3% 以內。[src: lewis2020, p.6]
- FEVER 中，top-1 檢索文件來自標準答案文章的比例是 71%，top-10 中含標準答案文章的比例是 90%。[src: lewis2020, p.7]
- 把檢索器換成 BM25：FEVER 上 BM25 最好（論文推測因為 FEVER 的陳述以實體為中心，適合字詞重疊式檢索），其他任務則是可微分的 dense 檢索較好。[src: lewis2020, p.7]

## 換索引就能更新知識（index hot-swapping）
- 實驗：82 位在 2016 到 2018 年間換人的世界領袖，用「Who is {position}?」提問。[src: lewis2020, p.7-8]
- 用 2016 索引問 2016 領袖答對 70%；用 2018 索引問 2018 領袖答對 68%；索引與年份不對時只剩 12% 與 4%。[src: lewis2020, p.8]
- 結論：只要替換非參數記憶，就能更新 RAG 的世界知識，不需重新訓練。[src: lewis2020, p.8]

## 作者指出的好處與限制
- 記憶由原始文字構成，所以人看得懂（human-readable）、也能直接編輯（human-writable）。[src: lewis2020, p.9]
- 作者認為以 Wikipedia 為依據讓模型較少「幻覺」、較符合事實。[src: lewis2020, p.10]
- 限制：Wikipedia 或任何外部知識來源都不可能完全正確、完全沒有偏誤。[src: lewis2020, p.10]

## Wiki 維護註記
- 論文內部數字不一致：內文說 RAG 與 BART「都符合事實」的比例是 17%（p.6），但 Table 4 的「Both good」是 11.7%、「Both poor」是 17.7%（p.8）。簡報不要使用這個數字。[src: lewis2020, p.6; lewis2020, p.8]

## 相關頁面
- [檢索增強生成（RAG）](../concepts/rag.md)
- [參數記憶 vs 非參數記憶](../concepts/parametric-vs-nonparametric-memory.md)
- [檢索器（retriever）](../concepts/retriever.md)
- [切塊（chunking）](../concepts/chunking.md)
- [LLM 的知識限制](../concepts/llm-knowledge-limits.md)
