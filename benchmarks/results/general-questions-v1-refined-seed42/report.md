# general-questions-v1-refined-seed42

Status: **complete** · implementation commit `0b0325030ecefb867c3735d6d2409084ae1ae70b`

Suite `general-questions-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 1/1 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 0/1 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 100.0% |
| Cases retrieving every expected evidence group | 1/1 |
| Answers with citations | 1/1 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 0/1 reviewed |
| Reviewed accuracy | 0.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 10.86 s |
| p95 successful response | 10.86 s |
| Median first visible answer token | 5.59 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | partial | 10.86 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does a card that says to perform some action ‘randomly’ actually work in paper Magic?

**Ruling:** The card or effect defines the eligible pool of options, and the player makes a fair random selection from that pool. The specific physical method (coin flip, die roll, shuffling a stack of tokens, etc.) is not prescribed by the rules as long as each outcome has an equal chance.

**Why:**

- **The pool comes from the card text.** If an effect says "choose one of these options at random," the options listed in the card are the only things that can be selected. If it says "deal 1 damage to a random creature," the pool is all legal creature targets. Only legal targets may be included in a targeting pool [CR 115.2], and the same target can't be chosen multiple times for a single instance of "target" [CR 601.2c].

- **Die-roll game actions in tournaments:** MTR 3.9 states that any method that simulates the roll is acceptable if every result has an equal chance of occurring, and advises avoiding dice whose values are clustered (like spindown life counters) [MTR 3.9]. This applies specifically to game actions that use a die roll.

- **Other random choices:** For non-die-roll random selections (e.g., "choose one of these three options at random"), the rules don't mandate a particular physical procedure. In practice, players commonly use a coin flip, a die, or a shuffled stack of tokens/notes — whatever gives each option an equal probability. The key requirement is fairness, not a specific tool.

**Practical example:** If a card says "Choose one of the following at random: You draw a card; or you lose 2 life; or you gain 2 life," you could write the three options on slips of paper, shuffle them, and draw one. In a tournament, a coin flip (heads/tails) plus a follow-up coin flip for the third option, or a six-sided die with two faces assigned to each option, would also work.

Review: **partial**. Answers without a follow-up and includes legal-target handling, but extends die-roll guidance to other choices and suggests an uneven two-coin procedure for three outcomes.
Reviewer: Codex

Missing reference groups: none

