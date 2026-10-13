# concise-general-v2-seed42

Status: **complete** · implementation commit `b26e4ea449f405a8debb43b1d3992d5e34a11bdd`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | pending / n/a/0 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 90.0% |
| Cases retrieving every expected evidence group | 4/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | pending / n/a |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 0/0 reviewed |
| Reviewed accuracy | pending / n/a |
| Mean reviewed rubric score | pending / n/a |
| Median successful response | 7.66 s |
| p95 successful response | 8.90 s |
| Median first visible answer token | 5.85 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | pending | 7.66 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | pending | 8.25 |
| g03-fight-and-double-strike (r1) | 100.0% | pending | 6.33 |
| g04-replacement-order-general (r1) | 100.0% | pending | 6.27 |
| g05-protection-and-random-target (r1) | 50.0% | pending | 8.90 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect determines the eligible pool of options, and whatever physical method you use must give each eligible option an equal chance of being selected.

**Why:** For die-roll game actions specifically, the Tournament Rules state that any method that simulates the roll is acceptable as long as every result has an equal chance of occurring [MTR 3.9]. In practice, common approaches include: shuffling identical slips of paper (one per eligible option) and drawing one, or using a die when its faces can be mapped evenly onto the options (rerolling any face that doesn't correspond to an eligible option). The key requirement is equal probability across all eligible choices. If the random choice is a target, only legal targets belong in the pool [CR 115.2].

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A creature that copies another creature does not copy counters on it, nor does it copy a +2/+2 bonus from an Aura.

**Why:** When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects, face-down status, and "as it enters" abilities that set power/toughness). Other effects—including type-changing and text-changing effects—status, counters, and stickers are explicitly not copied [CR 707.2]. A +2/+2 from an Aura is a continuous effect modifying the object's characteristics, not a copiable value, so it is not part of what gets copied. The Chimeric Staff example in the same rule illustrates this: a Clone copying a Staff that has become a 5/5 via its own ability enters as a plain artifact, not a 5/5 [CR 707.2].

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies the rules for the *combat damage step* specifically [CR 702.4a]. The fight action is a separate mechanic in which each creature deals damage equal to its power to the other, and that damage is explicitly not combat damage [CR 701.14a], [CR 701.14d]. Since double strike only applies during combat damage steps, it has no effect on the fight action.

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller) or the affected player chooses which replacement effect to apply first. They do not both automatically happen—the player picks one, applies it, then checks whether the other is still applicable to the modified event. If the modified event no longer triggers the second effect, it simply does nothing.

**Why:** [CR 616.1] establishes that the affected player chooses which replacement effect to apply when two or more are attempting to modify the same event. [CR 616.1f] explains that after one is applied, the process repeats with only the effects still applicable to the now-modified event. [CR 614.7] confirms that if the event a replacement effect would replace never happens, that effect simply doesn't do anything.

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red cannot be selected as a target by a red spell, even if the target is chosen at random.

**Why:** Protection from red means the creature "can't be targeted by spells with the stated quality" [CR 702.16b]. This is a hard restriction on targeting that applies regardless of the selection method. When choosing targets, only legal targets may be selected [CR 601.2c], so a random selection mechanism must exclude creatures that are illegal targets due to protection.

Missing reference groups: CR 115.2

