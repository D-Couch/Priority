# final-guardrails-low-gameplay

Status: **complete** · implementation commit `22ed98ddf31574780c627d0ea155d28ecdac5e4c`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 18/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 96.2% |
| Cases retrieving every expected evidence group | 18/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 18/20 reviewed |
| Reviewed accuracy | 90.0% |
| Mean reviewed rubric score | 92.5% |
| Median successful response | 7.85 s |
| p95 successful response | 12.55 s |
| Median first visible answer token | 6.77 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 5.96 |
| 02-hold-priority (r1) | 100.0% | correct | 6.38 |
| 03-illegal-target (r1) | 100.0% | correct | 6.62 |
| 04-partial-targets (r1) | 100.0% | correct | 6.15 |
| 05-trample-indestructible (r1) | 100.0% | correct | 11.82 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 6.46 |
| 07-zero-toughness (r1) | 100.0% | incorrect | 8.19 |
| 08-commander-dies (r1) | 100.0% | correct | 10.20 |
| 09-commander-tax (r1) | 100.0% | correct | 6.18 |
| 10-rest-in-peace (r1) | 75.0% | correct | 7.60 |
| 11-token-doublers (r1) | 100.0% | correct | 8.09 |
| 12-replacement-choice (r1) | 100.0% | correct | 10.18 |
| 13-apnap (r1) | 100.0% | correct | 8.14 |
| 14-humility-anthem (r1) | 100.0% | correct | 12.60 |
| 15-own-hexproof (r1) | 100.0% | correct | 5.55 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.55 |
| 17-token-blink (r1) | 100.0% | correct | 8.15 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 6.96 |
| 19-legend-response (r1) | 50.0% | partial | 9.13 |
| 20-clarify-interaction (r1) | 100.0% | correct | 6.31 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**Ruling:** No. You cannot respond to your opponent tapping a basic Forest for mana.

**Why:** An activated mana ability doesn't go on the stack, so it can't be targeted, countered, or otherwise responded to; it resolves immediately after it is activated [CR 605.3b]. A basic Forest's tap-for-mana ability qualifies as a mana ability because it doesn't require a target, could add mana to a player's mana pool, isn't a loyalty ability, and doesn't move cards to or from a library [CR 605.1a].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

**Ruling:** Yes, you get priority first after casting the instant. No, it does not resolve immediately—it resolves only after all players pass in succession.

**Why:** If you have priority when you cast a spell, you receive priority afterward [CR 117.3c]. The spell sits on the stack, and it resolves only when all players pass in succession [CR 405.5] [CR 117.4].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**Ruling:** No. If the target creature is destroyed before Defiant Strike resolves, the spell doesn't resolve at all, and you do not draw a card.

**Why:** Defiant Strike has a single target. If that creature has left the battlefield, it is an illegal target, and since all of the spell's targets are illegal, the spell doesn't resolve [CR 608.2b]. The card-specific ruling confirms this: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Ruling:** Yes, the remaining legal creature takes 2 damage.

**Why:** A spell only fails to resolve if *all* of its targets are illegal. Since one target is still legal, the spell resolves normally, and the illegal target simply isn't affected while the legal one is. [CR 608.2b]

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Ruling:** Yes. You must assign at least 2 damage to the indestructible blocker, and the remaining 4 may be assigned to the defending player.

**Why:** Trample requires that lethal damage be assigned to each blocking creature before excess may go to the player [CR 702.19b]. "Lethal damage" here is determined by the creature's toughness (2 in this case), not by whether the damage would actually destroy it. The rule's own example confirms this principle: a 6/6 with trample blocked by a 2/2 with protection from green must still assign 2 to the blocker even though that damage will be prevented [CR 702.19b]. Indestructible similarly doesn't raise the required assignment threshold; it only prevents destruction after damage is dealt [CR 702.12b].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling:** The maximum damage you can assign to the defending player is **4**.

**Why:** Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for trample purposes [CR 702.2c]. So you must assign only 1 damage to the 8/8 blocker to satisfy the trample requirement, and the remaining 4 damage (5 power − 1) may be assigned to the defending player [CR 702.19b].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**Ruling:** Yes, it survives. The creature remains on the battlefield as a 0/0.

**Why:** Indestructible permanents ignore the state-based action that checks for lethal damage (a creature with toughness 0 or less being put into its owner's graveyard) [CR 702.12b] [CR 704.5f]. The -3/-3 effect still applies, making it a 0/0, but the state-based action that would kill it is ignored due to indestructible.

Review: **incorrect**. Incorrectly says indestructible lets a 0/0 survive. CR 704.5f puts a creature with toughness 0 or less into its owner’s graveyard; this is not destruction and is not prevented by indestructible.
Reviewer: Codex

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling:** Yes, you may put your commander into the command zone, and "dies" triggers still trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4], and that event occurred when the commander was destroyed and entered the graveyard. The ability to move a commander from the graveyard to the command zone is a state-based action that happens afterward [CR 903.9a], so it does not prevent the trigger from having already fired.

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is {4}.

**Why:** Rule 903.8 states the additional cost is {2} for each previous time the player has cast the commander *from the command zone* that game. You have cast it from the command zone twice previously, so the next cast from the command zone costs an additional 2 × {2} = {4}. The cast from your hand does not count toward this total. [CR 903.8]

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No, Blood Artist does not trigger.

Why: "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect exiles the creature instead of putting it into a graveyard [C1], so the creature never dies. Since Blood Artist's trigger condition requires a creature to die [C5], it does not trigger.

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **four** tokens. The doublers do not loop forever.

Why: Each doubler is a replacement effect that multiplies the token count by 2, so two doublers produce a 2 × 2 = 4× multiplier [C2][C11]. Replacement effects don't invoke themselves repeatedly; each gets only one opportunity to affect an event or any modified events that may replace that event [CR 614.5].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** The affected player (you, the one being dealt damage) chooses which replacement effect to apply first. The final damage can be 7 or 8.

**Why:** Under [CR 616.1], when two or more replacement effects are attempting to modify the same event, the affected player chooses which to apply. Since neither is a self-replacement effect, the priority steps in 616.1a–d don't force a particular one, and [CR 616.1e] allows any applicable effect to be chosen. After the first is applied, [CR 616.1f] repeats the process for the remaining effect. Doubling first gives 3 × 2 = 6, then +1 = 7; increasing first gives 3 + 1 = 4, then doubling = 8.

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Ruling:** Bob's triggered ability resolves first.

**Why:** In APNAP order, Alice (the active player) puts her triggered ability on the stack first, then Bob puts his on top of it [CR 603.3b]. Each object placed on the stack goes on top of all objects already there [CR 405.2], and the top (last-added) object resolves first [CR 405.5].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

**Ruling:** The creature is 2/2. It does not matter which enchantment entered first.

**Why:** Humility's "have base power and toughness 1/1" is a setting effect that applies in layer 7b [CR 613.4b]. Glorious Anthem's "+1/+1" is a modifying effect that applies in layer 7c [CR 613.4c]. Since 7b is applied before 7c, the base P/T is set to 1/1 first, then +1/+1 is added on top, yielding 2/2. Timestamp order is irrelevant because the two effects are in different sublayers [CR 613.7].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Ruling:** Yes. You may target your own hexproof creature with your own Giant Growth.

**Why:** Hexproof on a permanent means it "can't be the target of spells or abilities your opponents control" [CR 702.11b]. Since you control both the creature and the Giant Growth, the hexproof restriction does not apply to your own spell.

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**Ruling:** No. In the second combat damage step, your 3/3 assigns no combat damage at all.

**Why:** Your attacker is still considered *blocked* (it was declared as blocked), and rule 510.1c explicitly states that a blocked creature with no creatures currently blocking it (e.g., they were destroyed) assigns no combat damage. Trample would change this outcome via rule 702.19d, but without trample there is no mechanism to redirect that damage to the player. [CR 510.1c] [CR 702.19d]

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Ruling:** No, the token does not return to the battlefield. It remains in exile and ceases to exist the next time state-based actions are checked.

**Why:** Once a token leaves the battlefield, it can't move to another zone or come back onto the battlefield; if it would change zones, it remains in its current zone instead [CR 111.8]. This is a rule that applies regardless of whether replacement effects are present, so the "return" instruction simply fails to move the token, and it ceases to exist as a state-based action [CR 111.7].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

**Ruling:** Yes. You can activate that ability on the turn you cast the creature.

**Why:** Summoning sickness restricts only a creature's activated abilities that include the tap symbol ({T}) or the untap symbol ({Q}) in their activation cost [CR 302.6] [CR 602.5a]. Since "Sacrifice this creature" contains neither symbol, the restriction does not apply, and you may activate the ability any time you have priority [CR 117.1b].

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant in response to the legend rule.

Why: The legend rule is a state-based action, which happens automatically and is dealt with before any player would receive priority [CR 704.5j] [CR 117.2d]. Each time a player would get priority, the game first performs all applicable state-based actions, and only after that process completes does a player actually receive priority [CR 117.5]. Since no player has priority at the moment the legend rule is applied, there is no window to cast an instant.

Review: **partial**. Correctly says no instant can be cast before the legend rule is applied, but omits that the state-based action requires keeping one of the legendary permanents.
Reviewer: Codex

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality does your creature's protection specify (e.g., "protection from red," "protection from black," "protection from a specific player")?
2. What is the removal spell (name or text), and what color is it?

Review: **correct**. Reviewed the ruling against both authored criteria and the supplied rule/card excerpts; material claims are supported.
Reviewer: Codex

Missing reference groups: none

