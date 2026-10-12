# source-quotes-original

Status: **complete** · implementation commit `6f31339abfd5340942dfa993252f48d1e50e7f60`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 20/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 96.2% |
| Cases retrieving every expected evidence group | 18/20 |
| Answers with citations | 18/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 20/20 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 9.92 s |
| p95 successful response | 15.98 s |
| Median first visible answer token | 8.55 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.30 |
| 02-hold-priority (r1) | 100.0% | correct | 8.42 |
| 03-illegal-target (r1) | 100.0% | correct | 8.75 |
| 04-partial-targets (r1) | 100.0% | correct | 9.39 |
| 05-trample-indestructible (r1) | 100.0% | correct | 15.79 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.27 |
| 07-zero-toughness (r1) | 100.0% | correct | 13.19 |
| 08-commander-dies (r1) | 100.0% | correct | 16.68 |
| 09-commander-tax (r1) | 100.0% | correct | 8.08 |
| 10-rest-in-peace (r1) | 75.0% | correct | 9.57 |
| 11-token-doublers (r1) | 100.0% | correct | 15.98 |
| 12-replacement-choice (r1) | 100.0% | correct | 11.17 |
| 13-apnap (r1) | 100.0% | correct | 10.53 |
| 14-humility-anthem (r1) | 100.0% | correct | 13.72 |
| 15-own-hexproof (r1) | 100.0% | correct | 6.79 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 11.33 |
| 17-token-blink (r1) | 100.0% | correct | 7.95 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 9.43 |
| 19-legend-response (r1) | 50.0% | correct | 10.88 |
| 20-clarify-interaction (r1) | 100.0% | correct | 6.83 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. Tapping a basic Forest for mana is an activated mana ability, and mana abilities don't go on the stack, so they can't be targeted, countered, or otherwise responded to.

Why: [CR 605.3b] states, "An activated mana ability doesn't go on the stack, so it can't be targeted, countered, or otherwise responded to. Rather, it resolves immediately after it is activated." A basic Forest's tap-for-mana ability meets the criteria in [CR 605.1a] (no target, adds mana, not a loyalty ability, no library interaction), making it a mana ability that resolves immediately without passing through the stack.

Review: **correct**. Correct; 605.3b applies and 605.1a confirms Forest ability is a mana ability.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again before your opponent. No, the instant does not resolve immediately; it sits on the stack and resolves only after all players pass in succession.

Why: "If a player has priority when they cast a spell, activate an ability, or take a special action, that player receives priority afterward." [CR 117.3c] This means you get the first chance to respond to your own instant. However, resolution is not automatic: "When all players pass in succession, the top (last-added) spell or ability on the stack resolves." [CR 405.5] Your opponent still gets a window to respond before the instant resolves.

Review: **correct**. Correct priority and pass sequence; cited rules support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card. Defiant Strike does not resolve at all.

Why: [CR 608.2b] states, "A target that's no longer in the zone it was in when it was targeted is illegal" and "If all its targets, for every instance of the word 'target,' are now illegal, the spell or ability doesn't resolve." Because the creature was destroyed and left the battlefield, it is no longer a legal target. Since Defiant Strike has only that one target, the entire spell fails to resolve, so neither the +1/+0 nor the "Draw a card" instruction occurs. This is confirmed by the card-specific ruling: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correct all-target-illegal result; 608.2b and Defiant Strike ruling support no draw.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The remaining legal creature takes 2 damage.

Why: Because not *all* targets are illegal, the spell resolves normally. [CR 608.2b] states: "Otherwise, the spell or ability will resolve normally. Illegal targets, if any, won't be affected by parts of a resolving spell's effect for which they're illegal. Other parts of the effect for which those targets are not illegal may still affect them." The creature that left the battlefield is an illegal target and is skipped; the creature still on the battlefield is a legal target and is dealt 2 damage.

Review: **correct**. Correct partial-target resolution; surviving legal target takes damage.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You must assign at least 2 damage to the 2/2 blocker (lethal damage based on its toughness) and may assign the remaining 4 to the defending player. The blocker's indestructible does not change the trample assignment requirement.

Why: [CR 702.19b] requires that "Once all those blocking creatures are assigned lethal damage, any excess damage is assigned as its controller chooses among those blocking creatures and the player." The blocker's toughness is 2, so 2 damage satisfies the lethal-damage threshold for assignment purposes. [CR 702.12b] states that an indestructible permanent "isn't destroyed by lethal damage" and "ignore[s] the state-based action that checks for lethal damage," meaning the blocker survives the damage, but it does not alter what counts as lethal damage for the trample assignment check. The trample rule governs how much must be *assigned*; indestructible governs whether the creature is *destroyed* after damage is dealt. These are separate steps.

Review: **correct**. Correct trample assignment and indestructible distinction under cited rules.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: The maximum damage you can assign to the defending player is **4**.

Why: Under trample, you must assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. Because your attacker has deathtouch, "any nonzero amount of combat damage assigned to a creature by a source with deathtouch is considered to be lethal damage for the purposes of determining if excess damage is being dealt" [CR 702.2c]. Therefore, assigning just 1 damage to the 8/8 satisfies the lethal-damage requirement, and the remaining 5 − 1 = 4 damage may be assigned to the defending player.

Review: **correct**. Correct one deathtouch damage is lethal for trample assignment; gives remaining four to player.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No. The creature is put into its owner's graveyard. Indestructible does not save it.

Why: [CR 704.5f] states, "If a creature has toughness 0 or less, it's put into its owner's graveyard." This is a state-based action that moves the permanent to the graveyard; it is not a destruction event. [CR 702.12b] protects only against destruction and specifically says the permanent "ignore[s] the state-based action that checks for lethal damage (see rule 704.5g)"—it references 704.5g, not 704.5f. Since the -3/-3 makes the creature's toughness 0, the 704.5f state-based action applies and the creature goes to the graveyard regardless of indestructible.

Review: **correct**. Correct toughness 0 SBA is separate from destruction prevented by indestructible.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes to both. You may put your commander into the command zone, and "dies" (leaves-the-battlefield) triggers still fire.

Why:

**Moving to the command zone:** [CR 903.9a] states, "If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action." The commander is already in the graveyard; the state-based action then lets you move it out. This is not a replacement effect, so your "no replacement effects apply" condition is satisfied.

**"Dies" triggers:** [CR 603.6c] states, "Leaves-the-battlefield abilities trigger when a permanent moves from the battlefield to another zone." The destruction event moved the permanent from the battlefield to the graveyard; that zone change already occurred before the state-based action in 903.9a is checked. [CR 603.10a] confirms these are zone-change triggers that "look back in time," so the trigger is generated at the moment of the zone change regardless of where the card subsequently ends up.

Review: **correct**. Correct dies trigger occurs before subsequent commander-zone SBA; 903.9a, 603.6c, 603.10a support sequence.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.

Why: Rule 903.8 states the commander "costs an additional {2} for each previous time the player casting it has cast it from the command zone that game." You have previously cast it from the command zone twice, so the tax is 2 × {2} = {4}. The cast from your hand does not count, because the rule specifically references times it was cast *from the command zone*. [CR 903.8]

Review: **correct**. Correct four additional mana from two prior command-zone casts; hand cast excluded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger.

Why: [CR 700.4] defines "dies" as "is put into a graveyard from the battlefield." Rest in Peace's static ability states, "If a card or token would be put into a graveyard from anywhere, exile it instead" [C1]. Because the replacement effect diverts the creature to exile, the event "is put into a graveyard from the battlefield" never occurs, so the creature does not die and Blood Artist's trigger condition ("Whenever this creature or another creature dies" [C5]) is never met.

Review: **correct**. Correct Rest in Peace prevents dies trigger; dies definition, Oracle and card ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

**Ruling:** You create **4** tokens. No, the doublers do not loop forever.

**Why:** Each doubler is a replacement effect that applies only once to the event. [CR 614.5] states: "A replacement effect doesn't invoke itself repeatedly; it gets only one opportunity to affect an event or any modified events that may replace that event." Meanwhile, [CR 614.16] confirms these token-doubling replacement effects "also apply if another replacement or prevention effect does so," so the second doubler can act on the already-modified count. The sequence is therefore 1 → 2 (first doubler) → 4 (second doubler), and the process stops because neither effect gets a second opportunity. This matches the supplied rulings for two identical doublers: "the number of tokens or counters is four times the original number" [C2] and "the number of tokens created is four times the original number" [C11].

Review: **correct**. Correct four tokens; each replacement has one opportunity, with 614.16 and two card rulings supporting sequence.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** You (the affected player) choose the order. The final damage can be 7 (double first, then +1: 3→6→7) or 8 (+1 first, then double: 3→4→8).

**Why:** Because neither effect is a self-replacement, modifies control, creates a copy, or involves a back face, the choice falls to the general rule: "the affected object's controller (or its owner if it has no controller) or the affected player chooses one to apply" [CR 616.1], and at that stage "Any of the applicable replacement and/or prevention effects may be chosen" [CR 616.1e]. After the first is applied, "this process is repeated (taking into account only replacement or prevention effects that would now be applicable) until there are no more left to apply" [CR 616.1f]. Doubling is defined as "that source instead deals twice that much damage" [CR 701.10g], so the arithmetic is simply 3×2+1 = 7 or (3+1)×2 = 8.

Review: **correct**. Correct affected player choice and arithmetic 7 or 8; 616.1/616.1e/f and 701.10g support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: Under [CR 603.3b], in the first part of the process "each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn't another ability triggering on the stack." Alice (active player) places hers first, then Bob places his. Because "each time an object is put on the stack, it's put on top of all objects already there" [CR 405.2], Bob's ability ends up on top. When all players pass, "the top (last-added) spell or ability on the stack resolves" [CR 405.5], so Bob's ability resolves before Alice's.

Review: **correct**. Correct APNAP order and Bob resolves first; 603.3b, stack rule and resolution rule support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

**Ruling:** The creature is 2/2. It does not matter which enchantment entered the battlefield first.

**Why:** Humility's "have base power and toughness 1/1" is a power/toughness-setting effect that applies in layer 7b [CR 613.4b]. Glorious Anthem's "get +1/+1" is a power/toughness-modifying effect that applies in layer 7c [CR 613.4c]. Because the two effects land in different sublayers, they are applied in the fixed sublayer order (7b before 7c) regardless of timestamp [CR 613.4]. The result is always 1/1 (Humility) + 1/+1 (Glorious Anthem) = 2/2.

Review: **correct**. Correct layer 7b before 7c regardless of timestamp; 613.4 supports result.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own hexproof creature with your own Giant Growth.

Why: Hexproof on a permanent means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. The restriction applies only to opponents' spells and abilities; it does not prevent you from targeting your own creature with a spell you control. Giant Growth simply reads "Target creature gets +3/+3 until end of turn" [C1], with no additional targeting restriction. Since you have priority and can pay the cost, you may cast it and choose your hexproof creature as the target.

Review: **correct**. Correct own hexproof does not prevent own Giant Growth targeting.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step your 3/3 assigns no combat damage at all.

Why: The blocker is dead, so it is no longer on the battlefield blocking. Rule 510.1c states: "If no creatures are currently blocking it (if, for example, they were destroyed or removed from combat), it assigns no combat damage." [CR 510.1c] Because the creature is no longer blocked, it cannot assign damage to the player. Trample would change this (702.19d allows damage to the player when no blockers remain), but your attacker does not have trample. [CR 702.19d]

Review: **correct**. Correct blocked attacker without trample assigns no second-step damage; 510.1c and trample exception support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No, the token does not return to the battlefield. Once the token was exiled (left the battlefield), it can't come back. It remains in exile and ceases to exist the next time state-based actions are checked.

Why: [CR 111.8] states, "A token that has left the battlefield can't move to another zone or come back onto the battlefield. If such a token would change zones, it remains in its current zone instead. It ceases to exist the next time state-based actions are checked." Since the token was exiled before the return instruction would apply, the return is a no-op; the token stays in exile and is removed from the game as a state-based action per [CR 111.7].

Review: **correct**. Correct token cannot return after leaving battlefield; 111.8/111.7 support timing and cease-to-exist result.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You may activate "Sacrifice this creature: Draw a card" on the turn you cast the creature, as long as you have priority. Summoning sickness does not restrict this ability.

Why: The restriction is limited to abilities whose activation cost includes the tap or untap symbol. Rule 302.6 states the restriction applies to "A creature's activated ability with the tap symbol or the untap symbol in its activation cost," and rule 602.5a repeats this: "A creature's activated ability with the tap symbol ({T}) or the untap symbol ({Q}) in its activation cost can't be activated unless the creature has been under its controller's control since the start of their most recent turn." [CR 302.6] [CR 602.5a] Since your ability's cost is "Sacrifice this creature" and contains neither {T} nor {Q}, the restriction never applies. You simply need priority to activate it, which you have per [CR 117.1b]: "A player may activate an activated ability any time they have priority."

Review: **correct**. Correct sacrifice ability is not restricted by summoning sickness without tap/untap symbol; 302.6/602.5a/117.1b support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant in response to the legend rule. The choice of which legendary permanent to keep is made as part of a state-based action, and no player has priority at that point.

Why: Rule 704.5j makes the legend rule a state-based action: "that player chooses one of them, and the rest are put into their owners' graveyards." Rule 117.2d states that "State-based actions happen automatically when certain conditions are met… They're dealt with before a player would receive priority." Rule 117.5 confirms the sequence: "Each time a player would get priority, the game first performs all applicable state-based actions as a single event… then repeats this process until no state-based actions are performed." Because the SBA (including your choice) is resolved before anyone receives priority, there is no window in which you could cast an instant or activate a non-mana ability.

Review: **correct**. Correct no response before legend-rule SBA and one must be kept; 704.5j/117.2d/117.5 support timing.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality is your creature's protection from (e.g., "protection from red," "protection from black," "protection from a specific player," "protection from everything")?
2. What is the removal spell? (Card name, or at minimum: does it target a creature, is it an Aura, does it deal damage, and what color(s) does it have?)

Review: **correct**. Appropriate clarification asks protection quality and removal details, with no unconditional answer.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

