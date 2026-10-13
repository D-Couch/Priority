# adaptive-reasoning-seed43

Status: **complete** · implementation commit `dcf0868a618770f1ceb3a9974f64021cac05e47d`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [43]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 19/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 96.2% |
| Cases retrieving every expected evidence group | 18/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 19/20 reviewed |
| Reviewed accuracy | 95.0% |
| Mean reviewed rubric score | 97.5% |
| Median successful response | 4.18 s |
| p95 successful response | 11.31 s |
| Median first visible answer token | 2.80 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 3.50 |
| 02-hold-priority (r1) | 100.0% | correct | 3.64 |
| 03-illegal-target (r1) | 100.0% | correct | 3.62 |
| 04-partial-targets (r1) | 100.0% | correct | 4.03 |
| 05-trample-indestructible (r1) | 100.0% | correct | 11.31 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 8.24 |
| 07-zero-toughness (r1) | 100.0% | correct | 3.98 |
| 08-commander-dies (r1) | 100.0% | correct | 9.55 |
| 09-commander-tax (r1) | 100.0% | correct | 4.26 |
| 10-rest-in-peace (r1) | 75.0% | correct | 6.38 |
| 11-token-doublers (r1) | 100.0% | correct | 4.32 |
| 12-replacement-choice (r1) | 100.0% | correct | 7.32 |
| 13-apnap (r1) | 100.0% | correct | 8.80 |
| 14-humility-anthem (r1) | 100.0% | correct | 4.09 |
| 15-own-hexproof (r1) | 100.0% | correct | 3.38 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 11.63 |
| 17-token-blink (r1) | 100.0% | correct | 7.39 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 3.80 |
| 19-legend-response (r1) | 50.0% | partial | 3.98 |
| 20-clarify-interaction (r1) | 100.0% | correct | 3.30 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No, you cannot respond to your opponent tapping a basic Forest for mana.

Why: Activated mana abilities do not go on the stack, so they cannot be targeted, countered, or otherwise responded to [CR 605.3b]. Instead, they resolve immediately after they are activated [CR 605.3b].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you get priority again before your opponent, and no, the instant does not resolve immediately.

Why: When a spell resolves, the active player receives priority first [CR 117.3b]. A spell only resolves when all players pass in succession [CR 117.4], meaning your opponent has the opportunity to act before it resolves.

Review: **correct**. The direct ruling is correct, but CR 117.3b concerns priority after resolution, not the caster receiving priority after casting; the cited passage does not support this point.
Reviewer: Codex

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card.
Why: If the target creature is destroyed before Defiant Strike resolves, it is no longer a legal target, causing the spell to fail to resolve entirely. When a spell with an illegal target doesn't resolve, none of its effects, including the card draw, occur. [CR 608.2b] [C2]

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes, the remaining legal creature takes 2 damage.

Why: When a spell with multiple targets resolves, it checks if each target is still legal; if at least one target remains legal, the spell resolves normally [CR 608.2b]. The parts of the effect that apply to illegal targets do not happen, but the parts of the effect that apply to legal targets still occur [CR 608.2b]. Therefore, the spell deals 2 damage to the one creature that is still a legal target.

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Ruling:** Yes. You must assign at least 2 damage to the blocking creature (its toughness), and the remaining 4 may be assigned to the defending player.

**Why:** Trample requires you to assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. Indestructible prevents destruction by lethal damage but does not change the amount of damage that must be assigned [CR 702.12b]. The rule explicitly states that when checking for assigned lethal damage, you do not consider "abilities or effects that might change the amount of damage that's actually dealt" [CR 702.19b]—indestructible is such an ability, so it does not increase the required assignment beyond the blocker's toughness of 2.

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling:** You can assign a maximum of **4 damage** to the defending player.

**Why:** Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for the purpose of determining excess damage [CR 702.2c]. Trample requires that all blocking creatures be assigned lethal damage before excess damage may be assigned to the defending player [CR 702.19b]. Since 1 damage is sufficient to satisfy the "lethal damage" requirement against the 8/8 blocker, the remaining 4 damage (5 power − 1) may be assigned to the defending player.

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No, it does not survive; it is put into its owner’s graveyard.

Why: Indestructible prevents a permanent from being destroyed, but it does not prevent it from being put into the graveyard due to having toughness 0 or less [CR 702.12b]. State-based actions require that a creature with toughness 0 or less be put into its owner’s graveyard, and this event cannot be replaced by regeneration or indestructible [CR 704.5f].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling:** Yes, you may put your commander into the command zone, and "dies" triggers still fire.

**Why:** Rule 903.9a allows the owner to put a commander from the graveyard into the command zone as a state-based action, but this happens *after* the card is already in the graveyard—it does not replace the zone change. Since the card did move from the battlefield to the graveyard, it "died" [CR 700.4], and leaves-the-battlefield triggers (including "dies" triggers) still trigger [CR 603.6c].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.

Why: The commander tax is an additional cost of {2} for each previous time the player has cast the commander from the command zone [CR 903.8]. Since you have cast it from the command zone twice previously, the total additional cost is 2 × {2} = {4} [CR 903.8]. Casting the commander from your hand does not count toward this tax, as the rule specifically references casts from the command zone [CR 903.8].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**Ruling:** No, Blood Artist does not trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect exiles the creature instead of putting it into a graveyard, so the creature never dies and Blood Artist's trigger condition is never met [C2].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create four tokens. The doublers do not loop forever.

Why: Doubling Season and Anointed Procession are both replacement effects that apply to the event of creating a token, and they apply sequentially rather than recursively [CR 614.16]. When multiple such effects are present, the number of tokens is multiplied by each effect in sequence (2 x 2 = 4), as explicitly stated for multiple Anointed Processions and Doubling Seasons [C11] [C2]. A replacement effect does not invoke itself repeatedly; it gets only one opportunity to affect an event [CR 614.5].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** You (the affected player) choose which replacement effect applies first. The final damage can be either 7 or 8.

**Why:** When multiple replacement effects modify the same event, the affected player chooses the order [CR 616.1]. Any applicable effect may be chosen [CR 616.1e], and after one is applied, the process repeats with the remaining effects [CR 616.1f]. If you choose double first: 3 × 2 = 6, then +1 = 7. If you choose +1 first: 3 + 1 = 4, then × 2 = 8.

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Ruling:** Bob's triggered ability resolves first.

**Why:** When multiple triggered abilities are waiting to go on the stack, each player in APNAP order puts their abilities on the stack [CR 603.3b]. Since it's Alice's turn, she is the active player and goes first, placing her ability on the stack before Bob places his. Each new object is put on top of all objects already on the stack [CR 405.2], so Bob's ability ends up on top. When all players pass in succession, the top (last-added) ability resolves [CR 405.5].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is a 2/2. It does not matter which enchantment entered first.

Why: Humility sets the creature's power and toughness to 1/1 in layer 7b, while Glorious Anthem adds +1/+1 in layer 7c [C1], [C5], [CR 613.4b], [CR 613.4c]. Because these effects apply in different sublayers, the setting effect is applied first regardless of timestamp order, and the modifying effect is applied afterward [CR 613.4], [CR 613.7].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes, you may target your own creature with hexproof using Giant Growth.

Why: Hexproof only prevents a permanent from being targeted by spells or abilities controlled by your opponents [CR 702.11b]. Since you control the spell, the hexproof ability does not restrict your ability to choose that creature as a target [CR 702.11b].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**Ruling:** No. In the second combat damage step, your 3/3 assigns no combat damage at all.

**Why:** A blocked creature assigns its combat damage to the creatures blocking it, but if no creatures are currently blocking it (e.g., they were destroyed), it assigns no combat damage [CR 510.1c]. Trample is what would allow a blocked creature with no current blockers to assign its damage to the defending player [CR 702.19d], but your attacker does not have trample.

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Ruling:** No, the token does not return to the battlefield. It remains in exile and ceases to exist the next time state-based actions are checked.

**Why:** Once a token has left the battlefield, it can't move to another zone or come back onto the battlefield; if such a token would change zones, it remains in its current zone instead [CR 111.8]. This applies regardless of whether the return effect is part of the same resolution. The token then ceases to exist as a state-based action [CR 111.7].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes, you can activate it this turn.
Why: Summoning sickness only restricts activating abilities that include the tap or untap symbol in their activation cost [CR 302.6]. Since your ability’s cost is only “Sacrifice this creature” and lacks those symbols, the restriction does not apply [CR 602.5a]. You may activate the ability any time you have priority [CR 117.1b].

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No, you cannot cast an instant in response to the legend rule.

Why: State-based actions, including the legend rule, are performed automatically by the game rules without players receiving priority [CR 117.2d] [CR 704.5j]. Priority is only granted to players when they are able to take actions, such as casting spells, which does not occur during the automatic performance of state-based actions [CR 117.1] [CR 117.5].

Review: **partial**. Correctly says state-based actions occur before priority, but omits that the legend rule requires keeping one of the legendary permanents.
Reviewer: Codex

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:
1. What is the specific quality of the protection (e.g., "protection from red," "protection from black," "protection from everything")?
2. What is the name or color of the removal spell used?
3. Did the spell target your creature, or did it deal damage to it?

Review: **correct**. Reviewed against both frozen criteria and supplied rule/card excerpts; the answer is complete and supported.
Reviewer: Codex

Missing reference groups: none

