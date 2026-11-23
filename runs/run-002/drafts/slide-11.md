---
slide: 11
title: 限制：資料塞越多越好嗎？（Lost in the Middle）
section: 限制與爭議
layout: content
evidence: [liu2023#E1, liu2023#E2, liu2023#E4, liu2023#E6, gao2023#E11, anthropic2024#E6]
wiki: [concepts/lost-in-the-middle.md, comparisons/rag-vs-long-context.md, sources/liu2023.md]
---
- **U 形曲線**：相關資訊在開頭或結尾時表現最好，在中間時最差。
- **嚴重時**：GPT-3.5-Turbo 在 20、30 篇文件設定的最差情況，比完全不給文件（closed-book，56.1%）還低。
- **多放不一定有用**：檢索超過 20 篇只帶來些微進步，卻大幅增加輸入長度；Anthropic 的實驗在 5、10、20 個片段中則以 20 最好。
- **作者建議**的值得研究的方向：用 reranking 把相關資訊推到輸入開頭，或截短排名清單。

> ⚖️ 兩種說法：Liu et al. 發現關鍵文件在中間時，表現可能比不給文件還差；Gao et al. 引述 Cuconasu et al. 的研究則發現，加入不相關文件反而可能讓準確率提升超過 30%。後者只有二手描述，無法比對實驗設定。
