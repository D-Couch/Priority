# Gameplay benchmark

Twenty development scenarios and a frozen corpus track the effect of implementation changes. Start with [HISTORY.md](HISTORY.md) for results. No vectorization has been added to the baseline.

## What is measured

- **Ruling quality:** two explicit criteria per scenario, plus a check for unsupported or contradictory claims. A fully correct answer must satisfy both, have no such claims, and complete without a request error. Review is explicit and attributed. Unreviewed answers remain pending, never automatically correct. The initial review is AI-assisted by Codex, not an independent human judge.
- **Expected-evidence recall:** fraction of authored evidence groups retrieved. A group can accept alternative rule passages. This measures retrieval of the reference set, not all possible valid support. Card-specific rulings may support answers even when the canonical rule is absent; answer review and retrieval scoring are separate.
- **Citation ID validity:** whether cited IDs exist in the supplied evidence. This is not a test of semantic support.
- **Latency:** retrieval time, first visible answer token, full response time, median, and nearest-rank p95. Failures are counted and excluded from successful latency percentiles.
- **Failures and diagnostics:** raw answers, all retrieved passages, warnings, missing evidence groups, request settings, prompt hashes, and errors.

Labels in `scenarios.json` and passages in `references.json` are only for evaluation. The answering model receives the same user messages and card selections as the app, never expected answers, rubric criteria, or reference labels. The runner starts the actual Python HTTP handler on an ephemeral loopback port and calls `/api/chat`; it does not reimplement the prompt or retrieval algorithm.

## Reproduce a baseline

Run commands from the project root. LM Studio must serve `qwen/qwen3.8-27b` on localhost:1234 for the full benchmark.

```bash
# After a fresh clone: restore the exact database used by the original benchmark.
python3 benchmark.py restore-corpus --output data/knowledge.sqlite
python3 benchmark.py validate
python3 -m unittest -v

# Commit implementation changes before measuring them.
python3 benchmark.py run --label pre-vectorization --output benchmarks/results/pre-vectorization-repeat
```

The restore command refuses to overwrite an existing database. Restoring the live database is optional for benchmark runs because they now use an isolated frozen copy. Each benchmark run extracts and verifies the frozen corpus into an isolated temporary database, so updating the live app cannot alter the benchmark. The temporary copy is removed after the run. The compressed 13 MB snapshot contains the full retrieval corpus, including distractors, so cloning the repo reproduces search conditions without depending on changing downloads. The snapshot and source passages remain attributed to Wizards and Scryfall in the manifest/references; they are external data, not original project code.

Full runs use the app's generation parameters plus an explicit seed (42 by default), one unmeasured warm-up request, sequential cases, and a fresh conversation per case. Installed model settings, loaded context, quantization, and reasoning capabilities/configuration are recorded when LM Studio exposes them. Settings not returned by LM Studio are not guaranteed reproducible. Seeds reduce variation; they do not guarantee deterministic GPU inference. Avoid concurrent chats, downloads, or other GPU workloads when timing. Do not tune a failed answer and overwrite the baseline.

For repeated measurements, add `--repeats 3`; repetitions use seeds 42, 43, and 44. Compare runs with the same repetition count and seed schedule. A single run is useful descriptively but does not establish statistical significance.

For fast retrieval-only checks without inference:

```bash
python3 benchmark.py run --mode retrieval --label retrieval-check --output benchmarks/results/retrieval-check
```

Retrieval-only and full runs are not directly comparable. Output directories cannot be reused. The runner checkpoints after every case; interrupted runs are marked incomplete and comparison refuses them.

## Review and compare

Each run writes `run.json`, `report.md`, and a `review.json` template. Read each answer against the scenario criteria and the frozen reference passages. In `review.json`, identify the reviewer and method (human or AI-assisted), grade every criterion with a boolean, set the unsupported-claims and abstention flags, and explain each grade. A clarification request is correct when the scenario itself is underspecified; it is an abstention if a fully specified scenario goes unanswered.

```bash
python3 benchmark.py review benchmarks/results/pre-vectorization-repeat
python3 benchmark.py compare benchmarks/results/pre-vectorization benchmarks/results/post-vectorization --output benchmarks/results/post-vectorization/comparison.md
```

Comparison rejects changed suite/reference/corpus hashes, model/runtime settings, repetition counts, seeds, case order, warm-up policy, sampling settings, and incomplete runs. Implementation differences are expected. Review coverage must be complete before accuracy deltas are reported. The comparison states improvements/regressions in percentage points and seconds and lists changed scenario outcomes. Record hardware changes separately; matching software metadata cannot make timings on different hardware comparable.

## Commit discipline

1. Commit the implementation under test, such as `feat: add hybrid vector retrieval`.
2. Run the frozen benchmark, review answers, and generate the comparison.
3. Commit results separately, such as `bench: record post-vectorization results and regressions`.
4. Tag the result commit `post-vectorization` (the report points to the preceding tested implementation commit).

The original application is preserved at `pre-vectorization-app`. The initial reviewed benchmark is tagged `pre-vectorization`. Keep historical run directories unchanged; a corrected evaluation belongs in a new run/review record with the correction explained. New scenarios or rule versions require a new suite version and a new baseline. This public development set can be overfit; add separate held-out scenarios before claiming general accuracy improvements.

GitHub Actions validates the corpus, regression tests, and suite on pushes/PRs. It does not contact your local LM Studio or claim to run inference on GitHub-hosted runners. Full benchmarks remain local and their reports are committed to Git.

## Controlled generation experiments

A generation experiment may deliberately change `sampling.reasoning_effort` or `sampling.max_tokens`. Declare the exact changed variable using `compare --allow-change sampling.reasoning_effort` (repeat the flag only for an explicitly planned multi-factor experiment). The report prints the before/after values. This does not waive checks on the corpus, labels, model/runtime, seed schedule, or any other sampling parameter. A generation experiment is not described as a retrieval-only comparison.

Runs now capture token usage, reasoning-character counts, finish reason, and transport completion in each result's `diagnostics` field. Private reasoning text is neither stored nor displayed. Telemetry-only `stream_options` are excluded from sampling comparisons. Stream decoder tests cover every split point in reasoning tags, separate reasoning fields, and truncated transport.

Answer completeness is separate from the frozen substantive rubric: `correct_and_complete` requires a fully correct review and a normal `stop` finish. `truncated_answers` records `length` finishes even when the response already contains the required ruling. Historical runs without finish telemetry have unknown completion status; do not infer normal completion. Comparisons calculate these fields from saved diagnostics without rewriting old artifacts.

Full runs measure evidence from the server's emitted `sources` event (the excerpts actually supplied to the model), retaining pre-packing candidates separately. Retrieval-only runs still measure candidate retrieval.

## Current runtime and verification

Run `./setup.sh` once from the project root, then `source .venv/bin/activate` before the benchmark commands above. The LM Studio Python client supplies local tokenization; all inference remains local. The current configuration uses medium reasoning effort and reserves 3,500 output tokens.

The vector-free baseline now has two reviewed 20/20 runs, seeds 42 and 43, with identical prompt and implementation hashes. These are repeated development cases, not 40 distinct questions. Before introducing embeddings, freeze a separate set of unseen cases and paraphrases and compare both sets. Do not weaken existing criteria or discard a regression to improve the headline score.

Reporting-only changes recompute the history from saved results without rerunning inference or modifying historical artifacts. Unknown historical completion telemetry is displayed as unavailable, rather than counted as zero successful completions. Append-only review-note corrections are linked from the history.
