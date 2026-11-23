# G3 忠實度審查 round 1（run-002，獨立 subagent）

- 結果：**FAIL — 3/15 頁**（8、12、14）

---

## 總結
FAIL；FAIL 的頁碼：[08, 12, 14]

## 逐頁（只列 FAIL 頁的原文要點；slide 01–07、09–11、13、15 均為 PASS）
### slide 08 — FAIL
- 問題 1：「Advanced RAG 在檢索前與檢索後加上各種策略。以下是改良檢索的一個例子」→ 把 Contextual Retrieval 歸成 Advanced RAG 的例子，是簡報自己的歸類；rag-paradigms.md 的 Advanced RAG 策略沒提到 Contextual Retrieval，contextual-retrieval.md 也沒把它歸到任何範式。類型：無依據
- 問題 2：「……再建索引；最後用 reranking 把最相關的片段排到前面」→ 讓人以為 reranking 是 Contextual Retrieval 固定的最後一步；wiki 中 reranking 是另外疊加的選項。類型：無依據
- 問題 3：表格「（降 35%）」等沒說跟誰比 → 拿掉了「和基準比的相對降幅」這個限定。類型：無依據（限定詞被拿掉）
### slide 12 — FAIL
- 問題 1：把「擴充脈絡長度的模型也有 Lost in the Middle」列為「RAG 仍有價值的理由」→ 自行歸類；wiki 把 Liu 的發現放在「長上下文的實際表現」，且 Lost in the Middle 也被列為 RAG 自己的問題。類型：無依據（自行歸類）
- 問題 2：拖慢推理、出處可驗證寫成無歸屬的一般事實 → wiki 中是 Gao 的論點。類型：無依據（歸屬被拿掉）
### slide 14 — FAIL
- 問題 1：小測驗「RAG 的三個步驟」→ 把 Naive RAG 的三步講成所有 RAG，拿掉限定詞（條列有寫，測驗題沒有）。類型：誇大
- 問題 2：「RAG 和 LLM Wiki 最大的差別」→「最大」是簡報自己的判斷，wiki 只並列多個面向。類型：無依據
