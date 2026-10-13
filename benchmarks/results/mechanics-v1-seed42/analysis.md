# Mechanics-v1 two-seed analysis

The frozen 20-case mechanics suite was run twice against the same implementation and local model, with seeds 42 and 43. The suite was authored from the frozen rules corpus and was not independently reviewed by a Magic judge. These are exploratory development measurements, not validated accuracy estimates.

| Measure | Seed 42 | Seed 43 |
|---|---:|---:|
| Fully correct answers | 14/20 (70%) | 13/20 (65%) |
| Completed requests | 20/20 | 20/20 |
| Errors / truncated answers | 0 / 0 | 0 / 0 |
| Exact authored evidence-group recall | 48.3% | 48.3% |
| All expected evidence groups retrieved | 9/20 | 9/20 |
| Citation ID validity | 100% | 100% |
| Semantic citation failures | 4 | 2 |
| Median latency | 7.31 s | 7.48 s |
| p95 latency | 14.24 s | 15.90 s |

The full answers, retrieved passages, telemetry, and per-answer review notes are in each run directory. Reviews were AI-assisted by Codex and were not independently checked by a Magic judge. The criterion judgments are therefore useful for engineering triage, not ground truth.

## Repeated failure patterns

- **Retrieval gaps lead to avoidable abstentions.** Both seeds declined to answer mana value for X outside the stack, the initiative trigger-count question, and retaking the initiative even though the frozen rules corpus contains the relevant rules. Both also declined to answer whether copying a spell counts as casting it. Improve query-to-rule retrieval for X and mana value, initiative, and copying before changing generation settings.
- **Small arithmetic omissions change rulings.** Seed 43 computed the mana value of `{4}{2}{R}` as 6, omitting the red symbol. A concise structured calculation or final-answer self-check could catch this class of mistake.
- **Rules can be cited without supporting the adjacent claim.** Seed 42 cited an Archenemy rule for the poison threshold. Seed 43 cited a split-card rule while explaining hybrid mana symbols. Citation IDs were valid in every case, showing that ID validity alone does not establish semantic support.
- **The model sometimes answers correctly while exposing missing evidence.** The hybrid-mana-value case produced 5 in both seeds, but the relevant hybrid rule was absent from the supplied excerpts. This is a retrieval weakness even where the final answer happens to be correct.
- **One seed made an unsupported source-independence claim.** Seed 43 said a planeswalker ability would still resolve after its source left, while acknowledging that its retrieved passages did not establish that rule. Seed 42 abstained on that part instead.

## Interpreting evidence recall

The 48.3% figure measures retrieval of the suite's authored evidence groups, not whether every answer has adequate rules support. The expected groups intentionally name narrow canonical passages. Some correct answers used other relevant provisions—for example, the loyalty timing rule, the regeneration replacement rule, or the Siege zero-defense exception. Conversely, an answer can cite a passage that exists but misapply it. Use the saved answer-level reviews and passages alongside this retrieval metric.

## Next engineering work

1. Inspect retrieval traces for the failed X/mana-value, initiative, and copied-spell cases; identify missing query terms, topic expansion, or candidate-ranking behavior.
2. Add a targeted retrieval regression test for each confirmed root cause, preserving the existing frozen suite and its criteria.
3. Evaluate any retrieval change on gameplay-v1, heldout-v1, novel-v1, and mechanics-v1. Treat seed-to-seed variation as uncertainty and preserve both answer records.
4. Consider a lightweight answer check for numeric mana-value calculations and citation-to-claim alignment only after a separate controlled experiment shows it helps without harming other suites.
