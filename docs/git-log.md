# Git 提交紀錄（檢查紀錄）

> 公開 repo 只放單一快照（避免公開課程簡報與原始論文副本）。以下是原始 repo 的完整 commit 歷史（`git log --stat`），每一步的階段、節點、輪次都在訊息裡。

```

fb4b5d6 2026-11-23 16:35 stage1: discuss-first - 10 questions, suggested answers, user reply (照預設)

 .gitignore             |   4 ++++
 docs/course-slides.pdf | Bin 0 -> 38314107 bytes
 docs/discussion.md     |  64 +++++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 68 insertions(+)

2070dca 2026-11-23 16:37 stage2: wiki schema - AGENTS.md, CLAUDE.md, index/log, requirements + check (2 gaps fixed: R1, R10)

 AGENTS.md                  | 114 +++++++++++++++++++++++++++++++++++++++++++++
 CLAUDE.md                  |   1 +
 docs/requirements-check.md |  29 ++++++++++++
 docs/requirements.md       |  24 ++++++++++
 scripts/html_to_md.py      |  88 ++++++++++++++++++++++++++++++++++
 wiki/index.md              |   9 ++++
 wiki/log.md                |   6 +++
 7 files changed, 271 insertions(+)

639d72e 2026-11-23 16:38 stage3: add raw sources (5 arXiv PDFs + 2 web pages as md with source_url) and html_to_md.py

 raw/anthropic2024.md    | 210 ++++++++++++++++++++++++++++++++++++++++++++++++
 raw/asai2023.pdf        | Bin 0 -> 1405127 bytes
 raw/edge2024.pdf        | Bin 0 -> 6893854 bytes
 raw/gao2023.pdf         | Bin 0 -> 1662567 bytes
 raw/karpathy-llmwiki.md |  82 +++++++++++++++++++
 raw/lewis2020.pdf       | Bin 0 -> 885323 bytes
 raw/liu2023.pdf         | Bin 0 -> 747542 bytes
 7 files changed, 292 insertions(+)

bc8c3fe 2026-11-23 16:40 ingest(lewis2020): source page + 5 concept pages; lint_wiki.py (fix false positive on inline code)

 scripts/lint_wiki.py                               | 290 +++++++++++++++++++++
 wiki/concepts/chunking.md                          |  18 ++
 wiki/concepts/llm-knowledge-limits.md              |  23 ++
 .../concepts/parametric-vs-nonparametric-memory.md |  25 ++
 wiki/concepts/rag.md                               |  28 ++
 wiki/concepts/retriever.md                         |  26 ++
 wiki/index.md                                      |  26 +-
 wiki/log.md                                        |   5 +
 wiki/sources/lewis2020.md                          |  64 +++++
 9 files changed, 496 insertions(+), 9 deletions(-)

8742b59 2026-11-23 16:41 ingest(gao2023): survey source page, paradigms, reranking, 2 comparisons; update 4 concepts

 wiki/comparisons/rag-vs-fine-tuning.md  | 28 +++++++++++++++
 wiki/comparisons/rag-vs-long-context.md | 23 ++++++++++++
 wiki/concepts/chunking.md               | 40 +++++++++++----------
 wiki/concepts/llm-knowledge-limits.md   | 53 +++++++++++++++------------
 wiki/concepts/rag-paradigms.md          | 33 +++++++++++++++++
 wiki/concepts/rag.md                    | 64 ++++++++++++++++++---------------
 wiki/concepts/reranking.md              | 20 +++++++++++
 wiki/concepts/retriever.md              | 57 +++++++++++++++--------------
 wiki/index.md                           |  6 ++++
 wiki/log.md                             |  6 ++++
 wiki/sources/gao2023.md                 | 60 +++++++++++++++++++++++++++++++
 11 files changed, 295 insertions(+), 95 deletions(-)

3147ac8 2026-11-23 16:42 ingest(liu2023): lost-in-the-middle; flag contradiction (more context good/bad) liu2023 vs gao2023

 wiki/comparisons/rag-vs-long-context.md |  56 +++++++++------
 wiki/concepts/lost-in-the-middle.md     |  25 +++++++
 wiki/concepts/reranking.md              |  42 +++++------
 wiki/index.md                           |   2 +
 wiki/log.md                             |   8 +++
 wiki/sources/gao2023.md                 | 121 ++++++++++++++++----------------
 wiki/sources/liu2023.md                 |  40 +++++++++++
 7 files changed, 191 insertions(+), 103 deletions(-)

50af67f 2026-11-23 16:43 ingest(asai2023): Self-RAG source + concept; link from paradigms and rag

 wiki/concepts/rag-paradigms.md | 69 ++++++++++++++++++++++--------------------
 wiki/concepts/rag.md           |  5 ++-
 wiki/concepts/self-rag.md      | 31 +++++++++++++++++++
 wiki/index.md                  |  2 ++
 wiki/log.md                    |  6 ++++
 wiki/sources/asai2023.md       | 37 ++++++++++++++++++++++
 6 files changed, 116 insertions(+), 34 deletions(-)

dc15433 2026-11-23 16:44 ingest(edge2024): GraphRAG source + concept; update rag, chunking

 wiki/concepts/chunking.md |  3 ++-
 wiki/concepts/graphrag.md | 29 +++++++++++++++++++++++++++++
 wiki/concepts/rag.md      |  4 +++-
 wiki/index.md             |  2 ++
 wiki/log.md               |  5 +++++
 wiki/sources/edge2024.md  | 41 +++++++++++++++++++++++++++++++++++++++++
 6 files changed, 82 insertions(+), 2 deletions(-)

7ca37f7 2026-11-23 16:45 ingest(anthropic2024): contextual retrieval source + concept; update retriever, reranking, chunking, long-context

 wiki/comparisons/rag-vs-long-context.md |  7 ++++-
 wiki/concepts/chunking.md               |  5 ++-
 wiki/concepts/contextual-retrieval.md   | 32 +++++++++++++++++++
 wiki/concepts/rag.md                    |  4 ++-
 wiki/concepts/reranking.md              |  5 ++-
 wiki/concepts/retriever.md              |  8 ++++-
 wiki/index.md                           |  2 ++
 wiki/log.md                             |  6 ++++
 wiki/sources/anthropic2024.md           | 54 +++++++++++++++++++++++++++++++++
 9 files changed, 118 insertions(+), 5 deletions(-)

042513e 2026-11-23 16:48 ingest(karpathy-llmwiki): source, llm-wiki concept, rag-vs-llm-wiki comparison

 wiki/comparisons/rag-vs-llm-wiki.md | 30 ++++++++++++
 wiki/concepts/llm-wiki.md           | 25 ++++++++++
 wiki/concepts/rag.md                |  5 +-
 wiki/index.md                       |  3 ++
 wiki/log.md                         | 91 ++++++++++++++++++++-----------------
 wiki/sources/karpathy-llmwiki.md    | 44 ++++++++++++++++++
 6 files changed, 155 insertions(+), 43 deletions(-)

255f012 2026-11-23 16:48 stage3: lint - add test_lint.py (found exemption hole), number-vs-raw check (j) found 3 unit-conversion errors; fixed; PASS

 AGENTS.md                             |   4 +-
 docs/lint-history.md                  |  17 +
 docs/lint-report-before-fix.md        |  24 ++
 docs/lint-report.md                   |   5 +
 scripts/lint_wiki.py                  | 635 ++++++++++++++++++----------------
 scripts/test_lint.py                  |  81 +++++
 wiki/concepts/contextual-retrieval.md |  64 ++--
 wiki/log.md                           | 103 +++---
 wiki/sources/edge2024.md              |  82 ++---
 wiki/sources/lewis2020.md             | 128 +++----
 10 files changed, 666 insertions(+), 477 deletions(-)

b12ae33 2026-11-23 16:55 stage4: graph design - workflow.md (mermaid, node specs, loops, brakes, rationale), topic-slides skill + 3 reviewer prompts, check_coverage/check_citations/check_deck + render_deck (smoke-tested; fixed layout-class collision and headless screenshot offset)

 .claude/skills/topic-slides/SKILL.md               |  89 +++++++++
 .claude/skills/topic-slides/reviewers/coverage.md  |  20 ++
 .../skills/topic-slides/reviewers/faithfulness.md  |  22 +++
 .claude/skills/topic-slides/reviewers/outline.md   |  21 ++
 .gitignore                                         |   1 +
 docs/workflow.md                                   |  96 ++++++++++
 scripts/check_citations.py                         |  83 ++++++++
 scripts/check_coverage.py                          | 110 +++++++++++
 scripts/check_deck.py                              | 212 +++++++++++++++++++++
 scripts/common.py                                  | 120 ++++++++++++
 scripts/deck_template.html                         | 120 ++++++++++++
 scripts/render_deck.py                             | 142 ++++++++++++++
 12 files changed, 1036 insertions(+)

aa50149 2026-11-23 16:56 run1: N1 retrieve + G1 coverage round1 PASS (22 pages, 7 sources)

 runs/run-001/checks/G1-round1.txt |  3 +++
 runs/run-001/report.md            |  9 +++++++++
 runs/run-001/sources.md           | 37 +++++++++++++++++++++++++++++++++++++
 3 files changed, 49 insertions(+)

3e341ca 2026-11-23 16:57 run1: N2 evidence cards (7, parallel per source) + G1b round1 PASS

 runs/run-001/cards/anthropic2024.md    | 11 +++++++++++
 runs/run-001/cards/asai2023.md         |  9 +++++++++
 runs/run-001/cards/edge2024.md         |  9 +++++++++
 runs/run-001/cards/gao2023.md          | 18 ++++++++++++++++++
 runs/run-001/cards/karpathy-llmwiki.md | 10 ++++++++++
 runs/run-001/cards/lewis2020.md        | 16 ++++++++++++++++
 runs/run-001/cards/liu2023.md          | 11 +++++++++++
 runs/run-001/checks/G1b-round1.txt     |  8 ++++++++
 runs/run-001/report.md                 |  1 +
 9 files changed, 93 insertions(+)

d2d17fb 2026-11-23 16:59 run1: N3 outline + G2 round1 - script PASS, independent outline review FAIL (slide 6 overloaded); fix workflow mermaid parse error

 README.md                              | 75 ++++++++++++++++++++++++++++++++++
 docs/workflow.md                       |  4 +-
 runs/run-001/checks/G2-round1.txt      |  3 ++
 runs/run-001/outline.md                | 75 ++++++++++++++++++++++++++++++++++
 runs/run-001/report.md                 |  2 +
 runs/run-001/reviews/outline-round1.md | 23 +++++++++++
 6 files changed, 180 insertions(+), 2 deletions(-)

38e2833 2026-11-23 17:00 run1: N3 outline round2 - split slide 6, add 'RAG also fails' slide, merge cover+hook (15 slides); G2 script PASS

 runs/run-001/checks/G2-round2.txt |  3 ++
 runs/run-001/outline.md           | 80 +++++++++++++++++++++------------------
 2 files changed, 46 insertions(+), 37 deletions(-)

c930411 2026-11-23 17:02 run1: G2 round2 PASS (fresh independent reviewer, 0 must-fix)

 SUBMISSION.md                          | 40 ++++++++++++++++++++++++++++++++++
 runs/run-001/report.md                 |  2 ++
 runs/run-001/reviews/outline-round2.md | 17 +++++++++++++++
 3 files changed, 59 insertions(+)

1285c64 2026-11-23 17:03 run1: N4 drafts (15 slides) - inner loop round1 check_citations PASS; G3 script PASS

 runs/run-001/checks/G3-round1-citations.txt |   2 +
 runs/run-001/checks/N4-loop-round1.txt      |   2 +
 runs/run-001/drafts/slide-01.md             |  11 ++
 runs/run-001/drafts/slide-02.md             |  15 +++
 runs/run-001/drafts/slide-03.md             |  17 +++
 runs/run-001/drafts/slide-04.md             |  16 +++
 runs/run-001/drafts/slide-05.md             |  16 +++
 runs/run-001/drafts/slide-06.md             |  13 +++
 runs/run-001/drafts/slide-07.md             |  17 +++
 runs/run-001/drafts/slide-08.md             |  20 ++++
 runs/run-001/drafts/slide-09.md             |  16 +++
 runs/run-001/drafts/slide-10.md             |  15 +++
 runs/run-001/drafts/slide-11.md             |  14 +++
 runs/run-001/drafts/slide-12.md             |  19 ++++
 runs/run-001/drafts/slide-13.md             |  16 +++
 runs/run-001/drafts/slide-14.md             |  18 +++
 runs/run-001/drafts/slide-15.md             |  17 +++
 runs/run-001/outline.md                     | 163 ++++++++++++++--------------
 runs/run-001/report.md                      |   2 +
 19 files changed, 328 insertions(+), 81 deletions(-)

44b7b7a 2026-11-23 17:06 run1: G3 round1 FAIL - independent faithfulness review fails slides 6,7,9,10 (overgeneralization, unmarked analogy, dropped hedge, content outside cards)

 runs/run-001/report.md                      |  1 +
 runs/run-001/reviews/faithfulness-round1.md | 63 +++++++++++++++++++++++++++++
 2 files changed, 64 insertions(+)

589ec66 2026-11-23 17:06 run1: N2 add lewis2020#E12 + N4 drafts round2 - fix slides 6,7,9,10 faithfulness; scripts PASS

 runs/run-001/cards/lewis2020.md             | 33 ++++++++++++++--------------
 runs/run-001/checks/G3-round2-citations.txt |  2 ++
 runs/run-001/drafts/slide-06.md             | 26 +++++++++++-----------
 runs/run-001/drafts/slide-07.md             | 34 ++++++++++++++---------------
 runs/run-001/drafts/slide-09.md             | 32 +++++++++++++--------------
 runs/run-001/drafts/slide-10.md             | 30 ++++++++++++-------------
 runs/run-001/outline.md                     |  2 +-
 runs/run-001/report.md                      |  1 +
 8 files changed, 82 insertions(+), 78 deletions(-)

b10026b 2026-11-23 17:08 run1: G3 round2 FAIL slide 10 (dropped 'Naive RAG' qualifier); N4 drafts round3 - fix slide 10

 runs/run-001/checks/G3-round3-citations.txt |  2 ++
 runs/run-001/drafts/slide-10.md             | 33 ++++++++++++++++-------------
 runs/run-001/report.md                      |  2 ++
 runs/run-001/reviews/faithfulness-round2.md | 23 ++++++++++++++++++++
 4 files changed, 45 insertions(+), 15 deletions(-)

1b8e015 2026-11-23 17:08 run1: G3 round3 FAIL slide 10 (own 2-way categorization) - brake hit after 3 rounds, recorded as unresolved, continue with best version

 runs/run-001/report.md                      |  1 +
 runs/run-001/reviews/faithfulness-round3.md | 14 ++++++++++++++
 2 files changed, 15 insertions(+)

1edab08 2026-11-23 17:09 run1: N5 render loop rounds1-3 (CSS-only overflow fixes) + G4 check_deck PASS

 runs/run-001/checks/N5-loop-round1.txt |  24 +++
 runs/run-001/checks/N5-loop-round2.txt |  21 +++
 runs/run-001/checks/N5-loop-round3.txt |  20 +++
 runs/run-001/deck.html                 | 303 +++++++++++++++++++++++++++++++++
 runs/run-001/report.md                 |   4 +
 runs/run-001/screenshots/slide-01.png  | Bin 0 -> 402162 bytes
 runs/run-001/screenshots/slide-02.png  | Bin 0 -> 97497 bytes
 runs/run-001/screenshots/slide-03.png  | Bin 0 -> 106511 bytes
 runs/run-001/screenshots/slide-04.png  | Bin 0 -> 105845 bytes
 runs/run-001/screenshots/slide-05.png  | Bin 0 -> 85639 bytes
 runs/run-001/screenshots/slide-06.png  | Bin 0 -> 116381 bytes
 runs/run-001/screenshots/slide-07.png  | Bin 0 -> 90729 bytes
 runs/run-001/screenshots/slide-08.png  | Bin 0 -> 131734 bytes
 runs/run-001/screenshots/slide-09.png  | Bin 0 -> 138852 bytes
 runs/run-001/screenshots/slide-10.png  | Bin 0 -> 103344 bytes
 runs/run-001/screenshots/slide-11.png  | Bin 0 -> 149931 bytes
 runs/run-001/screenshots/slide-12.png  | Bin 0 -> 116089 bytes
 runs/run-001/screenshots/slide-13.png  | Bin 0 -> 96158 bytes
 runs/run-001/screenshots/slide-14.png  | Bin 0 -> 87381 bytes
 runs/run-001/screenshots/slide-15.png  | Bin 0 -> 125196 bytes
 scripts/deck_template.html             | 240 +++++++++++++-------------
 21 files changed, 492 insertions(+), 120 deletions(-)

95cc9d3 2026-11-23 17:11 run1: G4 coverage review PASS (7 suggestions, 1 is a missed faithfulness issue) + N6 deliver with conditions; run1 summary; report_stats.py

 deck.html                               | 303 ++++++++++++++++++++++++++++++++
 runs/run-001/checks/report-stats.txt    |  12 ++
 runs/run-001/report.md                  |  10 ++
 runs/run-001/reviews/coverage-round1.md |  24 +++
 scripts/report_stats.py                 |  62 +++++++
 5 files changed, 411 insertions(+)

aace498 2026-11-23 17:13 stage6: workflow v2 - move mechanical faithfulness checks forward (G3 -> N2 card qualifiers, N4 qualifier/generalizer/quote checks); retro-test on run1 drafts catches 3/4; v1->v2 changelog

 .claude/skills/topic-slides/SKILL.md               | 180 +++++++--------
 .../skills/topic-slides/reviewers/faithfulness.md  |  45 ++--
 docs/workflow.md                                   | 228 +++++++++++--------
 .../checks/retro-v2-checks-on-round1-drafts.txt    |   9 +
 scripts/check_citations.py                         | 187 +++++++++-------
 scripts/check_coverage.py                          | 234 ++++++++++----------
 scripts/common.py                                  | 243 +++++++++++----------
 7 files changed, 606 insertions(+), 520 deletions(-)

9c900a5 2026-11-23 17:13 wiki query: file back run-001 coverage gaps (failure-rate definition, LLM-as-judge) - lint PASS

 wiki/concepts/contextual-retrieval.md |  3 ++
 wiki/concepts/graphrag.md             | 59 ++++++++++++++++++-----------------
 wiki/log.md                           |  5 +++
 3 files changed, 38 insertions(+), 29 deletions(-)

41d9a8f 2026-11-23 17:14 run2: N1 retrieve + G1 PASS; N2 cards v2 (qualifier tags) + G1b v2 PASS

 runs/run-002/cards/anthropic2024.md    | 12 +++++++++++
 runs/run-002/cards/asai2023.md         |  9 +++++++++
 runs/run-002/cards/edge2024.md         | 10 +++++++++
 runs/run-002/cards/gao2023.md          | 18 +++++++++++++++++
 runs/run-002/cards/karpathy-llmwiki.md | 10 +++++++++
 runs/run-002/cards/lewis2020.md        | 17 ++++++++++++++++
 runs/run-002/cards/liu2023.md          | 11 ++++++++++
 runs/run-002/checks/G1-round1.txt      |  3 +++
 runs/run-002/checks/G1b-round1.txt     |  8 ++++++++
 runs/run-002/report.md                 | 11 ++++++++++
 runs/run-002/sources.md                | 37 ++++++++++++++++++++++++++++++++++
 11 files changed, 146 insertions(+)

66ef650 2026-11-23 17:15 run2: N3 outline (from run1 structure + run1 G4 suggestions) + G2 script PASS

 runs/run-002/checks/G2-round1.txt |  3 ++
 runs/run-002/outline.md           | 81 +++++++++++++++++++++++++++++++++++++++
 runs/run-002/report.md            |  2 +-
 3 files changed, 85 insertions(+), 1 deletion(-)

7c72943 2026-11-23 17:17 run2: N4 drafts (15) - v2 inner loop PASS round1; mutation test proves qualifier check fires; G3 script PASS

 runs/run-002/checks/G3-round1-citations.txt        |   2 +
 runs/run-002/checks/N4-loop-round1.txt             |   2 +
 .../run-002/checks/mutation-test-v2-qualifiers.txt |   5 +
 runs/run-002/drafts/slide-01.md                    |  11 ++
 runs/run-002/drafts/slide-02.md                    |  15 ++
 runs/run-002/drafts/slide-03.md                    |  17 +++
 runs/run-002/drafts/slide-04.md                    |  16 ++
 runs/run-002/drafts/slide-05.md                    |  16 ++
 runs/run-002/drafts/slide-06.md                    |  13 ++
 runs/run-002/drafts/slide-07.md                    |  17 +++
 runs/run-002/drafts/slide-08.md                    |  19 +++
 runs/run-002/drafts/slide-09.md                    |  16 ++
 runs/run-002/drafts/slide-10.md                    |  17 +++
 runs/run-002/drafts/slide-11.md                    |  14 ++
 runs/run-002/drafts/slide-12.md                    |  19 +++
 runs/run-002/drafts/slide-13.md                    |  18 +++
 runs/run-002/drafts/slide-14.md                    |  19 +++
 runs/run-002/drafts/slide-15.md                    |  17 +++
 runs/run-002/outline.md                            | 162 ++++++++++-----------
 runs/run-002/report.md                             |   3 +
 runs/run-002/reviews/outline-round1.md             |  19 +++
 21 files changed, 356 insertions(+), 81 deletions(-)

af85cd8 2026-11-23 17:20 run2: G3 round1 FAIL slides 8,12,14 (own categorization, dropped attribution/qualifier in quiz) - paused here

 runs/run-002/report.md                      |  1 +
 runs/run-002/reviews/faithfulness-round1.md | 20 ++++++++++++++++++++
 2 files changed, 21 insertions(+)

49aef85 2026-11-23 22:48 run2: N4 drafts round2 - fix slides 8,12,14 faithfulness; scripts PASS

 runs/run-002/checks/G3-round2-citations.txt |  2 ++
 runs/run-002/drafts/slide-08.md             | 39 +++++++++++++++--------------
 runs/run-002/drafts/slide-12.md             |  5 ++--
 runs/run-002/drafts/slide-14.md             |  4 +--
 runs/run-002/outline.md                     |  4 +--
 runs/run-002/report.md                      |  1 +
 6 files changed, 30 insertions(+), 25 deletions(-)

11063a6 2026-11-23 22:49 run2: N5 render - slide 14 overflow back to N4 (shorten), re-render; G4 check_deck PASS; deck.html updated to run2

 deck.html                              |  83 ++++-----
 runs/run-002/checks/N5-loop-round1.txt |  21 +++
 runs/run-002/checks/N5-loop-round2.txt |  20 +++
 runs/run-002/deck.html                 | 304 +++++++++++++++++++++++++++++++++
 runs/run-002/drafts/slide-14.md        |   3 +-
 runs/run-002/outline.md                |   2 +-
 runs/run-002/report.md                 |   3 +
 runs/run-002/screenshots/slide-01.png  | Bin 0 -> 402162 bytes
 runs/run-002/screenshots/slide-02.png  | Bin 0 -> 101304 bytes
 runs/run-002/screenshots/slide-03.png  | Bin 0 -> 103596 bytes
 runs/run-002/screenshots/slide-04.png  | Bin 0 -> 106344 bytes
 runs/run-002/screenshots/slide-05.png  | Bin 0 -> 87536 bytes
 runs/run-002/screenshots/slide-06.png  | Bin 0 -> 118027 bytes
 runs/run-002/screenshots/slide-07.png  | Bin 0 -> 87796 bytes
 runs/run-002/screenshots/slide-08.png  | Bin 0 -> 132096 bytes
 runs/run-002/screenshots/slide-09.png  | Bin 0 -> 140542 bytes
 runs/run-002/screenshots/slide-10.png  | Bin 0 -> 94042 bytes
 runs/run-002/screenshots/slide-11.png  | Bin 0 -> 142795 bytes
 runs/run-002/screenshots/slide-12.png  | Bin 0 -> 141709 bytes
 runs/run-002/screenshots/slide-13.png  | Bin 0 -> 110849 bytes
 runs/run-002/screenshots/slide-14.png  | Bin 0 -> 91748 bytes
 runs/run-002/screenshots/slide-15.png  | Bin 0 -> 125196 bytes
 22 files changed, 392 insertions(+), 44 deletions(-)

c4e7d6b 2026-11-23 22:50 run2: G3 round2 FAIL slide 8 (own categorization) -> N4 round3 fix, re-render, check_deck PASS; reflection draft

 deck.html                                   |   2 +-
 docs/reflection.md                          |  65 ++++++++++++++++++++++++++++
 runs/run-002/checks/G4-script-final.txt     |  20 +++++++++
 runs/run-002/deck.html                      |   2 +-
 runs/run-002/drafts/slide-08.md             |   2 +-
 runs/run-002/report.md                      |   2 +
 runs/run-002/reviews/faithfulness-round2.md |  10 +++++
 runs/run-002/screenshots/slide-08.png       | Bin 132096 -> 134212 bytes
 8 files changed, 100 insertions(+), 3 deletions(-)

3aeae43 2026-11-23 22:50 run2: G4 coverage review PASS (0 must-fix)

 runs/run-002/report.md                  |  1 +
 runs/run-002/reviews/coverage-round1.md | 14 ++++++++++++++
 2 files changed, 15 insertions(+)

3acedd8 2026-11-23 22:51 run2: G3 round3 PASS slide 8 -> 15/15; N6 deliver; reflection + SUBMISSION finalized with real numbers

 SUBMISSION.md                               | 159 +++++++++++++++++++++-------
 docs/reflection.md                          | 131 +++++++++++------------
 runs/run-002/report.md                      |   7 ++
 runs/run-002/reviews/faithfulness-round3.md |   6 ++
 4 files changed, 198 insertions(+), 105 deletions(-)

851180c 2026-11-23 22:51 stage7: self-evaluation, README link

 README.md               |  1 +
 docs/self-evaluation.md | 23 +++++++++++++++++++++++
 2 files changed, 24 insertions(+)
```
