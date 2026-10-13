# speculative-depth1-gameplay

Status: **complete** · implementation commit `60d7e1217d85291a2e1d1ba872c590dd8d7833bc`

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
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 20/20 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 10.12 s |
| p95 successful response | 13.79 s |
| Median first visible answer token | 7.64 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.45 |
| 02-hold-priority (r1) | 100.0% | correct | 7.90 |
| 03-illegal-target (r1) | 100.0% | correct | 7.37 |
| 04-partial-targets (r1) | 100.0% | correct | 7.77 |
| 05-trample-indestructible (r1) | 100.0% | correct | 13.79 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.41 |
| 07-zero-toughness (r1) | 100.0% | correct | 13.04 |
| 08-commander-dies (r1) | 100.0% | correct | 9.84 |
| 09-commander-tax (r1) | 100.0% | correct | 7.55 |
| 10-rest-in-peace (r1) | 75.0% | correct | 8.94 |
| 11-token-doublers (r1) | 100.0% | correct | 10.79 |
| 12-replacement-choice (r1) | 100.0% | correct | 12.86 |
| 13-apnap (r1) | 100.0% | correct | 10.83 |
| 14-humility-anthem (r1) | 100.0% | correct | 15.69 |
| 15-own-hexproof (r1) | 100.0% | correct | 6.86 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 13.69 |
| 17-token-blink (r1) | 100.0% | correct | 8.69 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 10.95 |
| 19-legend-response (r1) | 50.0% | correct | 12.85 |
| 20-clarify-interaction (r1) | 100.0% | correct | 8.00 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**Ruling:** No. You cannot respond to your opponent tapping a basic Forest for mana.

**Why:** An activated mana ability doesn't go on the stack, so it can't be targeted, countered, or otherwise responded to; it resolves immediately after it is activated [CR 605.3b]. A basic Forest's tap-for-mana ability qualifies as a mana ability because it doesn't require a target, could add mana to a player's mana pool, isn't a loyalty ability, and doesn't move cards to or from a library [CR 605.1a].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

**Ruling:** Yes, you get priority first after casting the instant. No, it does not resolve immediately—it resolves only after all players pass in succession.

**Why:** If you have priority when you cast a spell, you receive priority afterward [CR 117.3c]. The spell on the stack resolves only when all players pass in succession [CR 405.5] [CR 117.4].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**Ruling:** No, you do not draw a card. Defiant Strike fails to resolve entirely.

**Why:** If the target creature is no longer a legal target when Defiant Strike tries to resolve, the spell doesn't resolve and is removed from the stack [CR 608.2b]. The card-specific ruling confirms this directly: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Ruling:** Yes, the remaining creature takes 2 damage.

**Why:** Since not all targets are illegal, the spell resolves normally. The illegal target simply isn't affected, while the legal target is still affected by the effect. [CR 608.2b]

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Ruling:** Yes. You must assign at least 2 damage to the 2/2 blocker (lethal damage for a 2-toughness creature), and the remaining 4 may be assigned to the defending player.

**Why:** Trample requires you to assign lethal damage to blocking creatures before assigning excess to the player, and the check for "lethal damage" considers only the creature's toughness and damage already marked—not abilities that affect what happens *after* damage is dealt [CR 702.19b]. Indestructible prevents destruction by lethal damage but does not change the amount of damage that counts as "lethal" for trample assignment purposes [CR 702.12b]. This is analogous to the supplied example where a 6/6 with trample blocked by a 2/2 with protection must still assign 2 to the blocker and may assign the rest to the player [CR 702.19b].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling:** You can assign a maximum of **4** damage to the defending player.

**Why:** Trample requires you to assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. However, deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for this purpose [CR 702.2c]. So you assign 1 damage to the 8/8 blocker (sufficient to be considered lethal) and the remaining 4 damage to the defending player.

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**Ruling:** No. The creature is put into its owner's graveyard.

**Why:** Indestructible makes a permanent ignore the state-based action for lethal damage (rule 704.5g), but a creature with toughness 0 or less is put into its owner's graveyard by a separate state-based action (rule 704.5f), which indestructible does not prevent. [CR 702.12b] [CR 704.5f]

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling:** Yes, you may put your commander into the command zone from the graveyard, and yes, abilities that trigger when it "dies" still trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Your commander was put into the graveyard, so the trigger event occurred. The owner's subsequent option to move it to the command zone is a state-based action that happens after the trigger has already fired [CR 903.9a]. The trigger doesn't retroactively fail just because the card later leaves the graveyard.

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is {4}.

**Why:** Rule 903.8 states the additional cost is {2} "for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice previously, so the tax is 2 × {2} = {4}. The cast from your hand does not count toward this total, as the rule specifically tracks casts *from the command zone*. [CR 903.8]

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**Ruling:** No, Blood Artist does not trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exiling the card [C1], so the creature is never put into a graveyard and therefore never dies. The official ruling confirms this: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

**Ruling:** You create 4 tokens. The doublers do not loop forever.

**Why:** Each doubler is a replacement effect that multiplies the token count by 2, so two doublers produce 2 × 2 = 4 times the original number [C2][C11]. A replacement effect doesn't invoke itself repeatedly; it gets only one opportunity to affect an event or any modified events that may replace that event [CR 614.5]. This is why the result is a finite multiplication rather than an infinite loop.

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** You (the affected player) choose the order. The final damage can be either 7 or 8.

**Why:** When two or more replacement effects are attempting to modify the same event, the affected player chooses which to apply first [CR 616.1]. Since neither is a self-replacement effect, control-changing effect, copy effect, or back-face effect, you may choose either one first [CR 616.1a–e]. After the first is applied, the process repeats with the remaining effect [CR 616.1f]. Doubling first gives 3 × 2 = 6, then +1 = 7; increasing first gives 3 + 1 = 4, then × 2 = 8.

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Ruling:** Bob's triggered ability resolves first.

**Why:** In APNAP order, the active player (Alice) puts her triggered ability on the stack first, then Bob puts his on top of it [CR 603.3b]. Each object placed on the stack goes on top of all objects already there [CR 405.2], so Bob's ability is the topmost object and resolves first when all players pass [CR 405.5].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

**Ruling:** The creature is 2/2, and it does not matter which enchantment entered first.

**Why:** Humility's "have base power and toughness 1/1" is a setting effect that applies in layer 7b [CR 613.4b], while Glorious Anthem's "+1/+1" is a modifying effect that applies in layer 7c [CR 613.4c]. Because they apply in different sublayers, the layer system—not timestamp order—determines the sequence: 1/1 is set first, then +1/+1 is added, yielding 2/2 regardless of entry order.

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own creature with hexproof using your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities your opponents control" [CR 702.11b]. Since you control both the creature and the spell, the restriction does not apply to you. Giant Growth simply requires "target creature" [C1], which your own creature satisfies.

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**Ruling:** No. In the second combat damage step, your attacker assigns no combat damage at all.

**Why:** Your attacker is still a blocked creature in the second combat damage step (being blocked persists even after the blocker dies). A blocked creature assigns its combat damage only to the creatures blocking it, and if no creatures are currently blocking it, it assigns no combat damage [CR 510.1c]. Without trample, there is no mechanism to redirect that damage to the player [CR 702.19b].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Ruling:** No, the token does not return to the battlefield. It remains in exile and ceases to exist the next time state-based actions are checked.

**Why:** A token that has left the battlefield can't move to another zone or come back onto the battlefield; if such a token would change zones, it remains in its current zone instead [CR 111.8]. It then ceases to exist the next time state-based actions are checked [CR 111.8].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You can activate that ability on the turn you cast the creature, as long as you have priority.

Why: The summoning sickness restriction applies only to a creature's activated abilities that include the tap symbol ({T}) or the untap symbol ({Q}) in their activation cost [CR 302.6] [CR 602.5a]. Since your ability's cost is "Sacrifice this creature" with no tap or untap symbol, the restriction does not apply. A player may activate an activated ability any time they have priority [CR 117.1b].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

**Ruling:** No. You cannot cast an instant in response to the legend rule. The choice of which legendary permanent to keep is made as part of the state-based action itself, and no player receives priority during that process.

**Why:** State-based actions are performed before a player would receive priority [CR 117.5], and the legend rule is a state-based action [CR 704.5j]. Since no one has priority at that moment, no one can cast a spell or activate an ability in response [CR 117.1].

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality does your creature's protection specify (e.g., "protection from red," "protection from black," "protection from a specific player")?
2. What is the removal spell (name or text)? Specifically, does it target your creature, and what color is it?

Review: **correct**. Reviewed against both authored criteria and the supplied rule/card excerpts; the answer is correct, complete, and its cited claims are supported.
Reviewer: Codex

Missing reference groups: none

