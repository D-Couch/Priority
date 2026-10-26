# focused-general-v2-seed42 → focused-general-v2-2026-10-26

Implementation `9bd6927e08e72f4dd5eee8de720e79ced44746bf` → `8b30a311015f6b7df72a8522ec3d89522ef45572`

- `answer_contract_sha256`: ab098cb019c3f97f0d1acccb45c74c47ff52421c24f5a1a6ce0c9ff9d162a7cd → 98780f9a73d8c51d60687aa5daeaad3546fcdf4cd25bd8e47cee3957586cf37f
Declared experimental variables: answer_contract. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 80.0% | 100.0% | +20.0 percentage points · improved |
| Expected-evidence recall | 90.0% | 90.0% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 10.27 | 8.40 | -1.87 · improved |
| p95 latency (s) | 12.20 | 9.91 | -2.30 · improved |
| Answers with unsupported claims | 0 | 0 | +0.00 · unchanged |
| Citation-support failures | 0 | 0 | +0.00 · unchanged |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 4 | 5 | +1.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| g01-random-paper-procedure / r1 | partial | correct | partial → correct |
| g02-copy-counters-and-bonuses / r1 | correct | correct | unchanged |
| g03-fight-and-double-strike / r1 | correct | correct | unchanged |
| g04-replacement-order-general / r1 | correct | correct | unchanged |
| g05-protection-and-random-target / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
