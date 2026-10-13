# Key-rule priority experiment

Implementation under test: `14003d067382dde6c6dbf7bc4a56ed2e4888aca6` (`fix: prioritize key mechanics rule retrieval`). The change made mana-value, initiative, and general spell-copy rules high-priority in the context packer. Four frozen suites were run after the implementation commit. Review was AI-assisted by Codex, not independently verified by a Magic judge.

| Suite | Prior reviewed baseline | This run | Expected-evidence recall | Median latency |
|---|---:|---:|---:|---:|
| Mechanics-v1, seed 42 | 14/20; 48.3%; 7.31 s | 18/20; 78.3%; 6.86 s | +30.0 percentage points | -0.45 s |
| Mechanics-v1, seed 43 | 13/20; 48.3%; 7.48 s | 18/20; 78.3%; 7.19 s | +30.0 percentage points | -0.29 s |
| Gameplay-v1, seed 42 | 20/20; 100%; 6.92 s | 19/20; 100%; 7.01 s | unchanged | +0.09 s |
| Heldout-v1, seed 42 | 30/32; 82.0%; 7.51 s | 29/32; 82.0%; 7.52 s | unchanged | +0.01 s |
| Novel-v1, seed 42 | 20/20; 87.5%; 5.95 s | 16/20; 82.5%; 6.20 s | -5.0 percentage points | +0.25 s |

All 112 requests across the five runs completed without transport errors or truncation. Every run used the same local model and seed as its corresponding baseline. One-seed comparisons remain sensitive to sampling variation.

## Findings

The targeted rules were retained in context: mechanics-v1 evidence recall rose from 48.3% to 78.3% in both seeds, and both initiative cases, all mana-value cases, and the copied-modal-spell case received their expected evidence. Both mechanics runs improved from 13–14/20 to 18/20 fully correct.

The broader copy priority had an adverse interaction. In the novel casualty case, retrieval found CR 702.153a in its candidate list, but the context pack omitted it after prioritizing the general CR 707.10 copy section. The model then incorrectly said that paying casualty does not copy the spell. The new run also had misses on two underspecified heldout prompts and one gameplay explanation. These outcomes are preserved in the individual reports; they are not hidden by the mechanics-suite improvement.

The next change should prioritize the casualty rule when the query names casualty, and restrict high priority for CR 707.10 to questions about copying spells. Rerun the affected suite and confirm all three established suites remain intact before adopting that narrower policy.
