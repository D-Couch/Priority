# focused-general-v2-seed42

Status: **complete** · implementation commit `9bd6927e08e72f4dd5eee8de720e79ced44746bf`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 4/5 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 90.0% |
| Cases retrieving every expected evidence group | 4/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 4/5 reviewed |
| Reviewed accuracy | 80.0% |
| Mean reviewed rubric score | 90.0% |
| Median successful response | 10.27 s |
| p95 successful response | 12.20 s |
| Median first visible answer token | 7.66 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | partial | 12.20 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 6.99 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 6.62 |
| g04-replacement-order-general (r1) | 100.0% | correct | 10.27 |
| g05-protection-and-random-target (r1) | 50.0% | correct | 10.87 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect determines which options are eligible, and you use any physical method that gives each eligible option an equal chance — most commonly writing each option on an identical slip, shuffling them, and drawing one. For die-roll game actions specifically, any method that simulates the roll is acceptable as long as every result has an equal chance of occurring.

**Why:** MTR 3.9 establishes the equal-chance standard for die-roll actions and explicitly permits any simulation method that meets it [MTR 3.9]. For non-die-roll random choices (e.g., "randomly choose one of your creatures"), the eligible pool comes from the card's text, and the physical procedure simply needs to ensure each option in that pool is equally likely to be selected — shuffled identical slips are the standard paper-play method for arbitrary option counts.

Review: **partial**. Gives equal-chance paper methods and correctly limits MTR 3.9 to die-roll actions. It omits the suite criterion that random targets must be legal, although that detail is not needed to describe the physical method.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it gain the +2/+2 bonus from an Aura attached to that creature.

**Why:** When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects, face-down status, and "as . . . enters" abilities). Counters, status, and other effects (including type-changing and text-changing effects) are explicitly not copied [CR 707.2]. Additionally, if a permanent on the battlefield changes what it's copying, any noncopy effects presently affecting it (such as an Aura's +2/+2) are not transferred to the new copy [CR 707.4].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies the rules for the combat damage step [CR 702.4a]. The "fight" action is a separate mechanic in which each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Since double strike only applies during combat damage steps, it has no effect on the fight action.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or the affected player) chooses which replacement effect to apply first. They do not both automatically happen—once one is applied, the process is repeated with the modified event, and the second effect may no longer be applicable.

**Why:** [CR 616.1] establishes that the affected object's controller or affected player chooses which replacement effect to apply. [CR 616.1f] clarifies that after the chosen effect is applied, the process repeats with only the effects that are now applicable to the modified event. The example in [CR 616.1f] illustrates this directly: if a creature would be put into a graveyard and two replacement effects (exile vs. shuffle into library) both apply, the controller picks one and the other does nothing. Note that [CR 616.1a]–[CR 616.1d] impose a priority order (self-replacement effects, control changes, copy effects, back-face-up effects) that must be chosen before any other applicable effect under [CR 616.1e].

Review: **correct**. Correctly describes the chooser and sequential re-evaluation. The sourced example from CR 616.1f is relevant and accurate.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red is not a legal target for a red spell, so it must be excluded from the pool of creatures from which the random target is chosen.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. When a spell says "target creature chosen at random," the target must still be a legal one at the time targets are chosen [CR 601.2c]. Since the creature with protection from red is not a legal target for that red spell, it is not part of the eligible pool for the random selection.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 115.2

