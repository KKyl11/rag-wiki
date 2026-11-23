# G2 大綱審查 round 2（新的獨立 subagent 原文）

- 審查者只拿到：`reviewers/outline.md`、`outline.md`、`cards/*.md`（沒有看 round 1 的審查）
- 結果：**PASS**（0 項必改、6 項建議）

---

## 總結
PASS

## 問題（若有）
- [建議] Slide 5：gao2023#E4 的切塊大小寫成「100、256、512 tokens」，但整份大綱都沒有說明 token 是什麼。token 之後還會出現在 Slide 8（50–100 tokens）和 Slide 12（200,000 tokens）。零基礎讀者仍然看得懂「切成固定長度」的意思，所以不列為必改。建議在 Slide 5 的教學目標加一句：「token 第一次出現時給白話說明」，例如說它是模型計算文字長度的單位。也可以先用 lewis2020#E9 的「100 字片段」帶入，再提 token。Slide 12 可以沿用 anthropic2024#E5 的「約 500 頁」，讓讀者有個實際的量感。
- [建議] Slide 8：這頁有三個新東西：三種範式（gao2023#E6）、Contextual Retrieval，以及第一次出現的 reranking（gao2023#E12）。另外還有 anthropic2024#E3 的四個數字，份量偏重。標題也只寫了 Contextual Retrieval，和教學目標對不太上。建議範式只用一句話當過場：「RAG 從 Naive 演進到 Advanced／Modular，以下是 Advanced 的一個例子」。reranking 給一句白話：「把最相關的片段排到前面」。圖表就用 anthropic2024#E3 的失敗率逐步下降。
- [建議] Slide 9：教學目標只寫「各一句做法」，evidence 卻放了 edge2024#E3 的全面性勝率數字（72–83%、72–80%），裡面還有沒解釋過的「vector RAG」和「勝率」。建議二選一：拿掉 E3；或保留一句「GraphRAG 的回答比一般 RAG 更全面，一般 RAG 的回答則比較直接」，並把 vector RAG 改稱「一般 RAG（Slide 6 那種用向量找片段的做法）」。
- [建議] Slide 11：這頁有 6 條 evidence，份量偏重。liu2023#E4 用到「recall」這個術語卻沒有安排白話說明。gao2023#E11（加入不相關文件反而可能讓準確率提升超過 30%）很反直覺，夾在「多放文件好不好」的兩種說法中間，零基礎讀者容易混亂。建議這頁的主軸是 U 形曲線，用 liu2023#E1、E2 加 closed-book 的白話說明。「多放文件」的兩種說法用 liu2023#E2/E4 對照 anthropic2024#E6 就夠了，並說明兩者的實驗設定不同。如果保留 gao2023#E11，要明講這是一個與原本假設相反的研究結果。recall 改寫成白話，例如「檢索器找到的相關文件越來越多，模型表現卻不再提升」。
- [建議] Slide 11 或 12：liu2023#E3（即使是擴充脈絡長度的模型也有中間迷失現象）完全沒用到。它正好可以銜接 Slide 12 的「模型讀得下整本書，還需要 RAG 嗎？」，也是零基礎讀者理解「長上下文不等於全部讀得好」的關鍵。建議加到 Slide 11 的結尾或 Slide 12 的 evidence。
- [建議] Slide 13：karpathy-llmwiki#E3 提到 schema（如 AGENTS.md），零基礎讀者不會懂。建議白話寫成「一份規定 AI 怎麼整理資料的規則檔」，或者這頁只用 E1、E2、E4 做比較，把三層架構留在一句話。karpathy-llmwiki#E5（LLM 負責維護、人負責挑來源與提問）沒用到，它很適合用來對照 RAG，可考慮補進來。
