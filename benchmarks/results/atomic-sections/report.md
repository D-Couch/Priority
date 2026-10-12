# atomic-sections

Status: **complete** · implementation commit `b486636207b2f856a53c2aeaeb072191c7ff8432`

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
| Reviewed fully correct | 20/20 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 10.21 s |
| p95 successful response | 16.35 s |
| Median first visible answer token | 8.69 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.32 |
| 02-hold-priority (r1) | 100.0% | correct | 8.56 |
| 03-illegal-target (r1) | 100.0% | correct | 7.31 |
| 04-partial-targets (r1) | 100.0% | correct | 8.61 |
| 05-trample-indestructible (r1) | 100.0% | correct | 13.95 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 9.48 |
| 07-zero-toughness (r1) | 100.0% | correct | 13.11 |
| 08-commander-dies (r1) | 100.0% | correct | 21.20 |
| 09-commander-tax (r1) | 100.0% | correct | 8.40 |
| 10-rest-in-peace (r1) | 75.0% | correct | 8.24 |
| 11-token-doublers (r1) | 100.0% | correct | 13.39 |
| 12-replacement-choice (r1) | 100.0% | correct | 10.99 |
| 13-apnap (r1) | 100.0% | correct | 12.34 |
| 14-humility-anthem (r1) | 100.0% | correct | 10.94 |
| 15-own-hexproof (r1) | 100.0% | correct | 7.27 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.66 |
| 17-token-blink (r1) | 100.0% | correct | 12.48 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 8.14 |
| 19-legend-response (r1) | 50.0% | correct | 16.35 |
| 20-clarify-interaction (r1) | 100.0% | correct | 7.84 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. You cannot respond to your opponent tapping a basic Forest for mana.

Why: A basic Forest's tap-for-mana ability is an activated mana ability, which doesn't go on the stack and therefore can't be targeted, countered, or otherwise responded to; it resolves immediately after activation [CR 605.3b]. The ability meets all criteria for a mana ability: it requires no target, adds mana to the player's mana pool, isn't a loyalty ability, and doesn't move cards to or from a library [CR 605.1a].

Review: **correct**. Correct activated mana ability ruling, immediate resolution, and supporting rules.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again before your opponent. No, the instant does not resolve immediately; it waits on the stack until all players pass in succession.

Why: When you have priority and cast a spell, you are the one who receives priority afterward [CR 117.3c]. The spell sits on the stack, and it only resolves once every player has passed in succession without taking an action in between [CR 405.5] [CR 117.4] [CR 608.1]. Your opponent therefore gets a chance to respond before the instant resolves.

Review: **correct**. Correct priority returned to caster and all players passing. Both canonical references now fit; same mean recall conceals changing coverage between cases.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No. You do not draw a card.

Why: When Defiant Strike tries to resolve, the destroyed creature is no longer on the battlefield, making it an illegal target [CR 608.2b]. Because that is the spell's only target, all targets are illegal, so the spell doesn't resolve and is put into its owner's graveyard [CR 608.2b]. The card-specific ruling confirms this: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correct no draw with sole target illegal and whole spell not resolving.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes, the remaining legal creature takes 2 damage.

Why: Because not *all* targets are illegal, the spell resolves normally; only the illegal target is skipped. [CR 608.2b] states that if all targets are illegal the spell doesn't resolve, but "otherwise, the spell or ability will resolve normally," and "illegal targets, if any, won't be affected" while "other parts of the effect for which those targets are not illegal may still affect them." The Plague Spores example in the same rule illustrates this exact pattern: one target became illegal, the other remained legal, and the spell still resolved affecting the legal target.

Review: **correct**. Correct remaining legal target takes damage and partial illegality does not stop resolution.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You may assign 2 damage to the 2/2 indestructible blocker and 4 damage to the defending player.

Why: Trample requires you to assign "lethal damage" (here, 2 damage, equal to the blocker's toughness) to the blocking creature before excess damage may go to the player [CR 702.19b]. Indestructible means the creature "isn't destroyed by lethal damage" and ignores the state-based action that would destroy it [CR 702.12b], but it does not raise the assignment threshold above the creature's toughness. The protection example in 702.19b confirms the threshold is set by the blocker's toughness regardless of whether the damage would actually be dealt or the creature destroyed.

Review: **correct**. Correct 2/4 assignment and indestructibility distinction with both operative definitions.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: You can assign a maximum of 4 damage to the defending player.

Why: Because your attacker has deathtouch, any nonzero amount of damage assigned to the 8/8 blocker counts as lethal damage for trample purposes [CR 702.2c]. Trample requires you to assign lethal damage to the blocker before assigning excess damage to the player [CR 702.19b]. So you assign 1 damage to the 8/8 (satisfying the lethal-damage requirement) and the remaining 4 damage to the defending player.

Review: **correct**. Correct maximum 4 and explicit nonzero deathtouch assignment rule.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No. The indestructible 3/3 does not survive; it is put into its owner's graveyard when its toughness becomes 0.

Why: Indestructible prevents a permanent from being destroyed and lets it ignore the state-based action for lethal damage (rule 704.5g) [CR 702.12b]. However, a creature with toughness 0 or less is put into its owner's graveyard by a separate state-based action (rule 704.5f) that is not a "destruction" event and is not the lethal-damage check [CR 704.5f]. Indestructible does not prevent that action, so the 0/0 creature goes to the graveyard.

Review: **correct**. Correct 0/0 goes to graveyard; explicitly distinguishes lethal-damage destruction from zero-toughness action.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes to both. You may put your commander into the command zone, and "dies" (leaves-the-battlefield) triggers still fire.

Why: Rule 903.9a makes moving a commander from the graveyard to the command zone a state-based action the owner may take, not a replacement effect, so it applies even when no replacement effect is present [CR 903.9a]. The "dies" trigger condition is met the moment the permanent moves from the battlefield to the graveyard; that zone-change event is not undone by the subsequent state-based action moving it to the command zone [CR 603.6c]. Leaves-the-battlefield triggers "look back in time" to confirm the permanent left the battlefield, so they trigger regardless of where the card ends up afterward [CR 603.10a].

Review: **correct**. Correct requested conclusions and repaired timing: explicitly puts state-based actions before waiting triggers are put on the stack, citing 704.3.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax on your next cast from the command zone is {4}.

Why: The tax is "{2} for each previous time the player casting it has cast it from the command zone that game" [CR 903.8]. You have cast it from the command zone twice previously, so the additional cost is 2 × {2} = {4}. The cast from your hand does not count toward the tax, since the rule specifically tracks casts *from the command zone* [CR 903.8].

Review: **correct**. Correct additional 4 and excludes hand cast. Citation ID now correct.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger.

Why: Rest in Peace's replacement effect exiles the creature instead of putting it into a graveyard [C1]. "Dies" specifically means "is put into a graveyard from the battlefield" [CR 700.4], so because the creature is exiled rather than placed in a graveyard, the "dies" event never occurs and Blood Artist's trigger condition is never met [C5].

Review: **correct**. Correct no Blood Artist trigger, exile replaces graveyard entry, and no dies event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4** tokens. The two doublers do **not** loop forever.

Why: Both Doubling Season and Anointed Procession are replacement effects that apply "if an effect would create one or more tokens under your control" [C1][C7]. Rule 614.16 explicitly states that these replacement effects apply even when another replacement effect has already modified the event, so the second doubler applies to the already-doubled number [CR 614.16]. This is the same multiplicative stacking confirmed by the Doubling Season ruling: two doublers yield four times the original [C2]. However, each replacement effect gets only one opportunity to affect an event and does not invoke itself repeatedly [CR 614.5], so the chain stops after both doublers have each applied once (1 → 2 → 4).

Review: **correct**. Correct four tokens and each replacement applies once to the event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: You (the affected player) choose the order. If you apply the doubling effect first, the damage goes 3 → 6 → 7. If you apply the +1 effect first, it goes 3 → 4 → 8. Both 7 and 8 are valid final results.

Why: When multiple replacement effects modify the same event, the affected player chooses which applies first [CR 616.1]. After one effect is applied, the process repeats with the remaining applicable effects [CR 616.1f]. Doubling is a replacement effect that changes the amount to twice the current value [CR 701.10g], so the order of application determines whether the +1 is doubled or not.

Review: **correct**. Correct affected-player choice, both arithmetic orders, and once-per-effect restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: Because neither ability triggers from another ability triggering, both are placed in the first part of the process, in APNAP order: Alice (active player) puts her ability on the stack first, then Bob puts his on top [CR 603.3b]. Each new object is placed on top of all objects already there [CR 405.2], so Bob's ability sits above Alice's. When all players pass in succession, the top (last-added) ability resolves [CR 405.5], which is Bob's.

Review: **correct**. Correct APNAP order and last-in-first-out resolution with supporting sources.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is 2/2. It does not matter which enchantment entered the battlefield first.

Why: Humility's "have base power and toughness 1/1" is an effect that refers to base power and toughness, so it applies in layer 7b [CR 613.4b]. Glorious Anthem's "get +1/+1" is a modifying effect that applies in layer 7c [CR 613.4c]. Because they operate in different sublayers, the layer system—not timestamp order—determines the sequence [CR 613.7], so the creature's base P/T is set to 1/1 first, then +1/+1 is added, yielding 2/2 regardless of entry order.

Review: **correct**. Correct 2/2 and sublayer order regardless of timestamps.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own creature with hexproof using your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Because you control both the creature and the Giant Growth spell, the hexproof restriction does not apply to your own targeting. Giant Growth simply requires "target creature" [C1], and your creature is a legal target for a spell you control.

Review: **correct**. Correct own-creature targeting and opponents-only hexproof restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step your 3/3 assigns no combat damage at all, so the player takes 0.

Why: Your attacker is still a *blocked* creature in the second combat damage step (it was declared as blocked), but the 2/2 is no longer on the battlefield. Rule 510.1c states that a blocked creature with no creatures currently blocking it "assigns no combat damage." Trample (702.19d) is the specific exception that lets a blocked attacker's excess damage reach the player when its blockers are gone; without trample, that exception does not apply.

Review: **correct**. Correct no second-step damage and continued blocked status without trample; no false first-step sequence. Cites rule numbers in prose rather than bracketed IDs, so the UI citation-format check does not detect links for this answer. This formatting defect is separate from substantive correctness.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No, the token does not return to the battlefield. Once it has been exiled (i.e., left the battlefield), it cannot come back.

Why: [CR 111.8] states that a token that has left the battlefield can't move to another zone or come back onto the battlefield; if such a token would change zones, it remains in its current zone instead. So when the second part of the effect tries to return the token, that action simply doesn't occur—the token stays in exile and ceases to exist the next time state-based actions are checked per [CR 111.7].

Review: **correct**. Correct no return under 111.8 and later cessation at the next state-based check under 111.7. Compact section packing now preserves both definitions and exceptions despite prompt-budget pressure; response finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You may activate "Sacrifice this creature: Draw a card" on the turn you cast the creature, as long as you have priority.

Why: Summoning sickness (rule 302.6) restricts only activated abilities whose activation cost includes the tap symbol ({T}) or the untap symbol ({Q}), and it restricts attacking. A sacrifice cost contains neither symbol, so the restriction does not apply. You may activate the ability any time you have priority [CR 117.1b].

Review: **correct**. Correct activation while priority is available and absence of tap/untap-symbol restriction. Names 302.6 in prose and brackets 117.1b; no unsupported timing claim.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant (or take any other action) in response to the legend rule. The choice of which legendary permanent to keep is made as part of a state-based action, and no player has priority at that moment.

Why: The legend rule (704.5j) is a state-based action, and state-based actions are performed automatically by the game before any player would receive priority [CR 117.2d] [CR 117.5]. Because no player has priority while the state-based action is being resolved, no player may cast a spell or activate an ability [CR 117.1] [CR 117.1a]. The choice of which duplicate to keep is a mandatory part of that automatic process, not a moment where you receive priority and could respond.

Review: **correct**. Correct no response window, explicit state-based checks before priority, and choice of one legendary permanent. Uses alternative timing evidence 117.5 rather than canonical reference 704.3.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality is your creature's protection from (e.g., "protection from red," "protection from black," "protection from a specific player," "protection from everything")?
2. What is the removal spell (name or text)? Specifically, does it target your creature, and what color/quality does it have?

Review: **correct**. Asks only for the protection quality and the removal spell’s name/text and targeting details. Correct expected clarification, with no premature ruling.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

