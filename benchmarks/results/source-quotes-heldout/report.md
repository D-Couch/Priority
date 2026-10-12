# source-quotes-heldout

Status: **complete** · implementation commit `6f31339abfd5340942dfa993252f48d1e50e7f60`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 25/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 75.5% |
| Cases retrieving every expected evidence group | 15/32 |
| Answers with citations | 29/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 4 |
| Reviewed citation-support failures | 9 |
| Reviewed fully correct | 25/32 reviewed |
| Reviewed accuracy | 78.1% |
| Mean reviewed rubric score | 90.6% |
| Median successful response | 10.25 s |
| p95 successful response | 28.99 s |
| Median first visible answer token | 9.05 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 14.33 |
| h02-intervening-if (r1) | 100.0% | correct | 7.35 |
| h03-independent-trigger (r1) | 50.0% | correct | 18.10 |
| h04-replacement-death (r1) | 75.0% | correct | 8.06 |
| h05-simultaneous-death (r1) | 100.0% | partial | 8.46 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 7.04 |
| h07-infect-lifelink (r1) | 100.0% | correct | 14.30 |
| h08-protection-wrath (r1) | 100.0% | correct | 11.01 |
| h09-protection-aura (r1) | 100.0% | correct | 6.12 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.60 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 10.47 |
| h12-split-second (r1) | 100.0% | correct | 14.79 |
| h13-sacrifice-cost (r1) | 66.7% | partial | 10.01 |
| h14-flashback-countered (r1) | 66.7% | correct | 10.03 |
| h15-rebound-countered (r1) | 66.7% | correct | 8.20 |
| h16-persist-counter (r1) | 100.0% | correct | 7.86 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 28.99 |
| h18-blink-target (r1) | 75.0% | correct | 13.54 |
| h19-equip-timing (r1) | 75.0% | correct | 16.55 |
| h20-crew-new-creature (r1) | 66.7% | correct | 11.03 |
| h21-new-vehicle (r1) | 50.0% | correct | 8.59 |
| h22-tapped-blocker (r1) | 0.0% | correct | 13.69 |
| h23-fight-double-strike (r1) | 100.0% | partial | 10.81 |
| h24-leaving-controller (r1) | 50.0% | partial | 34.42 |
| h25-leaving-stack (r1) | 50.0% | abstained | 12.33 |
| h26-commander-control (r1) | 0.0% | abstained | 20.19 |
| h27-commander-hand (r1) | 100.0% | correct | 7.91 |
| h28-replacement-order (r1) | 100.0% | correct | 11.78 |
| h29-empty-library (r1) | 100.0% | correct | 9.04 |
| h30-ambiguous-combat (r1) | 100.0% | correct | 9.76 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 8.30 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 9.19 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The triggered abilities go on the stack in the order Alice (bottom), Bob, Charlie (top). They resolve in the order Charlie, Bob, Alice.

Why: [CR 405.3] states that when multiple objects are put on the stack at the same time, "those controlled by the active player are put on lowest, followed by each other player's objects in APNAP order." Alice is the active player, so her ability is placed lowest; Bob's and Charlie's follow in APNAP order. [CR 608.1] then dictates that "the spell or ability on top of the stack resolves" first, so Charlie's (top) resolves, then Bob's, then Alice's (bottom).

Review: **correct**. Correct APNAP stack and reverse resolution; now cites applicable 405.3 and 608.1 rather than the shared-team rule.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: [CR 603.4] states, "If the ability triggers, it checks the stated condition again as it resolves. If the condition isn't true at that time, the ability is removed from the stack and does nothing." The example in the same rule confirms: "If that player has 39 or less life at this time, the ability is removed from the stack and has no effect." Since you dropped to 39 life before resolution, the intervening "if" clause fails and the win condition is not met.

Review: **correct**. Correct no win; CR 603.4 and Felidar ruling support checking again at resolution.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. You may still search your library for a basic land card, put it onto the battlefield tapped, and shuffle. The Simulacrum being destroyed before the ability resolves does not prevent the search.

Why: The triggered ability is on the stack as an independent object with only its own text: "you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle" [C1]. That effect does not attempt to do anything to the Simulacrum itself, so the zone-change limitation in [CR 603.6] ("the part of the ability attempting to do something to the object will fail to do anything") does not apply. The "may" choice is simply made when the ability resolves [CR 603.5], and the ability's text has no reference to the Simulacrum's location [CR 405.4].

Review: **correct**. Correct search survives source removal; still lacks 113.7a. Zone-change discussion and 405.4 do not directly establish the general independence rule.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "When this creature dies, you may draw a card" ability does not trigger.

Why: [CR 700.4] defines "dies" as "is put into a graveyard from the battlefield." Rest in Peace's replacement effect states "If a card or token would be put into a graveyard from anywhere, exile it instead" [C1], so the card is never actually put into a graveyard. The card-specific ruling confirms this directly: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Correct exile replacement prevents dies trigger; Oracle and card ruling establish it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers **3 times** (once for itself dying and once for each of the two tokens dying).

Why: The card-specific ruling states, "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures." [C2] With three creatures dying simultaneously, that is three separate trigger events. This is consistent with the general rule that leaves-the-battlefield triggers "look back in time," so the ability triggers for each creature even though they all move to the graveyard in the same state-based actions step. [CR 603.10a]

Review: **partial**. Three triggers is correct, but explanation assumes all deaths occurred during state-based actions; the question does not specify that and simultaneous deaths can occur during spell resolution. 603.10a does not support that added timing assertion.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: [CR 702.15b] states "Damage dealt by a source with lifelink causes that source's controller… to gain that much life." Because all 3 damage is prevented, no damage is *dealt*; the lifelink condition is never met, so no life gain occurs.

Review: **correct**. Zero life; lifelink requires damage actually dealt under CR 702.15b.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, your opponent gets 3 poison counters, and you gain 3 life.

**Why:**

- Infect replaces the life-loss result: "Damage dealt to a player by a source with infect doesn't cause that player to lose life. Rather, it causes that source's controller to give the player that many poison counters." [CR 702.90b]
- Lifelink adds a separate result for the controller: "Damage dealt by a source with lifelink causes that source's controller… to gain that much life (in addition to any other results that damage causes)." [CR 702.15b]

Infect only changes what happens to the player being damaged (poison counters instead of life loss). Lifelink's life gain is an additional result that applies to the source's controller regardless, so both effects apply simultaneously: the opponent receives 3 poison counters in place of losing 3 life, and you gain 3 life.

Review: **correct**. Correct totals; no longer classifies infect or lifelink as replacement effects. Quotes their damage-result rules. Ordinary wording about replacing life loss is not a technical replacement-effect classification.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature. Protection from white does not prevent it.

Why: Wrath of God reads "Destroy all creatures" [C1]. It does not target, deal damage, enchant, equip, or block. Protection from white only prevents being targeted by white spells, enchanted by white Auras, dealt damage by white sources, blocked by white creatures, or equipped by white Equipment [CR 702.16b]–[CR 702.16f]. None of those clauses apply to a non-targeting "destroy all creatures" effect, so the creature is destroyed.

Review: **correct**. Wrath destroys; cited protection clauses do not stop nontargeting destruction.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The white Aura is put into its owner's graveyard as a state-based action.

Why: [CR 702.16c] states that a permanent with protection "can't be enchanted by Auras that have the stated quality" and that "[s]uch Auras attached to the permanent or player with protection will be put into their owners' graveyards as a state-based action." Once the creature gains protection from white, the attached white Aura no longer legally enchants it, so the state-based action removes it to its owner's graveyard.

Review: **correct**. Aura goes to owner graveyard as SBA, directly supported by CR 702.16c.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes, you can target your own Slippery Bogle with your own Giant Growth.

Why: Hexproof on a permanent means "This permanent can't be the target of spells or abilities **your opponents** control." [CR 702.11b] Since you control both the Bogle and the Giant Growth, the spell is not controlled by an opponent, so the hexproof restriction does not apply to you.

Review: **correct**. Own Giant Growth is allowed; hexproof only restricts opponent-controlled targeting.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost. Abrupt Decay resolves and destroys the target.

Why: Abrupt Decay's Oracle text states "This spell can't be countered" [C1]. Ward's effect is "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but the card-specific ruling confirms the interaction directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2]. Because Abrupt Decay cannot be countered, the ward's counter instruction simply has no effect; the spell proceeds to resolve and destroy the target.

Review: **correct**. Ward triggers without countering uncounterable Decay; correct resolution, supported by Oracle and dated ruling.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. You may turn Willbender face up as a special action while Krosan Grip is on the stack, its triggered ability goes on the stack above Grip, and you can use it to change Grip's target to your other artifact.

Why:

- Turning a face-down permanent face up is a special action: "This is a special action; it doesn't use the stack" [CR 702.37e].
- Special actions are permitted during split second: "Players may activate mana abilities and take special actions while a spell with split second is on the stack" [CR 702.61b].
- The morph trigger fires: "The trigger occurs when you use the Morph ability to turn the card face up" [C13].
- The triggered ability is placed on the stack normally: "Triggered abilities trigger and are put on the stack as normal while a spell with split second is on the stack" [CR 702.61b].
- Because it is put on the stack after Grip, it sits on top and resolves first: "Each time an object is put on the stack, it's put on top of all objects already there" [CR 405.2].
- Willbender's ability reads "change the target of target spell or ability with a single target" [C8], and Krosan Grip targets "target artifact or enchantment" [C1], which is a single target, so Grip is a legal target for Willbender's ability.

The net result: Willbender's ability resolves, redirects Grip to your other artifact, and then Grip resolves destroying that artifact instead of the first one.

Review: **correct**. Correct morph special action and normal triggered ability despite split second; relevant clauses cited.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond to destroy the sacrificed creature, because the sacrifice is paid as part of the cost to cast Fling, which is completed before the spell is on the stack and before anyone receives priority to respond.

Why: [C3] states, "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." The sacrifice occurs during the cost-payment step of casting (before the spell is fully cast), so no one gets a window to act on that creature in response. Once Fling is on the stack, the creature is already in the graveyard.

Review: **partial**. No response to sacrifice is correct, but again explicitly says casting costs complete before spell is on stack. 601.2a places spell there before 601.2h cost payment.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 601.2h

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice is exiled, and you do not draw a card.

Why: [CR 702.34a] states, "If the flashback cost was paid, exile this card instead of putting it anywhere else any time it would leave the stack," and [C2] confirms, "A spell cast using flashback will always be exiled afterward, whether it resolves, is countered, or leaves the stack in some other way." Because the spell was countered, it never resolved, so the "Draw a card" instruction in [C1] was never followed (resolution is when the controller "follows its instructions," per [CR 608.2c]).

Review: **correct**. Correct exile and no draw. Flashback citation supports exile; CR 608.2c is a resolution-instructions rule, not support for the claimed countered-spell rule (701.5a).
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If Ephemerate is countered, rebound does not exile it and you do not get to cast it on your next upkeep. The card is put into its owner's graveyard.

Why: Rebound's replacement effect applies only "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never applies. The card-specific ruling confirms: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Review: **correct**. Correct no rebound because countered spell never resolves; graveyard answer includes harmless qualification about counter effects.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard, persist does not trigger and the card does not return to the battlefield.

Why: Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The Kitchen Finks ruling confirms this: "persist won't trigger and the card won't return to the battlefield" when the creature still has -1/-1 counters on it at the moment it leaves the battlefield [C6]. Since the condition is not met, the ability never triggers.

Review: **correct**. Correct no persist trigger; checks pre-death counter state using persist definition and C6 card ruling.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger. Young Wolf had a +1/+1 counter on it when it was last on the battlefield, so the condition "if it had no +1/+1 counters on it" is not met.

Why: [CR 702.93a] defines undying as triggering only "if it had no +1/+1 counters on it." [CR 603.10a] states that leaves-the-battlefield abilities "look back in time" using "the appearance of objects immediately prior to the event." The [CR 704.8] example uses this exact card: "You control Young Wolf, a 1/1 creature with undying, and it has a +1/+1 counter on it. A spell puts three -1/-1 counters on Young Wolf. … When it was last on the battlefield, it had a +1/+1 counter on it, so undying will not trigger." In your scenario the +1/+1 counter was still on the permanent immediately before it left the battlefield (the -1/-1 counter and the -1/-1 continuous effect merely offset it for P/T calculation; they do not remove the +1/+1 counter), so the "no +1/+1 counters" condition fails and undying does not trigger.

Review: **correct**. Correct undying result and pre-SBA state. The phrase about appearance immediately prior to event is attributed to 603.10a, but belongs to parent 603.10; 704.8 is correctly applied. Reference-label addendum still applies.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. Lightning Bolt will not damage the returned creature; it will fizzle entirely.

**Why:** The Cloudshift ruling states, "The returned card won't be the target of any spells or abilities that targeted it before" [C5]. Because Lightning Bolt's sole target is now illegal, [CR 608.2b] applies: "If all its targets, for every instance of the word 'target,' are now illegal, the spell or ability doesn't resolve." Lightning Bolt is removed from the stack without dealing damage.

Review: **correct**. Correct returned object is new and Bolt has no legal target; Cloudshift ruling and 608.2b support answer.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

**Why:** The equip ability reads "Equip only as a sorcery" [C2], and rule 702.6a confirms the timing restriction: "Activate only as a sorcery" [CR 702.6a]. This means the ability can only be activated during your main phase while the stack is empty. Because Lightning Bolt is on the stack, the stack is not empty, so the equip ability is not legally activatable at that moment.

Review: **correct**. Correct no equip in response; previous false claim about +10/+10 not saving creature is gone. Oracle and equip definition support timing.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: Yes. You can tap that 3/3 creature to pay the Crew 1 cost of Smuggler's Copter even though it just came under your control and has no haste.

Why: The Crew ability reads "Tap any number of other untapped creatures you control with total power N or greater" [CR 702.122a]. Your creature is untapped, you control it, and its power (3) meets the threshold (1). The card-specific ruling confirms this explicitly: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." [C12] The lack of haste is irrelevant here because you are not activating a tap ability on the creature; you are simply tapping it as part of the cost to activate the Vehicle's Crew ability.

Review: **correct**. Fixed: allows newly controlled creature to crew and cites the previously omitted C12 ruling. Correctly distinguishes another permanent’s cost from own tap-symbol ability.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No. Because you cast Smuggler's Copter this turn, you have not controlled it continuously since your turn began, and it has no haste, so it cannot attack this turn.

Why: [C10] states, "It can't attack unless you've controlled it continuously since your turn began." Since the Copter entered the battlefield this turn, that condition is not met. [CR 702.10b] confirms that only haste overrides this restriction: "If a creature has haste, it can attack even if it hasn't been controlled by its controller continuously since their most recent turn began." The Copter has no haste, so the normal summoning-sickness restriction applies.

Review: **correct**. Correct new Vehicle cannot attack without haste; card ruling and haste definition support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: Tapping the blocker does **not** remove it from combat and does **not** prevent it from assigning combat damage. It remains a blocking creature and still deals 3 damage to the creature it is blocking.

Why: A creature "remains a blocking creature until it's removed from combat or the combat phase ends" [CR 509.1g]. Tapping is neither removing from combat nor ending the combat phase, so the creature is still blocking. At the combat damage step, "a blocking creature assigns combat damage to the creatures it's blocking" [CR 510.1d], and the only listed reason it would assign no damage is if it "isn't currently blocking any creatures (if, for example, they were destroyed or removed from combat)" [CR 510.1d]. Tapping satisfies none of those conditions, so the 3/3 still assigns 3 damage.

Review: **correct**. Correct blocker remains blocking and deals normal damage; cited combat rules support results, though direct 506.4b omitted.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives as a 4/1. Double strike has no effect here.

**Why:** [CR 701.14a] states "Each of those creatures deals damage equal to its power to the other creature," and [CR 701.14d] states "The damage dealt when a creature fights isn't combat damage." Double strike is defined as "a static ability that modifies the rules for the combat damage step" [CR 702.4a], so it does not apply to a non-combat fight event.

Review: **partial**. Correct damage amounts and survivor, but calls survivor a 4/1. It remains a 4/4 with 3 damage marked; cited fight/double-strike definitions support damage, not a toughness reduction.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: The Control Magic Aura is removed from the game (it leaves the game or is exiled as a result of Bob leaving), and the creature is controlled by Alice, its owner.

Why: Control Magic's text "You control enchanted creature" [C1] is a control-changing effect applied in layer 2 [CR 613.1b]. When Bob loses and leaves the game, objects are affected: "objects may leave the game, cease to exist, change control, or be exiled as a result" [CR 405.6h]. Once the Aura is no longer on the battlefield, its control-changing effect ceases to apply, and the creature is controlled by its owner, Alice. The ruling that "Gaining control of a creature doesn't cause you to gain control of any Auras or Equipment attached to it" [C2] confirms Bob never gained control of the Aura itself; it remained his (as caster/owner) and is therefore the object affected by his departure.

Note: The specific mechanism (whether the Aura "leaves the game" vs. "is exiled") is governed by rule 800.4a, which is referenced by [CR 405.6h] but not included in the supplied excerpts. In standard play, a permanent owned by a player who leaves the game leaves the game.

Review: **partial**. Gives correct control return and finally states owned objects leave, but first says Aura may leave or be exiled. Bob-owned Aura leaves, not exile. Missing 800.4a leads to contradictory mechanism and misapplied C2 attachment ruling.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Need details: The supplied reference excerpts do not include the rules governing what happens to objects a player controls (including spells on the stack) when that player leaves the game (rule 800, "Leaving the Game"). I cannot cite a supporting excerpt for the outcome, so I'm unable to give a ruling based solely on the provided material. If you can supply the relevant rule 800 text (or the specific card/ruling that addresses a player leaving with a spell on the stack), I can give a definitive answer.

Review: **abstained**. Unnecessary abstention on a complete game state because 800.4a was not supplied. Also points to 104.3a rather than the applicable leaving-player rule.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

The specific rule governing commander damage (the 21-combat-damage loss condition and how that damage is tracked) is not included in the supplied reference excerpts. The excerpts cover combat damage assignment (rules 510.x) and commander zone/identity rules (rules 903.1–903.9), but they do not contain the rule that defines how commander damage is accumulated or whether it is tracked per player who received it versus per controller of the commander.

I cannot provide a fully cited ruling without that rule text. If you can supply the relevant commander-damage rule (typically found in rule 903.10 or a nearby subsection), I can give a precise, cited answer.

Review: **abstained**. Unnecessary abstention; same commander deals cumulative 21 regardless of controller. CR 903.10a omitted from context.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 903.10a

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect, not a state-based action.

Why: Rule 903.9b states, "If a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead. This replacement effect may apply more than once to the same event." [CR 903.9b] The state-based action in rule 903.9a applies only when the commander is already in a graveyard or exile, which is a different situation. [CR 903.9a]

Review: **correct**. Correct command-zone option is a hand/library replacement effect under 903.9b, not the graveyard/exile SBA.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace of Rath: 3 + 2 = 5, then 5 × 2 = 10) or **8** (Furnace of Rath first, then Torbran: 3 × 2 = 6, then 6 + 2 = 8).

Why: [C4] states "the player being dealt damage or the controller of the permanent being dealt damage chooses an order in which to apply those effects," and [CR 616.1] confirms "the affected object's controller (or its owner if it has no controller) or the affected player chooses one to apply." Because the opponent is the affected player, they select which replacement effect applies first, yielding either 10 or 8 damage.

Review: **correct**. Correct affected opponent chooses; both 8 and 10 with matching orders, supported by Oracle and 616.1.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having an empty library by itself does not cause you to lose the game. You lose only if you *attempt* to draw a card from that empty library.

Why: The state-based action in [CR 704.5b] requires that "a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked." The loss is keyed to the attempt to draw, not to the library being empty. Since you have not attempted a draw since the library became empty, the condition is not met and no state-based action causes you to lose.

Review: **correct**. Correct no loss merely for empty library; attempted draw condition explicitly cited.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Need details:

1. Does your attacker have trample (or trample over planeswalkers)?
2. What is the attacker's power?
3. What is the toughness of the blocking creature (or creatures), and how many blockers are there?

Review: **correct**. Appropriate clarification asks about trample and attacker/blocker stats, without inventing a total.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No. Your copy does not get the creature's counters, and it does not get the bonus from the enchantment attached to the original creature.

Why: [CR 707.2] states that "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." Counters are explicitly excluded, and an enchantment's ongoing bonus is an "other effect" that is likewise not part of the copiable values. The copy acquires only the values derived from the text printed on the object (as modified by other copy effects, face-down status, and certain "as it enters" abilities), so neither the counters nor the enchantment's bonus transfer to the copy.

Review: **incorrect**. Fails frozen clarification criteria: gives unconditional answer without asking copy effect/enchantment details. 707.2 describes ordinary copy values but includes exceptions; unspecified effects could affect those values.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details:

1. What is the base token-creation effect (e.g., "create a 1/1 token," "create two tokens")?
2. What is the exact text of each of the two replacement effects?
3. Who controls the tokens being created (you, an opponent, or a split)?

The number of tokens depends entirely on what each replacement effect says (e.g., "twice as many," "one additional," "three times as many") and the order in which they are applied, which the affected player chooses per [CR 616.1]. Without the specific effect texts, I can't calculate a number.

Review: **correct**. Asks starting effect and exact replacement texts, invents no total; extra general explanation is unnecessary but correct for the stated player affected.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

