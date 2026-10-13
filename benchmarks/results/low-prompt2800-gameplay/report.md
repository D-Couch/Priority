# low-prompt2800-gameplay

Status: **complete** · implementation commit `be096dc87615d993e7e9c5eba8e55a31227947b7`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 17/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 86.2% |
| Cases retrieving every expected evidence group | 14/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 17/20 reviewed |
| Reviewed accuracy | 85.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 7.80 s |
| p95 successful response | 15.54 s |
| Median first visible answer token | 6.70 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 6.45 |
| 02-hold-priority (r1) | 100.0% | correct | 7.80 |
| 03-illegal-target (r1) | 100.0% | correct | 6.84 |
| 04-partial-targets (r1) | 100.0% | correct | 6.92 |
| 05-trample-indestructible (r1) | 100.0% | correct | 9.70 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 7.94 |
| 07-zero-toughness (r1) | 100.0% | correct | 11.64 |
| 08-commander-dies (r1) | 50.0% | partial | 15.54 |
| 09-commander-tax (r1) | 100.0% | correct | 6.29 |
| 10-rest-in-peace (r1) | 75.0% | correct | 5.87 |
| 11-token-doublers (r1) | 100.0% | correct | 10.53 |
| 12-replacement-choice (r1) | 50.0% | partial | 15.87 |
| 13-apnap (r1) | 50.0% | correct | 7.47 |
| 14-humility-anthem (r1) | 100.0% | correct | 10.05 |
| 15-own-hexproof (r1) | 100.0% | correct | 5.55 |
| 16-first-strike-blocker (r1) | 50.0% | correct | 14.74 |
| 17-token-blink (r1) | 100.0% | correct | 7.81 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 6.72 |
| 19-legend-response (r1) | 50.0% | partial | 12.95 |
| 20-clarify-interaction (r1) | 100.0% | correct | 6.20 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**Ruling:** No. You cannot respond to your opponent tapping a basic Forest for mana.

**Why:** An activated mana ability doesn't go on the stack, so it can't be targeted, countered, or otherwise responded to; it resolves immediately after it is activated [CR 605.3b]. A basic Forest's tap-for-mana ability meets all the criteria for a mana ability [CR 605.1a]. Additionally, the active player receives priority after a spell or ability resolves *other than* a mana ability [CR 117.3b], meaning no one gets a chance to act in between.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

**Ruling:** Yes, you get priority again after casting the instant. No, it does not resolve immediately — it resolves only when all players pass in succession.

**Why:** A player who has priority when they cast a spell receives priority again afterward [CR 117.3c]. However, the spell sits on the stack and resolves only when all players pass in succession [CR 405.5], meaning your opponent gets a chance to respond before it resolves.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card. Defiant Strike does not resolve at all if its target is no longer legal.

Why: If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell doesn't resolve and is removed from the stack [C2]. This follows the general rule that if all targets are illegal, the spell doesn't resolve [CR 608.2b]. Since the spell never resolves, none of its effects—including the card draw—occur.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Ruling:** Yes, the remaining creature takes 2 damage.

**Why:** Since not all targets are illegal, the spell resolves normally. The illegal target simply isn't affected, while the legal target is still affected by the effect. [CR 608.2b]

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Ruling:** Yes. You may assign 2 damage to the indestructible blocker and 4 damage to the defending player.

**Why:** Trample requires that the blocking creature be assigned *lethal damage* before excess may go to the player [CR 702.19b]. Indestructible prevents the permanent from being *destroyed* by that damage, but it does not change the amount of damage dealt or prevent the creature from being assigned lethal damage [CR 702.12b]. Since 2 damage is lethal for a 2/2, the trample condition is satisfied and the remaining 4 may be assigned to the defending player.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling:** You can assign a maximum of **4** damage to the defending player.

**Why:** Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for the purposes of determining excess damage [CR 702.2c]. Trample requires that all blocking creatures be assigned lethal damage before excess damage can be assigned to the defending player [CR 702.19b]. Since 1 damage is sufficient to be "lethal" against the 8/8 due to deathtouch, you assign 1 to the blocker and the remaining 4 to the player.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**Ruling:** No. The creature is put into its owner's graveyard. Indestructible does not save it.

**Why:** Indestructible prevents a permanent from being *destroyed*, including by lethal damage [CR 702.12b]. However, the state-based action for a creature with toughness 0 or less simply puts it into its owner's graveyard [CR 704.5f]—this is not a destruction event, so indestructible has no effect on it.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling:** Yes, you may put your commander into the command zone from the graveyard. Yes, "dies" triggers still trigger.

**Why:** Rule 903.9a makes it a state-based action that the owner *may* put a commander into the command zone if it's in the graveyard and was put there since the last time state-based actions were checked [CR 903.9a]. The "dies" trigger fires when the commander is put into the graveyard from the battlefield — that event has already occurred. The subsequent state-based action of moving it to the command zone is a separate event and does not retroactively prevent the trigger from having already triggered.

Review: **partial**. Conclusion is correct, but the answer asserts that dies abilities trigger without citing or receiving the dies definition or zone-change trigger rule; these expected excerpts were omitted by the prompt cap.
Reviewer: Codex

Missing reference groups: 700.4|603.6c|603.10a

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is {4}.

**Why:** Rule 903.8 specifies that the additional cost is {2} "for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice previously, so the tax is 2 × {2} = {4}. The cast from your hand does not count, as the rule only tallies casts *from the command zone*. [CR 903.8]

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**Ruling:** No, Blood Artist does not trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event, exiling the creature instead [C1]. Since the creature is never put into a graveyard, it never dies, so Blood Artist's trigger condition is never met [C2].

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

**Ruling:** You create 4 tokens. The doublers do not loop forever.

**Why:** Each doubler is a replacement effect that applies once to the event. Doubling Season doubles the original 1 token to 2, then Anointed Procession doubles that result to 4 (or vice versa; the order doesn't matter). [CR 614.5] explicitly states that a replacement effect doesn't invoke itself repeatedly—it gets only one opportunity to affect an event or any modified events that may replace that event. This is consistent with the Anointed Procession ruling that multiple doublers stack multiplicatively (2×2 = 4) rather than infinitely [C11].

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** Yes, the final damage can be either 7 or 8 depending on the order of application. The provided reference excerpts do not contain the rule that specifies who chooses the order of multiple non-self replacement effects (typically rule 614.12), so I cannot cite a source for that part of the answer.

**Why:** If the doubling effect applies first, 3 becomes 6, then the +1 effect makes it 7. If the +1 effect applies first, 3 becomes 4, then the doubling effect makes it 8. Both effects are ordinary replacement effects (not self-replacement), so [CR 614.15] does not impose a fixed order between them. The math is straightforward, but the rule governing who selects the order is not present in the supplied excerpts.

Review: **partial**. Correctly calculates 7 and 8 but explicitly declines to identify who chooses the order because CR 616.1 was omitted. Criterion 1 fails; this is a direct evidence loss caused by the cap.
Reviewer: Codex

Missing reference groups: 616.1

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Ruling:** Bob's triggered ability resolves first.

**Why:** When triggered abilities are put on the stack at the same time, those controlled by the active player are put on lowest, followed by the other player's objects [CR 405.3]. Since Alice is the active player, her ability goes on the stack first (lowest) and Bob's goes on top. The top (last-added) object on the stack resolves first [CR 405.5], so Bob's ability resolves before Alice's.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: 603.3b

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

**Ruling:** The creature is 2/2. It does not matter which enchantment entered first.

**Why:** Humility's "have base power and toughness 1/1" is a set effect applied in layer 7b [CR 613.4b], while Glorious Anthem's "+1/+1" is a modifying effect applied in layer 7c [CR 613.4c]. Sublayers are always applied in order (7b before 7c) regardless of timestamp [CR 613.4], so the creature is set to 1/1 first, then receives +1/+1, resulting in 2/2.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Ruling:** Yes. You may target your own creature with hexproof using your own Giant Growth.

**Why:** Hexproof on a permanent means it "can't be the target of spells or abilities your opponents control" [CR 702.11b]. Since you control both the creature and the Giant Growth, hexproof does not prevent you from targeting it.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**Ruling:** No. Your 3/3 with double strike (but no trample) assigns no damage in the second combat damage step.

**Why:** A blocked creature without trample can only assign combat damage to the creatures blocking it. Since the 2/2 blocker is dead and there are no other blockers, there is no valid recipient for the damage. The rule that allows a blocked attacker to deal damage to the player when no creatures are blocking it (rule 702.19d) applies only to creatures with trample or trample over planeswalkers [CR 702.19d]. Your attacker lacks trample, so it simply deals no damage in the second combat damage step.

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: 510.1c

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Ruling:** No, the token does not return to the battlefield. It remains in exile and ceases to exist the next time state-based actions are checked.

**Why:** Once a token leaves the battlefield, it can't come back; if it would change zones, it remains in its current zone instead [CR 111.8]. The token ceases to exist as a state-based action [CR 111.7].

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes, you can activate it this turn.

Why: Summoning sickness only restricts a creature's activated abilities that have the tap or untap symbol in their activation cost, as well as attacking [CR 302.6]. Since your ability's cost is "Sacrifice this creature" with no tap or untap symbol, the restriction does not apply. You may activate it any time you have priority [CR 117.1b].

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. The legend rule is a state-based action; it does not use the stack and cannot be responded to. You simply choose one of the legendary permanents to keep, and the rest are put into their owners' graveyards.

Why: Rule 704.5j places the legend rule among state-based actions, which are checked whenever a player would receive priority and resolve without using the stack [CR 704.5j]. Because no spell or ability is placed on the stack, no player gets a chance to cast an instant in response.

Review: **partial**. Correctly says the legend rule cannot be responded to and one is kept, but does not explain the rubric-required timing that state-based actions occur before priority; the general state-based-action rule was omitted.
Reviewer: Codex

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What is your creature protected from (e.g., protection from red, protection from black, protection from a specific player)?
2. What is the removal spell (name or text)? Is it a targeted spell (e.g., "destroy target creature") or a non-targeted spell (e.g., "destroy all creatures")?

Review: **correct**. Answer satisfies the scenario rubric and its material claims are supported by the packed sources.
Reviewer: Codex

Missing reference groups: none

