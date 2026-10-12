# heldout-baseline

Status: **complete** · implementation commit `e184b2efaf1b5dc10398fb50c678fc24e49309f0`

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
| Answers with citations | 28/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 4 |
| Reviewed citation-support failures | 10 |
| Reviewed fully correct | 25/32 reviewed |
| Reviewed accuracy | 78.1% |
| Mean reviewed rubric score | 87.5% |
| Median successful response | 10.91 s |
| p95 successful response | 21.88 s |
| Median first visible answer token | 9.56 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 12.64 |
| h02-intervening-if (r1) | 100.0% | correct | 7.16 |
| h03-independent-trigger (r1) | 50.0% | correct | 11.97 |
| h04-replacement-death (r1) | 75.0% | correct | 8.98 |
| h05-simultaneous-death (r1) | 100.0% | correct | 8.15 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 8.71 |
| h07-infect-lifelink (r1) | 100.0% | partial | 14.00 |
| h08-protection-wrath (r1) | 100.0% | correct | 10.50 |
| h09-protection-aura (r1) | 100.0% | correct | 5.93 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.25 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 11.32 |
| h12-split-second (r1) | 100.0% | correct | 17.72 |
| h13-sacrifice-cost (r1) | 66.7% | partial | 10.46 |
| h14-flashback-countered (r1) | 66.7% | correct | 12.08 |
| h15-rebound-countered (r1) | 66.7% | correct | 9.80 |
| h16-persist-counter (r1) | 100.0% | correct | 9.13 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 21.88 |
| h18-blink-target (r1) | 75.0% | correct | 13.38 |
| h19-equip-timing (r1) | 75.0% | correct | 18.88 |
| h20-crew-new-creature (r1) | 66.7% | incorrect | 14.86 |
| h21-new-vehicle (r1) | 50.0% | correct | 18.65 |
| h22-tapped-blocker (r1) | 0.0% | correct | 14.83 |
| h23-fight-double-strike (r1) | 100.0% | partial | 9.98 |
| h24-leaving-controller (r1) | 50.0% | correct | 26.45 |
| h25-leaving-stack (r1) | 50.0% | abstained | 13.35 |
| h26-commander-control (r1) | 0.0% | abstained | 14.18 |
| h27-commander-hand (r1) | 100.0% | correct | 7.66 |
| h28-replacement-order (r1) | 100.0% | correct | 18.53 |
| h29-empty-library (r1) | 100.0% | correct | 8.37 |
| h30-ambiguous-combat (r1) | 100.0% | correct | 9.68 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 8.12 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 8.85 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The triggered abilities are put on the stack in this order (bottom to top): Alice's, then Bob's, then Charlie's. They resolve in the reverse order: Charlie's first, Bob's second, Alice's last.

Why: At the beginning of the upkeep, all triggered abilities are placed on the stack before the active player receives priority [CR 503.1a]. The active player (Alice) puts her triggered ability on the stack first, then each nonactive player in turn order (Bob, then Charlie) does the same [CR 805.7]. Each new object is placed on top of all objects already on the stack [CR 405.2], so Charlie's ability is on top and resolves first when all players pass [CR 608.1].

Review: **correct**. Correct Alice/Bob/Charlie stacking and reverse resolution. CR 805.7 is a shared-team-turn rule, not the ordinary multiplayer rule; citation does not support its application here.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, so the condition (you have 40 or more life) is checked both when the ability triggers and again as it resolves. [CR 603.4] states explicitly that if your life total is 39 or less at resolution, "the ability is removed from the stack and has no effect." The dated ruling [C2] confirms the same two-check sequence.

Review: **correct**. Correct no win; CR 603.4 and Felidar ruling support checking again at resolution.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. Once the enters-the-battlefield ability is on the stack, it exists independently of Solemn Simulacrum. Destroying the Simulacrum does not remove or affect the ability, so it resolves normally and you may choose to search your library for a basic land.

Why: A triggered ability, once on the stack, is an object with the text of the ability and no other characteristics; it does not require its source to remain on the battlefield [CR 603.3][CR 405.4]. The "may" choice is made when the ability resolves, not when it triggers [CR 603.5]. The ability's effect (search, put onto battlefield, shuffle) never references the Simulacrum, so its destruction is irrelevant to resolution [C1].

Review: **correct**. Correct independent trigger and search. CR 603.3/405.4 establish stack objects but do not explicitly support independence from the removed source; canonical 113.7a omitted.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "When this creature dies" ability does not trigger.

Why: "Dies" specifically means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exiling, so the card is never put into a graveyard and the trigger condition is never met [C1]. This is confirmed by the card-specific ruling: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Correct exile replacement prevents dies trigger; Oracle and card ruling establish it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers three times—once for itself dying and once for each of the two tokens dying.

Why: "Dies" means "is put into a graveyard from the battlefield" [CR 700.4], and leaves-the-battlefield triggers look back in time so each creature's death is a separate trigger event even when they all leave simultaneously [CR 603.10a]. The card-specific ruling confirms that when Blood Artist and other creatures die at the same time, its ability triggers for each of those creatures [C2].

Review: **correct**. Three triggers, including itself; CR 603.10a and Blood Artist ruling support simultaneous deaths.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: Lifelink is a static ability that causes life gain only when damage is actually *dealt* by the source [CR 702.15b]. If a prevention effect stops all 3 damage, no damage is dealt, so the condition for lifelink's life-gain effect is never met.

Review: **correct**. Zero life; lifelink requires damage actually dealt under CR 702.15b.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent gains 3 poison counters and does **not** lose 3 life. You gain 3 life.

Why: Infect is a replacement effect that changes the result of damage dealt to a player from "lose life" to "get poison counters" [CR 702.90b]. Lifelink is a separate replacement effect that causes the source's controller to gain life "in addition to any other results that damage causes" [CR 702.15b]. The two abilities modify different aspects of the same damage event (the player's result vs. the controller's result), so they apply simultaneously without conflict: the opponent's life total is unchanged, they receive 3 poison counters, and you gain 3 life.

Review: **partial**. Totals are correct, but infect and lifelink are incorrectly called replacement effects. CR 702.90b/702.15b describe damage results, not replacement effects.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature. Protection from white does not prevent a "destroy all creatures" effect.

Why: Protection only prevents targeting, enchanting, equipping, damage, and blocking by sources with the stated quality [CR 702.16b]–[CR 702.16f]. It does not include "can't be destroyed." Wrath of God's "Destroy all creatures" is a non-targeting, non-damage effect [C1], so none of protection's clauses apply. Since the creature has no indestructible, nothing prevents the destruction [CR 702.12b].

Review: **correct**. Wrath destroys; cited protection clauses do not stop nontargeting destruction.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The white Aura is put into its owner's graveyard as a state-based action.

Why: Protection from white means the permanent can't be enchanted by Auras that have the stated quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action [CR 702.16c]. The Aura doesn't become unattached and remain on the battlefield; it leaves the battlefield entirely.

Review: **correct**. Aura goes to owner graveyard as SBA, directly supported by CR 702.16c.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes. You can target your own Slippery Bogle with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you control both the Bogle and the Giant Growth, the restriction does not apply to your own spell. The Bogle's hexproof only blocks targeting by opponents [C1].

Review: **correct**. Own Giant Growth is allowed; hexproof only restricts opponent-controlled targeting.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost. Abrupt Decay still resolves and destroys the creature.

Why: Abrupt Decay's Oracle text reads "This spell can't be countered" [C1]. Ward's ability says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but a "can't" rule overrides any effect that would perform that action, so the counter simply doesn't happen. The 2024-04-12 card-specific ruling states explicitly: "Abrupt Decay won't be countered even if you don't" [C2].

Review: **correct**. Ward triggers without countering uncounterable Decay; correct resolution, supported by Oracle and dated ruling.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. Turning a face-down morph permanent face up is a special action, not an activated ability, so split second does not prevent you from doing it. Willbender's "when turned face up" ability triggers and is put on the stack normally, where it resolves before Krosan Grip and lets you redirect Grip's target to your other artifact.

Why: Split second only prohibits casting spells and activating non-mana abilities; it explicitly allows special actions and triggered abilities to function normally [CR 702.61b]. Turning a morph permanent face up is defined as a special action that doesn't use the stack [CR 702.37e]. Once Willbender's triggered ability is on the stack above Krosan Grip, it resolves first and changes Grip's single target to your second artifact [CR 405.2], after which Grip resolves against the new target [CR 608.2c].

Review: **correct**. Correct morph special action and normal triggered ability despite split second; relevant clauses cited.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond by destroying the sacrificed creature, because the sacrifice is completed as part of paying Fling's cost before the spell is considered cast and before anyone receives priority to respond.

Why: The sacrifice is an additional cost paid during the casting process, so the creature is already in the graveyard by the time the spell is on the stack and players get priority [C3]. The opponent's first opportunity to act is after the spell has been fully cast and all costs paid, at which point the creature is no longer on the battlefield [C3]. Fling then uses the sacrificed creature's power as it last existed on the battlefield to determine damage [C2].

Review: **partial**. Correct that opponent cannot interrupt cost payment, but says sacrifice happens before the spell is on the stack. CR 601.2a puts the spell on the stack before costs are paid at 601.2h; first response still occurs after payment. C3 supports no response, not that added sequencing claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 601.2h

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice goes to exile, and you do not draw a card.

Why: Because you paid the flashback cost, the replacement effect in [CR 702.34a] exiles the card "any time it would leave the stack," which includes when it is countered; [C2] confirms this applies whether the spell resolves, is countered, or leaves the stack any other way. Since the spell was countered, it never resolves, so the "Draw a card" instruction in [C1] is never carried out under the resolution process described in [CR 608.2c].

Review: **correct**. Correct exile and no draw. Flashback citation supports exile; CR 608.2c is a resolution-instructions rule, not support for the claimed countered-spell rule (701.5a).
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If your opponent counters Ephemerate, Rebound does not exile it and you do not get a chance to cast it next upkeep. The countered spell goes to the graveyard (or wherever the counter effect sends it) and Rebound never applies.

Why: Rebound's replacement effect modifies what happens "as it resolves"—specifically, it replaces the normal "put into your graveyard" step with "exile it" [CR 702.88a]. A countered spell never resolves, so there is no "as it resolves" event for Rebound to modify, and the delayed triggered ability to cast it next upkeep is never created.

Review: **correct**. Correct no rebound because countered spell never resolves; graveyard answer includes harmless qualification about counter effects.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks dies with a -1/-1 counter on it, persist does not return it to the battlefield.

Why: Persist's trigger condition includes the intervening "if" clause "if it had no -1/-1 counters on it" [CR 702.79a]. Under the intervening "if" rule, the ability triggers only if that condition is true; otherwise it does nothing [CR 603.4]. Since the counter is present at the moment it is put into the graveyard, the condition fails and the ability never goes on the stack.

Review: **correct**. Correct no persist trigger with existing -1/-1 counter; cited persist and intervening-if definitions support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger.

Why: Undying is a leaves-the-battlefield ability that "looks back in time" to check whether the creature had a +1/+1 counter [CR 603.10a] [CR 702.93a]. Because the +1/+1 counter and the -1/-1 counter are removed by a state-based action at the same time the 0-toughness creature is put into the graveyard, the creature's last known information is derived from the game state *before* any of those state-based actions were performed [CR 704.8]. In that pre-action state, Young Wolf still had a +1/+1 counter on it, so the "if it had no +1/+1 counters" condition is not met and undying does not trigger. This is the same principle as the worked example in [CR 704.8], where a Young Wolf with a +1/+1 counter and three -1/-1 counters dies and undying fails to trigger.

Review: **correct**. Correct no undying; explicitly uses CR 704.8 pre-SBA state. Frozen evidence group erroneously names 704.7; see addendum, no rubric changes.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No. The Lightning Bolt does not damage the returned creature. Because Cloudshift exiles the creature and then returns it as a new object, the original target no longer exists. When the Bolt later resolves, its target is illegal, so the Bolt doesn't resolve at all.

Why: Cloudshift's ruling states that "once the exiled permanent returns, it's considered a new object with no relation to the object that it was" [C3]. Under [CR 608.2b], a target that is no longer in the zone it was in when targeted is illegal, and if all targets are illegal the spell doesn't resolve. The new creature on the battlefield was never the target of the Bolt, so it takes no damage [C1][C2].

Review: **correct**. Correct returned object is new and Bolt has no legal target; Cloudshift ruling and 608.2b support answer.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

Why: The equip ability explicitly states "Activate only as a sorcery" [CR 702.6a], which restricts activation to your main phase when the stack is empty. Because Lightning Bolt is on the stack, the stack is not empty, so the equip ability is not legally activatable at that moment. Even if it were, equipping Colossus Hammer would only grant +10/+10 and remove flying [C2]; it provides no protection or damage prevention against the 3 damage Lightning Bolt will deal [C1].

Review: **correct**. Correct no equip response because stack is nonempty. Extra sentence about lack of damage prevention is unnecessary: toughness increase can save a creature if attached in time; it does not literally prevent damage.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: No. You cannot tap that 3/3 creature to pay the Crew 1 cost of Smuggler's Copter.

Why: Crew is an activated ability [CR 702.122a], and a creature that hasn't been under your control continuously since the beginning of your turn can't be tapped to pay the cost of an activated ability unless it has haste [CR 702.10c]. Because your 3/3 was just cast this turn and has no haste, it is still affected by summoning sickness and can't be tapped for the Crew cost.

Review: **incorrect**. Incorrect: newly controlled untapped creatures may crew. Misreads haste/tap-symbol restriction as applying to all tapping costs; relevant explicit Copter ruling was omitted from packed context.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No. Because you cast Smuggler's Copter this turn, you have not controlled it continuously since your turn began, so it is subject to summoning sickness and cannot attack. It has no haste to bypass that restriction.

Why: Once a Vehicle becomes a creature it "can't attack unless you've controlled it continuously since your turn began" [C10]. Haste is the ability that lets a creature attack despite not meeting that condition [CR 702.10b], and Smuggler's Copter's printed text includes no haste [C1]. Since you cast it during the current turn, the continuous-control requirement is not satisfied.

Review: **correct**. Correct new Vehicle cannot attack without haste; card ruling and haste definition support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: Tapping the blocker does **not** remove it from combat and does **not** stop it from assigning combat damage. It is still a blocking creature and will deal its 3 damage in the combat damage step.

Why: A creature "remains a blocking creature until it's removed from combat or the combat phase ends" [CR 509.1g], and tapping is not a removal-from-combat effect. In the combat damage step, "each attacking creature and each blocking creature assigns combat damage equal to its power" [CR 510.1a], and "a blocking creature assigns combat damage to the creatures it's blocking" [CR 510.1d]. Since the tapped creature is still a blocking creature still blocking the attacker, it assigns its full 3 damage as normal.

Review: **correct**. Correct blocker remains blocking and deals normal damage; cited combat rules support results, though direct 506.4b omitted.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 damage. Double strike has no effect here.

Why: In a fight, each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Double strike is a static ability that modifies the combat damage step [CR 702.4a], so it provides no additional damage instance in a non-combat fight.

Review: **partial**. Correct damage amounts and survivor, but says 4/4 survives with 1 damage. It has 3 damage marked, not 1. This is a factual contradiction despite correct core rubric conclusions.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: When Bob loses and leaves the game, the Control Magic Aura (an object Bob owns) leaves the game. The creature, which Alice owns, remains on the battlefield and is once again controlled by Alice, since the sole control-changing effect (the Aura) no longer exists.

Why: Losing the game causes a player to leave immediately [CR 104.5]. When a player leaves a multiplayer game, objects may leave the game, cease to exist, change control, or be exiled as a result, and these actions happen immediately [CR 405.6h]. Control Magic's only effect is "You control enchanted creature" [C1]; once the Aura leaves the game, that continuous control-changing effect (which would apply in layer 2 [CR 613.1b]) ceases, and the creature reverts to being controlled by its owner, Alice. Note that the specific determination of *which* objects leave is governed by rule 800.4a, which is referenced by [CR 405.6h] but not included in the supplied excerpts; the ruling above assumes the standard application that objects the leaving player own leave the game.

Review: **correct**. Correct Aura leaves and creature returns to Alice. Answer admits 800.4a is missing and assumes its content; 405.6h is only a cross-reference, not sufficient evidence for which objects leave.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Need details: The supplied reference excerpts do not include the rules governing what happens to spells on the stack when a player leaves the game (e.g., the rule that all objects a leaving player owns leave the game). I cannot determine the ruling without that rule text. Could you provide the relevant rule excerpt (typically found in the "Leaving the Game" section, around CR 104.3a), or confirm whether you'd like me to answer based on general knowledge rather than the supplied excerpts?

Review: **abstained**. Unnecessary abstention on a complete game state because 800.4a was not supplied. Also points to 104.3a rather than the applicable leaving-player rule.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Need details: The supplied reference excerpts do not include the commander damage rule (the 21-combat-damage threshold and how that damage is tracked per player). I cannot provide a fully cited ruling on whether damage dealt by a commander while controlled by different players accumulates on the same player without that rule in the references. Could you attach the relevant rule text (typically rule 903.10) or the card whose Oracle text references commander damage so I can ground the answer in a supplied source?

Review: **abstained**. Unnecessary abstention; same commander deals cumulative 21 regardless of controller. CR 903.10a omitted from context.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 903.10a

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect, not a state-based action.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner's hand from anywhere, the owner may put it into the command zone instead, and labels that mechanism a "replacement effect" [CR 903.9b]. The state-based action in rule 903.9a applies only when a commander is already in a graveyard or in exile, which is a different situation [CR 903.9a].

Review: **correct**. Correct command-zone option is a hand/library replacement effect under 903.9b, not the graveyard/exile SBA.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the affected player) chooses which replacement effect applies first. The possible damage totals are **8** (Furnace first, then Torbran: 3×2=6, then 6+2=8) or **10** (Torbran first, then Furnace: 3+2=5, then 5×2=10).

Why: Both Torbran's "+2" effect [C1] and Furnace's "double" effect [C5] are replacement effects modifying the same event (Lightning Bolt dealing 3 damage to a player) [C11]. Under [CR 616.1], the affected player chooses which applicable replacement to apply first. After the first is applied, [CR 616.1f] requires the process to repeat with the remaining effect, and [CR 614.5] confirms each effect gets only one opportunity, so both apply exactly once in the chosen order.

Review: **correct**. Correct affected opponent chooses; both 8 and 10 with matching orders, supported by Oracle and 616.1.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having an empty library by itself does not cause you to lose the game. You lose only if you *attempt to draw* a card from that empty library, and then state-based actions are checked.

Why: The state-based action that causes a loss is specifically tied to an attempted draw from an empty library, not to the library being empty in general. [CR 704.5b] requires that "a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] likewise conditions the loss on a player who "attempts to draw a card from a library with no cards in it." Neither rule imposes a loss for merely having zero cards in the library.

Review: **correct**. Correct no loss merely for empty library; attempted draw condition explicitly cited.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Need details: Does your attacking creature have trample (or trample over planeswalkers)? If so, what is its power, and what is the toughness of the creature(s) blocking it?

Review: **correct**. Appropriate clarification asks about trample and attacker/blocker stats, without inventing a total.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No. Your copy does not get the counters on the original creature, and it does not get the bonus from the enchantment attached to it.

Why: When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects, face-down status, and certain "as it enters" abilities). "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An enchantment's bonus is a continuous effect from a separate source, not part of the creature's printed or copiable values, so it is not transferred to the copy. [CR 707.2]

Review: **incorrect**. Fails frozen clarification criteria: gives unconditional answer without asking copy effect/enchantment details. 707.2 describes ordinary copy values but includes exceptions; unspecified effects could affect those values.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details:

1. What are the two replacement effects (exact card names or text)?
2. How many tokens does the original effect create before any replacement is applied?
3. Are either of the two effects a self-replacement effect (i.e., part of the same spell/ability that creates the tokens)?

Review: **correct**. Appropriate clarification asks exact effects and original count; no invented number.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

