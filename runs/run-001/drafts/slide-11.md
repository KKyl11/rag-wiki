---
slide: 11
title: 限制：資料塞越多越好嗎？（Lost in the Middle）
section: 限制與爭議
layout: content
evidence: [liu2023#E1, liu2023#E2, liu2023#E4, liu2023#E6, gao2023#E11, anthropic2024#E6]
wiki: [concepts/lost-in-the-middle.md, comparisons/rag-vs-long-context.md, sources/liu2023.md]
---
- **U 形曲線**：關鍵資訊放在長輸入的開頭或結尾時，模型表現最好；放在中間時明顯變差。
- **嚴重時**：GPT-3.5-Turbo 在 20、30 篇文件設定的最差情況，比完全不給文件（closed-book，56.1%）還差。
- **多放不一定有用**：檢索器找到的相關文件越來越多，模型表現卻早就不再進步；超過 20 篇只帶來些微進步，卻大幅增加延遲與成本。
- **對策**：用 reranking 把相關資訊推到開頭，或少放幾篇。

> ⚖️ 兩種說法：Liu et al. 發現關鍵文件被淹在中間時，表現可能比不給文件還差；但 Gao et al. 引述的研究發現，加入不相關文件反而可能讓準確率提升超過 30%（與原本假設相反）。後者只有二手描述，無法比對兩者的實驗設定。
