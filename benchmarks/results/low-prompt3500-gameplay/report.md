# low-prompt3500-gameplay

Status: **complete** · implementation commit `a21d18ee1336b3304398bab1727c8b3f114b6a4f`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 18/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 93.8% |
| Cases retrieving every expected evidence group | 17/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 2 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 18/20 reviewed |
| Reviewed accuracy | 90.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 8.50 s |
| p95 successful response | 15.50 s |
| Median first visible answer token | 7.24 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 6.53 |
| 02-hold-priority (r1) | 100.0% | correct | 6.85 |
| 03-illegal-target (r1) | 100.0% | correct | 7.47 |
| 04-partial-targets (r1) | 100.0% | correct | 8.00 |
| 05-trample-indestructible (r1) | 100.0% | correct | 13.53 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 9.47 |
| 07-zero-toughness (r1) | 100.0% | incorrect | 21.16 |
| 08-commander-dies (r1) | 100.0% | correct | 12.69 |
| 09-commander-tax (r1) | 100.0% | correct | 6.65 |
| 10-rest-in-peace (r1) | 75.0% | correct | 9.01 |
| 11-token-doublers (r1) | 100.0% | correct | 9.01 |
| 12-replacement-choice (r1) | 100.0% | correct | 9.51 |
| 13-apnap (r1) | 50.0% | partial | 7.34 |
| 14-humility-anthem (r1) | 100.0% | correct | 11.04 |
| 15-own-hexproof (r1) | 100.0% | correct | 6.01 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 10.57 |
| 17-token-blink (r1) | 100.0% | correct | 7.92 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 6.33 |
| 19-legend-response (r1) | 50.0% | correct | 15.50 |
| 20-clarify-interaction (r1) | 100.0% | correct | 7.18 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**Ruling:** No. You cannot respond to your opponent tapping a basic Forest for mana.

**Why:** A basic Forest's tap-for-mana ability is an activated mana ability, which doesn't go on the stack and therefore can't be targeted, countered, or otherwise responded to [CR 605.3b]. It resolves immediately after it is activated [CR 605.3b].

Review: **correct**. Correct ruling and explanation; cited CR 605.3b supports the mana-ability rule.
Reviewer: Codex

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

**Ruling:** Yes, you get priority back first. No, the instant does not resolve immediately.

**Why:** If you had priority when you cast the spell, you receive priority afterward, before your opponent [CR 117.3c]. The spell resolves only when all players pass in succession [CR 405.5] [CR 117.4], meaning your opponent still gets a chance to respond before it resolves.

Review: **correct**. Correct priority and resolution sequence; citations support both claims.
Reviewer: Codex

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**Ruling:** No, you do not draw a card. Defiant Strike does not resolve at all.

**Why:** Defiant Strike has only one target (the creature). If that creature is destroyed before the spell resolves, the target is illegal, and since all of the spell's targets are illegal, the spell doesn't resolve and is put into its owner's graveyard [CR 608.2b]. The card-specific ruling confirms this directly: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correct: all targets are illegal, so the spell does not resolve and no card is drawn; card ruling supports this.
Reviewer: Codex

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Ruling:** Yes, the remaining legal creature takes 2 damage.

**Why:** When a spell resolves, it checks whether its targets are still legal. If *all* targets are illegal, the spell doesn't resolve at all; otherwise it resolves normally, and only the illegal targets are unaffected while legal targets are still affected [CR 608.2b]. Since one target remains legal, the spell resolves and deals 2 damage to that creature.

Review: **correct**. Correct: the remaining legal target is affected because not all targets are illegal.
Reviewer: Codex

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Ruling:** Yes. You must assign at least 2 damage to the blocker (which is lethal damage to a 2/2), and you may assign the remaining 4 to the defending player.

**Why:** Trample requires that all blocking creatures be assigned lethal damage before excess may go to the player [CR 702.19b]. A 2/2 creature's toughness is 2, so 2 damage is lethal damage to it. Indestructible means the creature "isn't destroyed by lethal damage" and "ignore[s] the state-based action that checks for lethal damage" [CR 702.12b], but it does not change what amount of damage counts as "lethal" for the purposes of the trample assignment rule. The analogous protection example in 702.19b confirms that damage which will be prevented or have no effect still satisfies the "lethal damage" requirement for trample.

Review: **correct**. Correct assignment; indestructible does not change lethal damage assignment for trample.
Reviewer: Codex

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling:** You can assign a maximum of **4 damage** to the defending player.

**Why:** Under trample, you must assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. However, deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for the purpose of determining excess damage [CR 702.2c]. So assigning just 1 damage to the 8/8 blocker satisfies the "lethal damage" requirement, leaving 4 damage free to assign to the defending player.

Review: **correct**. Correct: one deathtouch damage is lethal for trample assignment, leaving four for the player.
Reviewer: Codex

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**Ruling:** Yes, the indestructible creature survives. It remains on the battlefield as a 0/0 creature.

**Why:** Indestructible permanents ignore the state-based action that checks for lethal damage, which includes the action that puts a creature with toughness 0 or less into its owner's graveyard [CR 702.12b] [CR 704.5f]. Since the creature is indestructible, that state-based action does not apply to it, so it stays on the battlefield despite having toughness 0.

Review: **incorrect**. Incorrect. Indestructible does not prevent the state-based action for toughness zero or less; the creature goes to its owner’s graveyard. Both criteria fail.
Reviewer: Codex

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling:** Yes, you may put your commander into the command zone, and "dies" triggers still fire.

**Why:** When your commander is destroyed, it is put into the graveyard, which is the event that triggers "dies" abilities (a type of leaves-the-battlefield zone-change trigger) [CR 603.6c]. After that zone change has occurred, the state-based action in rule 903.9a allows its owner to put it into the command zone [CR 903.9a]. The trigger was already created by the zone change before the state-based action is checked, so it remains on the stack regardless of the commander subsequently moving to the command zone.

Review: **correct**. Correct: the commander reaches the graveyard, dies triggers occur, then its owner may move it to the command zone under the stated rule version.
Reviewer: Codex

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is {4}.

**Why:** Rule 903.8 states the additional cost is {2} "for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice previously, so the tax is 2 × {2} = {4}. The cast from your hand does not count, as the rule specifically references casts *from the command zone*. [CR 903.8]

Review: **correct**. Correct: only the two prior command-zone casts count, for {4}.
Reviewer: Codex

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No, Blood Artist does not trigger.

Why: "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exile [C1], so the creature is never actually put into a graveyard and therefore never dies. Since Blood Artist's trigger condition requires a creature to die [C5], it does not trigger.

Review: **correct**. Correct: Rest in Peace replaces the graveyard event with exile, so the creature does not die and Blood Artist does not trigger.
Reviewer: Codex

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

**Ruling:** You create 4 tokens. The doublers do not loop forever.

**Why:** Each doubler is a replacement effect that applies once to the event. Doubling Season doubles the count (1 → 2), then Anointed Procession doubles that result (2 → 4), giving a total of 4 tokens. A replacement effect doesn't invoke itself repeatedly; it gets only one opportunity to affect an event or any modified events that may replace that event [CR 614.5]. This is consistent with the Anointed Procession ruling that two Anointed Processions produce 4× the original number, and three produce 8× [C11].

Review: **correct**. Correct: the two replacement effects produce four tokens and do not loop.
Reviewer: Codex

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** The affected player (you, the one being dealt damage) chooses which replacement effect to apply first. You can end up with either 7 or 8 damage.

**Why:** When multiple replacement effects modify the same event, the affected player chooses the order [CR 616.1]. Any applicable effect may be chosen [CR 616.1e], and the process repeats until no more apply [CR 616.1f]. Doubling damage is a replacement effect [CR 701.10g]. If you apply double first: 3 → 6 → 7. If you apply +1 first: 3 → 4 → 8.

Review: **correct**. Correct chooser and arithmetic for both replacement orders.
Reviewer: Codex

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Ruling:** Bob's triggered ability resolves first.

**Why:** When triggered abilities are put on the stack at the same time, those controlled by the active player are put on the bottom of the stack, followed by the other player's objects [CR 405.3]. Since Alice is the active player, her ability sits below Bob's, so Bob's ability is on top and resolves first [CR 405.5].

Review: **partial**. The outcome and APNAP stacking explanation are substantively correct, but cited CR 405.3 does not establish the APNAP triggered-ability ordering; the key CR 603.3b excerpt was omitted. Treat as unsupported and not fully correct under the evidence-grounded review.
Reviewer: Codex

Missing reference groups: 603.3b

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

**Ruling:** The creature is 2/2. It does not matter which enchantment entered first.

**Why:** Humility's "have base power and toughness 1/1" is a setting effect applied in layer 7b [CR 613.4b], while Glorious Anthem's "+1/+1" is a modifying effect applied in layer 7c [CR 613.4c]. Since sublayers are applied in fixed order (7b before 7c) [CR 613.4], the +1/+1 always applies on top of the 1/1, regardless of timestamp.

Review: **correct**. Correct layer ordering yields 2/2 independent of timestamp.
Reviewer: Codex

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Ruling:** Yes, you may target your own creature with hexproof using your own Giant Growth.

**Why:** Hexproof on a permanent means it "can't be the target of spells or abilities your opponents control" [CR 702.11b]. Since you control both the creature and the Giant Growth, the restriction does not apply to you.

Review: **correct**. Correct: hexproof restricts opponents, not the controller.
Reviewer: Codex

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**Ruling:** No. In the second combat damage step, your attacker assigns no combat damage at all.

**Why:** Although your creature was blocked, by the second combat damage step no creatures are currently blocking it (the blocker is dead). Rule 510.1c explicitly states that a blocked creature with no creatures currently blocking it "assigns no combat damage." Without trample, there is no exception that redirects its damage to the player. [CR 510.1c] [CR 702.19d]

Review: **correct**. Correct: the attacker remains blocked and has no trample, so assigns no damage to the player in the second step.
Reviewer: Codex

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Ruling:** No, the token does not return to the battlefield. It remains in exile and ceases to exist the next time state-based actions are checked.

**Why:** Once a token has left the battlefield, it can't move to another zone or come back onto the battlefield; if such a token would change zones, it remains in its current zone instead [CR 111.8]. This applies regardless of whether the exile and the attempted return occur during the same resolution. The token ceases to exist the next time state-based actions are checked [CR 111.8].

Review: **correct**. Correct: a token that left the battlefield cannot change zones again and will cease to exist at the next state-based-action check.
Reviewer: Codex

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You can activate that ability this turn.

Why: Summoning sickness only restricts activating a creature's activated ability if the activation cost includes the tap symbol or the untap symbol, and it restricts attacking [CR 302.6]. Since your ability's cost is "Sacrifice this creature" with no tap or untap symbol, it is not subject to that restriction.

Review: **correct**. Correct: a sacrifice-only cost is not restricted by summoning sickness.
Reviewer: Codex

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

**Ruling:** No. The legend rule is a state-based action. It does not use the stack and does not generate priority, so there is no window to cast an instant in response. You must choose which legendary permanent to keep as part of resolving the state-based action.

**Why:** The legend rule appears in rule 704, the state-based actions section [CR 704.5j]. State-based actions are checked and resolved before a player would receive priority, and they do not use the stack [CR 405.6]. Because no priority is generated, no player can cast a spell or activate an ability in response to the legend rule.

Review: **correct**. Correct: state-based actions occur before priority and the legend choice is made without a response window.
Reviewer: Codex

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality is your creature's protection from (e.g., "protection from black," "protection from red," "protection from a specific player")?
2. What is the removal spell (name or its color and whether it targets)?

Review: **correct**. Correct clarification request; the protection quality and removal spell are needed.
Reviewer: Codex

Missing reference groups: none

