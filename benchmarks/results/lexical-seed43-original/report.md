# lexical-seed43-original

Status: **complete** · implementation commit `4144f33dff3bf84ea1a7c76d5c62e972cdf75542`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [43]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 20/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 96.2% |
| Cases retrieving every expected evidence group | 18/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 20/20 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 10.95 s |
| p95 successful response | 15.79 s |
| Median first visible answer token | 9.38 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.51 |
| 02-hold-priority (r1) | 100.0% | correct | 8.77 |
| 03-illegal-target (r1) | 100.0% | correct | 8.61 |
| 04-partial-targets (r1) | 100.0% | correct | 10.62 |
| 05-trample-indestructible (r1) | 100.0% | correct | 15.67 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 9.96 |
| 07-zero-toughness (r1) | 100.0% | correct | 11.61 |
| 08-commander-dies (r1) | 100.0% | correct | 17.58 |
| 09-commander-tax (r1) | 100.0% | correct | 7.57 |
| 10-rest-in-peace (r1) | 75.0% | correct | 8.13 |
| 11-token-doublers (r1) | 100.0% | correct | 15.79 |
| 12-replacement-choice (r1) | 100.0% | correct | 13.48 |
| 13-apnap (r1) | 100.0% | correct | 11.29 |
| 14-humility-anthem (r1) | 100.0% | correct | 12.04 |
| 15-own-hexproof (r1) | 100.0% | correct | 7.71 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 13.34 |
| 17-token-blink (r1) | 100.0% | correct | 13.57 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 10.32 |
| 19-legend-response (r1) | 50.0% | correct | 11.60 |
| 20-clarify-interaction (r1) | 100.0% | correct | 8.36 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. Tapping a basic Forest for mana is an activated mana ability, which does not go on the stack and therefore cannot be targeted, countered, or otherwise responded to.

Why: A basic Forest's "Tap: Add one green mana" ability meets every criterion for an activated mana ability (no target, adds mana, not a loyalty ability, no library interaction) [CR 605.1a]. Because it is a mana ability, it resolves immediately after activation without using the stack, so no player ever gets priority to respond [CR 605.3b].

Review: **correct**. Correct activated mana ability resolves immediately without the stack; supported by 605.3b/605.1a.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again before your opponent. No, the instant does not resolve immediately; it waits on the stack until all players pass in succession.

Why: When you have priority and cast a spell, you are the first to receive priority again afterward [CR 117.3c]. The spell then sits on the stack, and it resolves only when every player passes in succession without taking an action in between [CR 405.5] [CR 117.4]. (Immediate resolution applies to mana abilities [CR 405.6c], not to instants.)

Review: **correct**. Correct caster regains priority; all players must pass for resolution; cited priority and stack rules support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card. Defiant Strike fails to resolve entirely.

Why: Defiant Strike has a single target (the creature). If that creature is destroyed and leaves the battlefield before the spell resolves, it is no longer in the zone it was in when targeted, making it an illegal target [CR 608.2b]. Because all of the spell's targets are illegal, the spell doesn't resolve and is put into its owner's graveyard [CR 608.2b]. The "Draw a card" instruction is never carried out. This is confirmed by the card-specific ruling: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correct no draw when only target becomes illegal; 608.2b and card ruling directly support result.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The remaining legal creature takes 2 damage.

Why: Because not *all* targets are illegal, the spell resolves normally; only the target that left the battlefield is unaffected. [CR 608.2b] states that if all targets are illegal the spell doesn't resolve, but "otherwise, the spell or ability will resolve normally," and "illegal targets, if any, won't be affected" while "other parts of the effect for which those targets are not illegal may still affect them." The Plague Spores example in the same rule illustrates this exact pattern: one illegal target is skipped, the legal target is still affected.

Review: **correct**. Correct legal remaining target takes damage; 608.2b supports partial legality.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You must assign at least 2 damage to the 2/2 blocker (lethal damage for a creature with toughness 2), and you may assign the remaining 4 damage to the defending player.

Why: Trample requires that lethal damage be assigned to each blocker before excess damage may go to the player, and "lethal damage" is measured against the creature's toughness, not against whether the damage would actually destroy it [CR 702.19b]. Indestructible prevents destruction and the state-based action, but it does not alter the toughness-based lethal-damage threshold used for trample assignment [CR 702.12b]. The trample rule explicitly instructs you to ignore "abilities or effects that might change the amount of damage that's actually dealt" when checking for assigned lethal damage [CR 702.19b], so the blocker's indestructible is irrelevant to the assignment calculation.

Review: **correct**. Correct 2 to indestructible blocker and 4 to player; lethal assignment differs from destruction under trample/indestructible clauses.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: The maximum damage you can assign to the defending player is **4**.

Why: Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for trample purposes [CR 702.2c]. Trample requires you to assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. Since 1 damage is nonzero, it satisfies the "lethal damage" threshold against the 8/8, leaving the remaining 4 of your 5 power to be assigned to the defending player.

Review: **correct**. Correct assign 1 deathtouch damage and 4 trample damage; 702.2c and 702.19b support calculation.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No. The creature is put into its owner's graveyard.

Why: A creature with toughness 0 or less is put into its owner's graveyard by the state-based action in [CR 704.5f]. Indestructible prevents a permanent from being *destroyed* and specifically ignores the lethal-damage state-based action (rule 704.5g), as stated in [CR 702.12b], but it does not prevent the separate 704.5f action that applies when toughness is 0 or less. Since the -3/-3 reduces the 3/3 to 0/0, the 704.5f state-based action puts it into the graveyard regardless of indestructible.

Review: **correct**. Correct 0 toughness goes to graveyard despite indestructible, using separate 704.5f SBA.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes to both. You may put your commander into the command zone, and leaves-the-battlefield (death) triggers still fire.

Why: The commander's move to the command zone is a state-based action available whenever it is in the graveyard and was put there since the last SBA check [CR 903.9a]; it is not a replacement effect, so your "no replacement effects" condition doesn't block it. The permanent did in fact move from the battlefield to the graveyard, which is the event that generates leaves-the-battlefield triggers [CR 603.6c], and those triggers "look back in time" at the zone-change event rather than requiring the object to still be in the graveyard when they resolve [CR 603.10a]. The SBA to the command zone is checked after the triggers have already been generated, so the triggers go on the stack normally.

Review: **correct**. Correct commander enters graveyard and dies triggers occur before optional command-zone SBA; 903.9a and leaves-battlefield rules support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.

Why: Rule 903.8 states the commander "costs an additional {2} for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice, so 2 × {2} = {4}. The cast from your hand does not count toward the tax, as the rule specifically tracks only casts *from the command zone* [CR 903.8].

Review: **correct**. Correct additional tax of four from two prior command-zone casts; hand cast excluded under 903.8.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger when the other creature is destroyed.

Why: "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's static ability replaces that zone change, exiling the creature instead [C1]. Because the creature is never actually put into a graveyard, the trigger condition "a creature dies" is never met, so Blood Artist's ability does not trigger [C2].

Review: **correct**. Correct no Blood Artist dies trigger under Rest in Peace; Oracle/ruling and dies definition support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4** tokens (1 × 2 × 2). The doublers do **not** loop forever.

Why: Doubling Season and Anointed Procession each apply a "twice as many" replacement effect to the same token-creation event, and they stack multiplicatively—exactly as the rulings confirm for multiple copies of either card (two Anointed Processions → 4×; two Doubling Seasons → 4×) [C11][C2]. A replacement effect gets only one opportunity to affect an event and does not invoke itself repeatedly, so the multiplication terminates after both effects have been applied [CR 614.5].

Review: **correct**. Correct four tokens and no loop, with one application of each replacement under 614.5.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: The affected player (the one receiving the damage) chooses which replacement effect to apply first. Yes, the final damage can be either 7 or 8.

Why: Under [CR 616.1], when two or more replacement effects modify the same event, the affected player chooses one to apply; since neither is a self-replacement effect and neither modifies control, copy status, or face-up entry, the choice is unrestricted per [CR 616.1e]. Applying the double first yields 3 → 6 → 7 (then +1); applying the +1 first yields 3 → 4 → 8 (then double, per [CR 701.10g]). After the first effect is applied, the process repeats for the remaining effect per [CR 616.1f].

Review: **correct**. Correct affected player chooses, producing 7 or 8 depending on order, with replacement ordering citations.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: Because it is Alice's turn, she is the active player, so in APNAP order Alice places her triggered ability on the stack before Bob does [CR 603.3b]. Each object placed on the stack goes on top of everything already there [CR 405.2], so Bob's ability ends up on top. When all players pass in succession, the top (last-added) object resolves [CR 405.5].

Review: **correct**. Correct Bob resolves first under APNAP stacking and last-in-first-out resolution.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is 2/2. It does not matter which enchantment entered the battlefield first.

Why: Humility's "have base power and toughness 1/1" is a setting effect applied in layer 7b [CR 613.4b], while Glorious Anthem's "+1/+1" is a modifying effect applied in layer 7c [CR 613.4c]. Because they fall in different sublayers, the set effect always applies before the modify effect regardless of timestamp [CR 613.4], so the creature is 1/1 + 1/+1 = 2/2 in either order.

Review: **correct**. Correct 2/2 independent of timestamp; base-setting sublayer precedes modification.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own hexproof creature with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Because the restriction applies only to opponents' spells and abilities, your own Giant Growth [C1] is not blocked by hexproof. Since you have priority and can pay the cost, you may cast it and choose your hexproof creature as the target [CR 117.1a].

Review: **correct**. Correct own Giant Growth allowed; hexproof only restricts opponents.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step the attacker assigns no combat damage at all, so the player takes 0 damage.

Why: The attacker is a *blocked* creature (it was declared as blocked), so rule 510.1c governs its damage assignment, not 510.1b (which applies only to unblocked creatures). Rule 510.1c explicitly states that a blocked creature "assigns no combat damage" if no creatures are currently blocking it, as is the case here after the blocker died in the first step. Trample would change this outcome (702.19d), but the attacker does not have trample, so that exception does not apply. [CR 510.1c] [CR 702.19d]

Review: **correct**. Correct no second-step damage to player; remains blocked without trample. Bare rule references are supplied and now link in UI.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No. Once the token is exiled it has left the battlefield, and it can't come back. The return effect fails; the token remains in exile and ceases to exist the next time state-based actions are checked.

Why: Rule 111.8 states that a token that has left the battlefield can't move to another zone or come back onto the battlefield, and if such a token would change zones it remains in its current zone instead. Because the exile occurs before the return within the same resolution, the token has already left the battlefield by the time the return is attempted, so the return has no legal effect. The token then ceases to exist as a state-based action under rule 111.7. [CR 111.8] [CR 111.7]

Review: **correct**. Correct token cannot change zones again during resolution and only later ceases to exist; 111.8/111.7 distinguish mechanisms.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You may activate "Sacrifice this creature: Draw a card" on the turn you cast the creature, as long as you have priority.

Why: Summoning sickness restricts only a creature's activated abilities that include the tap symbol ({T}) or the untap symbol ({Q}) in their activation cost, as well as the creature's ability to attack [CR 302.6]. A sacrifice cost is neither a tap nor an untap symbol, so the restriction does not apply. You may activate the ability any time you have priority [CR 117.1b].

Review: **correct**. Correct sacrifice ability usable without tap/untap symbols; rule 302.6 accurately paraphrased and 117.1b supports activation timing.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant (or take any other action) in response to the legend rule. The legend rule is a state-based action performed automatically by the game, not a spell or ability on the stack, so no player ever receives priority to respond.

Why: State-based actions are dealt with before a player would receive priority [CR 117.2d] [CR 117.5]. They are performed automatically by the game rules without priority [CR 117.2]. The legend rule specifically instructs the controller to choose one legendary permanent and puts the rest into their owners' graveyards as part of that automatic check [CR 704.5j]; there is no intervening window in which a player could cast an instant or activate an ability.

Review: **correct**. Correct no response before legend-rule SBA; chooses one before priority under 117.2d/117.5 and 704.5j.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality is your creature's protection from (e.g., "protection from red," "protection from black," "protection from everything," "protection from [a player]")?
2. What is the removal spell (name or, at minimum, its color and whether it targets a creature)?

Review: **correct**. Correct clarification asks protection quality and removal spell details without unconditional answer.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

