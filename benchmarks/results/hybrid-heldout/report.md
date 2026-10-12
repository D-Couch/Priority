# hybrid-heldout

Status: **complete** · implementation commit `2df6e9b3a650df2d3ac378ca0d7ad3bee538bf5e`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 29/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 81.0% |
| Cases retrieving every expected evidence group | 17/32 |
| Answers with citations | 28/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 2 |
| Reviewed citation-support failures | 6 |
| Reviewed fully correct | 29/32 reviewed |
| Reviewed accuracy | 90.6% |
| Mean reviewed rubric score | 93.8% |
| Median successful response | 10.69 s |
| p95 successful response | 18.44 s |
| Median first visible answer token | 9.33 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 66.7% | correct | 12.75 |
| h02-intervening-if (r1) | 100.0% | correct | 8.21 |
| h03-independent-trigger (r1) | 50.0% | correct | 16.92 |
| h04-replacement-death (r1) | 50.0% | correct | 8.07 |
| h05-simultaneous-death (r1) | 100.0% | correct | 13.72 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 10.43 |
| h07-infect-lifelink (r1) | 100.0% | correct | 10.62 |
| h08-protection-wrath (r1) | 33.3% | correct | 21.90 |
| h09-protection-aura (r1) | 100.0% | correct | 7.78 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.48 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 11.32 |
| h12-split-second (r1) | 100.0% | correct | 12.06 |
| h13-sacrifice-cost (r1) | 66.7% | partial | 10.72 |
| h14-flashback-countered (r1) | 66.7% | correct | 10.66 |
| h15-rebound-countered (r1) | 66.7% | correct | 8.93 |
| h16-persist-counter (r1) | 100.0% | correct | 7.99 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 13.73 |
| h18-blink-target (r1) | 75.0% | correct | 11.64 |
| h19-equip-timing (r1) | 75.0% | correct | 15.70 |
| h20-crew-new-creature (r1) | 100.0% | correct | 13.39 |
| h21-new-vehicle (r1) | 50.0% | correct | 13.50 |
| h22-tapped-blocker (r1) | 100.0% | correct | 6.70 |
| h23-fight-double-strike (r1) | 50.0% | correct | 11.62 |
| h24-leaving-controller (r1) | 100.0% | correct | 10.10 |
| h25-leaving-stack (r1) | 50.0% | abstained | 18.44 |
| h26-commander-control (r1) | 100.0% | correct | 10.35 |
| h27-commander-hand (r1) | 100.0% | correct | 7.80 |
| h28-replacement-order (r1) | 100.0% | correct | 12.84 |
| h29-empty-library (r1) | 100.0% | correct | 8.74 |
| h30-ambiguous-combat (r1) | 100.0% | correct | 7.73 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 8.28 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 14.79 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The abilities go on the stack in APNAP order—Alice's first (bottom), then Bob's, then Charlie's (top). With no responses, they resolve in reverse: Charlie's ability resolves first, then Bob's, then Alice's.

Why: At the beginning of upkeep, all triggered abilities are placed on the stack before the active player gets priority [CR 503.1a]. When multiple abilities trigger, each player in APNAP order (active player first, then non-active players in turn order) puts their triggered abilities on the stack [CR 603.3b]. Since Alice is active, the order is Alice → Bob → Charlie, each placing their single ability on top of what's already there [CR 405.2]. When all players pass, the topmost object resolves first [CR 405.5], so Charlie's resolves, then Bob's, then Alice's.

Review: **correct**. Correct APNAP stack order and reverse resolution; CR 603.3b, 405.2, and 405.5 support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, so the condition (40 or more life) is checked both when the ability triggers and again as it resolves. If your life total is 39 or less at resolution, the ability does nothing. [CR 603.4] [C2]

Review: **correct**. Correct intervening-if checks at trigger and resolution; CR 603.4 and the Felidar ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. You may still search your library for a basic land card, put it onto the battlefield tapped, and shuffle, even though the Simulacrum is no longer on the battlefield.

Why: Once the ETB ability triggers it goes on the stack as an independent object with no card associated with it [CR 603.3][CR 405.1]. Its effect—"you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle"—does not reference or require the Simulacrum to still be on the battlefield, so the ability resolves normally. The "may" decision is made when the ability resolves, not when it triggered [CR 603.5].

Review: **correct**. Correct surviving ETB search, but 603.3/405.1 do not directly supply the general independent-of-source rule (CR 113.7a). This is a citation support gap.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "when this creature dies" ability does not trigger.

Why: Rest in Peace's static ability replaces the event of the card being put into a graveyard with exile, so the card never enters a graveyard [C1]. Because the card is never put into a graveyard, the "dies" trigger condition is never met [C2]. This is confirmed by the card-specific ruling: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Correct: Rest in Peace replaces the graveyard event, so the creature does not die; Oracle and card-specific ruling support result.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 614.6, CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers **three** times—once for itself dying ("this creature") and once for each of the two other creatures dying ("another creature").

Why: The card-specific ruling states that if Blood Artist and one or more other creatures die at the same time, its ability triggers for each of those creatures [C2]. The "this creature" clause covers Blood Artist's own death, and the "another creature" clause fires separately for each of the two tokens. Because "dies" is a zone-change trigger, the game looks back in time to determine the triggers even though Blood Artist is already in the graveyard [CR 603.10a].

Review: **correct**. Correct three Blood Artist triggers, including its own; dated ruling states simultaneous deaths trigger for each creature.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life. Lifelink causes life gain only for damage that is actually dealt; prevented damage is never dealt, so no life gain occurs.

Why: Lifelink's effect is tied to "damage dealt by a source with lifelink" [CR 702.15b] [CR 120.3f]. Prevention effects modify the damage event before it is processed into results [CR 120.4c], so if all 3 damage is prevented, the resulting event contains 0 damage dealt, and lifelink produces no life gain. As the rules confirm, "If a player gains 0 life, no life gain event would occur" [CR 119.10].

Review: **correct**. Correct zero life. Cited rules establish when lifelink gains life, but the answer does not cite the rule defining what prevention does to the damage event; its cited excerpts do not fully establish the no-damage step.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent's life total is unchanged, your opponent gets 3 poison counters, and you gain 3 life.

Why: Because the source has infect, damage dealt to a player doesn't cause life loss; instead, the source's controller gives that player that many poison counters [CR 702.90b] [CR 120.3b]. Because the source also has lifelink, the source's controller gains that much life in addition to the damage's other results [CR 702.15b] [CR 120.3f]. The two abilities operate independently on the same damage event.

Review: **correct**. Correct poison and life totals. Correctly describes infect and lifelink as separate damage results, not replacement effects.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature. Protection from white does not save it.

Why: Wrath of God reads "Destroy all creatures" with no targeting language [C1], so it is a non-targeting global effect. Protection from a color prevents being *targeted* by spells of that color, being dealt damage by it, being blocked by it, and having auras of that color attached—but it does not prevent a non-targeting "destroy all creatures" effect from applying. Because the effect uses the word "destroy," the creature is destroyed under the standard destruction rule [CR 701.8b], and the "They can't be regenerated" clause [C1] means regeneration cannot replace that destruction.

Review: **correct**. Correct that Wrath destroys the creature, but the supporting citation is the card text and the general definition of destroy; the cited sources do not establish protection’s scope.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 702.16b, CR 702.16e

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The white Aura is put into its owner's graveyard as a state-based action.

Why: Protection from a quality means the protected permanent can't be enchanted by Auras with that quality, and any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c]. This differs from Equipment, which simply becomes unattached and stays on the battlefield [CR 702.16d]. No special card text (such as "this effect doesn't remove this Aura") is indicated, so the general rule applies.

Review: **correct**. Correct Aura is put in its owner’s graveyard as an SBA under protection; CR 702.16c supports this. Extra Equipment contrast is correct.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes. You can target your own Slippery Bogle with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. The restriction applies only to opponents' spells and abilities; it does not prevent you from targeting your own hexproof creature with your own spells. Giant Growth simply requires "target creature" [C2], and your Slippery Bogle is a legal target for your own spell.

Review: **correct**. Correct own spell may target own hexproof creature; 702.11b and Oracle text support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

Why: Abrupt Decay's "This spell can't be countered" text makes the spell uncounterable, so ward's "counter that spell or ability" effect cannot apply [C1][CR 702.21a]. The official ruling confirms that you may still choose to pay the ward cost, but Abrupt Decay won't be countered even if you don't [C2]. The spell resolves and destroys the target as normal.

Review: **correct**. Correct: ward ability triggers but cannot counter uncounterable Abrupt Decay, and it resolves if target remains legal; Oracle, ward rule and card ruling support this.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. You may turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will go on the stack above Grip, allowing you to redirect Grip's target to your other artifact.

Why: Turning a face-down permanent face up is a special action, not an activated ability, so split second does not prevent it [CR 702.37e][CR 702.61b]. Triggered abilities trigger and are put on the stack normally while a split-second spell is on the stack [CR 702.61b], so Willbender's "change the target of target spell or ability with a single target" trigger lands above Grip and can legally redirect it to your other artifact [C8]. This is confirmed by the Krosan Grip ruling: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5].

Review: **correct**. Correct morph as special action under split second and normal trigger can redirect Grip. Supplied morph, split-second, Willbender and Grip sources support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond to destroy the creature; the sacrifice is already complete by the time they receive priority.

Why: The sacrifice is part of paying Fling's additional cost, which occurs during the casting process before the spell is fully on the stack [CR 601.2h]. The card-specific ruling states explicitly: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell" [C3]. Priority is only granted to other players after the spell has been fully cast, including all cost payments [CR 117.1].

Review: **partial**. Correct no response to prevent sacrifice, but falsely says the spell is fully on the stack only after costs are paid. Casting procedure puts the spell on the stack before cost payment (601.2a before 601.2h); this confuses a meaningful timing detail.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice goes to exile, and you do not draw a card.

Why: The flashback replacement effect directs the card to exile "any time it would leave the stack," which includes when it is countered [CR 702.34a]. The card-specific ruling confirms this explicitly: "A spell cast using flashback will always be exiled afterward, whether it resolves, is countered, or leaves the stack in some other way" [C2]. Because the spell was countered, it never resolved, so the "Draw a card" instruction was never followed [CR 608.2c].

Review: **correct**. Correct flashback exiles countered spell and no draw; 702.34a and card ruling directly support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If Ephemerate is countered, Rebound does not exile it and you do not get to cast it again next upkeep. The spell goes to your graveyard.

Why: Rebound modifies what happens "as it resolves"—instead of the spell going to the graveyard, it is exiled [CR 702.88a]. A countered spell never resolves, so that replacement effect never applies. The card-specific ruling confirms: "If a spell with rebound that you cast from your hand is countered or doesn't resolve…none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Review: **correct**. Correct rebound applies only as spell resolves, so a countered spell goes to graveyard and has no rebound cast next turn; rule and dated ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard from the battlefield, persist does not trigger and it does not return to the battlefield.

Why: Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield; if a -1/-1 counter is present at that moment, the condition fails and the ability never triggers [C6].

Review: **correct**. Correct persist checks for -1/-1 counters at last moment on battlefield; 702.79a and Kitchen Finks ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger.

Why: Because the creature dying (toughness 0) and the +1/+1/−1/−1 counter removal (CR 122.3) are performed simultaneously as state-based actions, CR 704.8 dictates that Young Wolf's last known information is derived from the game state *before* any of those actions were performed. At that moment it still had a +1/+1 counter on it, so the "if it had no +1/+1 counters on it" condition in undying (CR 702.93a) is not met. This is the exact scenario illustrated in the example under CR 704.8.

Review: **correct**. Correct no undying using pre-SBA state; 704.8 supplies direct Young Wolf example. Frozen evidence group mistakenly names 704.7; see reference addendum.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No. Lightning Bolt does not damage the returned creature.

Why: Cloudshift's ruling states that "the returned card won't be the target of any spells or abilities that targeted it before" [C5]. Because the creature was exiled and returned as a new object, Lightning Bolt's target is no longer legal, so the spell doesn't resolve and deals no damage [CR 608.2b].

Review: **correct**. Correct new object invalidates Bolt target, so it does not damage returned creature; Cloudshift ruling and 608.2b support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

Why: The equip ability's text reads "Equip only as a sorcery" [C2], and [CR 702.6a] confirms this means "Activate only as a sorcery." That timing restriction limits activation to your main phase when the stack is empty. Because Lightning Bolt is on the stack, the stack is not empty, so you cannot activate the equip ability in response to it.

Review: **correct**. Correct equip timing; sorcery-only restriction and stack-not-empty fact support no activation in response.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: Yes. You can tap the 3/3 creature to pay the Crew 1 cost even though it was just cast and has no haste.

Why: The Crew ability is the Vehicle's activated ability, not the creature's own ability. Rule 302.6 restricts a creature from activating *its own* tap abilities and from attacking, but it does not prevent a creature from being tapped to pay a cost for another object's ability [CR 302.6] [CR 702.122a]. The card-specific ruling confirms this directly: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12].

Review: **correct**. Correct that a newly cast untapped creature may crew; 702.122a and Smuggler’s Copter ruling directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No. Because you cast Smuggler's Copter this turn, you have not controlled it continuously since your turn began, and it has no haste, so it cannot attack this turn even after being crewed.

Why: Once a Vehicle becomes a creature it behaves like any other artifact creature, which "can't attack unless you've controlled it continuously since your turn began" [C10]. The general rule is that a creature without haste must have been controlled by its controller continuously since their most recent turn began to attack [CR 702.10b]. Since the Copter entered the battlefield this turn, that condition is not met, and crewing it does not remove summoning sickness.

Review: **correct**. Correct new Vehicle cannot attack without haste after being cast this turn; Smuggler’s Copter ruling and haste definition support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from dealing combat damage.

Why: Once a creature is declared as a blocker, tapping or untapping it has no effect on its status in combat or its ability to assign combat damage [CR 506.4b]. More broadly, spells or abilities that would have kept a creature from blocking don't remove it from combat once it has already been declared as a blocker [CR 506.4a].

Review: **correct**. Correct tapped blocker remains in combat and assigns damage; 506.4b directly supports it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it. Double strike has no effect here.

Why: "Fight" is a one-time action in which each creature deals damage equal to its power to the other [CR 701.14a]. Double strike is a static ability that modifies the combat damage step [CR 702.4a], and a fight is not a combat damage step, so the ability never applies. The damage is dealt simultaneously as part of the fight resolution, and the 3/3's toughness (3) is less than the 4 damage it receives, so it dies.

Review: **correct**. Correct damage amounts, 3/3 dies and 4/4 survives with three damage marked; fight and double-strike rules support why double strike does not apply, but answer does not cite the state-based lethal-damage rule for survival.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.14d

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: Control Magic leaves the game, and the creature remains on the battlefield under Alice's control.

Why: When Bob leaves the game, all objects he owns leave the game, and any effects giving him control of objects end [CR 800.4a]. Control Magic is owned by Bob, so it leaves the game; the creature is owned by Alice, who remains, so it stays on the battlefield and reverts to her control. This mirrors the explicit example: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a]. Bob never gained control of the Aura itself—only of the creature [C2].

Review: **correct**. Correct Bob-owned Control Magic leaves the game and Alice’s creature reverts to her; 800.4a directly illustrates this.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Need details: The provided reference excerpts do not include the rule governing what happens to a player's objects (including spells on the stack) when that player leaves the game (typically Rule 104.3a or the equivalent "Leaving the Game" rule). Without that rule in the supplied references, I cannot cite a supporting source for the ruling. Could you attach the relevant "Leaving the Game" rule text, or should I proceed on the general principle that all objects a player owns are removed from the game when they leave?

Review: **abstained**. Unnecessary abstention: 800.4a is required evidence but was not packed. Also suggests 104.3a, which is not the leaving-player objects rule; incorrect reference is an unsupported claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 800.4a

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Ruling: Yes. The 12 damage dealt while Alice controlled the commander and the 9 damage dealt while Bob controlled it add together. Once the total reaches 21, you lose the game as a state-based action.

Why: The loss condition is triggered by combat damage dealt "by the same commander over the course of the game" [CR 903.10a] [CR 704.6c]. The rule tracks the commander as a card (the designation is an attribute of the card itself and persists regardless of zone or controller [CR 903.3]), not the player who happens to control it at the moment damage is dealt. Since 12 + 9 = 21, the threshold is met and you lose.

Review: **correct**. Correct commander-damage total and loss threshold regardless of controller; 903.10a, 704.6c and 903.3 support each claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect—not a state-based action.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner's hand from anywhere, the owner may put it into the command zone instead, and labels that choice a "replacement effect" [CR 903.9b]. The state-based action in rule 903.9a applies only when a commander is in a graveyard or in exile, not when it would go to a hand [CR 903.9a].

Review: **correct**. Correct hand-to-command-zone choice is a replacement effect, distinct from graveyard/exile SBA; 903.9b/903.9a directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the player being dealt damage) chooses the order. The possible damage totals are **10** (Torbran first, then Furnace of Rath) or **8** (Furnace of Rath first, then Torbran).

Why: When multiple replacement effects modify how damage is dealt, the affected player chooses the order [CR 616.1], confirmed by both the Torbran ruling [C4] and the Furnace of Rath ruling [C6]. Applying Torbran first changes 3 to 5, then Furnace doubles it to 10; applying Furnace first changes 3 to 6, then Torbran adds 2 for 8. Each replacement effect gets only one opportunity to apply [CR 614.5].

Review: **correct**. Correct affected player chooses, and totals/order are 10 or 8; card rulings and CR 616.1/614.5 support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having zero cards in your library does not, by itself, cause you to lose the game. You lose only if you *attempt to draw* a card from that empty library.

Why: The state-based action that causes a loss is specifically tied to an attempted draw from an empty library, not to the library being empty [CR 704.5b]. Rule 121.4 likewise frames the loss around a player who "attempts to draw a card from a library with no cards in it" [CR 121.4]. If no draw has been attempted since the library became empty, the condition for the state-based action has not been met, so no loss occurs.

Review: **correct**. Correct empty library alone causes no loss; 704.5b and 121.4 require an attempted draw.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Need details:

1. Does your attacking creature have trample (or trample over planeswalkers)?
2. What is the power of your attacker and the toughness of the blocking creature(s)?
3. Is your attacker attacking a player or a planeswalker?
4. Are there multiple blockers, or any other creatures dealing combat damage in the same step?

Review: **correct**. Appropriate clarification requests trample, relevant power/toughness and other combat details; gives no guessed amount.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No to both. Your copy does not get the counters on the original creature, and it does not get the bonus (e.g., +1/+1) from an enchantment attached to that creature.

Why: When copying an object, the copy acquires only the copiable values derived from the printed text (as modified by other copy effects, face-down status, and "as it enters" P/T-setting abilities). "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An enchantment's ongoing bonus is an "other effect," and counters are explicitly excluded, so neither transfers to the copy.

Review: **incorrect**. Does not ask for the unspecified copy effect or details and instead gives an unconditional answer, so it fails the frozen clarification criteria. Its default explanation that counters and separate continuous effects are not copied is otherwise supported by 707.2; no factual contradiction is identified.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details: What are the two replacement effects? (e.g., two "create twice as many tokens instead" effects, a doubling effect plus an "enters with X" effect, etc.) The number of tokens you end up with depends entirely on what each effect does. Please name the cards or quote the relevant ability text.

Review: **correct**. Appropriate clarification requests base event and exact replacement effects; no token number is guessed.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

