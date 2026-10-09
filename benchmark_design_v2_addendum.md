# Benchmark design v2 addendum

This addendum modifies the task-suite counts in the original design and nothing else.

The v2 suite contains 333 tasks. It preserves v1 tasks `T001`–`T236` and appends 97 tasks at the `after_day_0` snapshot: 17 direct single-hop tasks and 16 tasks in each category 2–6. Consequently, categories 1–6 each contain exactly 20 Day-0 tasks. Overall totals are 37 tasks in category 1, 39 tasks in each category 2–6, 23 tasks in each category 7–9, and 32 tasks in category 10.

The additions must use only facts disclosed by the end of Day 0. Category semantics remain unchanged:

1. Category 1 uses a canonical entity and exactly one directly attached fact.
2. Category 2 resolves one role or alias and then retrieves one directly attached fact; genuinely ambiguous forms are excluded unless candidate surfacing is intended.
3. Category 3 uses an exact shortest two-edge meaningful path.
4. Category 4 uses an exact shortest three-edge meaningful path.
5. Category 5 requires a bounded temporal filter, ordering operation, extremum, adjacency relation, or complete dated set without graph traversal.
6. Category 6 combines relationship traversal or entity resolution with a bounded temporal filter, comparison, or join.

Every added task requires a concept-level golden record derived from its frozen binding. Validation must recompute temporal answer sets, reject shorter paths in categories 3–4, confirm every support span occurs by Day 0, and independently review wording, answerability, golden sufficiency, cardinality, and category difficulty. The complete suite must retain the 65–75% actionable-task ratio.
