# Run 001 檢查紀錄（workflow v1）

- 主題：RAG 是什麼？讓 AI 先查資料再回答
- Graph：`docs/workflow.md`（v1）；skill：`.claude/skills/topic-slides/SKILL.md`
- 腳本完整輸出：`checks/`；AI 審查原文：`reviews/`；每一步的 commit 訊息以 `run1:` 開頭（`git log --oneline --grep=run1`）

| # | 輪次 | 節點 | 檢查項目 | 結果 | 失敗原因 | 退回到 |
|---|---|---|---|---|---|---|
| 1 | 1 | G1 覆蓋率關卡 | `check_coverage --stage retrieve`：相關頁面 ≥3、來源清單一致 | ✅ PASS | 22 頁、7 個來源 | — |
| 2 | 1 | G1b 卡片關卡 | `check_coverage --stage cards`：每個來源有卡、只引用自己的來源、只用已檢索頁面 | ✅ PASS | 7 張卡、49 個證據項目 | — |
| 3 | 1 | G2 大綱檢查（腳本） | `check_coverage --stage outline`：8–15 頁、證據存在、每個來源都被用到 | ✅ PASS | 14 頁、7/7 來源 | — |
| 4 | 1 | G2 大綱檢查（獨立 AI 審查） | 教學順序、環節完整、一頁一重點 | ❌ FAIL | [必改] Slide 6 一頁塞三個新概念（切塊取捨、embedding、BM25/dense）；另有 10 項建議，其中「限制段沒用到 gao2023#E13、lewis2020#E11，讀者會以為 RAG 能消除幻覺」很重要 | N3 大綱（小圈） |
| 5 | 2 | G2 大綱檢查（腳本） | 同上 | ✅ PASS | 15 頁、7/7 來源 | — |
| 6 | 2 | G2 大綱檢查（新的獨立 AI 審查） | 同上 | ✅ PASS | 0 必改；6 項建議帶到逐頁稿處理（token 白話說明因 wiki 無定義而不採用，避免用模型知識補） | — |
| 7 | 1 | N4 逐頁稿（節點內小 loop） | `check_citations`（全部 15 頁） | ✅ PASS | 第 1 輪即通過；另依 G2 round 2 建議把 liu2023#E3、karpathy-llmwiki#E5 補進大綱（重跑 G2 腳本仍 PASS） | — |
| 8 | 1 | G3 忠實度（腳本） | `check_citations`：出處存在且在檢索結果內、證據編號存在、數字都在被引用頁 | ✅ PASS | — | — |
| 9 | 1 | G3 忠實度（獨立 AI 審查） | 逐頁判定忠實度 | ❌ FAIL | **4/15 頁**：slide 6 加了「常」＋把單一例子推成一般特性（誇大／無依據）；slide 7 標題「換課本」是未標記的比喻；slide 9 把兩個資料集的勝率講成一般結論（誇大）；slide 10 刪掉「作者認為」（誇大），且這句內容**不在證據卡裡**——逐頁稿用了卡片以外的內容，`check_citations` 抓不到 | 只退 6、7、9 回 N4；slide 10 退回 **N2 補卡**（lewis2020 卡缺這一項）再回 N4 |
| 10 | 2 | N2 補卡 → N4 修稿 | lewis2020 卡新增 E12；只改 slide 6、7、9、10；`check_coverage --stage cards/outline` 與 `check_citations --slides 6,7,9,10` | ✅ PASS | — | — |
| 11 | 2 | G3 忠實度（新的獨立 AI 審查，只審 4 頁） | 同上 | ❌ FAIL | slide 6、7、9 通過；**slide 10 仍不過**：把 wiki 明確歸給 Naive RAG 的問題講成所有 RAG 的問題——卡片 gao2023#E13 本來就寫「Naive RAG 的缺點」，是**寫稿時把限定詞拿掉** | 只退 slide 10 回 N4 |
| 12 | 3 | N4 修稿 | 只改 slide 10：加回「Naive RAG」限定，第三點標明出自原始論文；`check_citations --slides 10` | （見下一列） | — | — |
| 13 | 3 | G3 忠實度（新的獨立 AI 審查，只審 slide 10） | 同上 | ❌ FAIL | 稿子說 Naive RAG 只在「兩個地方」出錯，並把「整合不連貫」歸進生成——wiki 是三項並列，這是稿子自己的歸類 | 🛑 **剎車**：G3 已滿 3 輪，不再修。以目前版本繼續（問題很小：分類方式不同，事實沒有錯），記為**未通過項目**，帶到 run-002 處理 |
| 14 | 1 | N5 渲染（節點內小 loop） | `render_deck` → `check_deck`（headless Chrome 量測） | ❌ FAIL | slide 8 溢出 12px、slide 15 溢出 28px | 留在 N5 調 CSS（小圈） |
| 15 | 2 | N5 渲染 | 改 CSS：行高 1.55→1.5、條列間距、表格 padding | ❌ FAIL | slide 15 仍溢出 2px | 留在 N5 |
| 16 | 3 | N5 渲染 | 改 CSS：標題下方間距 22→16px | ✅ PASS | — | — |
| 17 | 1 | G4 渲染檢查（腳本） | `check_deck`：15 頁、頁尾出處、頁碼、渲染文字＝逐頁稿、無溢出、鍵盤翻頁 | ✅ PASS | — | — |
| 18 | 1 | G4 覆蓋率（獨立 AI 審查） | 7 個來源是否實際用到、必要重點、⚖️ 兩說、教學結構 | ✅ PASS | 0 必改、7 項建議。**其中一項其實是忠實度問題、G3 三輪都沒抓到**：slide 8 表格第一列寫「＋ Contextual Embeddings」，暗示逐項疊加，wiki 中它是單獨使用 | — |
| 19 | — | N6 交件 | 全部關卡跑完 | ⚠️ 有條件交件 | 未通過／待修：① slide 10 的分類方式（G3 剎車）② slide 8 的「＋」（G4 發現）③ G4 的 6 項易讀性建議（top-K、失敗率定義、範式名稱、fine-tuning 對照、勝率評審、表格列名） | 帶到 run-002（v2 graph） |

## Run 001 總結

- 交件版本：`deck.html`（15 頁），`check_deck` 全過，G2／G4 獨立審查 PASS，G3 **14/15 頁** PASS（slide 10 剎車後未通過）。
- 失敗統計（`python scripts/report_stats.py runs/run-001`）：G3 忠實度 3 次失敗（共牽涉 5 個「頁次」：4＋1＋1）、N5 渲染小 loop 2 次、G2 大綱 1 次。
- 最常出錯的節點：**G3 忠實度**——但錯誤都是在 **N4 逐頁稿**「為了讓零基礎讀者看懂而簡化」時產生的：拿掉限定詞（「Naive RAG」「作者認為」「兩個資料集的實驗」）、加上概括詞（「常」）、沒標記的比喻（「課本」）、自己的歸類（「兩個地方」）、用了卡片以外的內容。
- `check_citations` 這些都抓不到（它只檢查數字和出處存在），每次都要等獨立 AI 審查才發現，而且每修一輪就要再開一個新的審查者 → 這就是要「往前移」的檢查。
- 一個大圈：G3 → N2（slide 10 用了卡片沒有的內容，回頭補卡）。
