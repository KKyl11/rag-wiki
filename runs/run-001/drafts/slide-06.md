---
slide: 6
title: 第二步拆開看：嵌入（embedding）與檢索
section: 流程
layout: content
evidence: [lewis2020#E10, gao2023#E5, anthropic2024#E4]
wiki: [concepts/retriever.md]
---
- **嵌入（embedding）**：把文件和問題各自編碼成向量，再計算相似度（例如 cosine similarity），找出最接近的 top-k 片段。
- **BM25**：字詞重疊式的檢索，比對問題和片段裡相同的字詞。
- **兩者互補**：查「Error code TS-999」時，embedding 可能只找到一般錯誤碼的內容，BM25 則能精確比對「TS-999」。兩者捕捉不同的相關性特徵，可以混合（hybrid）互補。

> 🎓 教學比喻（非來源內容）：把每段文字想成地圖上的一個點，意思越像的文字靠得越近；檢索就是找出離「問題」最近的幾個點。
