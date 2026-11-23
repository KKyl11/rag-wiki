---
type: comparison
title: RAG vs 長上下文（long context）
sources: [gao2023, liu2023, anthropic2024]
updated: 2026-11-23
---

# RAG vs 長上下文

## 一句話白話定義
既然新模型一次能讀很長的文字，為什麼不把所有資料直接塞進 prompt？這頁整理各來源對「長上下文能不能取代 RAG」的看法。[src: gao2023, p.14]

## 背景
- LLM 現在能處理超過 200,000 tokens 的脈絡，過去靠 RAG 的長文件問答，現在可以把整份文件直接放進 prompt。[src: gao2023, p.14]

- Anthropic 的建議：知識庫小於 200,000 tokens（約 500 頁）時，可以直接全部放進 prompt，不需要 RAG；知識庫變大時才需要可擴展的做法。[src: anthropic2024, §A note on simply using a longer prompt]
- Prompt caching 讓「全部放進 prompt」更可行：延遲降低 2 倍以上、成本最多降低 90%。[src: anthropic2024, §A note on simply using a longer prompt]

## 支持「RAG 仍需要」的理由
- 一次給大量脈絡會明顯拖慢推理速度；切塊檢索、按需輸入能提升效率。[src: gao2023, p.14]
- RAG 能快速找到原始出處讓使用者驗證，整個檢索與推理過程可觀察；只靠長上下文的生成像黑盒子。[src: gao2023, p.14]
- 長上下文也替 RAG 帶來新機會，例如處理需要讀大量資料的整合型、摘要型問題。[src: gao2023, p.14]

## 長上下文的實際表現
- 模型讀長輸入時有「Lost in the Middle」問題：關鍵資訊在中間時表現明顯下降，擴充脈絡長度的模型也一樣。見 [Lost in the Middle](../concepts/lost-in-the-middle.md)。[src: liu2023, p.1]
- 給更長的輸入是取捨：資訊多可能有幫助，但模型要推理的內容也變多，可能降低準確度。[src: liu2023, p.2-3]

- Anthropic 的實驗：放越多片段越可能包含相關資訊，但資訊太多會讓模型分心；在 5、10、20 片段中，20 最好。[src: anthropic2024, §Implementation considerations]

> ⚖️ 矛盾：多放幾篇文件（包含不相關的）到脈絡裡，是好是壞？
> - Liu et al.：含答案的文件在中間時，GPT-3.5-Turbo 表現可能下降超過 20%，甚至低於不給文件的 56.1%；檢索超過 20 篇只帶來些微進步。[src: liu2023, p.5; liu2023, p.10]
> - Gao et al. 引述 Cuconasu et al.：加入不相關文件反而可能讓準確率提升超過 30%，與原本假設相反。[src: gao2023, p.14]
> - 可能原因：實驗設定不同。Liu 固定只有一篇含答案、其餘為檢索來的干擾文件，觀察的是「位置」；Cuconasu 的原始實驗本 wiki 沒有收錄，只能透過 Gao 的二手描述得知，無法比對設定。簡報若提到要並陳兩說。

## 相關頁面
- [Liu et al. 2023](../sources/liu2023.md)
- [檢索增強生成（RAG）](../concepts/rag.md)
- [Gao et al. 2023](../sources/gao2023.md)
