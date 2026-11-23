# G2 大綱審查 round 1（run-002，獨立 subagent 原文，排版略精簡）

- 結果：**PASS**（0 必改、9 項建議）

---

## 總結
PASS

## 問題（若有）
- [建議] Slide 3：gao2023#E7 的比喻比較的是 RAG 和 fine-tuning，不是參數記憶和非參數記憶；標題「背在腦中 vs 隨時翻課本」把比喻延伸到參數記憶，fine-tuning 也在這裡第一次出現 → 寫明比喻出自 Gao et al. 的 RAG vs fine-tuning 比較，延伸部分標成教學比喻，或給 fine-tuning 一句白話；補一張參數記憶／外部索引的對照。
- [建議] Slide 4：總覽已用到 embedding、向量資料庫、top-K → 加白話，並註明下兩頁拆開看。
- [建議] Slide 5／8／12：token 沒有解釋 → 第一次出現時給一句白話；Slide 12 搭配「約 500 頁」。
- [建議] Slide 6：cosine similarity、sparse/dense、BERT 類等術語負擔太重 → 只保留「算相似度」與 BM25／embedding 互補，用 TS-999 例子。
- [建議] Slide 8：三種範式、Contextual Retrieval、reranking、失敗率定義與四列數字 → 範式只留一句開頭，主角是 Contextual Retrieval，寫清楚「第一列單獨使用，後兩列逐項疊加」；或把 Naive RAG 名稱移到 Slide 4。
- [建議] Slide 9：份量偏重 → 對稱格式，GraphRAG 數字附條件（Podcast／新聞、對 vector RAG、LLM 評審、勝率）。
- [建議] Slide 12：fine-tuning 跟標題無關 → 把 gao2023#E8 移到 Slide 3 或縮成一行。
- [建議] Slide 11：可補 anthropic2024#E6；gao2023#E11 要寫明是 Gao et al. 引述 Cuconasu et al.，與 Liu 並列不裁決。
- [建議] lewis2020#E8 可當 Slide 7 補充，不用也不影響理解。
