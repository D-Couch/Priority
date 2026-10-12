# hybrid-family-original

Status: **complete** · implementation commit `d55b40a747a4382d9e8aebb4d41c65db85575948`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 19/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 89.6% |
| Cases retrieving every expected evidence group | 15/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 19/20 reviewed |
| Reviewed accuracy | 95.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 11.73 s |
| p95 successful response | 17.70 s |
| Median first visible answer token | 10.54 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 8.52 |
| 02-hold-priority (r1) | 100.0% | correct | 9.15 |
| 03-illegal-target (r1) | 100.0% | correct | 9.16 |
| 04-partial-targets (r1) | 100.0% | correct | 11.31 |
| 05-trample-indestructible (r1) | 100.0% | correct | 14.00 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 9.65 |
| 07-zero-toughness (r1) | 50.0% | incorrect | 15.04 |
| 08-commander-dies (r1) | 100.0% | correct | 20.02 |
| 09-commander-tax (r1) | 100.0% | correct | 8.68 |
| 10-rest-in-peace (r1) | 75.0% | correct | 9.09 |
| 11-token-doublers (r1) | 66.7% | correct | 12.71 |
| 12-replacement-choice (r1) | 100.0% | correct | 14.55 |
| 13-apnap (r1) | 50.0% | correct | 12.14 |
| 14-humility-anthem (r1) | 100.0% | correct | 16.38 |
| 15-own-hexproof (r1) | 100.0% | correct | 7.26 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 15.45 |
| 17-token-blink (r1) | 100.0% | correct | 9.13 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 10.67 |
| 19-legend-response (r1) | 50.0% | correct | 17.70 |
| 20-clarify-interaction (r1) | 100.0% | correct | 12.47 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. You cannot respond to your opponent tapping a basic Forest for mana.

Why: A Forest's "{T}: Add {G}" is an activated mana ability [CR 305.6] [CR 605.1a]. Activated mana abilities don't go on the stack, so they can't be targeted, countered, or otherwise responded to; they resolve immediately after activation [CR 605.3b] [CR 405.6c].

Review: **correct**. Correct activated mana ability cannot be responded to; 605.3b and 605.1a directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again before your opponent after casting the instant. No, the instant does not resolve immediately; it sits on the stack until all players pass in succession.

Why: A player who has priority when they cast a spell receives priority afterward [CR 117.3c]. Once cast, the instant is placed on the stack [CR 405.1] and only resolves when all players pass in succession [CR 405.5, CR 117.4], giving your opponent a chance to respond first.

Review: **correct**. Correct caster retains priority and all-player-pass sequence; cited priority/stack rules support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card. Defiant Strike fails to resolve entirely.

Why: When Defiant Strike tries to resolve, it checks whether its target is still legal. A creature that has been destroyed is no longer on the battlefield, so it is an illegal target [CR 608.2b]. Because Defiant Strike has only one target and that target is illegal, the spell doesn't resolve and is put into its owner's graveyard [CR 608.2b]. The "Draw a card" instruction is never applied. This is confirmed by the card-specific ruling: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correct no card when all targets are illegal; 608.2b and Defiant Strike ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The spell resolves normally, and the remaining legal creature takes 2 damage. The creature that left the battlefield is simply not affected.

Why: A spell with multiple targets fails to resolve only if *all* of its targets are illegal; if at least one target is still legal, the spell resolves and the illegal target is simply skipped [CR 608.2b]. The Plague Spores example in the same rule confirms that a partially illegal multi-target spell still applies its effect to the targets that remain legal [CR 608.2b].

Review: **correct**. Correct remaining legal target takes 2 damage; 608.2b explains partial target legality.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You must assign at least 2 damage to the indestructible blocker (its toughness), and you may assign the remaining 4 damage to the defending player.

Why: Trample requires you to assign "lethal damage" (damage equal to the blocker's toughness) to the blocking creature before assigning excess to the player [CR 702.19b]. Indestructible prevents the creature from being destroyed by that damage, but it does not change the amount of damage that counts as "lethal" for the trample calculation [CR 702.12b]. The rule explicitly instructs you to ignore "abilities or effects that might change the amount of damage that's actually dealt" when checking for assigned lethal damage [CR 702.19b], so indestructible is irrelevant to the assignment split.

Review: **correct**. Correct trample assignment to indestructible blocker and player; cited example supports distinction between lethal assignment and damage dealt.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: The maximum damage you can assign to the defending player is **4**.

Why: Deathtouch means any nonzero amount of damage assigned to the blocker counts as lethal damage for trample purposes [CR 702.2c]. Trample requires you to assign at least that lethal amount to the blocker before assigning excess to the player [CR 702.19b]. With a 5-power attacker, you assign the minimum 1 damage to the 8/8 blocker and the remaining 4 to the defending player.

Review: **correct**. Correct one deathtouch damage satisfies trample assignment and leaves four for player.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: Yes, the creature survives as a 0/0, but not specifically because of indestructible. It survives because no state-based action destroys it.

Why: The -3/-3 effect (layer 7c, [CR 613.4c]) reduces the creature to 0/0. The only state-based action that destroys a creature based on toughness is the lethal-damage check, which requires the creature to have toughness *greater than 0* and damage marked on it equal to or exceeding that toughness [CR 704.5g]. A 0/0 creature with no damage on it fails that condition, so it simply remains on the battlefield as a 0/0. Indestructible [CR 702.12b] would be relevant if the creature had damage on it and its toughness were reduced to 0 or below, but here no destruction event occurs at all, so indestructible is not the reason it survives.

Review: **incorrect**. Incorrect and unsafe: claims a 0/0 creature survives. CR 704.5f sends a creature with toughness 0 or less to its owner’s graveyard regardless of damage or indestructible. Hybrid candidate selection omitted 704.5f even though the lexical source set contains it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.5f

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes to both. You may put your commander into the command zone as a state-based action, and "dies" triggers still trigger because the event of being put into a graveyard from the battlefield did occur.

Why: [CR 903.9a] lets the owner put a commander that is in the graveyard into the command zone as a state-based action. [CR 700.4] defines "dies" as "is put into a graveyard from the battlefield," and that zone-change event happened before the state-based action is checked, so the trigger condition is met. [CR 603.10a] confirms that leaves-the-battlefield triggers look back in time to the event. Note that if a triggered ability then tries to do something to the commander *in the graveyard* (e.g., return it to hand), that portion will fail to find it there per [CR 603.6], but the trigger itself still fires and any other effects it has still resolve.

Review: **correct**. Correct commander dies trigger occurs on battlefield-to-graveyard move before command-zone SBA; cited rules support timing.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax on your next cast from the command zone is {4}.

Why: Commander tax is calculated as an additional {2} for each previous time you have cast that commander **from the command zone** that game [CR 903.8]. You have cast it from the command zone twice, so the tax is 2 × {2} = {4}. The cast from your hand does not count toward the tax, since the rule specifically references casts "from the command zone" [CR 903.8].

Review: **correct**. Correct commander tax is four; counts only prior command-zone casts.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger when the other creature is destroyed while Rest in Peace is on the battlefield.

Why: "Dies" specifically means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect causes the creature to be exiled instead of being put into a graveyard [C1], so the creature never "dies" and Blood Artist's trigger condition is never met. This is confirmed directly: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Correct Rest in Peace replaces graveyard event and prevents dies trigger.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4** tokens. The doublers do **not** loop forever; each applies exactly once to the event.

Why: Both Doubling Season and Anointed Procession are replacement effects modifying the same token-creation event. You choose which applies first [CR 616.1]; after it doubles the count (1 → 2), the process repeats with the remaining applicable effect [CR 616.1f], which doubles again (2 → 4). The Anointed Procession ruling confirms the multiplicative pattern: two doublers yield four times the original number [C11].

Review: **correct**. Correct two token doublers yield four once each with no loop.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 614.5

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: You, as the affected player, choose which replacement effect to apply first. The final damage can be either 7 (double first: 3→6, then +1→7) or 8 (+1 first: 3→4, then double→8), depending on the order you select.

Why: When two or more replacement effects attempt to modify the same event, the affected player chooses which to apply, and since neither is a self-replacement, control-modifying, copy, or back-face effect, either may be chosen freely [CR 616.1][CR 616.1e]. After the first effect is applied, the process repeats with the remaining applicable effect on the now-modified event [CR 616.1f]. Doubling damage is itself a replacement effect that sets the new amount [CR 701.10g], so the second effect operates on whatever value results from the first.

Review: **correct**. Correct affected player chooses and arithmetic 7 or 8 is correct.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: Because it is Alice's turn, she is the active player. Under the APNAP ordering in [CR 603.3b], Alice puts her triggered ability on the stack first, then Bob puts his on the stack. Each ability becomes the topmost object when placed [CR 603.3], so Bob's ability sits on top of Alice's and resolves first (LIFO).

Review: **correct**. Correct Bob APNAP trigger is on top and resolves first.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 405.2|608.1

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is 2/2, and it does not matter which enchantment entered the battlefield first.

Why: Humility's "have base power and toughness 1/1" is a setting effect that applies in layer 7b [CR 613.4b], while Glorious Anthem's "get +1/+1" is a modifying effect that applies in layer 7c [CR 613.4c]. Because the two effects sit in different sublayers, the fixed sublayer order (7b before 7c) determines the result regardless of timestamp [CR 613.4]. Humility's "lose all abilities" clause (layer 6) only affects creatures, so Glorious Anthem's static ability continues to apply [C1][C5]. The creature's base P/T is set to 1/1, then +1/+1 is added, yielding 2/2.

Review: **correct**. Correct Humility/Anthem produces 2/2 independent of timestamp.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own hexproof creature with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. The restriction applies only to opponents' spells and abilities; it does not prevent the controller from targeting the creature with their own spells. Giant Growth simply requires "target creature" [C1], and your own creature is a legal target for your own spell.

Review: **correct**. Correct own hexproof creature can be targeted by own Giant Growth.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step your 3/3 assigns no combat damage at all, so the player takes 0 damage.

Why: Your attacker was blocked during the declare blockers step, making it a blocked creature. In the second combat damage step the 2/2 blocker is already dead, so no creatures are currently blocking it. Under [CR 510.1c], a blocked creature with no creatures currently blocking it "assigns no combat damage." Because your attacker lacks trample, there is no rule allowing it to redirect that damage to the player (contrast [CR 702.19d], which only applies to creatures that *have* trample). Double strike simply grants a second damage step [CR 702.4b]; it does not override the blocked-creature damage-assignment restriction.

Review: **correct**. Correct blocked attacker without trample assigns no second-step damage to player.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No. Once the token has left the battlefield (to exile), it cannot be returned to the battlefield. The return effect does nothing to the token; it remains in exile and ceases to exist the next time state-based actions are checked.

Why: Rule 111.8 states that a token that has left the battlefield can't move to another zone or come back onto the battlefield, and if such a token would change zones, it remains in its current zone instead [CR 111.8]. Combined with rule 111.7, which makes a token in a zone other than the battlefield cease to exist as a state-based action [CR 111.7], the token is gone permanently once it reaches exile.

Review: **correct**. Correct token cannot return and only ceases as subsequent SBA.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You can activate "Sacrifice this creature: Draw a card" on the turn you cast the creature, as long as you have priority. Summoning sickness does not restrict it.

Why: Summoning sickness only prevents activating a creature's activated abilities that include the tap ({T}) or untap ({Q}) symbol in their activation cost, and prevents that creature from attacking [CR 302.6] [CR 602.5a]. A sacrifice cost contains neither symbol, so the restriction does not apply. You may activate an activated ability any time you have priority [CR 117.1b], and no other restriction is present on this ability.

Review: **correct**. Correct sacrifice ability without tap-symbol cost can be activated despite summoning sickness.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant in response to the legend rule. The legend rule is a state-based action, which is an automatic game action that does not use the stack and does not grant any player priority to respond.

Why: The legend rule is listed under "The state-based actions are as follows" [CR 704.5] and specifically in [CR 704.5j]. State-based actions are checked automatically by the game (e.g., when a player would receive priority) and are applied immediately; they are not spells or abilities, so no one gets a window to cast an instant or activate an ability between the check and the result. After the spell that caused the duplication finishes resolving [CR 608.2n], the game checks state-based actions, you choose which legendary to keep and the other goes to its owner's graveyard, and only then does the appropriate player receive priority to cast instants.

Review: **correct**. Correct legend-rule SBA occurs before priority; no response window.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality does your creature have protection from (e.g., protection from red, protection from black, protection from a specific player)?
2. What is the removal spell (name or color, and does it target your creature)?

Review: **correct**. Appropriate clarification asks protection quality and removal spell/characteristics. Minor UI defect: closing `[[Exact Card Name]]` markup is missing in question 2; no rules error.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

