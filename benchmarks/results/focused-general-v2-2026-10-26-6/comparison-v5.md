# focused-general-v2-2026-10-26-5 → focused-general-v2-2026-10-26-6

Implementation `355b3487afbb597b105185bafea0c7cc76de6ee8` → `ede0095c1ceea2f1e9ce845330abb457fd4f33d5`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 100.0% | 80.0% | -20.0 percentage points · regressed |
| Expected-evidence recall | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 9.20 | 8.08 | -1.12 · improved |
| p95 latency (s) | 11.16 | 8.90 | -2.26 · improved |
| Answers with unsupported claims | 0 | 0 | +0.00 · unchanged |
| Citation-support failures | 0 | 0 | +0.00 · unchanged |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 5 | 4 | -1.00 · regressed |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| g01-random-paper-procedure / r1 | correct | partial | correct → partial |
| g02-copy-counters-and-bonuses / r1 | correct | correct | unchanged |
| g03-fight-and-double-strike / r1 | correct | correct | unchanged |
| g04-replacement-order-general / r1 | correct | correct | unchanged |
| g05-protection-and-random-target / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
