---
type: source
key: karpathy-llmwiki
title: LLM Wiki（Andrej Karpathy, GitHub gist）
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
raw: raw/karpathy-llmwiki.md
sources: [karpathy-llmwiki]
updated: 2026-11-23
---

# Karpathy — LLM Wiki（gist）

## 書目
- Andrej Karpathy 在 GitHub gist 發表的「idea file」，用來複製貼上給自己的 LLM agent，再一起做出適合自己的版本；抓取日期 2026-11-23。[src: karpathy-llmwiki, §LLM Wiki]

## 一句話摘要
與其每次提問都讓 LLM 從原始文件重新檢索拼湊（RAG），不如讓 LLM 持續建立並維護一個互相連結的 markdown wiki，知識「編譯一次、持續更新」。[src: karpathy-llmwiki, §The core idea]

## 核心主張
- 多數人用 LLM 處理文件的經驗像 RAG：查詢時檢索相關片段再生成答案；這可行，但 LLM 每次都從頭重新發現知識，沒有累積。[src: karpathy-llmwiki, §The core idea]
- LLM Wiki 的做法：加入新來源時，LLM 讀過、抽出重點、整合進既有 wiki，包括更新相關頁面、標註新資料與舊說法的矛盾。[src: karpathy-llmwiki, §The core idea]
- 關鍵差異：wiki 是持續累積的產物，交叉引用與矛盾標註都已經做好。[src: karpathy-llmwiki, §The core idea]
- 分工：人負責挑選來源、探索、問對問題；LLM 負責摘要、交叉引用、歸檔等繁瑣工作。[src: karpathy-llmwiki, §The core idea]

## 三層架構
- Raw sources：原始資料，唯讀，是事實來源。[src: karpathy-llmwiki, §Architecture]
- The wiki：LLM 產生並維護的 markdown 檔案。[src: karpathy-llmwiki, §Architecture]
- The schema：例如 CLAUDE.md 或 AGENTS.md，規定 wiki 結構、慣例與工作流程。[src: karpathy-llmwiki, §Architecture]

## 三種操作
- Ingest：加入新來源，LLM 讀取、寫摘要頁、更新 index 與相關頁面、記入 log；一篇來源可能動到 10–15 頁。作者偏好一次一篇。[src: karpathy-llmwiki, §Operations]
- Query：對 wiki 提問，好的答案可以寫回 wiki 成為新頁面。[src: karpathy-llmwiki, §Operations]
- Lint：定期健康檢查，找矛盾、過時說法、孤兒頁、缺少的交叉引用。[src: karpathy-llmwiki, §Operations]

## index 與 log
- index.md 是內容目錄，LLM 回答時先讀 index 找相關頁面；在中等規模（約 100 個來源、數百頁）下運作良好，不需要 embedding 式 RAG 基礎設施。[src: karpathy-llmwiki, §Indexing and logging]
- log.md 是只能附加的時間紀錄，每筆用一致的前綴方便用 unix 工具解析。[src: karpathy-llmwiki, §Indexing and logging]

## 為什麼可行
- 維護知識庫最累的是記帳式工作；人類會放棄 wiki 是因為維護負擔成長得比價值快，而 LLM 讓維護成本接近零。[src: karpathy-llmwiki, §Why this works]

## 相關頁面
- [LLM Wiki](../concepts/llm-wiki.md)
- [RAG vs LLM Wiki](../comparisons/rag-vs-llm-wiki.md)
