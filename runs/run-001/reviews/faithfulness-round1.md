# G3 忠實度審查 round 1（獨立 subagent 原文）

- 審查者只拿到：`reviewers/faithfulness.md`、`drafts/`、各頁 frontmatter 列出的 wiki 頁
- 結果：**FAIL — 4/15 頁**（6、7、9、10）

---

## 總結
FAIL；FAIL 的頁碼：[6, 7, 9, 10]

## 逐頁
### slide 01 — PASS
- 問題（若有）：無。「需要最新資訊的問題…可能會編造答案」有 llm-knowledge-limits.md 支持；RAG 定義與 rag.md 的一句話定義一致。

### slide 02 — PASS
- 問題（若有）：無。三個問題（幻覺／要再訓練才能跟上／難以說明依據）和「引用外部知識能有效減少事實錯誤、持續更新知識」，都和 llm-knowledge-limits.md 一致。

### slide 03 — PASS
- 問題（若有）：無。表格三列和 parametric-vs-nonparametric-memory.md 一致；課本／內化的比喻有標成來源原有（Gao），也和 rag-vs-fine-tuning.md 一致。

### slide 04 — PASS
- 問題（若有）：無。三步流程、Naive RAG＝「Retrieve-Read」、檢索器取 top-K 後由生成器回答，都有 rag-paradigms.md／rag.md 支持；圖書館比喻有標「🎓 教學比喻（非來源內容）」，而且沒有夾帶事實或數字。

### slide 05 — PASS
- 問題（若有）：無。100 字片段、21M 段、100／256／512 token，以及大塊和小塊的取捨，都和 chunking.md 一致。

### slide 06 — FAIL
- 問題（若有）：「所以常把兩者混合（hybrid）使用。」→ 稿子加上了「常」這個普遍程度的說法，wiki 沒寫 → retriever.md 只寫兩者「可以混合（hybrid）互補」，另外記錄了 Anthropic 的一種混合做法（rank fusion），沒說這是常見做法。
- 類型：誇大
- 問題（若有）：「BM25：用字詞重疊來比對，擅長找精確的詞句。」→「擅長找精確的詞句」是從單一例子推成一般特性，本頁引用的 wiki 沒有這句一般性的說法 → retriever.md 只寫 BM25 是「字詞重疊式檢索」，並舉 Anthropic 的例子：查「TS-999」時 BM25「能精確比對」。（這句一般性的說法只出現在 sources/anthropic2024.md，但本頁沒有引用那一頁。）
- 類型：無依據

### slide 07 — FAIL
- 問題（若有）：標題「換一本「課本」，答案就跟著更新」→ 把換索引比成換「課本」，這是比喻，但沒有標記。本頁只引用 sources/lewis2020.md，那一頁沒有這個比喻（課本比喻出自 Gao，在 rag-vs-fine-tuning.md，本頁沒引用）。所以以本頁的依據來說，這是沒標記的比喻 → lewis2020.md 只寫「只要替換非參數記憶，就能更新 RAG 的世界知識」（index hot-swapping）。內文的數字（82 位、70%、68%、12%／4%）都正確。
- 類型：未標比喻

### slide 08 — PASS
- 問題（若有）：無。營收 3% 的例子、50–100 tokens 的說明、先建 embedding 與 BM25 索引、reranking 的作用，都有依據；失敗率 5.7%→3.7%／2.9%／1.9%，降幅 35%／49%／67%，都和 contextual-retrieval.md 一致；三種範式的說法也有 rag-paradigms.md 支持。

### slide 09 — FAIL
- 問題（若有）：「結果：答案比一般 RAG 更全面；一般 RAG 的答案則比較直接。」→ 把特定實驗的勝率講成一般結論，省略了條件：只有兩個資料集（Podcast、新聞），而且是勝率 72–83%／72–80%，不是全面勝出 → graphrag.md 寫的是「全面性勝率對 vector RAG 為 72–83%（Podcast）與 72–80%（新聞）」「vector RAG 的答案則最直接」。
- 類型：誇大
- （Self-RAG 的部分忠實，沒有問題。）

### slide 10 — FAIL
- 問題（若有）：「以 Wikipedia 為依據能讓模型較少「幻覺」，但「較少」不等於「沒有」。」→ 刪掉了「作者認為」，把作者的看法講成既定事實 → sources/lewis2020.md 寫的是「作者認為以 Wikipedia 為依據讓模型較少「幻覺」、較符合事實」。
- 類型：誇大
- （三類錯誤來源的條列，有 rag-paradigms.md 與 lewis2020.md 的限制一節支持。）

### slide 11 — PASS
- 問題（若有）：無。U 形曲線、GPT-3.5-Turbo 在 20／30 篇文件的設定下低於 closed-book 的 56.1%、表現在 recall 飽和前就已飽和、超過 20 篇只有些微進步，以及 reranking／截短清單的對策，都和 wiki 一致。⚖️ 矛盾有並陳 Liu 與 Gao（引述）兩說，也註明後者只有二手描述、無法比對設定，和 rag-vs-long-context.md 一致。

### slide 12 — PASS
- 問題（若有）：無。200,000 tokens（約 500 頁）、拖慢推理、可找到出處而長上下文像黑盒子、擴充脈絡長度的模型也有中間迷失、和 fine-tuning 不互斥可互補，都和本頁引用的三頁一致。

### slide 13 — PASS
- 問題（若有）：無。表格四列和三層架構，都和 rag-vs-llm-wiki.md、llm-wiki.md 一致。

### slide 14 — PASS
- 問題（若有）：無。回顧重點和測驗答案（三步驟、換索引不必重新訓練、中間最容易被忽略、被問時才檢索 vs 加入資料時就整合），都有本頁引用的頁面支持。

### slide 15 — PASS
- 問題（若有）：無。七筆書目的作者、年份、標題、arXiv 編號，都和各 sources 頁一致。
