# RAG LLM Wiki → 教學 HTML 簡報

用 Karpathy 的 **LLM Wiki** 架構，先建立一個關於 **RAG（Retrieval-Augmented Generation，檢索增強生成）** 的知識庫，再用一個事先畫好的 **graph workflow**，只根據 wiki 的內容產生一份給零基礎大學生看的教學 HTML 簡報。

- 課程：第 10 週「把你的工作拆成 AI 能做的流程」（`docs/course-slides.pdf`）
- 工具：Claude Code（`CLAUDE.md` 只有一行 `@AGENTS.md`）
- 繳交說明：[`SUBMISSION.md`](SUBMISSION.md)

## 怎麼看成果

| 想看什麼 | 打開 |
|---|---|
| **最終簡報** | [`deck.html`](deck.html)：用瀏覽器直接打開；← → 翻頁、A 顯示小測驗答案、F 全螢幕 |
| Wiki 目錄 | [`wiki/index.md`](wiki/index.md)（22 頁：7 來源、12 概念、3 比較） |
| Wiki 時間線 | [`wiki/log.md`](wiki/log.md) |
| 流程圖與設計理由 | [`docs/workflow.md`](docs/workflow.md)（Mermaid 圖在 GitHub 上會直接渲染） |
| 兩次實際執行紀錄 | [`runs/run-001/report.md`](runs/run-001/report.md)、[`runs/run-002/report.md`](runs/run-002/report.md) |
| 反思 | [`docs/reflection.md`](docs/reflection.md) |
| 依評分標準自評 | [`docs/self-evaluation.md`](docs/self-evaluation.md) |

## 資料夾結構

```
rag-wiki/
├── AGENTS.md              # Wiki schema（規則只寫在這裡）
├── CLAUDE.md              # 一行：@AGENTS.md
├── deck.html              # 最終簡報（run-002 的成品）
├── raw/                   # 原始資料（唯讀）：5 篇 arXiv PDF＋2 篇網頁 markdown
├── wiki/                  # AI 維護的 wiki
│   ├── index.md / log.md
│   ├── sources/           # 每個來源一頁
│   ├── concepts/          # 概念頁
│   └── comparisons/       # 比較頁
├── docs/
│   ├── discussion.md      # 先討論：10 個問題＋建議答案＋使用者回覆
│   ├── requirements.md    # 需求摘要 R1–R18
│   ├── requirements-check.md  # 需求 → AGENTS.md 逐條對照
│   ├── lint-report.md / lint-history.md / lint-report-before-fix.md
│   ├── workflow.md        # Graph 設計（v1 → v2 修改紀錄）
│   └── reflection.md      # 反思
├── .claude/skills/topic-slides/   # 可重複呼叫的 skill（/topic-slides <主題>）＋3 份審查者指示
├── scripts/               # 所有檢查都是腳本（以 exit code 判定）
│   ├── lint_wiki.py / test_lint.py
│   ├── check_coverage.py / check_citations.py / check_deck.py
│   ├── render_deck.py / deck_template.html
│   └── html_to_md.py / common.py
└── runs/
    ├── run-001/           # v1 graph 的實際執行（sources、cards、outline、drafts、deck、report、checks、reviews、screenshots）
    └── run-002/           # v2 graph 的實際執行
```

## 怎麼重跑檢查

```bash
python scripts/lint_wiki.py                      # wiki 健康檢查 → docs/lint-report.md
python scripts/test_lint.py                      # 證明 lint 真的抓得到錯
python scripts/check_coverage.py runs/run-002 --stage outline
python scripts/check_citations.py runs/run-002
python scripts/check_deck.py runs/run-002 --screenshots   # 需要 Chrome/Edge；沒有會退回字數上限
```

需要 Python 3（`pypdf`，lint 讀 PDF 頁數與內文用）。

## 原始資料連結

| key | 資料 | 連結 |
|---|---|---|
| lewis2020 | Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | https://arxiv.org/abs/2005.11401 |
| gao2023 | Gao et al., Retrieval-Augmented Generation for Large Language Models: A Survey | https://arxiv.org/abs/2312.10997 |
| liu2023 | Liu et al., Lost in the Middle: How Language Models Use Long Contexts | https://arxiv.org/abs/2307.03172 |
| asai2023 | Asai et al., Self-RAG | https://arxiv.org/abs/2310.11511 |
| edge2024 | Edge et al., From Local to Global: A GraphRAG Approach | https://arxiv.org/abs/2404.16130 |
| anthropic2024 | Anthropic, Introducing Contextual Retrieval | https://www.anthropic.com/news/contextual-retrieval |
| karpathy-llmwiki | Karpathy, LLM Wiki（gist） | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |

本公開版本**不含** `raw/`（原始論文與網頁副本）與課程簡報 PDF，請用上表連結取得原始資料；完整 commit 歷史見 [`docs/git-log.md`](docs/git-log.md)。
