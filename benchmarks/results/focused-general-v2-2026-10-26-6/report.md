# focused-general-v2-2026-10-26-6

Status: **complete** · implementation commit `ede0095c1ceea2f1e9ce845330abb457fd4f33d5`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 4/5 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 100.0% |
| Cases retrieving every expected evidence group | 5/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 4/5 reviewed |
| Reviewed accuracy | 80.0% |
| Mean reviewed rubric score | 90.0% |
| Median successful response | 8.08 s |
| p95 successful response | 8.90 s |
| Median first visible answer token | 6.34 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | partial | 8.90 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 8.08 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 6.44 |
| g04-replacement-order-general (r1) | 100.0% | correct | 6.79 |
| g05-protection-and-random-target (r1) | 100.0% | correct | 8.20 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** Whatever physical method you use, every eligible option must have an equal chance of being selected. The card or effect determines which options are in the pool; the physical procedure just needs to be fair.

**Why:** For die-roll game actions in tournaments, any method that simulates the roll is acceptable as long as every result has an equal chance [MTR 3.9]. For other random choices (e.g., "randomly determine which player goes first" [CR 809.4]), the same fairness principle applies in practice. Common fair methods include: a coin flip for two options, a die with evenly mapped results (rerolling unused faces) for up to six, or shuffling identical slips of paper for any number of options. Avoid methods that cluster values unevenly, such as spindown life counters [MTR 3.9].

Review: **partial**. Gives practical equal-chance methods and distinguishes tournament die-roll guidance, but omits the frozen criterion’s explicit statement that randomly selected targets must be legal.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy acquires only the copiable values of the object it's copying (name, mana cost, color, type, subtype, supertype, rules text, power, toughness, loyalty). Counters and continuous effects like a +2/+2 from an Aura are not copied.

**Why:** Rule 707.2 explicitly states that "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." A +2/+2 from an Aura is a continuous effect modifying the object's characteristics, not a copiable value, so the copy enters with the original creature's printed (or copy-set) power and toughness, without the Aura's bonus and without any counters. [CR 707.2]

Review: **correct**. Directly and correctly states the general copy rule for counters and external Aura bonuses.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights.

**Why:** Double strike is a static ability that modifies the rules for the combat damage step [CR 702.4a]. The fight action deals damage equal to the creature's power once, and that damage is explicitly not combat damage [CR 701.14a], [CR 701.14d]. Since double strike only applies within the combat damage step, it has no effect on fight damage.

Review: **correct**. Correctly explains that each creature deals damage once in a fight and fight damage is not combat damage.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller), or the affected player, chooses which replacement effect to apply first. After that effect is applied, the process is repeated with any remaining applicable effects.

**Why:** [CR 616.1] assigns the choice to the affected player or controller. [CR 616.1f] explains that once the chosen effect is applied, the process repeats, taking into account only effects that would now be applicable to the modified event. So both effects don't automatically stack — the second one only applies if it's still applicable to the event as modified by the first.

Review: **correct**. Correctly identifies the affected object’s controller or owner, or affected player, and explains sequential reevaluation.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red cannot be selected, because it is not a legal target for a red spell.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. When a spell targets a creature "chosen at random," the random selection must still produce a legal target; only legal targets are eligible to be chosen [CR 115.2, CR 601.2c]. The creature with protection from red is excluded from the pool of possible random selections.

Review: **correct**. Correctly excludes an illegal target from random selection; randomness does not bypass protection.
Reviewer: Codex

Missing reference groups: none

