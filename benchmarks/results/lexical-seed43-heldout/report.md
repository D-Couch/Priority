# lexical-seed43-heldout

Status: **complete** · implementation commit `4144f33dff3bf84ea1a7c76d5c62e972cdf75542`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [43]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 27/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 75.5% |
| Cases retrieving every expected evidence group | 15/32 |
| Answers with citations | 28/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 3 |
| Reviewed citation-support failures | 9 |
| Reviewed fully correct | 27/32 reviewed |
| Reviewed accuracy | 84.4% |
| Mean reviewed rubric score | 90.6% |
| Median successful response | 11.13 s |
| p95 successful response | 31.33 s |
| Median first visible answer token | 9.54 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 36.35 |
| h02-intervening-if (r1) | 100.0% | correct | 8.14 |
| h03-independent-trigger (r1) | 50.0% | correct | 15.91 |
| h04-replacement-death (r1) | 75.0% | correct | 8.18 |
| h05-simultaneous-death (r1) | 100.0% | correct | 9.18 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 7.21 |
| h07-infect-lifelink (r1) | 100.0% | correct | 17.80 |
| h08-protection-wrath (r1) | 100.0% | correct | 9.75 |
| h09-protection-aura (r1) | 100.0% | correct | 5.85 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.41 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 10.95 |
| h12-split-second (r1) | 100.0% | correct | 17.81 |
| h13-sacrifice-cost (r1) | 66.7% | partial | 12.73 |
| h14-flashback-countered (r1) | 66.7% | correct | 10.33 |
| h15-rebound-countered (r1) | 66.7% | correct | 8.15 |
| h16-persist-counter (r1) | 100.0% | correct | 11.13 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 15.28 |
| h18-blink-target (r1) | 75.0% | correct | 12.77 |
| h19-equip-timing (r1) | 75.0% | correct | 15.32 |
| h20-crew-new-creature (r1) | 66.7% | correct | 12.92 |
| h21-new-vehicle (r1) | 50.0% | correct | 12.91 |
| h22-tapped-blocker (r1) | 0.0% | correct | 12.42 |
| h23-fight-double-strike (r1) | 100.0% | partial | 11.14 |
| h24-leaving-controller (r1) | 50.0% | correct | 31.33 |
| h25-leaving-stack (r1) | 50.0% | abstained | 13.23 |
| h26-commander-control (r1) | 0.0% | incorrect | 20.23 |
| h27-commander-hand (r1) | 100.0% | correct | 8.63 |
| h28-replacement-order (r1) | 100.0% | correct | 13.32 |
| h29-empty-library (r1) | 100.0% | correct | 8.10 |
| h30-ambiguous-combat (r1) | 100.0% | correct | 9.10 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 8.60 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 10.04 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The three triggered abilities are placed on the stack with Alice's (active player) at the bottom, Bob's in the middle, and Charlie's on top. They resolve in reverse stack order: Charlie's ability first, then Bob's, then Alice's.

Why: All three abilities trigger simultaneously at the beginning of the upkeep and are put on the stack before the active player receives priority [CR 503.1a]. When multiple objects are put on the stack at the same time, the active player's objects go lowest, followed by the other players' objects in APNAP (turn) order [CR 405.3]. The top (last-added) object on the stack resolves first [CR 405.5], so with no responses, Charlie's resolves, then Bob's, then Alice's [CR 608.1].

Review: **correct**. Correct Alice/Bob/Charlie stacking and reverse resolution. CR 805.7 is a shared-team-turn rule, not the ordinary multiplayer rule; citation does not support its application here.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, so the condition (40 or more life) is checked both when the ability triggers and again as it resolves. If your life total is 39 or less at resolution, the ability does nothing. [CR 603.4] [C2]

Review: **correct**. Correct no win; CR 603.4 and Felidar ruling support checking again at resolution.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. You may still search your library for a basic land card, put it onto the battlefield tapped, and shuffle.

Why: Once the ETB triggered ability is on the stack, it exists as an independent object carrying only its own text and no other characteristics [CR 405.4]. Its effect ("you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle") does not reference the Simulacrum or require it to be in any particular zone, so the Simulacrum's destruction does not prevent the ability from resolving [C1]. The optional "may" choice is made when the ability resolves, not when it triggers [CR 603.5].

Review: **correct**. Correct independent trigger and search. CR 603.3/405.4 establish stack objects but do not explicitly support independence from the removed source; canonical 113.7a omitted.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "when this creature dies" ability does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect causes the card to be exiled instead of being put into a graveyard [C1], so the trigger condition is never met. The card-specific ruling confirms this directly: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Correct exile replacement prevents dies trigger; Oracle and card ruling establish it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers three times—once for itself dying and once for each of the two tokens dying.

Why: The card-specific ruling states that if Blood Artist and one or more other creatures die at the same time, its ability triggers for each of those creatures [C2]. "Dies" means "is put into a graveyard from the battlefield" [CR 700.4], and leaves-the-battlefield triggers look back in time so they fire even when the source is in the graveyard at the moment the triggers are processed [CR 603.10a]. With three creatures dying simultaneously, that produces three separate trigger events.

Review: **correct**. Three triggers, including itself; CR 603.10a and Blood Artist ruling support simultaneous deaths.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: Lifelink causes life gain only when damage is actually *dealt* by the source [CR 702.15b]. If a prevention effect stops all 3 damage, no damage is dealt, so the condition for lifelink's life gain is never met.

Review: **correct**. Zero life; lifelink requires damage actually dealt under CR 702.15b.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent's life total is unchanged, your opponent gets 3 poison counters, and you gain 3 life.

Why: Infect is a static ability that replaces the "lose life" result of damage dealt to a player with "get that many poison counters" [CR 702.90b]. Lifelink is a separate static ability that causes the source's controller to gain life "in addition to any other results that damage causes" [CR 702.15b]. Because infect modifies what happens to the *recipient* and lifelink adds a result for the *source's controller*, both apply independently: the damage is still dealt, the opponent receives 3 poison counters instead of losing 3 life, and you gain 3 life.

Review: **correct**. Correct: infect gives the opponent poison counters instead of life loss, and lifelink separately gains three life for its controller; CR 702.90b and 702.15b support both results.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature. Protection from white does not prevent it.

Why: Protection from white only prevents being targeted by white spells/abilities, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b–f]. Wrath of God is a non-targeting global effect that simply reads "Destroy all creatures" [C1]; it does not target, deal damage, or enchant, so none of the protection clauses apply. Since your creature lacks indestructible, nothing stops the destruction [CR 702.12b].

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

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you control both the Bogle and the Giant Growth, the restriction does not apply to your own spell. The Bogle's hexproof only blocks targeting by your opponents [C1].

Review: **correct**. Own Giant Growth is allowed; hexproof only restricts opponent-controlled targeting.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

Why: Abrupt Decay's Oracle text states "This spell can't be countered" [C1], which prevents any effect—including ward's "counter that spell or ability" clause [CR 702.21a]—from actually countering it. The 2024-04-12 card-specific ruling confirms this directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2]. The ward ability still triggers and you are still offered the option to pay, but the "can't be countered" restriction means the counter effect simply doesn't apply.

Review: **correct**. Ward triggers without countering uncounterable Decay; correct resolution, supported by Oracle and dated ruling.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will resolve before Grip to redirect the target to your other artifact.

Why: Turning a face-down permanent face up is a special action, not an activated ability, so split second does not prohibit it [CR 702.37e][CR 702.61b]. The Krosan Grip ruling confirms this explicitly: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5]. Willbender's "when turned face up" trigger fires from the morph special action [C13], goes on the stack above Grip [CR 405.2], and resolves first [CR 608.1], changing Grip's target to your second artifact before Grip resolves.

Review: **correct**. Correct morph special action and normal triggered ability despite split second; relevant clauses cited.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond to destroy the creature. The sacrifice is part of paying Fling's additional cost, and costs are paid as part of the act of casting the spell. Players can only respond after the spell has been fully cast and all its costs have been paid, at which point the creature is already in the graveyard.

Why: Fling's text requires sacrificing a creature "as an additional cost to cast this spell" [C1], and the card-specific ruling explicitly states, "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." [C3] The sacrifice is not a separate interruptible action; it is consumed during cost payment before the spell reaches the stack and priority is granted to opponents.

Review: **partial**. Correct that opponent cannot interrupt cost payment, but says sacrifice happens before the spell is on the stack. CR 601.2a puts the spell on the stack before costs are paid at 601.2h; first response still occurs after payment. C3 supports no response, not that added sequencing claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 601.2h

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice is exiled, and you do not draw a card.

Why: The flashback ability creates a static effect that exiles the card "any time it would leave the stack," which includes when it is countered [CR 702.34a]. The card-specific ruling confirms it is exiled "whether it resolves, is countered, or leaves the stack in some other way" [C2]. Because the spell was countered, it never resolved, so its "Draw a card" instruction was never carried out [CR 608.1].

Review: **correct**. Correct exile and no draw. Flashback citation supports exile; CR 608.2c is a resolution-instructions rule, not support for the claimed countered-spell rule (701.5a).
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If Ephemerate is countered, rebound does not apply. The spell is put into your graveyard and you do not get to cast it again next upkeep.

Why: Rebound is a replacement effect that modifies what happens "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The card-specific ruling confirms that if a rebound spell cast from your hand is countered, "none of its effects will happen, including rebound," and it goes to the graveyard [C5].

Review: **correct**. Correct no rebound because countered spell never resolves; graveyard answer includes harmless qualification about counter effects.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it is put into a graveyard from the battlefield, persist does not trigger and the card does not return to the battlefield.

Why: Persist's trigger condition includes the intervening "if" clause "if it had no -1/-1 counters on it" [CR 702.79a]. That condition is checked at the moment the creature is put into the graveyard; if it fails, the ability simply does not trigger [CR 603.4]. The card-specific ruling confirms that persist checks the creature's counters just before it leaves the battlefield, and if -1/-1 counters are present, persist won't trigger [C6].

Review: **correct**. Correct no persist trigger with existing -1/-1 counter; cited persist and intervening-if definitions support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger.

Why: The +1/+1 counter and the -1/-1 counter are removed simultaneously with the death as part of the same state-based-action check [CR 704.3]. Under [CR 704.8], when a state-based action causes a permanent to leave the battlefield at the same time other state-based actions are performed, the permanent's last known information is derived from the game state *before* any of those actions. In that prior state, Young Wolf still had a +1/+1 counter on it, so the "if it had no +1/+1 counters on it" condition in undying's trigger is not met [CR 702.93a]. This is the same principle as the worked example in [CR 704.8], where a Young Wolf with one +1/+1 counter and three -1/-1 counters dies and undying does not trigger.

Review: **correct**. Correct no undying; explicitly uses CR 704.8 pre-SBA state. Frozen evidence group erroneously names 704.7; see addendum, no rubric changes.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No. Lightning Bolt does not deal damage to the creature after Cloudshift resolves.

Why: Cloudshift exiles the creature and returns it as a new object on the battlefield; the returned card is not the target of any spell that targeted it before [C5]. Because the original targeted object is no longer on the battlefield, it is an illegal target [CR 608.2b], and since Lightning Bolt has only that one target, the spell doesn't resolve and deals no damage [CR 608.2b].

Review: **correct**. Correct returned object is new and Bolt has no legal target; Cloudshift ruling and 608.2b support answer.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

Why: The equip ability is restricted to sorcery timing—"Activate only as a sorcery"—meaning it can only be activated during your main phase while the stack is empty [C2][CR 702.6a]. Because Lightning Bolt is on the stack, the stack is not empty, so the equip ability is not legally activatable at that moment [CR 117.1a]. Separately, even if you could equip it, Colossus Hammer grants +10/+10 and removes flying; it does not prevent or redirect damage, so it would not "save" the creature from the 3 damage Lightning Bolt deals [C1][C2].

Review: **correct**. Correct no equip response because stack is nonempty. Extra sentence about lack of damage prevention is unnecessary: toughness increase can save a creature if attached in time; it does not literally prevent damage.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: Yes. You can tap that 3/3 creature to pay the Crew 1 cost even though it just entered the battlefield and lacks haste.

Why: The Crew ability requires you to tap "any number of other untapped creatures you control with total power N or greater" [CR 702.122a]. A creature that was just cast enters untapped, so it satisfies the "untapped" requirement, and its power of 3 meets the "1 or greater" threshold. The card-specific ruling for Smuggler's Copter explicitly confirms: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. Haste is irrelevant here because the restriction it removes applies to attacking, not to tapping a creature to pay an activated-ability cost.

Review: **correct**. Correct: an untapped creature that just entered may be tapped to pay a Vehicle crew cost; CR 702.122a and the Smuggler’s Copter ruling support this.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No. Because you cast Smuggler's Copter this turn, you haven't controlled it continuously since your turn began, and it has no haste, so it cannot attack this turn.

Why: Once crewed, a Vehicle "behaves exactly like any other artifact creature" and "can't attack unless you've controlled it continuously since your turn began" [C10]. Haste is the only way to bypass that restriction [CR 702.10b], and Smuggler's Copter's printed abilities are Flying, the draw/discard trigger, and Crew 1—no haste [C1].

Review: **correct**. Correct new Vehicle cannot attack without haste; card ruling and haste definition support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: No. Tapping the blocker does not remove it from combat, and it still assigns its combat damage normally.

Why: A creature "remains a blocking creature until it's removed from combat or the combat phase ends" [CR 509.1g], and tapping is not a removal-from-combat effect. In the combat damage step, "each blocking creature assigns combat damage equal to its power" [CR 510.1a], and a blocking creature "assigns combat damage to the creatures it's blocking" [CR 510.1d]. None of these rules condition damage assignment on the creature being untapped, so the tapped 3/3 still deals 3 damage to the creature it is blocking.

Review: **correct**. Correct blocker remains blocking and deals normal damage; cited combat rules support results, though direct 506.4b omitted.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 damage on it. Double strike has no effect here.

Why: In a fight, each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Double strike is a static ability that modifies only the combat damage step [CR 702.4a], so it does not cause the 3/3 to deal damage a second time in a fight.

Review: **partial**. Correctly distinguishes fight damage from double strike and says the 3/3 dies and 4/4 survives, but adds the false detail that only 1 damage is marked on the 4/4; it was dealt 3 damage. The required answer criteria pass, but this unsupported factual claim makes the answer not fully correct.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: The Control Magic Aura leaves the game, and the creature remains on the battlefield under Alice's control.

Why: When Bob loses and leaves the game, objects he owns (including the Control Magic Aura he cast) leave the game as a result [CR 405.6h]. The creature is owned by Alice, so it stays; with the Aura gone, the "You control enchanted creature" effect ceases and the creature reverts to its owner's control [C1]. Bob's prior control of the creature did not extend to the Aura attached to it [C2]. The specific disposition of objects owned by a leaving player is governed by rule 800.4a, which is referenced by [CR 405.6h] but not reproduced in the supplied excerpts; the answer above assumes the standard application of that rule (objects owned by the leaving player leave the game).

Review: **correct**. Correct Aura leaves and creature returns to Alice. Answer admits 800.4a is missing and assumes its content; 405.6h is only a cross-reference, not sufficient evidence for which objects leave.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Need details: The supplied reference excerpts do not include the rule governing what happens to objects a player owns or controls when that player leaves the game (the relevant provision is in the "Leaving the Game" section of the rules, which is not among the provided excerpts). I cannot determine from the given sources whether the Lightning Bolt is removed from the stack when Bob leaves, and therefore cannot rule on whether it still resolves. Please provide the applicable "Leaving the Game" rule text (or the specific rule number you'd like me to work from) so I can give a supported answer.

Review: **abstained**. Unnecessary abstention; the supplied complete game state has a determinate answer under the multiplayer leaving-game rule, though this retrieval result did not pack that rule. This answer makes no unsupported rule-number claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Ruling: No. The 12 damage dealt while the commander was controlled by Alice and the 9 damage dealt while it was controlled by Bob are tracked separately. You have 12 commander damage from Alice and 9 from Bob, but neither total reaches 21, so you do not lose.

Why: Commander damage is tracked per player, not per card. The loss condition is met when a player has been dealt 21 or more combat damage by *that player's* commanders during the game. Because the controller changed between the two damage events, the damage is attributed to two different players and does not combine.

Note: The specific commander-damage rule (903.10) is not included in the reference excerpts provided here, so I cannot attach a direct citation. If you'd like, I can re-answer once that rule text is supplied.

Review: **incorrect**. Incorrect and unsupported: the same commander dealt both amounts, so its 12 and 9 combat damage to the same player accumulate to 21 regardless of who controlled it. This answer falsely says they are tracked separately by controller.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 903.10a

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand. That choice is a replacement effect, not a state-based action.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, the owner may put it into the command zone instead, and labels this a replacement effect [CR 903.9b]. The state-based action in rule 903.9a applies only when the commander is already in a graveyard or in exile [CR 903.9a], which is a different situation from a "return to hand" event.

Review: **correct**. Correct command-zone option is a hand/library replacement effect under 903.9b, not the graveyard/exile SBA.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the player being dealt damage) chooses the order. The possible damage totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran).

Why: When multiple replacement effects modify how damage is dealt, the affected player chooses the order [CR 616.1], confirmed by both the Torbran ruling [C4] and the Furnace of Rath ruling [C6]. Applying Torbran first changes 3 → 5, then Furnace doubles 5 → 10; applying Furnace first changes 3 → 6, then Torbran adds 2 to get 8. The opponent picks whichever order they prefer.

Review: **correct**. Correct affected opponent chooses; both 8 and 10 with matching orders, supported by Oracle and 616.1.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having an empty library by itself is not a state-based action that causes you to lose the game. You lose only if you *attempt to draw* a card from that empty library.

Why: The loss condition is specifically tied to an attempted draw from an empty library, not to the library being empty in general. [CR 704.5b] states the player loses only if they "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] likewise requires that the player "attempts to draw a card from a library with no cards in it." No rule in the supplied excerpts makes an empty library alone a losing condition.

Review: **correct**. Correct no loss merely for empty library; attempted draw condition explicitly cited.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Need details:

1. Does your attacking creature have trample (or trample over planeswalkers)?
2. What is the power of your attacker, and what is the toughness of the blocking creature (or creatures)?
3. Is your attacker attacking a player or a planeswalker?

Review: **correct**. Appropriate clarification asks about trample and attacker/blocker stats, without inventing a total.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No to both. Your copy does not get the counters on the original creature, and it does not get the bonus (e.g., +1/+1) from an enchantment attached to that creature.

Why: When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects, face-down status, and certain "as it enters" abilities). "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An enchantment's bonus is a continuous effect from a separate source, not part of the creature's printed or copiable values, so it does not transfer to the copy. [CR 707.2]

Review: **incorrect**. Fails frozen clarification criteria: gives unconditional answer without asking copy effect/enchantment details. 707.2 describes ordinary copy values but includes exceptions; unspecified effects could affect those values.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details: What are the two replacement effects (their exact text), and what is the original effect that creates the token (e.g., "create a 1/1 token," "create two tokens")? The number of tokens depends entirely on what each replacement effect does (e.g., doubling, tripling, adding a fixed number, etc.).

Review: **correct**. Appropriate clarification asks exact effects and original count; no invented number.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

