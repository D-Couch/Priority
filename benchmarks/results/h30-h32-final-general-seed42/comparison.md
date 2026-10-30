# focused-general-v2-seed42 → h30-h32-final-general-seed42

Implementation `9bd6927e08e72f4dd5eee8de720e79ced44746bf` → `33b8429a85867b385e2030f3d3971845f32b5b3c`

- `answer_contract_sha256`: ab098cb019c3f97f0d1acccb45c74c47ff52421c24f5a1a6ce0c9ff9d162a7cd → add5b7b53fb93a88bbdafb339b22d61c875c6a0b04e2c2cf0f7e30e0ee1bb2dd
Declared experimental variables: answer_contract. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 80.0% | 100.0% | +20.0 percentage points · improved |
| Expected-evidence recall | 90.0% | 100.0% | +10.0 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 10.27 | 10.09 | -0.18 · improved |
| p95 latency (s) | 12.20 | 10.37 | -1.84 · improved |
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
