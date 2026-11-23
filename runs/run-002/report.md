# Run 002 檢查紀錄（workflow v2）

- 主題：RAG 是什麼？讓 AI 先查資料再回答（與 run-001 相同，方便比較）
- Graph：`docs/workflow.md` **v2**（差異見 §8：忠實度的機械檢查往前移到 N2／N4）
- 執行前的 wiki 更新：把 run-001 覆蓋率審查發現的兩個缺口寫回 wiki（`wiki/log.md` 的 query 紀錄）
- 腳本完整輸出：`checks/`；AI 審查原文：`reviews/`；commit 訊息以 `run2:` 開頭

| # | 輪次 | 節點 | 檢查項目 | 結果 | 失敗原因 | 退回到 |
|---|---|---|---|---|---|---|
| 1 | 1 | G1 覆蓋率關卡 | `check_coverage --stage retrieve` | ✅ PASS | 22 頁、7 個來源 | — |
| 2 | 1 | G1b 卡片關卡（v2） | `check_coverage --stage cards`：＋含數字的項目必須有〔限定〕、限定詞必須在 wiki | ✅ PASS | 7 張卡、52 個證據項目，28 個帶〔限定〕 | — |
| 3 | 1 | G2 大綱檢查（腳本＋獨立 AI 審查） | 8–15 頁、證據存在、來源全用到；教學結構 | ✅ PASS | 腳本 PASS；審查 0 必改、9 項建議（帶到逐頁稿）。G2 後小調：Slide 15 的 anthropic 證據改用不帶限定的 E4、Slide 11 依建議補 anthropic2024#E6（重跑 G2 腳本 PASS） | — |
| 4 | 1 | N4 逐頁稿（小 loop，v2 規則） | `check_citations`：數字、出處＋**限定詞保留、概括詞、引號詞** | ✅ PASS | 第 1 輪通過。為確認不是「檢查沒作用」：在副本中故意拿掉 slide 9 的「Podcast／新聞」與 slide 10 的「Naive RAG」，腳本正確 FAIL（`checks/mutation-test-v2-qualifiers.txt`）——正好是 run-001 G3 抓到的兩種錯 | — |
| 5 | 1 | G3 忠實度（腳本） | 同上 | ✅ PASS | — | — |
| 6 | 1 | G3 忠實度（獨立 AI 審查） | 逐頁判定忠實度 | ❌ FAIL | **3/15 頁**（run-001 第 1 輪是 4/15）：slide 8 把 Contextual Retrieval 歸成 Advanced RAG 例子（自行歸類）、reranking 寫成固定步驟、降幅沒寫「相對基準」；slide 12 把 Lost in the Middle 歸為 RAG 的理由（自行歸類）、拿掉 Gao 的歸屬；slide 14 測驗題拿掉「Naive」限定、「最大的差別」自下判斷 | 只退 8、12、14 回 N4（待續） |
| 7 | 2 | N4 修稿 | 只改 slide 8、12、14（拿掉自行歸類、加回 Gao 歸屬與相對降幅、測驗題加 Naive 限定）；`check_citations` 全部 15 頁 | ✅ PASS | — | — |
| 8 | 1 | N5 渲染（小 loop） | `render_deck` → `check_deck`（headless Chrome） | ❌ FAIL | slide 14 溢出 6px（字太多，不是版面問題） | 依 graph 退回 N4 縮短 slide 14（拿掉與小測驗重複的第 4 點） |
| 9 | 2 | N5 渲染 | 重新渲染＋`check_deck` | ✅ PASS | — | — |
| 10 | 1 | G4 渲染檢查（腳本） | 15 頁、頁尾出處、頁碼、文字＝逐頁稿、無溢出、鍵盤翻頁 | ✅ PASS | — | — |
| 11 | 2 | G3 忠實度（新的獨立 AI 審查，只審 8、12、14） | 同上 | ❌ FAIL | 12、14 通過；slide 8 新加的引言「改良檢索這一步」又是自行歸類（實際改的是建索引前的處理） | 只退 slide 8 回 N4 |
| 12 | 3 | N4 修稿＋重新渲染 | slide 8 引言改用 wiki 原句「先替每個片段補一句說明，再拿去建索引」；`check_citations`、`check_deck` | ✅ PASS | 註：因截止時間，渲染與 G3 審查並行（渲染是確定性腳本，改字後已重新渲染並重跑 `check_deck`） | — |
| 13 | 1 | G4 覆蓋率（獨立 AI 審查） | 來源都用到、必要重點、⚖️ 兩說、教學結構 | ✅ PASS | 0 必改、5 項易讀性建議（記錄於 reviews/，因截止時間未再改，列為後續改進） | — |
| 14 | 3 | G3 忠實度（新的獨立 AI 審查，只審 slide 8） | 同上 | ✅ PASS | **15/15 頁通過**，未觸發剎車 | — |
| 15 | — | N6 交件 | 全部關卡通過 | ✅ 交件 | `deck.html`（15 頁）；G4 的 5 項易讀性建議列為後續改進 | 使用者最終驗收 |

## Run 002 總結
- 全部關卡通過：G3 **15/15**（3 輪內完成，未觸發剎車）、G2／G4 獨立審查 PASS、`check_deck` 全過。
- 失敗統計（`python scripts/report_stats.py runs/run-002`）：3 次（G3 2 次、N5 1 次），run-001 是 6 次；大圈 1 → 0；剎車 1 → 0。
- v2 往前移的檢查：run-001 的「拿掉實驗條件、概括詞、未標記比喻」沒有再出現；剩下的 G3 錯誤都是「自行歸類／拿掉歸屬」這類意思層次的問題。
