# copy-priority-fix-mechanics-seed43

Status: **complete** · implementation commit `855024db872f940013d5d90071b234da601e493f`

Suite `mechanics-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [43]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 18/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 78.3% |
| Cases retrieving every expected evidence group | 15/20 |
| Answers with citations | 20/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 2 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 18/20 reviewed |
| Reviewed accuracy | 90.0% |
| Mean reviewed rubric score | 98.3% |
| Median successful response | 7.14 s |
| p95 successful response | 10.14 s |
| Median first visible answer token | 5.71 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| m01-poison-threshold (r1) | 0.0% | partial | 8.75 |
| m02-x-on-stack (r1) | 100.0% | correct | 5.34 |
| m03-x-outside-stack (r1) | 100.0% | correct | 5.78 |
| m04-hybrid-mana-value (r1) | 100.0% | correct | 5.12 |
| m05-loyalty-stack-window (r1) | 0.0% | correct | 5.38 |
| m06-new-planeswalker-activation (r1) | 0.0% | correct | 7.15 |
| m07-loyalty-limit-permanent (r1) | 100.0% | correct | 7.13 |
| m08-loyalty-cost-and-source (r1) | 66.7% | partial | 15.85 |
| m09-siege-protector (r1) | 100.0% | correct | 6.65 |
| m10-siege-last-counter (r1) | 100.0% | correct | 8.70 |
| m11-monarch-combat-trigger (r1) | 100.0% | correct | 7.43 |
| m12-monarch-draw-trigger (r1) | 100.0% | correct | 10.14 |
| m13-initiative-multiple-damage (r1) | 100.0% | correct | 9.60 |
| m14-retake-initiative (r1) | 100.0% | correct | 7.32 |
| m15-phased-out-token (r1) | 100.0% | correct | 7.34 |
| m16-phased-out-board-wipe (r1) | 100.0% | correct | 5.33 |
| m17-regeneration-shield (r1) | 0.0% | correct | 6.25 |
| m18-extra-turn-order (r1) | 100.0% | correct | 4.88 |
| m19-land-not-a-spell (r1) | 100.0% | correct | 6.01 |
| m20-copy-not-cast (r1) | 100.0% | correct | 7.45 |

## Answers and review notes

### m01-poison-threshold / repetition 1

I have nine poison counters. A creature deals combat damage to me that gives me one more poison counter. Does the game end the instant I reach ten, or when does the loss happen?

**Ruling:** You don't lose the game the instant the counter is applied. Losing due to ten or more poison counters is a state-based action, which is checked when a player would next receive priority.

**Why:** Rule 904.13c explicitly states that having ten or more poison counters causes a player to lose the game and labels it a state-based action [CR 904.13c]. State-based actions are dealt with automatically before a player would receive priority [CR 117.2d]. So the loss is recognized at the next point where the game checks state-based actions (i.e., before the next player is about to get priority), not at the exact moment the counter is added.

Review: **partial**. The threshold and timing are correct, but CR 904.13c is specific to Archenemy games and does not support the general-format claim as cited. CR 104.3d is the general poison-loss rule.
Reviewer: Codex

Missing reference groups: CR 104.3d

### m02-x-on-stack / repetition 1

A spell has mana cost {X}{2}{R}. I cast it choosing X=4. What is its mana value while it is on the stack?

**Ruling:** The mana value is 7.

**Why:** While on the stack, X is treated as the number chosen for it [CR 202.3e]. The mana value is the total amount of mana in the mana cost, regardless of color [CR 202.3]. So {X}{2}{R} with X=4 gives 4 + 2 + 1 = 7.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m03-x-outside-stack / repetition 1

A permanent has mana cost {X}{G} and is on the battlefield with several counters on it. What is its mana value?

**Ruling:** Its mana value is 1.

**Why:** A permanent on the battlefield is not on the stack, so the {X} in its mana cost is treated as 0 when calculating mana value [CR 202.3e]. The {G} contributes 1, giving a total mana value of 1. Counters on the permanent do not affect its mana value.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m04-hybrid-mana-value / repetition 1

A card has mana cost {2/W}{2/W}{1}. What is its mana value?

**Ruling:** The mana value is 5.

**Why:** When calculating the mana value of an object with a hybrid mana symbol in its mana cost, use the largest component of each hybrid symbol [CR 202.3f]. Each {2/W} contributes 2, and the {1} contributes 1, for a total of 5.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m05-loyalty-stack-window / repetition 1

It is my main phase and I have priority, but an opponent’s instant is still on the stack. May I activate a loyalty ability of my planeswalker in response?

Ruling: No. You may not activate a loyalty ability while an opponent's instant is on the stack.

Why: A loyalty ability may only be activated "any time [you] have priority and the stack is empty during a main phase of your turn" [CR 113.5]. Since the opponent's instant is still on the stack, the stack is not empty, so the condition is not met.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: CR 606.3

### m06-new-planeswalker-activation / repetition 1

I cast a planeswalker during my first main phase. After it resolves and the stack is empty, may I activate one of its loyalty abilities this turn if I have not activated one of its loyalty abilities yet?

Ruling: Yes. After the planeswalker spell resolves, you receive priority, the stack is empty, it is still your main phase, and you have not activated any of that permanent's loyalty abilities this turn, so all conditions are met.

Why: A player may activate a loyalty ability of a permanent they control any time they have priority and the stack is empty during a main phase of their turn, provided none of that permanent's loyalty abilities have been activated that turn [CR 306.5d]. The active player receives priority after a spell resolves [CR 117.3b], so you have priority at the moment you need it.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: CR 606.3

### m07-loyalty-limit-permanent / repetition 1

I activated a +1 loyalty ability of one planeswalker earlier this turn. After it resolves, may I activate a different loyalty ability of that same planeswalker? What about a second planeswalker I control?

**Ruling:** No, you may not activate a different loyalty ability of that same planeswalker this turn. Yes, you may activate a loyalty ability of a second planeswalker you control.

**Why:** The once-per-turn restriction on loyalty abilities is tied to each individual permanent, not to the player. Once any player has activated a loyalty ability of a given planeswalker that turn, no further loyalty abilities of that same permanent may be activated [CR 606.3]. A different planeswalker is a different permanent, so its loyalty abilities remain available [CR 306.5d].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m08-loyalty-cost-and-source / repetition 1

My planeswalker has exactly three loyalty counters. I activate an ability with a −3 cost. Can I wait until it resolves to remove the counters, and does the ability still resolve if the planeswalker is put into the graveyard before the ability resolves?

**Ruling:** No, you cannot wait until resolution to remove the counters. The loyalty counters are removed as part of the cost to activate the ability, which happens before the ability is on the stack. Yes, the ability will still resolve even if the planeswalker is put into the graveyard before it resolves, because once an ability is on the stack it is independent of its source.

**Why:** [CR 606.4] states that the cost to activate a loyalty ability is to remove the specified number of loyalty counters, and [CR 606.6] confirms the permanent must have at least that many counters to activate. Costs are paid as part of the activation process, not at resolution. The provided excerpts do not include the specific rule establishing that an ability on the stack resolves independently of its source's continued presence on the battlefield, so I cannot cite a supporting excerpt for that portion.

Review: **partial**. Correctly states counters are paid as an activation cost and the activated ability survives its source leaving. It does not say a planeswalker at zero loyalty is put into its owner’s graveyard; it also acknowledges the source-independence claim lacks a supporting excerpt.
Reviewer: Codex

Missing reference groups: CR 113.7a

### m09-siege-protector / repetition 1

I control a Battle — Siege in a two-opponent game. As it enters, may I choose myself as its protector, or must I choose one of my opponents?

**Ruling:** You must choose one of your opponents as the Siege's protector. You cannot choose yourself.

**Why:** Rule 310.12a explicitly states that "As a Siege enters the battlefield, its controller must choose its protector from among their opponents. Only an opponent of a Siege's controller can be its protector." [CR 310.12a] This is the specific restriction for Sieges under rule 310.12, which rule 310.9a references when determining which players may be chosen. [CR 310.9a]

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m10-siege-last-counter / repetition 1

The last defense counter is removed from a Siege. Does it transform immediately as part of removing the counter, or does an ability trigger? What happens when that ability resolves?

**Ruling:** A triggered ability triggers. It is not an immediate transformation. When the ability resolves, the Siege is exiled, and then its controller may cast it transformed without paying its mana cost.

**Why:** The intrinsic ability on Sieges is written as a triggered ability: "When the last defense counter is removed from this permanent, exile it, then you may cast it transformed without paying its mana cost." [CR 310.12b] Because it is a triggered ability, it goes on the stack and resolves at the next opportunity rather than happening as part of the counter removal itself. Additionally, the Siege does not immediately go to the graveyard when its defense reaches 0, because the state-based action that would do so is suspended while it is the source of an ability that has triggered but not yet left the stack. [CR 310.7]

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m11-monarch-combat-trigger / repetition 1

A creature deals combat damage to the current monarch. Does its controller become the monarch immediately as damage is dealt, or only after a triggered ability resolves?

**Ruling:** The controller becomes the monarch when the triggered ability resolves, not immediately when the damage is dealt.

**Why:** The monarch's damage-triggered ability is a triggered ability with the text "Whenever a creature deals combat damage to the monarch, its controller becomes the monarch" [CR 725.2]. Triggered abilities trigger on the event, then go on the stack the next time a player would receive priority, and only take effect when they resolve [CR 603.2] [CR 603.3].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m12-monarch-draw-trigger / repetition 1

Alice is the monarch when her end step begins, so the monarch draw ability triggers. Before it resolves, an effect makes Bob the monarch. Does Alice’s already-triggered ability still make her draw a card?

Ruling: Yes, Alice still draws a card.

Why: The monarch draw ability is controlled by the player who was the monarch at the time it triggered, and its effect is to make "that player" (i.e., Alice) draw a card [CR 725.2]. Once the ability is on the stack, its effect is fixed; there is no intervening "if" clause or condition that re-checks who is the monarch at resolution [CR 603.4]. Bob becoming the monarch afterward does not alter what the already-triggered ability does.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m13-initiative-multiple-damage / repetition 1

I have the initiative. During one combat damage event, two creatures controlled by Bob each deal combat damage to me. How many times does the damage ability trigger, and what happens if it resolves?

**Ruling:** The ability triggers **once**, and when it resolves, Bob takes the initiative.

**Why:** The trigger condition is "whenever **one or more** creatures a player controls deal combat damage to the player who has the initiative" [CR 726.2]. Since both creatures are controlled by the same player (Bob) and deal damage in the same simultaneous combat damage event [CR 510.2], this constitutes a single instance of the trigger condition being met, producing one triggered ability. When it resolves, "the controller of those creatures takes the initiative" [CR 726.2], so Bob gains the initiative.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m14-retake-initiative / repetition 1

I already have the initiative, and an effect instructs me to take the initiative. Do I get a second initiative designation, and does anything trigger?

**Ruling:** No, you do not get a second initiative designation. However, the third inherent triggered ability from rule 726.2 does trigger: "Whenever a player takes the initiative, that player ventures into the Dungeon."

**Why:** Rule 726.5 explicitly states that if the player who currently has the initiative is instructed to take the initiative, it "causes the last triggered ability in 726.2 to trigger but does not create a second initiative designation." The last (third) ability listed in 726.2 is the "ventures into the Dungeon" trigger. [CR 726.5] [CR 726.2]

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m15-phased-out-token / repetition 1

A creature token with counters on it phases out. Does it leave the battlefield, cease to exist, or cause leaves/enters-the-battlefield abilities to trigger?

**Ruling:** The token does not leave the battlefield, does not cease to exist, and does not cause any enters- or leaves-the-battlefield abilities to trigger.

**Why:** The phasing event does not cause a permanent to change zones or control, and zone-change triggers do not trigger when a permanent phases in or out [CR 702.26d]. Tokens continue to exist on the battlefield while phased out, and counters remain on them [CR 702.26d]. A phased-out permanent is merely treated as though it does not exist for most game purposes, but it has not actually left the battlefield [CR 702.26b].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m16-phased-out-board-wipe / repetition 1

A phased-out creature is on the battlefield in the game’s history. A spell says “Destroy all creatures.” Is that phased-out creature destroyed?

Ruling: No, the phased-out creature is not destroyed.

Why: A phased-out permanent is treated as though it does not exist and can't be affected by anything else in the game, unless a rule or effect specifically mentions phased-out permanents [CR 702.26b]. The example in that rule explicitly states that a phased-out creature is not destroyed by a spell that says "Destroy all creatures" [CR 702.26b].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m17-regeneration-shield / repetition 1

An attacking creature has a regeneration shield. It would be destroyed by lethal damage. What does the shield do?

**Ruling:** The regeneration shield replaces the destruction. Instead of being destroyed, the creature has all damage marked on it removed, is tapped by its controller, and is removed from combat.

**Why:** Regeneration is a destruction-replacement effect that applies the next time the permanent would be destroyed that turn [CR 614.8]. When a creature with lethal damage would be destroyed as a state-based action, regeneration can replace that event [CR 704.5g]. Since the creature is attacking, it is also removed from combat [CR 614.8].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: CR 701.19a

### m18-extra-turn-order / repetition 1

Two extra turns are created for the same player after the current turn. First one effect creates an extra turn; later another effect creates a second extra turn. Which extra turn is taken first?

Ruling: The second extra turn (the most recently created one) is taken first.

Why: Rule 500.7 explicitly states that "the most recently created turn will be taken first." Since the second effect created its extra turn after the first, it is the most recently created and therefore occurs before the first extra turn. [CR 500.7]

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m19-land-not-a-spell / repetition 1

I have priority in my main phase with an empty stack and play a land from my hand. Does the land go on the stack, and can my opponent respond to the land play with an instant?

Ruling: No, the land does not go on the stack, and your opponent cannot respond with an instant.

Why: Playing a land is a special action that doesn't use the stack; the player simply puts the land onto the battlefield. [CR 305.1] Since the land never becomes a spell and the action doesn't use the stack, players can't respond to it with instants or activated abilities. [CR 305.1] [CR 505.6b]

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m20-copy-not-cast / repetition 1

An effect copies a modal instant on the stack and says I may choose new targets for the copy. Does the copy count as being cast for “whenever you cast” abilities? Can I choose a different mode as well as new targets?

**Ruling:** No, the copy is not cast, so "whenever you cast" abilities do not trigger. No, you cannot choose a different mode; the copy retains the same mode as the original spell.

**Why:** A copy of a spell isn't cast [CR 707.10]. A copy of a spell copies all decisions made for it, including modes [CR 707.10]. The "may choose new targets" clause only permits changing targets; it does not extend to changing modes [CR 707.10c].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

