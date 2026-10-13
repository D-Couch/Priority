# poison-loyalty-retrieval-seed42

Status: **complete** · implementation commit `7b7297d9aae78fdafe8b311fd541666794edc9f2`

Suite `mechanics-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 20/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 95.0% |
| Cases retrieving every expected evidence group | 19/20 |
| Answers with citations | 20/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 20/20 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 6.80 s |
| p95 successful response | 8.99 s |
| Median first visible answer token | 5.69 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| m01-poison-threshold (r1) | 100.0% | correct | 8.50 |
| m02-x-on-stack (r1) | 100.0% | correct | 5.52 |
| m03-x-outside-stack (r1) | 100.0% | correct | 6.95 |
| m04-hybrid-mana-value (r1) | 100.0% | correct | 5.70 |
| m05-loyalty-stack-window (r1) | 100.0% | correct | 5.14 |
| m06-new-planeswalker-activation (r1) | 100.0% | correct | 6.53 |
| m07-loyalty-limit-permanent (r1) | 100.0% | correct | 6.54 |
| m08-loyalty-cost-and-source (r1) | 100.0% | correct | 7.00 |
| m09-siege-protector (r1) | 100.0% | correct | 6.32 |
| m10-siege-last-counter (r1) | 100.0% | correct | 10.27 |
| m11-monarch-combat-trigger (r1) | 100.0% | correct | 8.08 |
| m12-monarch-draw-trigger (r1) | 100.0% | correct | 8.99 |
| m13-initiative-multiple-damage (r1) | 100.0% | correct | 8.89 |
| m14-retake-initiative (r1) | 100.0% | correct | 7.19 |
| m15-phased-out-token (r1) | 100.0% | correct | 7.34 |
| m16-phased-out-board-wipe (r1) | 100.0% | correct | 5.19 |
| m17-regeneration-shield (r1) | 0.0% | correct | 6.65 |
| m18-extra-turn-order (r1) | 100.0% | correct | 5.27 |
| m19-land-not-a-spell (r1) | 100.0% | correct | 5.91 |
| m20-copy-not-cast (r1) | 100.0% | correct | 7.25 |

## Answers and review notes

### m01-poison-threshold / repetition 1

I have nine poison counters. A creature deals combat damage to me that gives me one more poison counter. Does the game end the instant I reach ten, or when does the loss happen?

**Ruling:** The game does not end the instant you reach ten poison counters. You lose the game the next time a player would receive priority.

**Why:** Having ten or more poison counters is a state-based action that is checked "the next time a player would receive priority" [CR 104.3d]. State-based actions are dealt with before a player would receive priority [CR 117.2d]. So after the poisonous trigger resolves and the 10th counter is placed, you don't lose immediately—you lose at the next priority check, which gives a brief window where the game state exists but the loss hasn't been applied yet.

Review: **correct**. The answer cites the general poison-loss rule CR 104.3d and correctly explains that the loss occurs at the next priority check.
Reviewer: Codex

Missing reference groups: none

### m02-x-on-stack / repetition 1

A spell has mana cost {X}{2}{R}. I cast it choosing X=4. What is its mana value while it is on the stack?

**Ruling:** The mana value is 7.

**Why:** The mana value of an object is the total amount of mana in its mana cost, regardless of color [CR 202.3]. While on the stack, X is treated as the number chosen for it [CR 202.3e]. With X = 4, the cost is effectively {4}{2}{R}, which sums to 4 + 2 + 1 = 7.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m03-x-outside-stack / repetition 1

A permanent has mana cost {X}{G} and is on the battlefield with several counters on it. What is its mana value?

**Ruling:** The permanent's mana value is 1.

**Why:** A permanent on the battlefield is not on the stack, so the {X} in its mana cost is treated as 0 for mana value purposes [CR 202.3e]. The {G} contributes 1, giving a total mana value of 1. Counters on the permanent do not affect its mana value.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m04-hybrid-mana-value / repetition 1

A card has mana cost {2/W}{2/W}{1}. What is its mana value?

**Ruling:** The mana value is 5.

**Why:** When calculating mana value, each hybrid mana symbol contributes its largest component [CR 202.3f]. Each {2/W} contributes 2 (the larger of 2 and 1), and the {1} contributes 1, for a total of 2 + 2 + 1 = 5.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m05-loyalty-stack-window / repetition 1

It is my main phase and I have priority, but an opponent’s instant is still on the stack. May I activate a loyalty ability of my planeswalker in response?

Ruling: No. You may not activate a loyalty ability while any spell or ability is on the stack.

Why: Rule 606.3 requires that "the stack is empty" as a condition for activating a loyalty ability. Since your opponent's instant is still on the stack, that condition is not met, so you cannot activate the loyalty ability in response. [CR 606.3]

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passage supports the ruling.
Reviewer: Codex

Missing reference groups: none

### m06-new-planeswalker-activation / repetition 1

I cast a planeswalker during my first main phase. After it resolves and the stack is empty, may I activate one of its loyalty abilities this turn if I have not activated one of its loyalty abilities yet?

Ruling: Yes. You may activate one of its loyalty abilities this turn.

Why: Rule 606.3 requires only that you control the permanent, have priority, the stack is empty, it's a main phase of your turn, and no player has previously activated a loyalty ability of that permanent that turn. There is no requirement that the planeswalker has been on the battlefield since the beginning of the turn. [CR 606.3]

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passage supports the ruling.
Reviewer: Codex

Missing reference groups: none

### m07-loyalty-limit-permanent / repetition 1

I activated a +1 loyalty ability of one planeswalker earlier this turn. After it resolves, may I activate a different loyalty ability of that same planeswalker? What about a second planeswalker I control?

**Ruling:** No, you cannot activate another loyalty ability of that same planeswalker this turn. Yes, you may activate a loyalty ability of a different planeswalker you control.

**Why:** The once-per-turn restriction on loyalty abilities is per permanent, not per player. Rule 606.3 states you may activate a loyalty ability "only if no player has previously activated a loyalty ability of *that permanent* that turn" [CR 606.3]. Since the restriction is tied to the specific planeswalker, a second planeswalker is unaffected and may have its own loyalty ability activated the same turn.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passage supports the ruling.
Reviewer: Codex

Missing reference groups: none

### m08-loyalty-cost-and-source / repetition 1

My planeswalker has exactly three loyalty counters. I activate an ability with a −3 cost. Can I wait until it resolves to remove the counters, and does the ability still resolve if the planeswalker is put into the graveyard before the ability resolves?

**Ruling:** No, you cannot wait until resolution to remove the counters. Yes, the ability still resolves even if the planeswalker is put into the graveyard before it resolves.

**Why:** Removing loyalty counters is part of the cost to activate the ability, which is paid at activation, not at resolution [CR 606.4]. Once the ability is on the stack, it exists independently of its source, so destruction or removal of the planeswalker does not affect it [CR 113.7a].

Review: **correct**. Correctly states loyalty counters are paid at activation, that a planeswalker with zero loyalty is put into its owner’s graveyard, and that the activated ability still resolves independently of its source.
Reviewer: Codex

Missing reference groups: none

### m09-siege-protector / repetition 1

I control a Battle — Siege in a two-opponent game. As it enters, may I choose myself as its protector, or must I choose one of my opponents?

**Ruling:** You must choose one of your opponents as the Siege's protector. You cannot choose yourself.

**Why:** Rule 310.12a explicitly states that a Siege's controller "must choose its protector from among their opponents" and that "only an opponent of a Siege's controller can be its protector" [CR 310.12a]. This is a restriction on the general rule that a battle's controller chooses a player to be its protector [CR 310.9a].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m10-siege-last-counter / repetition 1

The last defense counter is removed from a Siege. Does it transform immediately as part of removing the counter, or does an ability trigger? What happens when that ability resolves?

**Ruling:** Removing the last defense counter from a Siege triggers its intrinsic ability; it does not transform immediately. When that ability resolves, the Siege is exiled, and then its controller may cast it transformed without paying its mana cost.

**Why:** The intrinsic ability is written as a triggered ability ("When the last defense counter is removed…"), so it triggers and goes on the stack like any other triggered ability [CR 310.12b] [CR 603.2] [CR 603.3]. Because the ability has triggered and is on the stack, the state-based action that would put a Siege with 0 defense into its owner's graveyard does not apply [CR 310.7]. Upon resolution, the Siege is exiled and the controller gets the option to cast it transformed for free [CR 310.12b].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m11-monarch-combat-trigger / repetition 1

A creature deals combat damage to the current monarch. Does its controller become the monarch immediately as damage is dealt, or only after a triggered ability resolves?

**Ruling:** The controller becomes the monarch when the triggered ability resolves, not immediately when the damage is dealt.

**Why:** The monarch rule is implemented as a triggered ability with the text "Whenever a creature deals combat damage to the monarch, its controller becomes the monarch" [CR 725.2]. Triggered abilities go on the stack and resolve as normal [CR 603.3], so the change of monarch occurs at resolution, not at the moment damage is dealt.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m12-monarch-draw-trigger / repetition 1

Alice is the monarch when her end step begins, so the monarch draw ability triggers. Before it resolves, an effect makes Bob the monarch. Does Alice’s already-triggered ability still make her draw a card?

Ruling: Yes, Alice still draws a card.

Why: The monarch draw ability is controlled by the player who was the monarch at the time it triggered, and its effect is "that player draws a card" — referring to the monarch at the moment of triggering, not at resolution. [CR 725.2] The ability is already on the stack with a fixed effect; a later change in who the monarch is does not alter what the ability does when it resolves.

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m13-initiative-multiple-damage / repetition 1

I have the initiative. During one combat damage event, two creatures controlled by Bob each deal combat damage to me. How many times does the damage ability trigger, and what happens if it resolves?

**Ruling:** The ability triggers once. When it resolves, Bob takes the initiative.

**Why:** The trigger condition is "whenever **one or more** creatures a player controls deal combat damage to the player who has the initiative" [CR 726.2]. This is a single trigger event that is satisfied regardless of how many creatures dealt the damage, so two creatures dealing damage in the same combat damage step produces only one trigger. When that ability resolves, its effect is that "the controller of those creatures takes the initiative" [CR 726.2].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m14-retake-initiative / repetition 1

I already have the initiative, and an effect instructs me to take the initiative. Do I get a second initiative designation, and does anything trigger?

**Ruling:** No, you do not get a second initiative designation. However, the inherent triggered ability "Whenever a player takes the initiative, that player ventures into Undercity" does trigger.

**Why:** Rule 726.5 explicitly states that if the player who currently has the initiative is instructed to take the initiative, it "does not create a second initiative designation" but "causes the last triggered ability in 726.2 to trigger." The last of the three inherent abilities listed in 726.2 is "Whenever a player takes the initiative, that player ventures into Undercity." [CR 726.5] [CR 726.2]

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m15-phased-out-token / repetition 1

A creature token with counters on it phases out. Does it leave the battlefield, cease to exist, or cause leaves/enters-the-battlefield abilities to trigger?

**Ruling:** The token does not leave the battlefield, does not cease to exist, and does not cause any leaves-the-battlefield or enters-the-battlefield abilities to trigger.

**Why:** The phasing event does not cause a permanent to change zones or control, and zone-change triggers do not trigger when a permanent phases in or out [CR 702.26d]. Tokens continue to exist on the battlefield while phased out, and counters remain on them [CR 702.26d]. A phased-out permanent is merely treated as though it does not exist for most game interactions [CR 702.26b], but it has not actually left the battlefield.

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

**Why:** Regeneration is a destruction-replacement effect that applies the next time the permanent would be destroyed that turn [CR 614.8]. When it applies, all damage marked on the creature is removed, its controller taps it, and if it's an attacking or blocking creature, it is removed from combat [CR 614.8]. The state-based action that would destroy it for lethal damage is the event that regeneration replaces [CR 704.5g].

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

**Ruling:** No, the land does not go on the stack, and your opponent cannot respond with an instant.

**Why:** Playing a land is a special action that doesn't use the stack; the player simply puts the land onto the battlefield [CR 305.1]. Since neither the land nor the action of playing it is a spell or ability, players can't respond to it with instants or activated abilities [CR 505.6b]. Special actions happen immediately [CR 405.6d].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

### m20-copy-not-cast / repetition 1

An effect copies a modal instant on the stack and says I may choose new targets for the copy. Does the copy count as being cast for “whenever you cast” abilities? Can I choose a different mode as well as new targets?

**Ruling:** No, the copy does not count as being cast, so "whenever you cast" abilities do not trigger. No, you cannot choose a different mode; the copy uses the same mode as the original, and you may only choose new targets.

**Why:** A copy of a spell is explicitly not cast [CR 707.10]. A copy acquires all decisions made for the original, including modes, and an effect that lets you choose new targets only permits changing targets, not modes [CR 707.10, CR 707.10c].

Review: **correct**. The answer satisfies each frozen case criterion and its cited rule passages support the relevant ruling.
Reviewer: Codex

Missing reference groups: none

