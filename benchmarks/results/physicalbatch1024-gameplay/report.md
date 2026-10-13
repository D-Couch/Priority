# physicalbatch1024-gameplay

Status: **complete** · implementation commit `afac0771aedba06591bf09027417a72c767fa690`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

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
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 19/20 reviewed |
| Reviewed accuracy | 95.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 7.43 s |
| p95 successful response | 12.59 s |
| Median first visible answer token | 6.19 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 3.92 |
| 02-hold-priority (r1) | 100.0% | correct | 6.34 |
| 03-illegal-target (r1) | 100.0% | correct | 6.28 |
| 04-partial-targets (r1) | 100.0% | correct | 5.68 |
| 05-trample-indestructible (r1) | 100.0% | correct | 10.65 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 7.68 |
| 07-zero-toughness (r1) | 100.0% | incorrect | 12.59 |
| 08-commander-dies (r1) | 100.0% | correct | 13.47 |
| 09-commander-tax (r1) | 100.0% | correct | 7.74 |
| 10-rest-in-peace (r1) | 75.0% | correct | 5.69 |
| 11-token-doublers (r1) | 100.0% | correct | 8.25 |
| 12-replacement-choice (r1) | 100.0% | correct | 7.34 |
| 13-apnap (r1) | 100.0% | correct | 7.52 |
| 14-humility-anthem (r1) | 100.0% | correct | 11.64 |
| 15-own-hexproof (r1) | 100.0% | correct | 5.38 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 10.10 |
| 17-token-blink (r1) | 100.0% | correct | 7.19 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 6.31 |
| 19-legend-response (r1) | 50.0% | correct | 7.70 |
| 20-clarify-interaction (r1) | 100.0% | correct | 5.72 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**Ruling:** No. You cannot respond to your opponent tapping a basic Forest for mana.

**Why:** An activated mana ability doesn't go on the stack, so it can't be targeted, countered, or otherwise responded to; it resolves immediately after it is activated [CR 605.3b]. A basic Forest's tap-for-mana ability qualifies as a mana ability because it doesn't require a target, could add mana to a player's mana pool, isn't a loyalty ability, and doesn't move cards to or from a library [CR 605.1a].

Review: **correct**. Correct ruling; the expanded explanation accurately defines a mana ability and cites supplied rules.
Reviewer: Codex

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

**Ruling:** Yes, you get priority first after casting the instant. No, it does not resolve immediately—it resolves only after all players pass in succession.

**Why:** When you have priority and cast a spell, you receive priority again afterward [CR 117.3c]. The spell sits on the stack and resolves only when all players pass in succession without taking any actions in between [CR 117.4] [CR 405.5].

Review: **correct**. Correct priority timing and all-players-pass resolution condition.
Reviewer: Codex

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**Ruling:** No, you do not draw a card.

**Why:** When Defiant Strike tries to resolve, the target creature is no longer on the battlefield, making it an illegal target. Since all of Defiant Strike's targets are illegal, the spell doesn't resolve at all and is put into its owner's graveyard, so neither the +1/+0 nor the card draw occurs. [C2] [CR 608.2b]

Review: **correct**. Correct: all targets are illegal, so Defiant Strike does not resolve and no card is drawn.
Reviewer: Codex

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes, the remaining creature takes 2 damage.

Why: Since not all targets are illegal, the spell resolves normally. The illegal target simply isn't affected, while the legal target is. [CR 608.2b]

Review: **correct**. Correct: with one legal target the spell resolves and affects that target.
Reviewer: Codex

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Ruling:** Yes. You must assign at least 2 damage to the 2/2 blocker, and you may assign the remaining 4 to the defending player.

**Why:** Trample requires that lethal damage be assigned to blocking creatures before excess damage may be assigned to the player [CR 702.19b]. "Lethal damage" here means damage equal to the creature's toughness (2 in this case), and the rule explicitly states that the check does not consider "any abilities or effects that might change the amount of damage that's actually dealt" [CR 702.19b]. Indestructible does not alter damage assignment—it only means the creature won't be destroyed by the damage it receives [CR 702.12b]. So you assign 2 to the blocker (satisfying the trample requirement) and 4 to the player.

Review: **correct**. Correct assignment and explanation: indestructible does not increase lethal damage required for trample.
Reviewer: Codex

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling:** You can assign a maximum of 4 damage to the defending player.

**Why:** Under trample, you must assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. However, deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for this purpose [CR 702.2c]. So you assign 1 damage to the 8/8 blocker (satisfying the lethal-damage requirement) and the remaining 4 damage to the defending player.

Review: **correct**. Correct: one damage is lethal for trample assignment due to deathtouch, leaving four for the player.
Reviewer: Codex

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**Ruling:** Yes, it survives. The creature becomes a 0/0, but because it has indestructible, it ignores the state-based action that would put it into its owner's graveyard for having toughness 0 or less.

**Why:** A creature with toughness 0 or less is normally put into its owner's graveyard as a state-based action [CR 704.5f]. However, indestructible permanents "aren't destroyed by lethal damage, and they ignore the state-based action that checks for lethal damage" [CR 702.12b]. So the 0/0 indestructible creature remains on the battlefield.

Review: **incorrect**. Incorrect. Indestructible does not stop the zero-toughness state-based action; the creature is put into its owner’s graveyard. Both criteria fail.
Reviewer: Codex

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling:** Yes, you may put your commander into the command zone, and yes, abilities that trigger when it dies still trigger.

**Why:** The commander is actually put into the graveyard from the battlefield, which satisfies the definition of "dies" [CR 700.4]. The option to move it to the command zone is a state-based action that occurs *after* it is already in the graveyard [CR 903.9a], so the death event has already happened and any triggered abilities have already triggered.

Review: **correct**. Correct: the commander first reaches the graveyard, satisfying dies, and may then be moved to the command zone.
Reviewer: Codex

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is {4}.

**Why:** Rule 903.8 states the additional cost is {2} "for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice, so the additional cost is 2 × {2} = {4}. The cast from your hand does not count, as the rule specifically references casts *from the command zone*. [CR 903.8]

Review: **correct**. Correct: only the two prior casts from the command zone count, for {4}.
Reviewer: Codex

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No, Blood Artist does not trigger.

Why: "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exile, so the creature is never put into a graveyard [C1]. Since the trigger condition is never met, Blood Artist's ability does not trigger [C2].

Review: **correct**. Correct: Rest in Peace replaces the graveyard event with exile, so Blood Artist does not trigger.
Reviewer: Codex

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

**Ruling:** You create 4 tokens. The doublers do not loop forever.

**Why:** Each replacement effect gets only one opportunity to affect an event or any modified events that may replace that event [CR 614.5]. With two doublers, the original count of 1 is doubled by each one in sequence, yielding 4 (2 × 2 = 4), consistent with the pattern that two doublers produce four times the original number [C2][C11].

Review: **correct**. Correct: two replacement effects yield four tokens without looping; cited rulings support the result.
Reviewer: Codex

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** You (the affected player) choose which replacement effect to apply first. The final damage can be either 7 or 8.

**Why:** When multiple replacement effects modify the same event, the affected player chooses the order [CR 616.1]. Once the first effect is applied, the process repeats with the remaining effect [CR 616.1f]. Doubling first gives 3 × 2 = 6, then +1 = 7; increasing first gives 3 + 1 = 4, then × 2 = 8. Doubling damage is a replacement effect [CR 701.10g].

Review: **correct**. Correct affected-player choice and both damage-order calculations.
Reviewer: Codex

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: In APNAP order, the active player (Alice) puts her triggered ability on the stack first, then Bob puts his on top [CR 603.3b]. Each new object is placed on top of all objects already on the stack [CR 405.2], so Bob's ability is the topmost object and resolves first when all players pass [CR 405.5].

Review: **correct**. Correct: Alice puts her trigger on first, Bob on top, so Bob resolves first.
Reviewer: Codex

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

**Ruling:** The creature is 2/2. It does not matter which enchantment entered first.

**Why:** Humility's "have base power and toughness 1/1" is a power/toughness-setting effect that applies in layer 7b [CR 613.4b]. Glorious Anthem's "+1/+1" is a power/toughness-modifying effect that applies in layer 7c [CR 613.4c]. Since 7b always precedes 7c regardless of timestamp, the result is 1/1 + 1/+1 = 2/2 [CR 613.4].

Review: **correct**. Correct layer ordering gives 2/2 regardless of timestamp.
Reviewer: Codex

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Ruling:** Yes. You may target your own creature with hexproof using your own Giant Growth.

**Why:** Hexproof on a permanent means it "can't be the target of spells or abilities your opponents control" [CR 702.11b]. Since you control both the creature and the Giant Growth, the hexproof restriction does not apply to your own spell.

Review: **correct**. Correct: hexproof restricts opponents, not the controller.
Reviewer: Codex

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**Ruling:** No. In the second combat damage step, your 3/3 assigns no combat damage at all.

**Why:** A blocked creature assigns its combat damage to the creatures blocking it; if no creatures are currently blocking it (e.g., they were destroyed), it assigns no combat damage [CR 510.1c]. Double strike lets it deal damage in both steps [CR 702.4b], but without trample there is no rule that redirects its damage to the player once the blocker is gone. Trample specifically provides that exception [CR 702.19d], which your attacker lacks.

Review: **correct**. Correct: the attacker remains blocked with no blocker and has no trample, so it assigns no player damage.
Reviewer: Codex

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Ruling:** No, the token does not return to the battlefield. It remains in exile and ceases to exist the next time state-based actions are checked.

**Why:** Once a token leaves the battlefield, it can't move to another zone or come back onto the battlefield; if such a token would change zones, it remains in its current zone instead [CR 111.8]. It then ceases to exist the next time state-based actions are checked [CR 111.8]. This is a general rule about tokens, not a replacement effect, so the absence of replacement effects doesn't change the outcome.

Review: **correct**. Correct: a token that left the battlefield cannot return and ceases to exist at the next state-based-action check.
Reviewer: Codex

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

**Ruling:** Yes. You can activate that ability this turn even though the creature is under your control for the first time.

**Why:** The summoning sickness restriction applies only to a creature's activated abilities that include the tap symbol ({T}) or the untap symbol ({Q}) in their activation cost [CR 302.6] [CR 602.5a]. Your ability's cost is "Sacrifice this creature," which contains neither symbol, so the restriction does not apply.

Review: **correct**. Correct: sacrificing the creature does not invoke the tap/untap summoning-sickness restriction.
Reviewer: Codex

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

**Ruling:** No. You cannot cast an instant in response to the legend rule. The choice of which legendary permanent to keep is made as part of the state-based action itself, and no player receives priority during that process.

**Why:** State-based actions are performed automatically before a player would receive priority [CR 117.2d][CR 117.5]. The legend rule is a state-based action that requires the player to choose one permanent to keep [CR 704.5j]. Since no one has priority at that point, no one can cast an instant or activate an ability in response [CR 117.1].

Review: **correct**. Correct: the legend state-based action happens before priority, so there is no response window.
Reviewer: Codex

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality is your creature's protection from (e.g., "protection from red," "protection from black," "protection from a specific player")?
2. What is the removal spell (name or text)? Specifically, does it target your creature, and what color is it?

Review: **correct**. Correct clarification request asks for protection quality and removal details before ruling.
Reviewer: Codex

Missing reference groups: none

