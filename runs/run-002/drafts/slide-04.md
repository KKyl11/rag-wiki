---
slide: 4
title: RAG 怎麼運作：索引 → 檢索 → 生成
section: 流程
layout: content
evidence: [gao2023#E3, lewis2020#E2]
wiki: [concepts/rag-paradigms.md, concepts/rag.md]
---
```flow
① 索引：把資料切成小塊，用 embedding 模型編碼成向量，存進向量資料庫 → ② 檢索：把問題也轉成向量，取最相似的 top-K 片段 → ③ 生成：問題＋片段一起交給 LLM 回答
```

- 這是最基本的 Naive RAG，也就是「Retrieve-Read」流程：先檢索、再閱讀。
- top-K：和問題最相似的前 K 個片段。下兩頁拆開看「切塊」與「檢索」。

> 🎓 教學比喻（非來源內容）：像寫報告前先去圖書館——先替書做好目錄，再找出相關的幾頁，最後根據那幾頁寫答案。
