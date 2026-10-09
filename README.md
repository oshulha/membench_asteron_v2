# Asteron CISO Memory-Subsystem Benchmark v2

This closed-book benchmark evaluates only the free-form memory context returned by a hypothetical memory subsystem. It does not supply, prescribe, or score a memory representation, index, retrieval algorithm, storage architecture, or downstream agent. For actionable prompts, the retrieved memory needed to perform the action is judged; the action itself is not executed.

## Scenario

Mara Voss, CISO of fictional 503-person SaaS company Asteron Collaborative, onboards a personal administrative assistant for calendar work, drafts, briefings, meeting preparation, and follow-up tracking. Asteron has 500 workstations, three offices (Boston HQ, Denver, and overseas Dublin), five SaaS products, about 250 vendors, and about 2,000 public-cloud resources. The overlapping week covers a Northstar identity migration, SOC 2 Type II preparation, a contested Veridian renewal, recent and Q1 incidents, a five-product release train, weekly executive reporting, and cyber-insurance renewal.

Day 0 is Monday 2026-06-01; days 1–6 are June 2–7. Coworker/external sessions occur June 8–9, the user debrief follows them on June 9, and the final battery is issued June 9–10. Relative time is resolved from each task's `issue_timestamp`, never from run time.

## Intended-use contract

1. Feed `conversations/sessions.jsonl` to the evaluated subsystem strictly in ascending `stream_position`. Each message's timestamp, session ID, speaker identity, and speaker type are trusted metadata.
2. Only the evaluated subsystem's own state persists between sessions. Do not persist a downstream agent or any benchmark oracle state.
3. Tasks are evaluation calls, never memory messages. Do not ingest them. Each call supplies `task_text`, `issue_timestamp`, `requester_id`, `requester_type`, `snapshot_ref`/exact stream position, and `max_output_tokens`.
4. Copy/snapshot subsystem state at the exact `snapshot_position`; exclude every later message. The subsystem returns one free-form context block in any faithful representation.
5. Enforce the frozen `cl100k_base` token-counting contract against `max_output_tokens` (1,500 by default; up to 2,500 for large sets). This is the only programmatic scoring check. The LLM judge is the sole semantic scorer and receives the task/requester fields, candidate block, and golden record—but never transcript or world artifacts.
6. A downstream answer/action is neither required nor scored. Implementation-neutral paraphrases and encodings are acceptable when they convey the golden concepts, source/temporal status, and required behavior.

## Artifacts

- `world/`: hierarchical authoring sheets, 664 atomic canonical facts, typed patches, authority/disclosure matrix, and analysis-only graph export.
- `conversations/`: the single chronological stream and character-precise accepted fact-to-span map.
- `tasks/`: 333 naturalized tasks with frozen bindings and exactly one concept-level golden record each. All 236 v1 tasks are preserved; v2 appends 97 Day-0 tasks across categories 1–6.
- `judge/`: final semantic judge prompt, executable contract helper, calibrated foil suite, and calibration report.
- `validation/`: ten-gate report, oracle traces, scene checks, invariance results, and per-requirement evidence.
- `generation/`: frozen schemas, disclosure plan, stage state, scene packets/checks, and LLM/subagent review records.

Fictional documents are represented only by `DOC_META` title/alias/location/subject/information-class/consultation/maintainer/replacement facts. Their bodies do not exist. Tasks involving them test routing or absence handling and never hidden contents. Aggregate vendor/cloud long tails likewise live only behind disclosed system pointers.

## Size and acceptance

The accepted stream contains approximately 46,925 user/assistant tokens across days 0–6, 8,023 third-party-session tokens, and 638 debrief tokens. The v2 expansion changes only the task suite, golden records, and their validation/review artifacts; the world and conversation stream remain unchanged. Final acceptance is recorded only when all ten gates are green; rerun `python build_benchmark.py` to reconstruct and revalidate every generated artifact without an API key. Surface form and semantic audits were completed during construction by the primary model and independent subagents; their frozen results ship under `generation/llm_reviews/`.
