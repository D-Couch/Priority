# focused-rulings

Status: **complete** · implementation commit `c9ceef4f9720abcb28ebd8ca228b6289dcd7b42b`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 17/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 93.8% |
| Cases retrieving every expected evidence group | 17/20 |
| Answers with citations | 20/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Reviewed fully correct | 17/20 reviewed |
| Reviewed accuracy | 85.0% |
| Mean reviewed rubric score | 90.0% |
| Median successful response | 9.88 s |
| p95 successful response | 17.72 s |
| Median first visible answer token | 8.43 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 6.53 |
| 02-hold-priority (r1) | 100.0% | correct | 7.56 |
| 03-illegal-target (r1) | 100.0% | correct | 10.12 |
| 04-partial-targets (r1) | 100.0% | correct | 8.46 |
| 05-trample-indestructible (r1) | 100.0% | correct | 13.70 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 9.64 |
| 07-zero-toughness (r1) | 100.0% | incorrect | 10.38 |
| 08-commander-dies (r1) | 100.0% | correct | 15.42 |
| 09-commander-tax (r1) | 100.0% | correct | 7.06 |
| 10-rest-in-peace (r1) | 75.0% | correct | 7.49 |
| 11-token-doublers (r1) | 100.0% | correct | 17.72 |
| 12-replacement-choice (r1) | 100.0% | correct | 9.53 |
| 13-apnap (r1) | 100.0% | correct | 11.40 |
| 14-humility-anthem (r1) | 100.0% | correct | 13.14 |
| 15-own-hexproof (r1) | 100.0% | correct | 6.87 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.24 |
| 17-token-blink (r1) | 50.0% | incorrect | 21.81 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 7.77 |
| 19-legend-response (r1) | 50.0% | correct | 11.85 |
| 20-clarify-interaction (r1) | 100.0% | partial | 8.82 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**No.** You cannot respond to your opponent tapping a basic Forest for mana.

A basic Forest's tap ability ("{T}: Add {G}") is a mana ability [CR 305.6]. Mana abilities don't go on the stack, so they can't be targeted, countered, or otherwise responded to; they resolve immediately after being activated [CR 605.3b].

Review: **correct**. Correct activated mana ability ruling, immediate resolution, and supporting rules.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

**Ruling:** Yes, you get priority back first. No, the instant does not resolve immediately.

**Explanation:**

When you cast the instant, it goes on the stack. You then receive priority again before your opponent, so you have the first chance to respond (e.g., cast another instant or activate an ability). [CR 117.3c]

The instant only resolves once **all** players pass in succession. Your opponent gets a chance to respond before it resolves. [CR 608.1] [CR 405.5]

Review: **correct**. Correct priority returned to caster and all players passing. Both canonical references now fit; same mean recall conceals changing coverage between cases.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**No, you do not draw a card.**

Defiant Strike has only one target: the creature. When it resolves, that creature is no longer on the battlefield, so the target is illegal. Since **all** of the spell's targets are illegal, the spell doesn't resolve at all — it's removed from the stack and put into its owner's graveyard, and none of its effects (including the card draw) happen.

This is the same principle as the Sorin's Thirst example: if the target is illegal at resolution, the spell doesn't resolve and its controller gains no life. [CR 608.2b]

Review: **correct**. Correct no draw with sole target illegal and whole spell not resolving.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Yes, the remaining creature takes 2 damage.**

When a spell or ability resolves, it checks whether its targets are still legal. If *all* targets are illegal, the spell doesn't resolve at all. But if at least one target remains legal, the spell resolves normally and affects only the legal target(s). The illegal target simply isn't affected by the effect.

In your case, one target left the battlefield (making it illegal), but the other is still a legal target. The spell resolves and deals 2 damage to the remaining creature.

This is the same principle illustrated by the Plague Spores example: one target became illegal, the other remained legal, and the spell still resolved and destroyed the legal target. [CR 608.2b]

Review: **correct**. Correct remaining legal target takes damage and partial illegality does not stop resolution.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Yes.** You must assign at least 2 damage to the blocker (lethal damage) and may assign the remaining 4 to the defending player.

Indestructible prevents the creature from being *destroyed* by lethal damage, but it does not change what counts as "lethal damage" for trample purposes. The trample rule requires you to assign lethal damage (damage equal to the creature's toughness, here 2) to the blocker before assigning excess to the player. The creature's toughness is still 2 regardless of its indestructible status.

This is analogous to the protection example in the rules: even if the damage assigned to the blocker would be prevented or have no effect, the controller must still assign lethal damage to it before trampling through. [CR 702.19b] [CR 702.12b]

Review: **correct**. Correct 2/4 assignment and indestructibility distinction with both operative definitions.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling: 4 damage.**

**Explanation:**

Trample requires that the blocking creature be assigned lethal damage before excess damage can be assigned to the defending player [CR 702.19b]. Normally, an 8/8 would need 8 damage assigned to satisfy this. However, deathtouch changes the threshold: "Any nonzero amount of combat damage assigned to a creature by a source with deathtouch is considered to be lethal damage for the purposes of determining if excess damage is being dealt" [CR 702.2c].

So you must assign at least 1 damage to the 8/8 blocker, and the remaining 4 damage can be assigned to the defending player.

Review: **correct**. Correct maximum 4 and explicit nonzero deathtouch assignment rule.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**Yes, it survives.**

The -3/-3 makes the creature a 0/0, which would normally trigger the state-based action in [CR 704.5f]: "If a creature has toughness 0 or less, it's put into its owner's graveyard." However, [CR 702.12b] states that a permanent with indestructible "ignore[s] the state-based action that checks for lethal damage." Since indestructible causes the creature to ignore that specific state-based action, it remains on the battlefield as a 0/0 until the "until end of turn" effect expires during the cleanup step (per [CR 514.2]).

Review: **incorrect**. Incorrectly keeps a 0/0 alive. Both operative rules were provided, but the answer extends indestructibility’s lethal-damage exception to zero toughness. This is a rule-application failure despite complete evidence.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling:** Yes to both. You may move your commander to the command zone, and "dies" triggers still fire.

**Explanation:**

When your commander is destroyed, it is put into the graveyard from the battlefield. That event satisfies the definition of "dies" [CR 700.4]. The trigger event has already occurred, so the ability automatically triggers [CR 603.2].

After that, state-based actions are checked. Since your commander is in the graveyard and was put there since the last time state-based actions were checked, you *may* put it into the command zone [CR 903.9a]. This is a state-based action, not a replacement effect, so it doesn't prevent the trigger from having already fired.

Leaves-the-battlefield triggers (including "dies" triggers) look back in time to the event that caused the zone change [CR 603.10a]. The commander was put into the graveyard from the battlefield; that's the event that triggered the ability. Moving it to the command zone afterward doesn't retroactively cancel the trigger.

Review: **correct**. Correct both conclusions with graveyard entry, dies trigger, and subsequent command-zone state-based action. The unsupported extra targeted-ability caveat is gone.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is **{4}**.

**Explanation:** Rule 903.8 states that a commander cast from the command zone costs an additional {2} "for each previous time the player casting it has cast it **from the command zone** that game." Only casts from the command zone count toward the tax. Since you have previously cast it from the command zone twice, the tax is 2 × {2} = {4}. The cast from your hand does not contribute to the count. [CR 903.8]

Review: **correct**. Correct additional 4 and excludes hand cast. Citation ID now correct.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**No, Blood Artist does not trigger.**

"Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect causes the creature to be exiled instead of being put into a graveyard [C1]. Since the creature is never actually put into a graveyard, it does not die, and Blood Artist's trigger condition is never met [C5].

Review: **correct**. Correct no Blood Artist trigger, exile replaces graveyard entry, and no dies event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

**You create 4 tokens. The doublers do not loop forever.**

**Explanation:**

Both Doubling Season and Anointed Procession are replacement effects that modify the same event (creating 1 token). Under [CR 616.1], you (the affected player) choose which one applies first. Suppose you choose Doubling Season:

1. **Doubling Season applies:** 1 token → 2 tokens.
2. **CR 616.1f** then says the process is repeated with any remaining applicable effects. Anointed Procession is still applicable to the modified event (which now creates 2 tokens).
3. **Anointed Procession applies:** 2 tokens → 4 tokens.
4. No more applicable replacement effects remain, so the process stops.

The reason this doesn't loop infinitely is [CR 614.5]: *"A replacement effect doesn't invoke itself repeatedly; it gets only one opportunity to affect an event or any modified events that may replace that event."* Each doubler fires exactly once.

This is directly analogous to the example in [CR 614.5], where two "double the damage" effects on a creature dealing 2 damage result in 8 damage (2 × 2 × 2), not an infinite amount.

Review: **correct**. Correct four tokens and each replacement applies once to the event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** The affected player (you) chooses the order, and the final damage can be either **7** or **8**.

**Explanation:**

- **Who chooses:** Under [CR 616.1], when two or more replacement effects are attempting to modify the same event, the affected player chooses which one to apply first. Since neither effect is a self-replacement effect, a control-changing effect, a copy effect, or a back-face effect, the choice falls to [CR 616.1e]: "Any of the applicable replacement and/or prevention effects may be chosen."

- **Possible outcomes:**
  - **Double first, then +1:** 3 → 6 → **7**
  - **+1 first, then double:** 3 → 4 → **8**

After the first effect is applied, the process repeats with the remaining effect per [CR 616.1f]. Doubling is a replacement effect per [CR 701.10g], so it applies to whatever amount of damage the source "would deal" at that moment.

Review: **correct**. Correct affected-player choice, both arithmetic orders, and once-per-effect restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Bob's triggered ability resolves first.**

When multiple triggered abilities are waiting to go on the stack, they are placed in APNAP (Active Player, then Non-Active Player) order. Since it is Alice's turn, she is the active player and puts her ability on the stack first; Bob, as the non-active player, puts his ability on the stack second [CR 603.3b]. Each object placed on the stack goes on top of everything already there [CR 405.2], so Bob's ability ends up on top. When all players pass in succession, the topmost object on the stack resolves [CR 608.1], meaning Bob's ability resolves before Alice's.

Review: **correct**. Correct APNAP order and last-in-first-out resolution with supporting sources.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

**Ruling: The creature is 2/2. It does not matter which enchantment entered first.**

**Explanation:**

The two effects apply in different sublayers of layer 7, so their relative order is fixed by the layer system regardless of timestamp:

1. **Layer 7b** – Humility's "have base power and toughness 1/1" is an effect that sets power and toughness to a specific value. [CR 613.4b] states: "Effects that set power and/or toughness to a specific number or value are applied. Effects that refer to the base power and/or toughness of a creature apply in this layer."

2. **Layer 7c** – Glorious Anthem's "get +1/+1" is a modifying effect (it doesn't set P/T to a specific value). [CR 613.4c] states: "Effects and counters that modify power and/or toughness (but don't set power and/or toughness to a specific number or value) are applied."

Since 7b always applies before 7c, the creature's base P/T is set to 1/1 first, then +1/+1 is added on top, yielding **2/2**. This is the same result whether Humility or Glorious Anthem entered the battlefield first, because sublayer order is determined by the rules, not by timestamp.

This mirrors the example in [CR 613.5]: "An effect that says 'Target creature becomes 0/1 until end of turn' is applied to it (layer 7b), making it 5/8 (0/1, with +4/+4 from the resolved spell, +0/+2 from the enchantment, and +1/+1 from the counter)."

Review: **correct**. Correct 2/2 and sublayer order regardless of timestamps.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Yes.** You may target your own hexproof creature with your own Giant Growth.

Hexproof on a permanent means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you are the controller of both the creature and the spell, hexproof imposes no restriction on your targeting. Giant Growth simply requires "target creature" [C1], and your creature is a legal target for your own spell.

Review: **correct**. Correct own-creature targeting and opponents-only hexproof restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**No.** The attacker assigns no combat damage in the second combat damage step.

The creature is still considered *blocked* (that status persists even after the blocker dies). Rule 510.1c explicitly covers this situation:

> "A blocked creature assigns its combat damage to the creatures blocking it. **If no creatures are currently blocking it (if, for example, they were destroyed or removed from combat), it assigns no combat damage.**" [CR 510.1c]

The rule that would let a blocked creature with no current blockers assign damage to the player is trample:

> "If an attacking creature with trample or trample over planeswalkers is blocked, but there are no creatures blocking it when damage is assigned, its damage is assigned to the defending player and/or planeswalker as though all blocking creatures have been assigned lethal damage." [CR 702.19d]

Since your 3/3 does **not** have trample, that exception doesn't apply. It simply assigns no damage in the second combat damage step.

Review: **correct**. Correct no second-step player damage and explicit continued blocked status without trample.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Yes, the token returns to the battlefield.**

A token ceasing to exist when it's in a zone other than the battlefield is a **state-based action**, not an immediate effect [CR 111.7]. State-based actions are checked when a player would receive priority, not between the individual steps of a single spell or ability's resolution. So during the resolution of the effect that both exiles and returns the token, the token still exists in exile when the "return it" instruction is applied. It is successfully put back onto the battlefield before state-based actions are ever checked.

If the exile and the return were instead two *separate* effects (e.g., one effect exiles it, then a later effect tries to return it), the token would have ceased to exist by the time the second effect looks for it, and the return would fail.

Review: **incorrect**. Incorrectly returns the token during resolution. Packing omitted 111.8 after the longer prompt changed the remaining budget, leaving only 111.7. The answer mistakes existence before state-based checks for permission to change zones again.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 111.8

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

**Yes, you can activate it this turn.**

Summoning sickness (rule 302.6) only restricts a creature's activated abilities that include the **tap symbol** ({T}) or the **untap symbol** ({Q}) in their activation cost. Your ability's cost is "Sacrifice this creature," which contains neither symbol, so the restriction does not apply.

As long as you have priority, you may activate the ability. [CR 117.1b] states a player may activate an activated ability any time they have priority, and [CR 302.6] limits only tap/untap-cost abilities for creatures that haven't been under their controller's control continuously since their most recent turn began.

Review: **correct**. Correct sacrifice activation and tap/untap-symbol distinction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

**No.** You cannot respond to the legend rule with an instant.

The legend rule is a state-based action. State-based actions are handled automatically and are dealt with **before** a player would receive priority [CR 117.2d]. After a spell resolves, the sequence is:

1. The spell finishes resolving.
2. State-based actions are checked. If the legend rule applies, you choose one of the matching legendary permanents to keep, and the rest are put into their owners' graveyards [CR 704.5j].
3. Only then does the active player receive priority [CR 117.3b].

Because the choice and the resulting graveyard placement happen as part of the state-based action—before anyone gets priority—there is no window to cast an instant "in response." By the time you have priority, the excess permanents are already in the graveyard.

Review: **correct**. Correct no response window, explicit state-based checks before priority, and choice of one legendary permanent. Uses alternative timing evidence 117.5 rather than canonical reference 704.3.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

**It depends on the quality of the protection and the removal spell.**

Protection from a quality prevents a creature from being **targeted** by spells with that stated quality [CR 702.16b]. So:

- **Safe:** If your creature has "Protection from red" and your opponent casts a red spell that targets it, the spell can't target your creature.
- **Not safe:** If the removal spell doesn't target (e.g., a board wipe like *Wrath of God*), protection doesn't help. Similarly, if the spell has a different color than what your creature has protection from, it can still target and destroy your creature.

**Key question:** What quality does your creature have protection from, and what is the removal spell? If you share those details, I can give a definitive answer.

Review: **partial**. Asks both clarifications, but still offers hypothetical rulings and broadly says protection does not help if removal does not target. This remains false for preventable non-targeted damage of the relevant quality.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

