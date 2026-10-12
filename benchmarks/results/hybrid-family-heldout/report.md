# hybrid-family-heldout

Status: **complete** · implementation commit `d55b40a747a4382d9e8aebb4d41c65db85575948`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 28/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 77.9% |
| Cases retrieving every expected evidence group | 16/32 |
| Answers with citations | 29/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 3 |
| Reviewed citation-support failures | 6 |
| Reviewed fully correct | 28/32 reviewed |
| Reviewed accuracy | 87.5% |
| Mean reviewed rubric score | 90.6% |
| Median successful response | 11.11 s |
| p95 successful response | 20.92 s |
| Median first visible answer token | 9.21 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 66.7% | correct | 13.42 |
| h02-intervening-if (r1) | 100.0% | correct | 8.19 |
| h03-independent-trigger (r1) | 50.0% | correct | 13.64 |
| h04-replacement-death (r1) | 75.0% | correct | 8.66 |
| h05-simultaneous-death (r1) | 100.0% | correct | 19.04 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 10.47 |
| h07-infect-lifelink (r1) | 100.0% | correct | 12.02 |
| h08-protection-wrath (r1) | 33.3% | correct | 20.92 |
| h09-protection-aura (r1) | 100.0% | correct | 6.64 |
| h10-own-hexproof (r1) | 100.0% | correct | 8.49 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 10.41 |
| h12-split-second (r1) | 100.0% | correct | 15.86 |
| h13-sacrifice-cost (r1) | 66.7% | partial | 12.89 |
| h14-flashback-countered (r1) | 66.7% | correct | 9.01 |
| h15-rebound-countered (r1) | 66.7% | correct | 9.30 |
| h16-persist-counter (r1) | 100.0% | correct | 9.51 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 19.97 |
| h18-blink-target (r1) | 75.0% | correct | 25.59 |
| h19-equip-timing (r1) | 50.0% | correct | 19.41 |
| h20-crew-new-creature (r1) | 100.0% | correct | 13.10 |
| h21-new-vehicle (r1) | 50.0% | correct | 10.04 |
| h22-tapped-blocker (r1) | 100.0% | correct | 6.33 |
| h23-fight-double-strike (r1) | 0.0% | incorrect | 11.76 |
| h24-leaving-controller (r1) | 100.0% | correct | 12.00 |
| h25-leaving-stack (r1) | 50.0% | abstained | 15.49 |
| h26-commander-control (r1) | 100.0% | correct | 14.43 |
| h27-commander-hand (r1) | 100.0% | correct | 8.29 |
| h28-replacement-order (r1) | 100.0% | correct | 14.77 |
| h29-empty-library (r1) | 100.0% | correct | 8.93 |
| h30-ambiguous-combat (r1) | 50.0% | correct | 6.50 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 8.57 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 9.13 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The abilities go on the stack in APNAP order—Alice's first (bottom), Bob's second, Charlie's third (top). They resolve in reverse: Charlie's ability resolves first, then Bob's, then Alice's.

Why: When multiple triggered abilities are waiting, each player in APNAP order (active player first, then turn order) puts their triggered abilities on the stack [CR 603.3b]. Since Alice is active and turn order is Alice → Bob → Charlie, APNAP is Alice, Bob, Charlie, so their abilities are added in that sequence, each on top of the ones already there [CR 405.2]. When all players pass, the topmost object resolves first [CR 405.5], so Charlie's resolves, then Bob's, then Alice's.

Review: **correct**. Correct APNAP stack order and reverse resolution; CR 603.3b, 405.2, and 405.5 support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, so the 40-or-more-life condition is checked both when the ability triggers and again as it resolves. [CR 603.4] The card-specific ruling confirms that if you have fewer than 40 life when the ability tries to resolve, it does nothing. [C2]

Review: **correct**. Correct intervening-if checks at trigger and resolution; CR 603.4 and the Felidar ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. You may still search for a basic land, put it onto the battlefield tapped, and shuffle. The Simulacrum no longer needs to be on the battlefield for that ability to resolve.

Why: Once the enters-the-battlefield ability triggered, it went on the stack as an independent object carrying the text of the ability, with no ongoing link to the source permanent [CR 603.3]. The "you may" option is a choice made when the ability resolves, not when it triggers [CR 603.5], and the effect ("search your library…") places no requirement that the Simulacrum still exist. The destruction of the Simulacrum is irrelevant to the ability already sitting on the stack.

Review: **correct**. Correct surviving ETB search, but 603.3/405.1 do not directly supply the general independent-of-source rule (CR 113.7a). This is a citation support gap.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "when this creature dies" ability does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's static ability replaces that zone change with exile, so the card is never actually put into a graveyard [C1]. Because the creature is never put into a graveyard, the "dies" trigger condition is never met, and the ability does not trigger [C2].

Review: **correct**. Correct: Rest in Peace replaces the graveyard event, so the creature does not die; Oracle and card-specific ruling support result.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers **three** times—once for itself dying and once for each of the two other creatures dying.

Why: The trigger condition "Whenever this creature or another creature dies" is satisfied by each individual creature's death, so simultaneous deaths produce one trigger per creature [C2]. Because this is a leaves-the-battlefield trigger, the game looks back in time to confirm the trigger even though Blood Artist is itself moving to the graveyard in the same event [CR 603.10a]. With three creatures dying (Blood Artist + two tokens), you get three separate triggers, each causing a target player to lose 1 life and you to gain 1 life [C1].

Review: **correct**. Correct three Blood Artist triggers, including its own; dated ruling states simultaneous deaths trigger for each creature.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: Lifelink causes life gain only for damage that is actually *dealt*—[CR 702.15b] states "Damage dealt by a source with lifelink causes that source's controller… to gain that much life." Under the damage-processing sequence, prevention effects are applied before damage is dealt [CR 120.4b], so if all 3 damage is prevented, 0 damage is dealt and the lifelink condition is never met.

Review: **correct**. Correct zero life. Cited rules establish when lifelink gains life, but the answer does not cite the rule defining what prevention does to the damage event; its cited excerpts do not fully establish the no-damage step.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent's life total is unchanged, your opponent gains 3 poison counters, and you gain 3 life.

Why: Infect replaces the normal life-loss result of damage dealt to a player with the application of poison counters, so the opponent does not lose life [CR 702.90b] [CR 120.3b]. Lifelink is an "in addition to" effect: the controller of the source gains life equal to the damage dealt, regardless of what other results the damage produces [CR 702.15b] [CR 120.3f]. The two abilities operate on separate results (the recipient's life loss vs. the source controller's life gain), so both apply simultaneously.

Review: **correct**. Correct poison and life totals. Correctly describes infect and lifelink as separate damage results, not replacement effects.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature. Protection from white does not save it.

Why: Wrath of God reads "Destroy all creatures" and does not target any specific creature [C1]. Protection from a color prevents only being targeted, damaged, blocked, or enchanted by that color; it does not prevent a permanent from being destroyed by a non-targeting effect. Because the creature lacks indestructible, nothing stops the destruction [CR 702.12b]. (Note: the specific protection rule, 702.16, is not included in the supplied excerpts, so I cannot cite it directly, but the Wrath of God text and the destroy rule [CR 701.8b] confirm the effect applies to all creatures regardless of protection.)

Review: **correct**. Correct that Wrath destroys the creature, but the supporting citation is the card text and the general definition of destroy; the cited sources do not establish protection’s scope.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 702.16b, CR 702.16e

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The white Aura is put into its owner's graveyard as a state-based action.

Why: Protection from a quality means the protected permanent can't be enchanted by Auras with that quality, and any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c]. This is distinct from Equipment, which simply becomes unattached and remains on the battlefield [CR 702.16d].

Review: **correct**. Correct Aura is put in its owner’s graveyard as an SBA under protection; CR 702.16c supports this. Extra Equipment contrast is correct.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes. You can target your own Slippery Bogle with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you are the controller of both the Bogle and the Giant Growth, you are not an opponent, so the hexproof restriction does not apply to your own spell. Giant Growth simply requires "target creature" [C2], which the Bogle satisfies.

Review: **correct**. Correct own spell may target own hexproof creature; 702.11b and Oracle text support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

Why: Abrupt Decay's text states "This spell can't be countered" [C1], which overrides ward's "counter that spell or ability unless that player pays [cost]" instruction [CR 702.21a]. The 2024 card-specific ruling confirms this directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2]. The ward ability still triggers and you are still offered the choice to pay, but the counter effect simply cannot apply to a spell that can't be countered.

Review: **correct**. Correct: ward ability triggers but cannot counter uncounterable Abrupt Decay, and it resolves if target remains legal; Oracle, ward rule and card ruling support this.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. You can turn Willbender face up as a special action while Krosan Grip is on the stack, its "when turned face up" trigger fires and goes on the stack, and it resolves before Grip to redirect Grip's target to your other artifact.

Why: Turning a face-down permanent face up is a special action, not an activated ability, so split second does not prohibit it [CR 702.37e][CR 702.61b]. Willbender's trigger fires when it is turned face up [C13], and triggered abilities are put on the stack and resolve normally during split second [CR 702.61b][C2]. Because the trigger sits above Grip on the stack, it resolves first and can change Grip's single target to your other legal artifact [C1].

Review: **correct**. Correct morph as special action under split second and normal trigger can redirect Grip. Supplied morph, split-second, Willbender and Grip sources support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond to destroy the sacrificed creature, because the sacrifice is paid as part of the cost before the spell is considered cast, and opponents only receive priority after the spell is fully cast.

Why: The sacrifice is part of paying Fling's total cost at step 601.2h, which occurs before the spell "becomes cast" at step 601.2i [CR 601.2h][CR 601.2i]. Opponents can only respond once the spell has been cast and all its costs have been paid; by that point the creature is already in the graveyard [C3]. You must sacrifice exactly one creature as the additional cost, and you cannot cast Fling without doing so [C4].

Review: **partial**. Correct no response to prevent sacrifice, but falsely says the spell is fully on the stack only after costs are paid. Casting procedure puts the spell on the stack before cost payment (601.2a before 601.2h); this confuses a meaningful timing detail.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice is exiled, and you do not draw a card.

Why: The flashback ability creates a replacement effect that says "exile this card instead of putting it anywhere else any time it would leave the stack" [CR 702.34a], so when the countered spell is removed from the stack it goes to exile rather than the graveyard [C2]. Because the spell was countered, it never resolved, so the "Draw a card" instruction was never carried out [CR 608.1].

Review: **correct**. Correct flashback exiles countered spell and no draw; 702.34a and card ruling directly support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If Ephemerate is countered, Rebound does not exile it. The spell goes to your graveyard and you do not get to cast it again next upkeep.

Why: Rebound is a static ability that modifies what happens "as it resolves"—specifically, it replaces the final step of putting the spell into the graveyard with exiling it [CR 702.88a]. A countered spell never resolves, so that replacement effect never applies. The card-specific ruling confirms this directly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve…none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn" [C5].

Review: **correct**. Correct rebound applies only as spell resolves, so a countered spell goes to graveyard and has no rebound cast next turn; rule and dated ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist does not trigger and it does not return to the battlefield.

Why: Persist's condition requires that the permanent "had no -1/-1 counters on it" at the moment it is put into the graveyard from the battlefield [CR 702.79a]. The Kitchen Finks-specific ruling confirms that persist checks the creature's counters just before it leaves the battlefield, and if any -1/-1 counters are present, the ability simply does not trigger [C6].

Review: **correct**. Correct persist checks for -1/-1 counters at last moment on battlefield; 702.79a and Kitchen Finks ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger.

Why: Undying's condition is "if it had no +1/+1 counters on it," checked using last known information because it is a leaves-the-battlefield trigger [CR 702.93a] [CR 603.10a]. Your Young Wolf had a +1/+1 counter on it when it was last on the battlefield; the -1/-1 counter and the -1/-1 until end of turn effect modify its toughness but do not remove or negate the +1/+1 counter. The example in [CR 704.8] addresses this exact scenario (Young Wolf with a +1/+1 counter and -1/-1 counters) and concludes undying does not trigger because the +1/+1 counter was present. Counters do not "cancel" each other; they simply coexist on the object until it leaves the battlefield.

Review: **correct**. Correct no undying using pre-SBA state; 704.8 supplies direct Young Wolf example. Frozen evidence group mistakenly names 704.7; see reference addendum.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No. Lightning Bolt will not deal damage to the returned creature. Because the target is no longer legal when the Bolt tries to resolve, the Bolt doesn't resolve at all.

Why: Cloudshift exiles the creature, removing it from the battlefield, and the card that returns is not the same target as the one Lightning Bolt was aiming at [C5]. A target that is no longer in the zone it was in when targeted is illegal [CR 608.2b]. Since all of Lightning Bolt's targets are illegal, it doesn't resolve and deals no damage [CR 608.2b].

Review: **correct**. Correct new object invalidates Bolt target, so it does not damage returned creature; Cloudshift ruling and 608.2b support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

Why: The equip ability's text reads "Equip only as a sorcery" [C2], which restricts activation to the same timing as casting a sorcery—your main phase with an empty stack. Once Lightning Bolt is on the stack, the stack is no longer empty, so the equip ability is not legally activatable at that moment.

Review: **correct**. Correct equip timing; sorcery-only restriction and stack-not-empty fact support no activation in response.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 702.6a, CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: Yes. You can tap that 3/3 creature to pay the Crew 1 cost of Smuggler's Copter even though it has summoning sickness.

Why: Summoning sickness (CR 302.6) only prevents a creature from attacking or activating its *own* activated abilities that include tap or untap in the cost. Tapping a creature to pay the cost of *another* object's ability (here, the Vehicle's crew ability under CR 702.122a) is not restricted by that rule. The card-specific ruling confirms this directly: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. Since your creature is untapped and has power 3 ≥ 1, it satisfies the crew requirement.

Review: **correct**. Correct that a newly cast untapped creature may crew; 702.122a and Smuggler’s Copter ruling directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No. Smuggler's Copter cannot attack the turn you cast and crew it.

**Why:** Once a Vehicle becomes a creature, it "can't attack unless you've controlled it continuously since your turn began" [C10]. Because you cast it this turn, you have not controlled it since your turn began, and it has no haste to bypass that restriction [CR 702.10b].

Review: **correct**. Correct new Vehicle cannot attack without haste after being cast this turn; Smuggler’s Copter ruling and haste definition support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: No. Tapping the blocker after it has been declared does not remove it from combat and does not prevent it from dealing combat damage.

Why: Rule 506.4b explicitly states that tapping or untapping a creature that's already been declared as an attacker or blocker doesn't remove it from combat and doesn't prevent its combat damage [CR 506.4b]. The creature remains a valid blocker and will assign combat damage normally in the combat damage step [CR 510.1d].

Review: **correct**. Correct tapped blocker remains in combat and assigns damage; 506.4b directly supports it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: Both creatures die. The 3/3 deals 3 damage in the first combat damage step and another 3 in the second (6 total to the 4/4). The 4/4 deals 4 damage in the second combat damage step (4 total to the 3/3). The 3/3 (3 toughness) is dealt 4 damage and dies; the 4/4 (4 toughness) is dealt 6 damage and dies.

Why: Because the 3/3 has double strike, combat is split into two damage steps; only the double-striker assigns damage in the first step, while the 4/4 (no first/double strike) assigns only in the second [CR 510.4]. Each creature assigns damage equal to its power [CR 510.1a], and all assigned damage is dealt simultaneously within each step [CR 510.2]. The 4/4 survives the first step (4 − 3 = 1 HP) but is destroyed by the second step's 3 damage; the 3/3 is destroyed by the 4 damage it takes in the second step.

Review: **incorrect**. Incorrect: applies double strike to a fight and claims both creatures die. Fighting is not combat damage; the 4/4 survives with 3 damage marked. The retrieved primary rules include the fight ability text only indirectly and omit the rule resolving the exact fight; the cited combat-damage rules do not support this result.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.14a, CR 701.14d

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: Control Magic leaves the game (it is owned by Bob, and all objects owned by a player who leaves the game leave the game). The creature reverts to Alice's control, since she is its owner and the only control-changing effect on it has ended.

Why: Rule 800.4a states that when a player leaves the game, all objects they own leave the game and any effects giving that player control of objects end. The worked example in that rule is directly on point: "Alex casts Mind Control, an Aura that reads, 'You control enchanted creature,' on Bianca's Assault Griffin. If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control." [CR 800.4a] Additionally, gaining control of a creature does not transfer attached Auras to the new controller, so the Aura was never Alice's to begin with and leaves with Bob. [C2]

Review: **correct**. Correct Bob-owned Control Magic leaves the game and Alice’s creature reverts to her; 800.4a directly illustrates this.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Need details: The provided reference excerpts do not include the rule governing what happens to a player's objects (including spells on the stack) when that player leaves a multiplayer game (the relevant rule is in the 800s range, e.g., CR 810.5). Without that excerpt I cannot cite a supporting source for the ruling. Could you confirm whether you'd like me to answer based on general knowledge of that rule, or can you supply the relevant excerpt?

Review: **abstained**. Unnecessary abstention: 800.4a is required evidence but was not packed. Also suggests 104.3a, which is not the leaving-player objects rule; incorrect reference is an unsupported claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Ruling: Yes. The 12 and 9 add together to 21, and you lose the game. Commander damage is tracked by the commander (the card), not by whoever controls it at the time the damage is dealt.

Why: The loss condition is "dealt 21 or more combat damage by the same commander over the course of the game" [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of zone or controller [CR 903.3], so all combat damage that card deals to you—whether while controlled by Alice, Bob, or anyone else—accumulates toward the same 21-damage threshold.

Review: **correct**. Correct commander-damage total and loss threshold regardless of controller; 903.10a, 704.6c and 903.3 support each claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect—not a state-based action.

Why: Rule 903.9b explicitly states that if a commander "would be put into its owner's hand or library from anywhere," the owner may put it into the command zone instead, and labels this a "replacement effect" [CR 903.9b]. The state-based action in rule 903.9a applies only to commanders in a graveyard or in exile, not to the hand [CR 903.9a].

Review: **correct**. Correct hand-to-command-zone choice is a replacement effect, distinct from graveyard/exile SBA; 903.9b/903.9a directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the player being dealt damage) chooses the order. The possible damage totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran).

Why: When multiple replacement effects modify the same damage event, the affected player chooses the order [CR 616.1], confirmed by both the Torbran ruling ("the player being dealt damage…chooses an order") [C4] and the Furnace of Rath ruling ("the player who would be dealt damage…chooses the order") [C6]. Applying Torbran first turns 3 into 5, then Furnace doubles it to 10; applying Furnace first turns 3 into 6, then Torbran adds 2 for 8. Each replacement effect applies only once [CR 614.5].

Review: **correct**. Correct affected player chooses, and totals/order are 10 or 8; card rulings and CR 616.1/614.5 support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having zero cards in your library does not, by itself, cause you to lose the game. You lose only if you *attempt to draw* a card from that empty library.

Why: The state-based action that causes a loss is specifically tied to an attempted draw from an empty library, not to the library being empty [CR 704.5b]. Rule 121.4 likewise frames the loss around the act of attempting to draw [CR 121.4]. As long as no effect has required or caused you to draw since the library became empty, no losing condition has been met.

Review: **correct**. Correct empty library alone causes no loss; 704.5b and 121.4 require an attempted draw.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Need details:

1. Does your attacking creature have trample (or trample over planeswalkers)?
2. What is the power of your attacker?
3. What is the toughness of the blocking creature (or creatures), and are there any damage already marked on it?
4. Is your attacker attacking a player or a planeswalker?

Review: **correct**. Appropriate clarification requests trample, relevant power/toughness and other combat details; gives no guessed amount.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 510.1c

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No to both. Your copy does not get the counters on the original creature, and it does not get the bonus (e.g., +1/+1) from an enchantment attached to that creature.

Why: When copying an object, the copy acquires only the copiable values derived from the printed text (as modified by other copy effects, face-down status, and "as it enters" P/T-setting abilities). "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An enchantment's ongoing bonus is an "other effect," and counters are explicitly excluded, so neither transfers to the copy.

Review: **incorrect**. Does not ask for the unspecified copy effect or details and instead gives an unconditional answer, so it fails the frozen clarification criteria. Its default explanation that counters and separate continuous effects are not copied is otherwise supported by 707.2; no factual contradiction is identified.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details: What are the two specific replacement effects? (e.g., "Doubling Season" + "another Doubling Season," or "create twice as many" + "create an additional token," etc.) The final token count depends entirely on what each effect does to the number.

Review: **correct**. Appropriate clarification requests base event and exact replacement effects; no token number is guessed.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

