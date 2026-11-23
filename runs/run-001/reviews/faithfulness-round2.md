# G3 忠實度審查 round 2（新的獨立 subagent，只審 slide 6、7、9、10）

- 結果：**FAIL — 1/4 頁**（slide 10）
- 註：審查者原文較長，此處保留判定與理由全文要點；slide 6/7/9 的 PASS 理由略為精簡排版

---

## 總結
FAIL；FAIL 的頁碼：[10]

## 逐頁
### slide 06 — PASS
- 問題：無。編碼成向量、用相似度（例如 cosine similarity）找 top-k，在 retriever.md 有依據；BM25 是字詞重疊式檢索、TS-999 例子、hybrid 可以互補，都是同義改寫；比喻已標記且無數字。

### slide 07 — PASS
- 問題：無。82 位領袖、「Who is {position}?」、70%、68%、12% 與 4%，以及換掉非參數記憶即可更新知識的結論，都和 sources/lewis2020.md 一致。

### slide 09 — PASS
- 問題：無。Self-RAG 與 GraphRAG 的問題、做法與 72–83%／72–80% 勝率都和 wiki 一致；「回答時再彙整這些摘要」簡化了 map-reduce 但意思未反轉。

### slide 10 — FAIL
- 問題：「RAG 不是『保證正確』的魔法。錯誤可能出在三個地方：檢索找錯……生成沒照資料……」→ 把 wiki 明確歸給 **Naive RAG** 的問題講成所有 RAG 共通的錯誤來源（過度概括）；「三個地方」的完整分類也是稿子自己的歸納 → concepts/rag-paradigms.md 把這些放在「## Naive RAG 的問題」底下，同頁也寫 Advanced RAG 加上了檢索前與檢索後的策略 → 修正方向：改成「最基本的 RAG（Naive RAG）可能在檢索和生成出錯」，第三點另外標明出自 lewis2020 p.10。
- 類型：誇大
