# general-questions-v1-concise-seed42

Status: **complete** · implementation commit `2935da7b0d98c6c078148641ae5fa0e47e5795b6`

Suite `general-questions-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 1/1 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 1/1 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 100.0% |
| Cases retrieving every expected evidence group | 1/1 |
| Answers with citations | 1/1 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 1/1 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 7.96 s |
| p95 successful response | 7.96 s |
| Median first visible answer token | 4.84 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 7.96 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does a card that says to perform some action ‘randomly’ actually work in paper Magic?

**Ruling:** The card or effect defines the eligible pool of options, and the player must use a method that gives each eligible option an equal chance of being selected. If the random choice is a target, only legal targets (permanents, or objects/players the spell specifically allows) belong in that pool.

**Why:** The rules don't mandate a specific randomizer for most effects—the card determines what can be chosen, and the player just needs a fair method. For die-roll game actions specifically, the Tournament Rules state that any method simulating the roll is acceptable as long as every result has an equal chance [MTR 3.9]. For non-die-roll random choices (e.g., "choose a card at random from your hand"), the same fairness principle applies: each eligible option must have the same probability of being selected. A practical method is to shuffle the eligible items and take the top one, or map a die's faces evenly onto the options (rerolling any face that doesn't map to an option). If the random selection is a target, remember that only legal targets may be included [CR 115.2].

Review: **correct**. Gives a direct practical answer, explicitly limits MTR 3.9 to die-roll game actions, and says a random target pool contains only legal targets. The die mapping and shuffled slips are even-probability methods.
Reviewer: Codex

Missing reference groups: none

