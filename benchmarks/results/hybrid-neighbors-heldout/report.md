# hybrid-neighbors-heldout

Status: **complete** · implementation commit `8cd2f2fdefeaa477f6f6707ae9bc5e1222f826f2`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 28/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 80.2% |
| Cases retrieving every expected evidence group | 17/32 |
| Answers with citations | 29/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 3 |
| Reviewed citation-support failures | 6 |
| Reviewed fully correct | 28/32 reviewed |
| Reviewed accuracy | 87.5% |
| Mean reviewed rubric score | 90.6% |
| Median successful response | 10.91 s |
| p95 successful response | 17.22 s |
| Median first visible answer token | 9.36 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 66.7% | correct | 14.34 |
| h02-intervening-if (r1) | 100.0% | correct | 7.10 |
| h03-independent-trigger (r1) | 50.0% | correct | 16.98 |
| h04-replacement-death (r1) | 75.0% | correct | 8.21 |
| h05-simultaneous-death (r1) | 100.0% | correct | 12.10 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 9.61 |
| h07-infect-lifelink (r1) | 100.0% | correct | 11.38 |
| h08-protection-wrath (r1) | 33.3% | correct | 13.26 |
| h09-protection-aura (r1) | 100.0% | correct | 8.31 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.83 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 8.72 |
| h12-split-second (r1) | 100.0% | correct | 16.00 |
| h13-sacrifice-cost (r1) | 66.7% | partial | 11.83 |
| h14-flashback-countered (r1) | 66.7% | correct | 9.44 |
| h15-rebound-countered (r1) | 66.7% | correct | 9.11 |
| h16-persist-counter (r1) | 100.0% | correct | 8.38 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 16.21 |
| h18-blink-target (r1) | 75.0% | correct | 17.22 |
| h19-equip-timing (r1) | 75.0% | correct | 14.41 |
| h20-crew-new-creature (r1) | 100.0% | correct | 11.46 |
| h21-new-vehicle (r1) | 50.0% | correct | 12.97 |
| h22-tapped-blocker (r1) | 100.0% | correct | 6.54 |
| h23-fight-double-strike (r1) | 0.0% | incorrect | 13.30 |
| h24-leaving-controller (r1) | 100.0% | correct | 12.48 |
| h25-leaving-stack (r1) | 50.0% | abstained | 18.76 |
| h26-commander-control (r1) | 100.0% | correct | 10.43 |
| h27-commander-hand (r1) | 100.0% | correct | 7.87 |
| h28-replacement-order (r1) | 100.0% | correct | 12.11 |
| h29-empty-library (r1) | 100.0% | correct | 8.88 |
| h30-ambiguous-combat (r1) | 100.0% | correct | 6.66 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 10.42 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 9.67 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The abilities go on the stack in APNAP order—Alice's first (bottom), then Bob's, then Charlie's (top). If nobody responds, they resolve in reverse stack order: Charlie's ability first, then Bob's, then Alice's last.

Why: All three abilities trigger "at the beginning of upkeep," which is not "another ability triggering," so they are all placed in the first part of the two-part process, each player acting in APNAP order (Alice as active player, then Bob, then Charlie) [CR 603.3b]. Each new object is placed on top of everything already on the stack [CR 405.2], making Charlie's ability the topmost. When all players pass in succession, the topmost object resolves first [CR 405.5], so the resolution order is Charlie → Bob → Alice.

Review: **correct**. Correct APNAP stack order and reverse resolution; CR 603.3b, 405.2, and 405.5 support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, so the condition (40 or more life) is checked both when the ability triggers and again as it resolves. [CR 603.4] If you have 39 or less life at resolution, the ability is removed from the stack and does nothing. [C2]

Review: **correct**. Correct intervening-if checks at trigger and resolution; CR 603.4 and the Felidar ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. You may still search your library for a basic land card, put it onto the battlefield tapped, and shuffle. The Simulacrum does not need to remain on the battlefield for the triggered ability to resolve.

Why: Once the ETB ability triggers, it goes on the stack as an independent object with no card associated with it [CR 405.1]. The ability's effect instructs *you* to search, put a land onto the battlefield, and shuffle; it never attempts to do anything to the Simulacrum itself, so the zone-change "look for the object" failure described in [CR 603.6] does not apply. Because the effect contains no condition checking whether the source is still on the battlefield, it resolves normally even after the Simulacrum has been destroyed.

Review: **correct**. Correct surviving ETB search, but 603.3/405.1 do not directly supply the general independent-of-source rule (CR 113.7a). This is a citation support gap.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "When this creature dies, you may draw a card" ability does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's static ability replaces that event with exile, so the card is never actually put into a graveyard [C1]. Because the creature is never put into a graveyard, it never "dies," and the trigger condition is never met [C2].

Review: **correct**. Correct: Rest in Peace replaces the graveyard event, so the creature does not die; Oracle and card-specific ruling support result.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers **three** times—once for itself dying and once for each of the two other creatures dying.

Why: The trigger condition "Whenever this creature or another creature dies" is satisfied three separate times in the simultaneous event: once for "this creature" (Blood Artist) and once for each "another creature" (the two tokens) [C1]. The card-specific ruling confirms that when Blood Artist and other creatures die simultaneously, its ability triggers for each of those creatures [C2]. Because dies-trigger abilities look back in time, the ability triggers even though Blood Artist is already in the graveyard when the triggers are generated [CR 603.10a].

Review: **correct**. Correct three Blood Artist triggers, including its own; dated ruling states simultaneous deaths trigger for each creature.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: Lifelink causes life gain only for damage that is actually **dealt** by the source [CR 702.15b]. Prevention effects remove damage before it is dealt [CR 120.4b], so if all 3 damage is prevented, no damage is dealt and the condition for lifelink's effect is never met.

Review: **correct**. Correct zero life. Cited rules establish when lifelink gains life, but the answer does not cite the rule defining what prevention does to the damage event; its cited excerpts do not fully establish the no-damage step.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent's life total is unchanged, your opponent gains 3 poison counters, and you gain 3 life.

Why: Because the source has infect, the damage to a player does not cause life loss; instead, the controller gives the player that many poison counters [CR 702.90b] [CR 120.3b]. Because the source also has lifelink, its controller gains life equal to the damage dealt, "in addition to any other results that damage causes" [CR 702.15b] [CR 120.3f]. The two abilities produce independent, non-conflicting results.

Review: **correct**. Correct poison and life totals. Correctly describes infect and lifelink as separate damage results, not replacement effects.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes. Wrath of God destroys your creature. Protection from white does not prevent this.

Why: Wrath of God reads "Destroy all creatures. They can't be regenerated" [C1]. It is a non-targeting effect that does not deal damage, enchant, or block—none of which are the things protection actually prevents. Since your creature lacks indestructible, nothing stops the destruction: a permanent without indestructible can be destroyed by an effect that uses the word "destroy" [CR 701.8a], and the "can't be regenerated" clause means a regeneration shield cannot replace the event [C1].

Review: **correct**. Correct that Wrath destroys the creature, but the supporting citation is the card text and the general definition of destroy; the cited sources do not establish protection’s scope.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 702.16b, CR 702.16e

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The white Aura is put into its owner's graveyard as a state-based action.

Why: Protection from white means the creature can't be enchanted by Auras that are white, and any such Aura already attached is removed to its owner's graveyard as a state-based action [CR 702.16c]. This is distinct from Equipment, which simply becomes unattached and stays on the battlefield [CR 702.16d]. The Aura does not remain attached or become unattached on the battlefield; it leaves the battlefield entirely.

Review: **correct**. Correct Aura is put in its owner’s graveyard as an SBA under protection; CR 702.16c supports this. Extra Equipment contrast is correct.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes. You can target your own Slippery Bogle with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you control both the Bogle and the Giant Growth, you are not an opponent of the Bogle, so the hexproof restriction does not apply to your own spell. The Bogle's Oracle text confirms the same limitation: "This creature can't be the target of spells or abilities your opponents control" [C1].

Review: **correct**. Correct own spell may target own hexproof creature; 702.11b and Oracle text support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

Why: Abrupt Decay's Oracle text states "This spell can't be countered" [C1]. Ward's triggered ability instructs the game to "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but a "can't be countered" clause makes that instruction impossible to carry out. The card-specific ruling confirms this directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2].

Review: **correct**. Correct: ward ability triggers but cannot counter uncounterable Abrupt Decay, and it resolves if target remains legal; Oracle, ward rule and card ruling support this.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. You may turn Willbender face up as a special action while Krosan Grip is on the stack, and its triggered ability will go on the stack and resolve, letting you redirect Grip to your other artifact.

Why: Turning a face-down permanent face up via morph is a special action that doesn't use the stack [CR 702.37e], and special actions and triggered abilities are explicitly permitted while a split-second spell is on the stack [CR 702.61b]. The Krosan Grip ruling confirms this: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5]. Willbender's "when turned face up" trigger fires from the morph action [C13], and because it's a triggered ability (not a cast spell or activated ability), it is legal on the stack during split second [CR 702.61b], allowing you to change Grip's target to your other artifact [C8].

Review: **correct**. Correct morph as special action under split second and normal trigger can redirect Grip. Supplied morph, split-second, Willbender and Grip sources support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond to destroy the creature, because the sacrifice is paid as part of the cost before the spell is considered cast, and opponents only receive priority after the spell is fully cast with all costs paid.

Why: The sacrifice is paid during the "pay the total cost" step (601.2h), which occurs before the spell becomes cast (601.2i) and before any player other than the controller gets priority to respond [CR 601.2h][CR 601.2i]. The card-specific ruling confirms this directly: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." [C3]

Review: **partial**. Correct no response to prevent sacrifice, but falsely says the spell is fully on the stack only after costs are paid. Casting procedure puts the spell on the stack before cost payment (601.2a before 601.2h); this confuses a meaningful timing detail.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice is exiled, and you do not draw a card.

Why: The flashback ability creates a replacement effect that says "exile this card instead of putting it anywhere else any time it would leave the stack" [CR 702.34a], so when the countered spell leaves the stack it goes to exile rather than the graveyard [C2]. Because the spell was countered it never resolved, so the "Draw a card" instruction is never carried out [CR 608.1].

Review: **correct**. Correct flashback exiles countered spell and no draw; 702.34a and card ruling directly support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If Ephemerate is countered, Rebound does not exile it. The card goes to your graveyard and you do not get to cast it again next upkeep.

Why: Rebound modifies what happens "as it resolves"—instead of the spell going to the graveyard, it is exiled [CR 702.88a]. A countered spell never resolves, so that replacement effect never applies. The card-specific ruling confirms: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn" [C5].

Review: **correct**. Correct rebound applies only as spell resolves, so a countered spell goes to graveyard and has no rebound cast next turn; rule and dated ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist does not return it to the battlefield.

Why: Persist's trigger condition requires the permanent to have had **no** -1/-1 counters on it when it was put into the graveyard from the battlefield [CR 702.79a]. The card-specific ruling confirms that persist checks the creature's state just before it leaves the battlefield, and if it still has -1/-1 counters at that point, the ability does not trigger [C6].

Review: **correct**. Correct persist checks for -1/-1 counters at last moment on battlefield; 702.79a and Kitchen Finks ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger.

Why: At the state-based action check, Young Wolf dies (toughness 0 or less) and its +1/+1 and −1/−1 counters are removed simultaneously. Under [CR 704.8], when a permanent leaves the battlefield at the same time other state-based actions are performed, its last known information is derived from the game state *before* those actions. In that pre-action state, Young Wolf still had a +1/+1 counter on it. Undying's intervening "if" clause checks whether it "had no +1/+1 counters on it" [CR 702.93a] [CR 603.4]; because it did have one, the condition is not met and the ability does not trigger. This is the same logic as the worked example in [CR 704.8], which uses Young Wolf with one +1/+1 counter and multiple −1/−1 counters.

Review: **correct**. Correct no undying using pre-SBA state; 704.8 supplies direct Young Wolf example. Frozen evidence group mistakenly names 704.7; see reference addendum.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No. After Cloudshift resolves, the returned creature is no longer the target of Lightning Bolt, so Lightning Bolt has no legal target and does not resolve.

Why: The Cloudshift ruling states explicitly that "the returned card won't be the target of any spells or abilities that targeted it before" [C5]. Because Lightning Bolt's only target is now illegal, the spell doesn't resolve at all [CR 608.2b].

Review: **correct**. Correct new object invalidates Bolt target, so it does not damage returned creature; Cloudshift ruling and 608.2b support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

Why: The equip ability is restricted to "Equip only as a sorcery" [C2], meaning it may be activated only during your main phase when the stack is empty [CR 702.6a]. Because Lightning Bolt is on the stack, the stack is not empty, so the equip ability is not legally activatable at that moment. Even if it were, attaching Colossus Hammer would give the creature +10/+10 but would not prevent the 3 damage Lightning Bolt deals [C1].

Review: **correct**. Correct equip timing; sorcery-only restriction and stack-not-empty fact support no activation in response.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: Yes. You can tap your 3/3 creature to pay the Crew 1 cost of Smuggler's Copter even though it just entered the battlefield and has no haste.

Why: Summoning sickness (CR 302.6) only restricts a creature from attacking or activating its *own* tap/untap abilities; it does not prevent that creature from being tapped to pay the cost of another permanent's ability. The card-specific ruling confirms this directly: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. Haste is irrelevant here because it only bypasses the summoning-sickness restriction on attacking and self-activation [CR 702.10b][CR 702.10c].

Review: **correct**. Correct that a newly cast untapped creature may crew; 702.122a and Smuggler’s Copter ruling directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No. Because you cast Smuggler's Copter this turn, you have not controlled it continuously since your turn began, so it cannot attack even after you crew it.

Why: Once a Vehicle becomes a creature it "behaves exactly like any other artifact creature" and "can't attack unless you've controlled it continuously since your turn began" [C10]. Haste is the exception that would allow a creature to attack despite not having been under your control since the turn began [CR 702.10b], but the Copter has no haste. Crewing it makes it a legal creature for the declare attackers step [C13], but it still fails the continuous-control requirement.

Review: **correct**. Correct new Vehicle cannot attack without haste after being cast this turn; Smuggler’s Copter ruling and haste definition support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: No. Tapping the blocker after it has been declared does not remove it from combat and does not prevent it from dealing combat damage.

Why: Once a creature has been declared as a blocker, tapping or untapping it has no effect on its combat status or its ability to assign combat damage [CR 506.4b]. More broadly, spells or abilities that would have kept a creature from blocking don't remove it from combat once it has already been declared [CR 506.4a].

Review: **correct**. Correct tapped blocker remains in combat and assigns damage; 506.4b directly supports it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: The 3/3 deals 3 damage in the first combat damage step and another 3 in the second, for 6 total on the 4/4. The 4/4 deals 4 damage in the second combat damage step. Both creatures die: the 4/4 has 6 damage marked (exceeding its 4 toughness) and the 3/3 has 4 damage marked (exceeding its 3 toughness).

Why: Because the 3/3 has double strike, combat is split into two damage steps; only the double-striker assigns damage in the first step, and both assign in the second [CR 702.4b][CR 510.4]. All assigned damage is dealt simultaneously within each step [CR 510.2], and marked damage exceeding toughness causes the creature to die [CR 120.3e].

Review: **incorrect**. Incorrect: applies double strike to a fight and claims both creatures die. Fighting is not combat damage and double strike does not cause a second fight; the 4/4 survives with 3 damage marked. This error appeared after injecting lettered neighbors into the first 64 ranked slots, which dropped the fight rules.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.14a, CR 701.14d

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: Control Magic leaves the game, and the creature reverts to Alice's control.

Why: When Bob leaves the game, all objects he owns leave the game, and any effects giving him control of objects end [CR 800.4a]. The supplied example is directly on point: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a]. Because Alice (the creature's owner) is still in the game, the creature simply returns to her control rather than being exiled [CR 800.4c].

Review: **correct**. Correct Bob-owned Control Magic leaves the game and Alice’s creature reverts to her; 800.4a directly illustrates this.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Need details: The reference excerpts provided do not include the multiplayer rule governing what happens to a player's objects (including spells on the stack) when that player leaves the game. I would need the relevant excerpt (typically in the 810-range multiplayer rules, e.g., the rule stating that all objects a player owns are removed from the game when they leave) to cite a supporting source. Could you attach that rule or the specific card/ruling you'd like me to work from?

Review: **abstained**. Unnecessary abstention: 800.4a is required evidence but was not packed. Also suggests 104.3a, which is not the leaving-player objects rule; incorrect reference is an unsupported claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Ruling: Yes. The 12 and 9 add together, totaling 21, and you lose the game.

Why: The loss condition tracks combat damage dealt "by the same commander over the course of the game" [CR 903.10a] [CR 704.6c]. The commander is a designation on the card itself [CR 903.3], so the damage is attributed to that commander regardless of which player controlled it when the damage was dealt. Since 12 + 9 = 21, the state-based action causes you to lose [CR 704.6c].

Review: **correct**. Correct commander-damage total and loss threshold regardless of controller; 903.10a, 704.6c and 903.3 support each claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect—not a state-based action.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner's hand from anywhere, the owner may put it into the command zone instead, and labels that choice a "replacement effect" [CR 903.9b]. The state-based action in rule 903.9a applies only when a commander is in a graveyard or in exile, which is a different zone and a different mechanism [CR 903.9a].

Review: **correct**. Correct hand-to-command-zone choice is a replacement effect, distinct from graveyard/exile SBA; 903.9b/903.9a directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the player being dealt damage) chooses the order. The possible damage totals are **8** (Furnace of Rath first, then Torbran) or **10** (Torbran first, then Furnace of Rath).

Why: When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace of Rath doubles it to 10; applying Furnace of Rath first gives 3 × 2 = 6, then Torbran adds 2 for 8. The opponent will naturally pick the order that results in 8.

Review: **correct**. Correct affected player chooses, and totals/order are 10 or 8; card rulings and CR 616.1/614.5 support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having zero cards in your library is not, by itself, a losing condition. You lose only if you *attempt to draw* a card from that empty library.

Why: The state-based action that causes a loss is specifically tied to an attempted draw: "If a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked, that player loses the game" [CR 704.5b]. Rule 121.4 confirms the trigger is the attempt: "A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority" [CR 121.4]. Merely having an empty library, without an attempted draw, satisfies neither condition.

Review: **correct**. Correct empty library alone causes no loss; 704.5b and 121.4 require an attempted draw.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Need details:

- What creature is attacking (its power, and whether it has trample or trample over planeswalkers)?
- What creature(s) are blocking it (their toughness)?
- Is it attacking a player or a planeswalker?

Review: **correct**. Appropriate clarification requests trample, relevant power/toughness and other combat details; gives no guessed amount.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No to both. The copy does **not** get the counters on the original creature, and it does **not** receive the bonus from the enchantment attached to that creature.

Why: Counters are explicitly listed among the things that are not copied when an object is copied [CR 707.2]. The enchantment is a separate permanent attached to the original creature; its effect is an "other effect" (a text-changing or type-changing effect) that is not part of the original's copiable values, so the copy does not acquire it [CR 707.2]. The enchantment remains attached to the original creature, not to the new copy.

Review: **incorrect**. Does not ask for the unspecified copy effect or details and instead gives an unconditional answer, so it fails the frozen clarification criteria. Its default explanation that counters and separate continuous effects are not copied is otherwise supported by 707.2; no factual contradiction is identified.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details: What are the two replacement effects, and what is the original effect creating the token? (For example, are both "double the number of tokens" effects like Doubling Season, or do they do different things such as changing the token's type or number?)

Review: **correct**. Appropriate clarification requests base event and exact replacement effects; no token number is guessed.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

