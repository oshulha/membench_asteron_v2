# Asteron Membench v2 change log

V2 is a task-suite expansion of v1. The world semantics, patches, authority model, conversations, span map, judge contract, and original 236 task/golden pairs are unchanged. Fact-level `distractor` bookkeeping is recomputed because 22 formerly unused facts become load-bearing in the added tasks; no subject, predicate, object, source, time, authority, or disclosure field changes.

## Added

- 97 tasks appended as `T237`–`T333`, all evaluated at `after_day_0`.
- 17 category-1 tasks and 16 tasks in each category 2–6.
- Exactly 20 Day-0 tasks in every category 1–6.
- Broader entity coverage across people, products, systems, vendors, cloud containers, documents, incidents, and projects.
- Additional relationship families for two-hop and three-hop tasks.
- Additional interval, extremum, adjacency, temporal-filter, and traversal-plus-temporal tasks.
- Programmatic v2 temporal-completeness and category-difficulty checks.
- Independent LLM/subagent semantic, golden-record, transcript-answerability, and difficulty reviews for all 97 additions.

## Preserved

- `T001`–`T236` and their golden records.
- The 664-fact fictional world and accepted conversation stream.
- Snapshot positions, authority rules, judge semantics, token budgets, and ten-gate validation model.
- The 65–75% actionable-task target; v2 contains 234 actionable tasks out of 333 (70.27%).

## Revised v2 quotas

| Category | v1 total | Added at Day 0 | v2 total | Day-0 total |
|---|---:|---:|---:|---:|
| 1 | 20 | 17 | 37 | 20 |
| 2 | 23 | 16 | 39 | 20 |
| 3 | 23 | 16 | 39 | 20 |
| 4 | 23 | 16 | 39 | 20 |
| 5 | 23 | 16 | 39 | 20 |
| 6 | 23 | 16 | 39 | 20 |
| 7 | 23 | 0 | 23 | 0 |
| 8 | 23 | 0 | 23 | 0 |
| 9 | 23 | 0 | 23 | 0 |
| 10 | 32 | 0 | 32 | 0 |

The v1 approximate total-task target and category-1 exact-total constraint are superseded only as stated in the v2 requirements checklist. All other requirements remain in force.
