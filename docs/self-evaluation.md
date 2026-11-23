# 依評分標準自評

| 評分條件 | 是否達成 | 證據檔案 |
|---|---|---|
| **6 分**：完成 Wiki 與 HTML 簡報 | ✅ | `wiki/`（22 頁）、`deck.html` |
| **7–8 分**：LLM Wiki 完成 | ✅ 先討論後生成；7 篇逐篇 ingest；lint 0 error | `docs/discussion.md`、`docs/requirements-check.md`、`wiki/log.md`、`docs/lint-report.md`、`git log` |
| 7–8 分：可正常瀏覽的教學 HTML 簡報 | ✅ 單檔、鍵盤翻頁、頁碼；headless Chrome 量測無溢出、翻頁實測有效 | `deck.html`、`runs/run-002/checks/G4-script-final.txt`、`runs/run-002/screenshots/` |
| 7–8 分：清楚說明 loop / graph 設計 | ✅ Mermaid 圖、節點規格表（輸入／輸出／只能看／不能做／檢查／退回）、重複步驟、剎車、設計理由 | `docs/workflow.md` §1–7、`.claude/skills/topic-slides/SKILL.md` |
| 7–8 分：實際執行結果 | ✅ 兩次完整執行，逐關紀錄 | `runs/run-001/report.md`、`runs/run-002/report.md` |
| **9–10 分**：Wiki 資料與簡報內容有明確對應 | ✅ 每頁頁尾列 wiki 頁面；簡報數字由腳本驗證出現在被引用 wiki 頁，wiki 數字再由 lint 驗證出現在原始 PDF 那一頁（簡報 → wiki → raw 全鏈可驗證）；證據卡標出每條證據的 wiki 頁 | `scripts/check_citations.py`、`scripts/lint_wiki.py`（檢查 j）、`runs/run-002/cards/` |
| 9–10 分：loop / graph 設計合理且說明清楚 | ✅ 依課程 p.43–47 的 graph；大圈小圈理由；每關權限；誠實寫出「人工確認大綱」的取捨 | `docs/workflow.md` §5–6 |
| 9–10 分：有實際執行與檢查紀錄 | ✅ 腳本輸出、AI 審查原文、每步 commit；失敗都是真實的（run-001 6 次、run-002 3 次） | `runs/*/checks/`、`runs/*/reviews/`、`git log --grep=run1`／`--grep=run2` |
| 9–10 分：反思哪個節點容易出錯、如何提前檢查 | ✅ G3 最常出錯、錯誤源頭在 N4；檢查往前移到 N2／N4；回測＋突變測試證明有效；run-002 失敗 6→3、大圈 1→0、剎車 1→0 | `docs/reflection.md`、`docs/workflow.md` §8 |
| 9–10 分：簡報具有清楚的教學結構 | ✅ 開場問題→問題→概念→流程→例子→進階→限制與爭議→比較→回顧＋小測驗→參考資料；兩次獨立覆蓋率審查確認結構完整 | `runs/run-002/outline.md`、`runs/run-002/reviews/coverage-round1.md` |

## 已知不足（誠實列出）
- 「人工確認大綱」以 AI 審查替代（時間限制），見 `docs/workflow.md` §6。
- run-002 的 G4 覆蓋率審查有 5 項易讀性建議（例如 vector RAG 的白話、知識圖的定義）因截止時間未再修改。
- 「token」的白話定義 wiki 沒有，依規則不用模型知識補，所以簡報沒有解釋 token。
- 溢出只量測 1280×720 一種尺寸。
- 因截止時間，run-002 的渲染與 G3 第 2、3 輪審查並行進行（渲染為確定性腳本，改字後已重新渲染並重跑檢查）。

自評：**9–10 分**的五個條件都有對應證據。
