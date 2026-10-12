# concise-outcomes-heldout

Status: **complete** · implementation commit `18b40500a9f85ff3ac141891bccab543e0d10c9d`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 24/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 78.6% |
| Cases retrieving every expected evidence group | 17/32 |
| Answers with citations | 29/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 6 |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 24/32 reviewed |
| Reviewed accuracy | 75.0% |
| Mean reviewed rubric score | 93.8% |
| Median successful response | 11.04 s |
| p95 successful response | 21.71 s |
| Median first visible answer token | 9.43 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | partial | 21.71 |
| h02-intervening-if (r1) | 100.0% | correct | 7.75 |
| h03-independent-trigger (r1) | 50.0% | correct | 14.01 |
| h04-replacement-death (r1) | 75.0% | correct | 7.60 |
| h05-simultaneous-death (r1) | 100.0% | correct | 8.77 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 8.51 |
| h07-infect-lifelink (r1) | 100.0% | partial | 11.24 |
| h08-protection-wrath (r1) | 100.0% | correct | 11.11 |
| h09-protection-aura (r1) | 100.0% | correct | 6.27 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.81 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 10.98 |
| h12-split-second (r1) | 100.0% | correct | 17.07 |
| h13-sacrifice-cost (r1) | 66.7% | partial | 12.30 |
| h14-flashback-countered (r1) | 66.7% | correct | 12.30 |
| h15-rebound-countered (r1) | 66.7% | correct | 8.14 |
| h16-persist-counter (r1) | 100.0% | correct | 8.15 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 26.70 |
| h18-blink-target (r1) | 75.0% | correct | 12.34 |
| h19-equip-timing (r1) | 75.0% | partial | 17.07 |
| h20-crew-new-creature (r1) | 66.7% | correct | 14.87 |
| h21-new-vehicle (r1) | 50.0% | correct | 10.30 |
| h22-tapped-blocker (r1) | 0.0% | correct | 12.61 |
| h23-fight-double-strike (r1) | 100.0% | partial | 9.36 |
| h24-leaving-controller (r1) | 100.0% | correct | 11.17 |
| h25-leaving-stack (r1) | 100.0% | partial | 20.05 |
| h26-commander-control (r1) | 0.0% | abstained | 11.53 |
| h27-commander-hand (r1) | 100.0% | correct | 7.36 |
| h28-replacement-order (r1) | 100.0% | correct | 12.94 |
| h29-empty-library (r1) | 100.0% | correct | 8.06 |
| h30-ambiguous-combat (r1) | 100.0% | correct | 8.91 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 7.09 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 8.71 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: All three abilities are put on the stack simultaneously. From bottom to top the stack is Alice, Bob, Charlie. They resolve in the reverse order: Charlie's ability first, then Bob's, then Alice's last.

Why: Because all three abilities trigger at the same time (the beginning of upkeep) and are put on the stack at the same time, [CR 405.3] applies: the active player's objects go on lowest, followed by the other players' objects in APNAP order (Alice → Bob → Charlie). Resolution proceeds from the top of the stack, so Charlie's resolves first, then Bob's, then Alice's [CR 608.1][CR 405.5]. The active player receives priority only after all of these have been placed on the stack [CR 117.3a][CR 503.1a].

Review: **partial**. Correct APNAP ordering and resolution, but says the abilities are put on the stack simultaneously; they are placed in APNAP order sequentially. CR 603.3b supports the required order, while the added simultaneity claim is incorrect.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, so the condition (40 or more life) is checked both when the ability triggers and again as it resolves. If your life total is 39 or less at resolution, the ability does nothing. [CR 603.4] [C2]

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. Once the enters-the-battlefield ability is on the stack, it exists independently of Solemn Simulacrum. Destroying the Simulacrum does not remove or affect the ability, and it will resolve normally, letting you search your library for a basic land card, put it onto the battlefield tapped, and shuffle.

Why: A triggered ability on the stack "has the text of the ability that created it and no other characteristics" [CR 405.4], and it "remains on the stack until it's countered, it resolves, a rule causes it to be removed from the stack, or an effect moves it elsewhere" [CR 603.3]. The ability's effect ("you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle" [C1]) references your library and the battlefield, not the Simulacrum, so the source being in a graveyard at resolution is irrelevant.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "when this creature dies" ability does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exile, so the card is never actually put into a graveyard [C1]. Because the trigger condition is never met, the ability does not trigger [C2].

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers **three** times—once for itself dying and once for each of the two other creatures dying.

Why: The card-specific ruling states that if Blood Artist and one or more other creatures die at the same time, its ability triggers for each of those creatures [C2]. "Dies" means "is put into a graveyard from the battlefield" [CR 700.4], and leaves-the-battlefield triggers look back in time so they fire even when the source is itself leaving the battlefield in the same event [CR 603.10a]. Since all three creatures are put into a graveyard from the battlefield simultaneously, each one satisfies the "this creature or another creature dies" condition independently, producing three separate triggers.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: Lifelink triggers only when damage is actually **dealt** by the source: "Damage dealt by a source with lifelink causes that source's controller… to gain that much life" [CR 702.15b]. If a prevention effect stops all 3 damage, no damage is dealt, so the condition for lifelink's life gain is never met.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent's life total is unchanged, your opponent gains 3 poison counters, and you gain 3 life.

Why: Infect is a replacement effect that changes the result of damage dealt to a player from life loss to gaining poison counters, so the 3 damage does not reduce your opponent's life total [CR 702.90b]. Lifelink causes the source's controller to gain life equal to the damage dealt "in addition to any other results that damage causes," so the infect replacement does not prevent the life gain [CR 702.15b]. Both effects apply independently to the same damage event.

Review: **partial**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature. Protection from white does not prevent it.

Why: Protection only prevents targeting, enchanting, equipping, damage, and blocking by sources with the stated quality [CR 702.16b]–[CR 702.16f]. Wrath of God is a non-targeting "Destroy all creatures" effect [C1], which none of those protections address. Since your creature is still a creature when Wrath resolves, it is destroyed.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The white Aura is put into its owner's graveyard as a state-based action.

Why: Protection from white means the permanent can't be enchanted by Auras that have the stated quality, and any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c]. The Aura was legal when it attached, but the moment the creature gains protection from white, the Aura becomes an illegal attachment and is removed to the graveyard.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes. You can target your own Slippery Bogle with your own Giant Growth.

Why: Hexproof restricts targeting only by spells or abilities your *opponents* control [CR 702.11b]. Since you control both the Bogle and the Giant Growth, the hexproof restriction does not apply to your own spell. The Bogle is a legal target for your Giant Growth.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

Why: Abrupt Decay's Oracle text states "This spell can't be countered" [C1], which prevents any effect—including ward's "counter that spell or ability" clause [CR 702.21a]—from countering it. The 2024-04-12 card ruling confirms this directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2]. The ward ability still triggers and you are still offered the option to pay, but the counter portion simply cannot apply to Abrupt Decay.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. You can turn Willbender face up as a special action while Krosan Grip is on the stack, and its triggered ability will resolve before Grip to redirect its target to your other artifact.

Why: Split second prevents casting spells and activating non-mana abilities, but it explicitly allows special actions and triggered abilities to function normally [CR 702.61b]. Turning a face-down permanent face up is a special action that doesn't use the stack [CR 702.37e], and the Krosan Grip ruling confirms this interaction directly [C5]. Once Willbender's "when turned face up" ability triggers, it is put on the stack above Krosan Grip [CR 405.2], so it resolves first and changes Grip's target to your second artifact before Grip resolves.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond to destroy the creature, because the sacrifice is completed as part of paying Fling's additional cost before the spell is on the stack and before anyone receives priority to respond.

Why: The card-specific ruling states explicitly that "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." [C3] The sacrifice is a mandatory part of the casting process [C4], and priority is only given after the spell is fully cast with all costs paid [CR 117.3c]. By the time your opponent could act, the creature is already in the graveyard and Fling is on the stack.

Review: **partial**. The conclusion is right, but it falsely says the sacrifice happens before the spell is on the stack. CR 601.2a moves the spell to the stack before CR 601.2h pays costs; CR 117.2e says players do not receive priority during casting. That governing sequence is missing from packed excerpts. The card ruling supports no response, not the stated stack chronology.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 601.2h

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice is exiled, and you do not draw a card.

Why: Because you paid the flashback cost, Think Twice is exiled instead of going to the graveyard any time it leaves the stack, including when it is countered [CR 702.34a] [C2]. The "Draw a card" instruction is part of the spell's resolution [CR 608.2c]; a countered spell never resolves, so that effect never occurs [C2].

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If Ephemerate is countered, rebound does not exile it and you do not get to cast it again next upkeep. The spell is put into its owner's graveyard.

Why: Rebound's replacement effect applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The card-specific ruling confirms that if a rebound spell cast from your hand is countered, "none of its effects will happen, including rebound," and the spell goes to the graveyard [C5].

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard from the battlefield, persist does not trigger and the card does not return to the battlefield.

Why: Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield; if a -1/-1 counter is present at that moment, the condition fails and the ability never triggers [C6].

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger.

Why: At the moment the state-based action puts Young Wolf into the graveyard, it still has a +1/+1 counter on it, so the condition "if it had no +1/+1 counters on it" is not met [CR 702.93a]. +1/+1 and -1/-1 counters do not cancel or "remove" each other; they are separate counters that both remain on the permanent until it leaves the battlefield, and the -1/-1 until end of turn effect is a continuous P/T modifier, not a counter removal [CR 704.8]. The example in [CR 704.8] is directly on point: Young Wolf with one +1/+1 counter and -1/-1 counters dies, and undying does not trigger because it had a +1/+1 counter when it was last on the battlefield.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No. The Lightning Bolt will not damage the creature that Cloudshift returns.

Why: Cloudshift's ruling explicitly states that "the returned card won't be the target of any spells or abilities that targeted it before" [C5], and the returned permanent is "considered a new object with no relation to the object that it was" [C3]. Because Lightning Bolt's target is no longer legal when it resolves, the spell doesn't resolve and deals no damage [CR 608.2b].

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

Why: The equip ability carries the timing restriction "Equip only as a sorcery" [C2], which the rules define as "Activate only as a sorcery" [CR 702.6a]. A sorcery-speed action may be taken only during your main phase while the stack is empty [CR 117.1a]. Because Lightning Bolt is on the stack when you would respond, the stack is not empty, so the equip ability is not legally activatable at that moment.

Review: **partial**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: Yes. You can tap your 3/3 creature (even though it was just cast and has no haste) to pay the Crew 1 cost of Smuggler's Copter.

Why: Crew is an activated ability of the Vehicle, not of the creature; the creature is simply tapped as part of that ability's cost [CR 702.122a]. The card-specific ruling for Smuggler's Copter explicitly states: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. The summoning-sickness restriction on a creature's own tap/untap abilities [CR 702.10c] does not prevent it from being tapped as a cost for another permanent's ability.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No. Because you cast Smuggler's Copter this turn, you have not controlled it continuously since your turn began, and it has no haste, so it cannot attack this turn.

Why: A Vehicle that becomes a creature "can't attack unless you've controlled it continuously since your turn began" [C10]. Haste would waive that requirement [CR 702.10b], but Smuggler's Copter does not have haste [C1]. Even though you can crew it before the declare attackers step [C13], the continuous-control restriction still applies.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: No. Tapping the blocker does not remove it from combat and does not stop it from assigning combat damage. It remains a blocking creature and will still assign 3 damage to the creature it is blocking during the combat damage step.

Why: A creature "remains a blocking creature until it's removed from combat or the combat phase ends" [CR 509.1g], and tapping is neither of those events. A blocking creature "assigns combat damage to the creatures it's blocking" and only assigns no damage if it "isn't currently blocking any creatures (if, for example, they were destroyed or removed from combat)" [CR 510.1d]. Since tapping does not remove the creature from combat or cause it to stop blocking, it still assigns combat damage equal to its power [CR 510.1a].

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 damage on it. Double strike has no effect here.

Why: Fight damage is not combat damage [CR 701.14d], and double strike is a static ability that modifies only the combat damage step [CR 702.4a]. In a fight, each creature simply deals damage equal to its power to the other [CR 701.14a], so the 3/3's double strike is irrelevant and the 4/4's 4 damage exceeds the 3/3's toughness.

Review: **partial**. The damage and survival conclusions are correct, and double strike is irrelevant, but the answer says the surviving 4/4 has 1 damage marked. It took 3 damage from the 3/3, so that detail is wrong and unsupported.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: When Bob leaves the game, his Control Magic (which he owns) leaves the game, and the control effect it was generating ends. Alice's creature reverts to her control, since she is its owner.

Why: When a player leaves the game, all objects they own leave the game and any effects giving that player control of objects end [CR 800.4a]. The rules example directly parallels this situation: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a]. Because Bob owns the Aura, it is removed from the game rather than remaining attached to Alice's creature.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Ruling: No, the Lightning Bolt does not resolve. When Bob leaves the game, the Bolt is removed from the stack before it ever gets the chance to resolve.

Why: [CR 800.4a] states that when a player leaves the game, "all objects owned by that player leave the game." The Lightning Bolt is a card owned by Bob, so it leaves the game (is removed from the stack) as part of that process. The Bribery example in the same rule confirms that a spell on the stack owned by the departing player simply leaves the game. Because the Bolt is no longer on the stack, [CR 608.1] (resolution occurs when all players pass in succession) can never trigger for it, and no damage is dealt to Alice.

Review: **partial**. Correctly says Bolt leaves and does not resolve under CR 800.4a. However, the Bribery example concerns a permanent put onto the battlefield from a leaving player’s library, not a spell on the stack; it does not confirm that claim. The rule’s general owned-object sentence directly supports the conclusion.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Need details: The supplied reference excerpts do not include the Commander damage rule (the 21-combat-damage threshold and how it is tracked across controllers). I cannot confirm or deny whether damage dealt by the same commander while controlled by different players accumulates toward that threshold without the relevant rule text. Could you attach the specific Commander damage rule (typically found in rule 903.10 or 903.11) or the card's Oracle text so I can ground the answer in a cited source?

Review: **abstained**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 903.10a

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect—not a state-based action.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner's hand from anywhere, the owner may put it into the command zone instead, and labels that choice a "replacement effect" [CR 903.9b]. The state-based action in rule 903.9a applies only when the commander is already in a graveyard or in exile, which is a different scenario [CR 903.9a].

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: Your opponent (the player being dealt damage) chooses the order. The possible totals are **8** (Furnace of Rath first, then Torbran: 3 → 6 → 8) or **10** (Torbran first, then Furnace of Rath: 3 → 5 → 10).

Why: When multiple replacement effects modify how damage is dealt, the affected player chooses the order to apply them [CR 616.1], a principle confirmed in both Torbran's and Furnace of Rath's card-specific rulings [C4][C6]. Torbran adds 2 to the damage [C1], while Furnace of Rath doubles it [C5]; applying them in either order to Lightning Bolt's 3 damage [C11] yields 8 or 10, and the opponent picks which.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having an empty library by itself is not a state-based action that causes you to lose the game. You lose only if you *attempt to draw* a card from that empty library.

Why: The loss condition is specifically tied to an attempted draw from an empty library, not to the library being empty in general. [CR 704.5b] states the player loses only if they "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] likewise requires that the player "attempts to draw a card from a library with no cards in it." Neither rule imposes a loss for merely having zero cards in the library.

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Need details:

1. Does your attacking creature have trample (or trample over planeswalkers)?
2. What is the creature's power, and what is the toughness of the blocking creature (or creatures)?
3. Is the creature attacking a player or a planeswalker?

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No to both. Your copy does not get the creature's counters, and it does not get the bonus from the enchantment attached to the original.

Why: When copying an object, "other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied" [CR 707.2]. An enchantment's bonus is an external effect on the original, not part of its copiable values, so it does not transfer to the copy. Likewise, any counters on the original creature are explicitly excluded from what a copy acquires.

Review: **incorrect**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details:

1. What are the two replacement effects (card names or exact text)?
2. What is the original effect creating the tokens, and how many tokens does it normally create?

Review: **correct**. Same substantive ruling as the previous reviewed run; rechecked this wording. Citation support not separately regraded for this prompt run.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

