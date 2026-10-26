# focused-general-v2-2026-10-26-4

Status: **complete** · implementation commit `a2be46ded16abba4fd06cadc1d07d995afaf5dd8`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 5/5 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 90.0% |
| Cases retrieving every expected evidence group | 4/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 5/5 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 8.22 s |
| p95 successful response | 9.68 s |
| Median first visible answer token | 6.44 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 8.17 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 8.22 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 5.78 |
| g04-replacement-order-general (r1) | 100.0% | correct | 9.02 |
| g05-protection-and-random-target (r1) | 50.0% | correct | 9.68 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** Whatever method you use to resolve a random instruction in paper play, every eligible option must have an equal chance of being selected. The card or effect determines which objects or players are in the eligible pool; if the random choice is a target, only legal targets belong in that pool [CR 115.2].

**Why:** In tournaments, MTR 3.9 specifically addresses die-roll game actions and states that any method that simulates the roll is acceptable as long as every result has an equal chance of occurring [MTR 3.9]. The same equal-chance principle applies to any random instruction in casual or paper play. Practical methods include: shuffling identical slips of paper (one per eligible option) and drawing one; using a die with results evenly mapped to the options (rerolling any result that doesn't map to an option); or flipping a coin when there are exactly two options. Avoid methods that give some options more chance than others, such as a sequence of coin flips for more than two options.

Review: **correct**. Correctly explains equal chance and eligible pools, limits MTR 3.9 to tournament die-roll game actions, and states random targets must be legal.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A creature that copies another creature does not copy counters on it, nor does it copy a +2/+2 bonus from an Aura (or any other continuous effect) on that creature.

**Why:** When copying an object, the copy acquires only the copiable values — the characteristics derived from the text printed on the object, as modified by other copy effects and certain "as it enters" abilities. Other effects (including type-changing and text-changing effects), status, counters, and stickers are explicitly not copied [CR 707.2]. A +2/+2 from an Aura is a continuous effect modifying the object's power and toughness, not a copiable value, so the copy enters with its own base power and toughness (or whatever its own copy effect specifies).

Review: **correct**. Correctly distinguishes copiable values from counters and the Aura’s continuous bonus.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike only modifies the combat damage step; it has no effect on the "fight" action.

**Why:** Double strike is defined as a static ability that modifies the rules for the combat damage step [CR 702.4a]. The fight action is a separate mechanic where each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Since double strike only applies during combat damage steps, it does not cause a creature to deal damage a second time when it fights.

Review: **correct**. Correct; fight damage is not combat damage and double strike does not add a second event.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or the affected player, if the object has no controller) chooses which replacement effect to apply first. They do not both automatically happen — once the first effect is applied, the process is repeated, but the second effect only applies if it is still applicable to the modified event.

**Why:** [CR 616.1] establishes that the affected object's controller or affected player makes the choice. [CR 616.1f] states that after the chosen effect is applied, the process is repeated "taking into account only replacement or prevention effects that would now be applicable," and the example in that rule shows a case where the second effect simply does nothing because the event it was watching for no longer occurs. This is consistent with [CR 614.6], which says a replaced event never happens, and [CR 614.7], which says a replacement effect whose event never happens simply does nothing.

Review: **correct**. Correctly names who chooses and explains re-evaluation after one effect is applied.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red is not a legal target for a red spell, so it is excluded from the eligible pool for the random selection.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. A random target must be a legal target, so the creature is not in the pool from which the random choice is made. The spell's targeting requirement is the same whether the target is chosen manually or at random [CR 601.2c].

Review: **correct**. Correct; protection makes the creature illegal to target, and CR 601.2c supports legal target selection.
Reviewer: Codex

Missing reference groups: CR 115.2

