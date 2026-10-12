# atomic-sections-seed43

Status: **complete** · implementation commit `47ceb48a2f9f7767d5996143203256b85a9369f1`

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
| Reviewed fully correct | 20/20 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 9.95 s |
| p95 successful response | 14.81 s |
| Median first visible answer token | 8.59 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.19 |
| 02-hold-priority (r1) | 100.0% | correct | 8.25 |
| 03-illegal-target (r1) | 100.0% | correct | 7.53 |
| 04-partial-targets (r1) | 100.0% | correct | 9.97 |
| 05-trample-indestructible (r1) | 100.0% | correct | 14.81 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 9.47 |
| 07-zero-toughness (r1) | 100.0% | correct | 11.02 |
| 08-commander-dies (r1) | 100.0% | correct | 16.32 |
| 09-commander-tax (r1) | 100.0% | correct | 7.46 |
| 10-rest-in-peace (r1) | 75.0% | correct | 9.08 |
| 11-token-doublers (r1) | 100.0% | correct | 9.93 |
| 12-replacement-choice (r1) | 100.0% | correct | 12.56 |
| 13-apnap (r1) | 100.0% | correct | 10.67 |
| 14-humility-anthem (r1) | 100.0% | correct | 12.68 |
| 15-own-hexproof (r1) | 100.0% | correct | 7.35 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.69 |
| 17-token-blink (r1) | 100.0% | correct | 12.06 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 9.18 |
| 19-legend-response (r1) | 50.0% | correct | 10.48 |
| 20-clarify-interaction (r1) | 100.0% | correct | 7.99 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. Tapping a basic Forest for mana is an activated mana ability, which does not go on the stack and therefore cannot be targeted, countered, or otherwise responded to.

Why: A basic Forest's "Tap: Add one green mana" ability meets every criterion for an activated mana ability (no target, adds mana, not a loyalty ability, no library interaction) [CR 605.1a]. Because it is a mana ability, it resolves immediately after activation without using the stack, so no player ever gets priority to respond [CR 605.3b].

Review: **correct**. Correct activated mana ability, no stack, and immediate resolution under 605.1a and 605.3b.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again before your opponent. No, the instant does not resolve immediately; it waits on the stack until all players pass in succession.

Why: When you have priority and cast a spell, you are the first to receive priority again afterward [CR 117.3c]. The spell then sits on the stack, and it resolves only when every player passes in succession without taking an action in between [CR 405.5] [CR 117.4]. (Immediate resolution applies to mana abilities [CR 405.6c], not to instants.)

Review: **correct**. Correct caster receives priority again and resolution waits for all-player passing under 117.3c, 117.4, and 405.5.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No. If your creature is destroyed before Defiant Strike resolves, it is no longer a legal target, the spell doesn't resolve, and you do not draw a card.

Why: A target that has left the zone it was in when targeted is illegal [CR 608.2b]. Because Defiant Strike's only target is that creature, all of its targets are illegal, so the spell is removed from the stack without resolving and the "Draw a card" instruction is never carried out [CR 608.2b]. This is confirmed by the card-specific ruling: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correct no draw because the only target is illegal and the entire spell does not resolve; 608.2b and the card ruling support it.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The remaining legal creature takes 2 damage.

Why: Because not *all* targets are illegal, the spell resolves normally; only the target that left the battlefield is unaffected. [CR 608.2b] states that if all targets are illegal the spell doesn't resolve, but "otherwise, the spell or ability will resolve normally," and "illegal targets, if any, won't be affected" while "other parts of the effect for which those targets are not illegal may still affect them." The Plague Spores example in the same rule illustrates this exact pattern: one illegal target is skipped, the legal target is still affected.

Review: **correct**. Correct remaining legal target takes 2 damage; 608.2b permits resolution when some targets remain legal.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You must assign at least 2 damage to the 2/2 blocker (lethal damage for a creature with toughness 2), and you may assign the remaining 4 damage to the defending player.

Why: Trample requires that lethal damage be assigned to each blocker before excess damage may go to the player, and "lethal damage" is measured against the creature's toughness, not against whether the damage would actually destroy it [CR 702.19b]. Indestructible prevents destruction and the state-based action, but it does not alter the toughness-based lethal-damage threshold used for trample assignment [CR 702.12b]. The trample rule explicitly instructs you to ignore "abilities or effects that might change the amount of damage that's actually dealt" when checking for assigned lethal damage [CR 702.19b], so the blocker's indestructible is irrelevant to the assignment calculation.

Review: **correct**. Correct 2/4 assignment and distinction between lethal assignment and indestructibility preventing destruction. The lethal-damage discussion is read within the stated undamaged blocker scenario.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: The maximum damage you can assign to the defending player is **4**.

Why: Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for trample purposes [CR 702.2c]. Trample requires you to assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. Since 1 damage is nonzero, it satisfies the "lethal damage" threshold against the 8/8, leaving the remaining 4 of your 5 power to be assigned to the defending player.

Review: **correct**. Correct maximum 4; one nonzero assigned damage is lethal for trample via deathtouch under 702.2c.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No. The creature is put into its owner's graveyard.

Why: A creature with toughness 0 or less is put into its owner's graveyard by the state-based action in [CR 704.5f]. Indestructible prevents a permanent from being *destroyed* and specifically ignores the lethal-damage state-based action (rule 704.5g), as stated in [CR 702.12b], but it does not prevent the separate 704.5f action that applies when toughness is 0 or less. Since the -3/-3 reduces the 3/3 to 0/0, the 704.5f state-based action puts it into the graveyard regardless of indestructible.

Review: **correct**. Correct 0/0 goes to graveyard; distinguishes zero-toughness action 704.5f from lethal-damage destruction 704.5g.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes to both. You may put your commander into the command zone, and leaves-the-battlefield (death) triggers still fire.

Why: The commander's move to the command zone is a state-based action available whenever it is in the graveyard and was put there since the last SBA check [CR 903.9a]; it is not a replacement effect, so your "no replacement effects" condition doesn't block it. The permanent did in fact move from the battlefield to the graveyard, which is the event that generates leaves-the-battlefield triggers [CR 603.6c], and those triggers "look back in time" at the zone-change event rather than requiring the object to still be in the graveyard when they resolve [CR 603.10a]. The SBA to the command zone is checked after the triggers have already been generated, so the triggers go on the stack normally.

Review: **correct**. Correct optional command-zone state-based action after graveyard entry and dies triggers already generated. Does not put triggers on the stack before state-based actions or claim a targeted ability necessarily resolves.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.

Why: Rule 903.8 states the commander "costs an additional {2} for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice, so 2 × {2} = {4}. The cast from your hand does not count toward the tax, as the rule specifically tracks only casts *from the command zone* [CR 903.8].

Review: **correct**. Correct additional 4 and explicitly excludes the hand cast from 903.8 counting.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect changes that event so the card is exiled instead of being put into a graveyard [C1]. Because the creature is never put into a graveyard, it does not die, and Blood Artist's trigger condition ("whenever this creature or another creature dies") is never met [C5].

Review: **correct**. Correct exile replacement, no graveyard entry, and therefore no Blood Artist dies trigger.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4** tokens. The doublers do **not** loop forever.

Why: Each replacement effect gets only one opportunity to affect an event and does not re-trigger on the modified event [CR 614.5]. The two doublers therefore stack multiplicatively (2 × 2 = 4), exactly as the Doubling Season ruling confirms for multiple doublers on the battlefield [C2]. Doubling Season's "twice that many… instead" [C1] and Anointed Procession's identical text [C7] each apply once to the single token-creation event, yielding 1 → 2 → 4.

Review: **correct**. Correct four tokens and each replacement applies once to the event, with 614.5 and both Oracle texts supporting the explanation.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: The affected player (the one receiving the damage) chooses which replacement effect to apply first. Yes, the final damage can be either 7 or 8.

Why: Under [CR 616.1], when two or more replacement effects modify the same event, the affected player chooses one to apply; since neither is a self-replacement effect and neither modifies control, copy status, or face-up entry, the choice is unrestricted per [CR 616.1e]. Applying the double first yields 3 → 6 → 7 (then +1); applying the +1 first yields 3 → 4 → 8 (then double, per [CR 701.10g]). After the first effect is applied, the process repeats for the remaining effect per [CR 616.1f].

Review: **correct**. Correct affected-player choice and both arithmetic orders yielding 7 or 8; 616.1 and 616.1f support sequential application.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: Because it is Alice's turn, she is the active player, so in APNAP order Alice places her triggered ability on the stack before Bob does [CR 603.3b]. Each object placed on the stack goes on top of everything already there [CR 405.2], so Bob's ability ends up on top. When all players pass in succession, the top (last-added) object resolves [CR 405.5].

Review: **correct**. Correct Bob first through APNAP stacking and last-in-first-out resolution.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is a 2/2. It does not matter which enchantment entered the battlefield first.

Why: Humility's "have base power and toughness 1/1" is an effect that refers to base power and toughness, so it applies in layer 7b [CR 613.4b]. Glorious Anthem's "get +1/+1" is a modifying effect, so it applies in layer 7c [CR 613.4c]. Because 7b is applied before 7c, the creature's power and toughness are set to 1/1 first, then +1/+1 is added, yielding 2/2. Since the two effects fall in different sublayers, timestamp order (which enchantment entered first) is irrelevant [CR 613.4].

Review: **correct**. Correct 2/2 independent of timestamps because 7b setting precedes 7c modification.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own hexproof creature with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Because the restriction applies only to opponents' spells and abilities, your own Giant Growth [C1] is not blocked by hexproof. Since you have priority and can pay the cost, you may cast it and choose your hexproof creature as the target [CR 117.1a].

Review: **correct**. Correct own-creature targeting because hexproof restricts opponents only.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step the attacker assigns no combat damage at all, so the player takes 0 damage.

Why: The attacker is a *blocked* creature (it was declared as blocked), so rule 510.1c governs its damage assignment, not 510.1b (which applies only to unblocked creatures). Rule 510.1c explicitly states that a blocked creature "assigns no combat damage" if no creatures are currently blocking it, as is the case here after the blocker died in the first step. Trample would change this outcome (702.19d), but the attacker does not have trample, so that exception does not apply. [CR 510.1c] [CR 702.19d]

Review: **correct**. Correct no second-step damage: still blocked, no remaining blocker, no trample. Uses bracketed citations this time and does not invent first-step damage from the blocker.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No. Once the token is exiled it has left the battlefield, and it can't come back. The return effect fails; the token remains in exile and ceases to exist the next time state-based actions are checked.

Why: Rule 111.8 states that a token that has left the battlefield can't move to another zone or come back onto the battlefield, and if such a token would change zones it remains in its current zone instead. Because the exile occurs before the return within the same resolution, the token has already left the battlefield by the time the return is attempted, so the return has no legal effect. The token then ceases to exist as a state-based action under rule 111.7. [CR 111.8] [CR 111.7]

Review: **correct**. Correct no further zone change after exile under 111.8, followed by cessation at a later state-based check under 111.7.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You may activate "Sacrifice this creature: Draw a card" on the turn you cast the creature, as long as you have priority.

Why: Summoning sickness restricts only a creature's activated abilities that include the tap symbol ({T}) or the untap symbol ({Q}) in their activation cost, as well as the creature's ability to attack [CR 302.6]. A sacrifice cost is neither a tap nor an untap symbol, so the restriction does not apply. You may activate the ability any time you have priority [CR 117.1b].

Review: **correct**. Correct sacrifice activation with priority and absence of tap/untap-symbol restriction. No unsupported immediate-resolution or active-player claim.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant (or take any other action) in response to the legend rule. The legend rule is a state-based action performed automatically by the game, not a spell or ability on the stack, so no player ever receives priority to respond.

Why: State-based actions are dealt with before a player would receive priority [CR 117.2d] [CR 117.5]. They are performed automatically by the game rules without priority [CR 117.2]. The legend rule specifically instructs the controller to choose one legendary permanent and puts the rest into their owners' graveyards as part of that automatic check [CR 704.5j]; there is no intervening window in which a player could cast an instant or activate an ability.

Review: **correct**. Correct no response window; state-based actions precede priority and the legend-rule choice is part of the automatic action.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality is your creature's protection from (e.g., "protection from red," "protection from black," "protection from everything," "protection from [a player]")?
2. What is the removal spell (name or, at minimum, its color and whether it targets a creature)?

Review: **correct**. Correctly requests protection quality and the removal spell without offering an unsupported ruling. This is the expected clarification, not an abstention failure.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

