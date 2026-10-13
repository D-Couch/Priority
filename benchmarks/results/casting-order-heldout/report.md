# casting-order-heldout

Status: **complete** · implementation commit `2d31122fca1b51b6ac9e46d75a058488395305e6`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 27/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 79.7% |
| Cases retrieving every expected evidence group | 18/32 |
| Answers with citations | 29/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 3 |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 27/32 reviewed |
| Reviewed accuracy | 84.4% |
| Mean reviewed rubric score | 93.8% |
| Median successful response | 10.40 s |
| p95 successful response | 17.38 s |
| Median first visible answer token | 9.01 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 13.11 |
| h02-intervening-if (r1) | 100.0% | correct | 7.96 |
| h03-independent-trigger (r1) | 50.0% | correct | 12.49 |
| h04-replacement-death (r1) | 75.0% | correct | 8.25 |
| h05-simultaneous-death (r1) | 100.0% | correct | 9.24 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 8.51 |
| h07-infect-lifelink (r1) | 100.0% | partial | 14.18 |
| h08-protection-wrath (r1) | 100.0% | correct | 10.48 |
| h09-protection-aura (r1) | 100.0% | correct | 5.73 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.28 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 10.32 |
| h12-split-second (r1) | 100.0% | correct | 17.38 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 11.82 |
| h14-flashback-countered (r1) | 66.7% | correct | 8.61 |
| h15-rebound-countered (r1) | 66.7% | correct | 8.30 |
| h16-persist-counter (r1) | 100.0% | correct | 8.19 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 18.00 |
| h18-blink-target (r1) | 75.0% | correct | 11.22 |
| h19-equip-timing (r1) | 75.0% | partial | 15.22 |
| h20-crew-new-creature (r1) | 66.7% | correct | 15.15 |
| h21-new-vehicle (r1) | 50.0% | correct | 10.98 |
| h22-tapped-blocker (r1) | 0.0% | correct | 14.91 |
| h23-fight-double-strike (r1) | 100.0% | partial | 10.10 |
| h24-leaving-controller (r1) | 100.0% | correct | 10.49 |
| h25-leaving-stack (r1) | 100.0% | correct | 12.40 |
| h26-commander-control (r1) | 0.0% | abstained | 14.77 |
| h27-commander-hand (r1) | 100.0% | correct | 8.10 |
| h28-replacement-order (r1) | 100.0% | correct | 13.78 |
| h29-empty-library (r1) | 100.0% | correct | 8.23 |
| h30-ambiguous-combat (r1) | 100.0% | correct | 9.40 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 8.18 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 8.64 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The triggered abilities are put on the stack in this order (bottom to top): Alice's, then Bob's, then Charlie's. They resolve in the reverse order: Charlie's first, Bob's second, Alice's last.

Why: At the beginning of the upkeep, all triggered abilities are placed on the stack before the active player receives priority [CR 503.1a]. The active player (Alice) puts her triggered ability on the stack first, then each nonactive player in turn order (Bob, then Charlie) does the same [CR 805.7]. Each new object is placed on top of all objects already on the stack [CR 405.2], so Charlie's ability is on top and resolves first when all players pass [CR 608.1].

Review: **correct**. Correct APNAP stack order and reverse resolution. The current answer accurately says abilities are put on the stack sequentially in active-player then turn order; the unsupported simultaneity error from the prior prompt run is gone.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, so the condition (40 or more life) is checked both when the ability triggers and again as it resolves. If you have 39 or less life at resolution, the ability does nothing. [CR 603.4] [C2]

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. Once the enters-the-battlefield ability is on the stack, it exists independently of Solemn Simulacrum. Destroying the Simulacrum does not remove or affect the ability, so it resolves normally and you may choose to search your library for a basic land.

Why: A triggered ability, once on the stack, is an object with the text of the ability and no other characteristics; it does not require its source to remain on the battlefield [CR 603.3][CR 405.4]. The "may" choice is made when the ability resolves, not when it triggers [CR 603.5]. The ability's effect (search, put onto battlefield, shuffle) never references the Simulacrum, so its destruction is irrelevant to resolution [C1].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "When this creature dies, you may draw a card" ability does not trigger.

Why: "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event, so the card is exiled instead and is never put into a graveyard [C1]. Because the trigger condition is never met, the ability does not trigger [C2].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers **three** times—once for itself dying and once for each of the two tokens dying.

Why: Blood Artist's trigger condition is "whenever this creature **or another creature** dies," so each individual creature death is a separate trigger event. The card-specific ruling confirms that when Blood Artist and other creatures die simultaneously, the ability triggers for each of those creatures [C2]. The general rule for zone-change triggers looking back in time likewise supports multiple simultaneous deaths producing multiple triggers [CR 603.10a], and "dies" is defined as being put into a graveyard from the battlefield [CR 700.4].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: Lifelink is a static ability that causes life gain only when damage is actually *dealt* by the source [CR 702.15b]. If a prevention effect stops all 3 damage, no damage is dealt, so the condition for lifelink's life-gain effect is never met.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent gains 3 poison counters and does **not** lose 3 life. You gain 3 life.

Why: Infect is a replacement effect that changes the result of damage dealt to a player from "lose life" to "get poison counters" [CR 702.90b]. Lifelink is a separate replacement effect that causes the source's controller to gain life "in addition to any other results that damage causes" [CR 702.15b]. The two abilities modify different aspects of the same damage event (the player's result vs. the controller's result), so they apply simultaneously without conflict: the opponent's life total is unchanged, they receive 3 poison counters, and you gain 3 life.

Review: **partial**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature. Protection from white does not prevent a "destroy all creatures" effect.

Why: Protection only prevents targeting, enchanting, equipping, damage, and blocking by sources with the stated quality [CR 702.16b]–[CR 702.16f]. It does not include "can't be destroyed." Wrath of God's "Destroy all creatures" is a non-targeting, non-damage effect [C1], so none of protection's clauses apply. Since the creature has no indestructible, nothing prevents the destruction [CR 702.12b].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The white Aura is put into its owner's graveyard as a state-based action.

Why: Protection from white means the permanent can't be enchanted by Auras that have the stated quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action [CR 702.16c]. The Aura doesn't become unattached and remain on the battlefield; it leaves the battlefield entirely.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes. You can target your own Slippery Bogle with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you control both the Bogle and the Giant Growth, the restriction does not apply to your own spell. The Bogle's hexproof only blocks targeting by opponents [C1].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

Why: Abrupt Decay's Oracle text states "This spell can't be countered" [C1], which prevents any effect—including ward's "counter that spell or ability" clause [CR 702.21a]—from actually countering it. The 2024 card-specific ruling confirms this directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2]. The ward ability still triggers and you are still offered the option to pay, but the "can't be countered" restriction makes the counter effect impossible to apply.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will resolve before Grip to redirect its target to your other artifact.

Why: Turning a face-down permanent face up is a special action, not an activated ability, so split second does not prohibit it [CR 702.37e][CR 702.61b]. This is confirmed by the Krosan Grip ruling: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5]. Willbender's trigger fires when it is turned face up [C13], and triggered abilities are put on the stack as normal during split second [CR 702.61b]. Because it enters on top of the stack [CR 405.2], it resolves before Grip, letting you change Grip's single target to your other legal artifact.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond to destroy the sacrificed creature. The sacrifice is part of paying Fling's additional cost, which occurs during the casting process before the spell is considered "cast" and before any player receives priority to respond.

Why: Fling's text states "As an additional cost to cast this spell, sacrifice a creature" [C1], and the card-specific ruling confirms that "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell" [C3]. The sacrifice is paid as part of the total cost in step 601.2h [CR 601.2h], and the spell only becomes cast—and the controller regains priority—after all steps through 601.2h are completed [CR 601.2i]. Because no player receives priority between the sacrifice and the spell being cast, there is no window in which your opponent could target or destroy that creature.

Review: **correct**. Correct. Costs are paid during casting before the spell becomes cast; the spell is on the stack from the start of casting, but no opponent receives priority between payment and completion. CR 601.2a, 601.2h, 601.2i, 117.2e, and 117.3c are in the packed context and support the sequence; the Fling ruling confirms there is no response window.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice is exiled, and you do not draw a card.

Why: The flashback static ability replaces the normal "put into graveyard" action with "exile" any time the spell would leave the stack, including when it is countered [CR 702.34a][C2]. Because the spell was countered, it never resolved, so the "Draw a card" instruction was never carried out [CR 608.1].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If Ephemerate is countered, rebound does not exile it. The spell is put into your graveyard and you do not get to cast it again on your next turn.

Why: Rebound is a static ability that modifies what happens "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never applies. The card-specific ruling confirms that if a rebound spell cast from your hand is countered, "none of its effects will happen, including rebound," and it goes to the graveyard [C5].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard from the battlefield, persist does not trigger and the card does not return to the battlefield.

Why: Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield; if a -1/-1 counter is present at that moment, the condition fails and the ability never triggers [C6].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger.

Why: Before any state-based actions are performed, Young Wolf still has its +1/+1 counter on it (the -1/-1 counter and the -1/-1 continuous effect only reduce its toughness to 0; they don't remove the counter). Because the creature dying and the opposing counters being removed are state-based actions performed simultaneously, rule 704.8 dictates that its last known information is derived from the game state *before* those actions, at which point it had a +1/+1 counter. Undying's condition ("if it had no +1/+1 counters on it") is therefore not met, so the ability does not trigger. [CR 704.8] [CR 702.93a]

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No. The returned creature is not damaged by Lightning Bolt.

Why: Cloudshift's ruling states that "the returned card won't be the target of any spells or abilities that targeted it before" [C5]. Because the original creature was exiled and the creature that re-enters is a new object, Lightning Bolt's target is no longer in the zone it was in when targeted, making it illegal [CR 608.2b]. With all its targets illegal, Lightning Bolt doesn't resolve and deals no damage [CR 608.2b].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

Why: The equip ability is restricted to sorcery speed—"Activate only as a sorcery" [CR 702.6a], meaning it may only be activated during your main phase while the stack is empty. When Lightning Bolt is on the stack, the stack is not empty, so the equip ability is not legal to activate at that moment [CR 117.1a]. Additionally, even if you could equip it, Colossus Hammer grants +10/+10 and removes flying [C2]; it does not prevent or redirect damage, so it would not "save" the creature from the 3 damage Lightning Bolt deals [C1].

Review: **partial**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: Yes. You can tap your 3/3 creature (even though it has summoning sickness and no haste) to pay the Crew 1 cost of Smuggler's Copter.

Why: Crew is an activated ability of the Vehicle, not of the creature; the creature is simply tapped as part of that cost [CR 702.122a]. The card-specific ruling for Smuggler's Copter explicitly confirms that "any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. Haste only matters for a creature attacking or activating its *own* tap-abilities [CR 702.10b–c], not for being tapped as a cost for another permanent's ability.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No. Because you cast Smuggler's Copter this turn, you have not controlled it continuously since the beginning of your turn, and it has no haste, so it cannot attack this turn even after being crewed.

Why: Once a Vehicle becomes a creature it behaves like any other artifact creature, which means it can't attack unless you've controlled it continuously since your turn began [C10]. Haste is the ability that overrides that requirement [CR 702.10b], and Smuggler's Copter's printed text includes no haste [C1].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: Tapping the blocker does **not** remove it from combat and does **not** stop it from assigning combat damage. It is still a blocking creature and will deal its 3 damage in the combat damage step.

Why: A creature "remains a blocking creature until it's removed from combat or the combat phase ends" [CR 509.1g], and tapping is not a removal-from-combat effect. In the combat damage step, "each attacking creature and each blocking creature assigns combat damage equal to its power" [CR 510.1a], and "a blocking creature assigns combat damage to the creatures it's blocking" [CR 510.1d]. Since the tapped creature is still a blocking creature still blocking the attacker, it assigns its full 3 damage as normal.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 damage. Double strike has no effect here.

Why: In a fight, each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Double strike is a static ability that modifies the combat damage step [CR 702.4a], so it provides no additional damage instance in a non-combat fight.

Review: **partial**. Correct fight damage and survival, but says the surviving 4/4 has 1 damage marked. It took 3 damage, so that detail is wrong and unsupported.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: Control Magic leaves the game, and the creature reverts to Alice's control.

Why: When a player leaves the game, all objects they own leave the game and any effects giving them control of objects end [CR 800.4a]. The rule's example directly mirrors this situation: if the controller of a "You control enchanted creature" Aura leaves the game, the Aura leaves the game and the creature reverts to its owner's control [CR 800.4a]. Because Alice owns the creature, it remains on the battlefield under her control.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Ruling: No, Lightning Bolt does not resolve. It leaves the game when Bob leaves.

Why: When a player leaves the game, all objects owned by that player leave the game [CR 800.4a]. Lightning Bolt is a card owned by Bob, so it leaves the game at that moment and never gets the chance to resolve. The rule that a spell "will continue to resolve fully" if it leaves the stack once it starts to resolve [CR 608.2m] does not apply here, because the spell was still waiting on the stack and had not begun resolving.

Review: **correct**. Correct: Bob-owned Lightning Bolt leaves immediately when he leaves the game and therefore does not resolve. CR 800.4a supports the ruling; CR 608.2m is correctly distinguished as applying after resolution has begun.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Need details: The supplied reference excerpts do not include the commander damage rule (the 21-combat-damage threshold and how that damage is tracked per player). I cannot provide a fully cited ruling on whether damage dealt by a commander while controlled by different players accumulates on the same player without that rule in the references. Could you attach the relevant rule text (typically rule 903.10) or the card whose Oracle text references commander damage so I can ground the answer in a supplied source?

Review: **abstained**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 903.10a

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect, not a state-based action.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner's hand from anywhere, the owner may put it into the command zone instead, and labels that mechanism a "replacement effect" [CR 903.9b]. The state-based action in rule 903.9a applies only when a commander is already in a graveyard or in exile, which is a different situation [CR 903.9a].

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace: (3+2)×2) or **8** (Furnace first, then Torbran: (3×2)+2).

Why: When multiple replacement effects modify how damage is dealt, the affected player chooses the order in which they are applied [CR 616.1], a principle confirmed in both Torbran's and Furnace's card-specific rulings [C4][C6]. Torbran adds 2 to the damage [C1], and Furnace doubles it [C5]; applying them in either order to Lightning Bolt's 3 damage [C11] yields 10 or 8, and the opponent picks which.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having an empty library by itself does not cause you to lose the game. You lose only if you *attempt to draw* a card from that empty library, and then state-based actions are checked.

Why: The state-based action that causes a loss is specifically tied to an attempted draw from an empty library, not to the library being empty in general. [CR 704.5b] requires that "a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] likewise conditions the loss on a player who "attempts to draw a card from a library with no cards in it." Neither rule imposes a loss for merely having zero cards in the library.

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Need details: Does your attacking creature have trample (or trample over planeswalkers)? If so, what is its power, and what is the toughness of the creature(s) blocking it?

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No. Your copy does not get the counters on the original creature, and it does not get the bonus from the enchantment attached to it.

Why: When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects, face-down status, and certain "as it enters" abilities). "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An enchantment's bonus is a continuous effect from a separate source, not part of the creature's printed or copiable values, so it is not transferred to the copy. [CR 707.2]

Review: **incorrect**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details:

1. What are the two replacement effects (exact card names or text)?
2. How many tokens does the original effect create before any replacement is applied?
3. Are either of the two effects a self-replacement effect (i.e., part of the same spell/ability that creates the tokens)?

Review: **correct**. Rechecked current wording against the frozen rubric; substantive grade matches the prior review. Semantic citation support was not independently regraded.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

