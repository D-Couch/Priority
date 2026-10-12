# Pre-vectorization findings

The implementation tested is `98cd7e431879a9817252d623a3ca5fe5373a06ea`. This commit adds the benchmark harness but leaves application inference/retrieval identical to the original `pre-vectorization-app` commit. The results commit and `pre-vectorization` tag preserve this starting point before algorithm changes.

## Baseline

- Fully correct: **12/20 (60%)** under the explicit rubric and support check.
- Other outcomes: **1 evidence-limited abstention**, **1 partially correct answer with an overbroad assurance**, and **6 requests with no final answer after exhausting the output limit**.
- Expected-evidence recall: **63.3%** averaged over scenarios. All reference groups were retrieved for 8/20 scenarios.
- Every visible answer cited recognized source IDs (**100% ID validity**). This is not 100% factual accuracy or citation support.
- Median successful request: **20.02 seconds**; successful-request p95: **41.05 seconds**. Failed requests are excluded from these percentiles and remain visible in the case table.
- Settings: Qwen3.8 27B Q4_K_M; loaded context 8,192; temperature 0.1; max output 3,500; seed 42. One sequential repetition, with a warm-up before timing.

The review is **AI-assisted by Codex and not independently human-validated**. Each criterion and explanation is inspectable in `review.json`; questions, answers, citations, source passages, and timings are in `run.json` and `report.md`. This is a public development benchmark, not a held-out general accuracy estimate.

## What the failures tell us

**Retrieval needs improvement.** The priority question missed CR 117.3c and 117.4 and the assistant declined to answer that part. Deathtouch/trample, zero toughness, token blinking, and other questions also missed important canonical evidence. Some correct answers found equivalent support in card rulings or other rule passages, so reference recall is a diagnostic rather than an answer-quality score.

**Generation settings also need investigation.** Six cases reached the output cap without a visible final answer. The Commander death question had all expected evidence and still failed this way. The warnings identify output-limit exhaustion, but do not establish that vector retrieval would fix it. Keep any reasoning/output-budget or context-length experiment separate from the retrieval experiment. If changing those settings, establish a matching baseline before claiming a controlled comparison.

**Valid citation IDs do not ensure a safe ruling.** The protection question correctly asked for more details, but also broadly assured that protection would make the creature safe from a damage spell. Protection prevents damage (CR 702.16e), while unpreventable damage bypasses prevention (CR 615.12 in the frozen corpus). Because the actual spell was unspecified, that extra assurance was too broad. Its two clarification criteria passed, but the extra-claim check prevented a fully-correct grade.

## Next comparisons

For a vector-search change, preserve this suite, complete corpus, model, seed schedule, and sampling/runtime settings. Commit the new implementation first, run the suite into a new directory, review all answers, and generate `comparison.md` with the provided command. Record both gains and regressions. Do not overwrite this run or remove difficult cases. Use multiple repetitions before treating latency or small quality changes as robust.
