# focused-general-v2-2026-10-26

Status: **complete** · implementation commit `8b30a311015f6b7df72a8522ec3d89522ef45572`

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
| Median successful response | 8.40 s |
| p95 successful response | 9.91 s |
| Median first visible answer token | 7.42 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 9.52 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 7.40 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 5.97 |
| g04-replacement-order-general (r1) | 100.0% | correct | 9.91 |
| g05-protection-and-random-target (r1) | 50.0% | correct | 8.40 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect determines the eligible pool of options, and whatever physical method you use must give each eligible option an equal chance of being selected.

**Why:** For die-roll game actions specifically, any method that simulates the roll is acceptable as long as every result has an equal chance of occurring [MTR 3.9]. For other random choices (such as randomly selecting one card from a set), the standard paper procedure is to shuffle the eligible options and select one at random, which naturally gives each option an equal probability. If a random choice involves a target, only legal targets may be included in the pool [CR 115.2]. The key principle across all cases is equal chance per eligible option; the specific physical method (die, shuffled slips, etc.) is flexible as long as that condition is met.

Review: **correct**. Correctly gives a fair method, limits MTR 3.9 to die-roll game actions, and states that random targets must be legal.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it acquire a +2/+2 (or any other) bonus from an Aura or similar effect on that creature.

**Why:** When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects and certain "as it enters" abilities). Counters, status, and other effects—including type-changing and text-changing effects—are explicitly not copied [CR 707.2]. A +2/+2 from an Aura is a noncopy effect that modifies the original's characteristics but is not part of its copiable values, so the copy enters with its own base power and toughness (or whatever the copy effect specifies) [CR 707.2].

Review: **correct**. Correctly distinguishes copiable values from counters and the Aura’s continuous bonus.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies the rules for the combat damage step [CR 702.4a]. The "fight" action is a separate mechanic in which each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Since double strike only applies during the combat damage step, it has no effect on the fight action.

Review: **correct**. Correct; fight damage is not combat damage, so double strike does not add another damage event.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller) or the affected player chooses which replacement effect to apply first. They do not both automatically happen — after one is applied, the process is repeated with the *modified* event, and the second effect only applies if it is still applicable to that modified event.

**Why:** Rule 616.1 establishes that the affected player chooses which replacement effect to apply, following a priority order (self-replacement effects first, then control-changing, then copy, then back-face, then any remaining). Rule 616.1f states that once the chosen effect is applied, the process repeats "taking into account only replacement or prevention effects that would now be applicable." Because the original event is replaced and never happens [CR 614.6], the second effect may no longer match the modified event and simply does nothing — as illustrated by the example in 616.1f where one replacement is chosen and "the other does nothing."

Review: **correct**. Correctly names the chooser and explains that remaining effects are reevaluated against the modified event.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red cannot be selected as a target by a red spell, even when the target is chosen at random.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. When a spell requires a target, only legal targets may be chosen [CR 601.2c]. The random selection must be made from the pool of legal targets, so a creature with protection from red is excluded from that pool.

Review: **correct**. Correct; protection makes the creature an illegal target and random selection does not bypass targeting legality.
Reviewer: Codex

Missing reference groups: CR 115.2

