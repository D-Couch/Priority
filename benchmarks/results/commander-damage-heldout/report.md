# commander-damage-heldout

Status: **complete** · implementation commit `9acdbc3a36fabd68f3a42ef9be95f22b06570bcb`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 26/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 81.2% |
| Cases retrieving every expected evidence group | 18/32 |
| Answers with citations | 31/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 5 |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 26/32 reviewed |
| Reviewed accuracy | 81.2% |
| Mean reviewed rubric score | 93.8% |
| Median successful response | 10.50 s |
| p95 successful response | 17.42 s |
| Median first visible answer token | 9.09 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | partial | 17.42 |
| h02-intervening-if (r1) | 100.0% | correct | 8.05 |
| h03-independent-trigger (r1) | 50.0% | correct | 14.84 |
| h04-replacement-death (r1) | 75.0% | correct | 7.89 |
| h05-simultaneous-death (r1) | 100.0% | correct | 10.40 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 8.80 |
| h07-infect-lifelink (r1) | 100.0% | partial | 12.33 |
| h08-protection-wrath (r1) | 100.0% | correct | 11.02 |
| h09-protection-aura (r1) | 100.0% | correct | 6.19 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.56 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 9.74 |
| h12-split-second (r1) | 100.0% | correct | 16.14 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 12.76 |
| h14-flashback-countered (r1) | 66.7% | correct | 13.44 |
| h15-rebound-countered (r1) | 66.7% | correct | 8.29 |
| h16-persist-counter (r1) | 100.0% | correct | 8.22 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 21.20 |
| h18-blink-target (r1) | 75.0% | correct | 10.59 |
| h19-equip-timing (r1) | 75.0% | partial | 16.87 |
| h20-crew-new-creature (r1) | 66.7% | correct | 16.47 |
| h21-new-vehicle (r1) | 50.0% | correct | 8.93 |
| h22-tapped-blocker (r1) | 0.0% | correct | 14.25 |
| h23-fight-double-strike (r1) | 100.0% | partial | 10.22 |
| h24-leaving-controller (r1) | 100.0% | correct | 9.18 |
| h25-leaving-stack (r1) | 100.0% | correct | 12.83 |
| h26-commander-control (r1) | 100.0% | correct | 12.31 |
| h27-commander-hand (r1) | 100.0% | correct | 9.35 |
| h28-replacement-order (r1) | 100.0% | correct | 12.90 |
| h29-empty-library (r1) | 100.0% | correct | 9.13 |
| h30-ambiguous-combat (r1) | 50.0% | incorrect | 8.35 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 8.70 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 10.65 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The triggered abilities go on the stack in the order Alice (bottom), Bob, Charlie (top). If nobody responds, they resolve in the order Charlie, Bob, Alice.

Why: At the beginning of Alice's upkeep, all three abilities trigger and are put on the stack before the active player receives priority [CR 117.3a][CR 117.5]. Because they are put on the stack at the same time, the active player's (Alice's) ability is placed lowest, followed by the other players' abilities in APNAP order (Bob, then Charlie) [CR 405.3]. When all players pass in succession, the top object on the stack resolves first, so Charlie's ability resolves, then Bob's, then Alice's [CR 608.1][CR 405.5].

Review: **partial**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, so the condition (40 or more life) is checked both when the ability triggers and again as it resolves [CR 603.4]. The card-specific ruling confirms that if you don't have 40 or more life at resolution, "the ability won't do anything" [C2]. Since you dropped to 39 life before resolution, the condition fails at that second check and the ability does nothing [CR 603.4].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. Once the "When this creature enters" ability is on the stack, it exists independently of the Simulacrum. The Simulacrum being destroyed before the ability resolves does not prevent it from resolving, and you may still search for a basic land.

Why: A triggered ability on the stack "has the text of the ability that created it and no other characteristics" [CR 405.4], so it no longer depends on the source permanent existing. The ability's effect ("you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle" [C1]) acts on your library, not on the Simulacrum, so the zone-change rule about looking for the object in its new zone [CR 603.6] does not apply here. The "may" choice is made when the ability resolves [CR 603.5], at which point you simply decide whether to search.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No. Solemn Simulacrum's "when this creature dies" ability does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exile, so the card is never actually put into a graveyard [C1]. Because the trigger condition is never met, the ability does not trigger [C2].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers **three** times—once for itself dying and once for each of the two other creatures dying.

Why: The card-specific ruling states that "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures" [C2]. This is consistent with the general rule that zone-change (leaves-the-battlefield) triggers look back in time, so the ability triggers even though Blood Artist is itself leaving the battlefield in the same event [CR 603.10a]. Each of the three deaths is a separate trigger event matching the condition "this creature or another creature dies."

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: Lifelink causes life gain only when damage is actually **dealt** by the source. [CR 702.15b] states "Damage dealt by a source with lifelink causes that source's controller… to gain that much life." If a prevention effect stops all 3 damage, no damage is dealt, so the condition for lifelink's life-gain effect is never met.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent's life total is unchanged, your opponent gains 3 poison counters, and you gain 3 life.

Why: Infect replaces the "lose life" result of damage dealt to a player with the application of an equal number of poison counters, so your opponent does not lose life [CR 702.90b] [CR 120.3b]. Lifelink independently causes the source's controller to gain life equal to the damage dealt, "in addition to any other results that damage causes" [CR 702.15b]. The two effects operate on different players and do not conflict, so both apply simultaneously.

Review: **partial**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature. Protection from white does not prevent it.

Why: Protection's listed benefits are limited to preventing targeting, enchanting, equipping, damage, and blocking [CR 702.16b]–[CR 702.16f]. Wrath of God is a non-targeting sorcery that simply says "Destroy all creatures" [C1]; it does not target, deal damage, or attach anything, so none of protection's sub-rules apply. Since the creature lacks indestructible, nothing prevents the destruction [CR 702.12b].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The white Aura is put into its owner's graveyard as a state-based action.

Why: Protection from white means the permanent can't be enchanted by Auras that have the stated quality, and any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c]. The Aura doesn't become unattached and remain on the battlefield; it is removed to the graveyard.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes. You can target your own Slippery Bogle with your own Giant Growth.

Why: Hexproof restricts only targeting by *opponents*: "This permanent can't be the target of spells or abilities your opponents control" [CR 702.11b]. Since you control both the Bogle and the Giant Growth, the restriction does not apply to you. Giant Growth simply requires "target creature" [C2], and your own Bogle is a legal target for a spell you control.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

Why: Abrupt Decay's Oracle text states "This spell can't be countered" [C1]. Ward's ability instructs to "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but the "can't be countered" restriction prevents that counter from occurring. The card-specific ruling confirms this directly: "Abrupt Decay won't be countered even if you don't [pay the ward cost]" [C2].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes. You can turn Willbender face up as a special action while Krosan Grip is on the stack, its triggered ability goes on the stack above Grip, and you can redirect Grip to your other artifact.

Why: Turning a face-down permanent face up is a special action, and special actions are permitted while a split-second spell is on the stack [CR 702.37e][CR 702.61b][C5]. Willbender's ability triggers when you use the morph action to turn it face up [C13], and triggered abilities are put on the stack and resolve normally during split second [CR 702.61b][C2]. Because the ability is placed on top of the stack [CR 405.2], it resolves before Krosan Grip, letting you change Grip's target to your other legal artifact.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No. Your opponent cannot respond to destroy the creature. The sacrifice is part of paying Fling's additional cost during the casting process, and no player receives priority at any point between the spell being put on the stack and the costs being paid.

Why: Fling's sacrifice is an additional cost paid under rule 601.2h, which occurs after the spell is already on the stack (601.2a) but before the spell is considered "cast" (601.2i). No one gets priority during that sequence, so there is no window in which your opponent could act. The Fling-specific ruling states explicitly: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." [C3] [CR 601.2a] [CR 601.2h] [CR 601.2i]

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice is exiled, and you do not draw a card.

Why: Because you paid the flashback cost, the card is exiled instead of going anywhere else any time it would leave the stack, including when it is countered [CR 702.34a] [C2]. The "Draw a card" instruction is the effect that occurs when the spell resolves; since the spell was countered it never resolves, so that effect never happens [C2].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No. If Ephemerate is countered, Rebound does not exile it. The card is put into your graveyard and you do not get to cast it again next upkeep.

Why: Rebound is a static ability that modifies what happens "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never applies. The card-specific ruling confirms that if a Rebound spell cast from your hand is countered, "none of its effects will happen, including rebound," and the spell goes to its owner's graveyard [C5].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard from the battlefield, persist does not trigger and it does not return to the battlefield.

Why: Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. Because the creature still has that counter at the moment it leaves the battlefield, the condition is not met and the ability never triggers. This is consistent with the card-specific ruling that persist checks the creature's state just before it leaves the battlefield [C6].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, undying does not trigger. Young Wolf had a +1/+1 counter on it when it was last on the battlefield, so the "if it had no +1/+1 counters on it" condition is not met.

Why: Undying is a leaves-the-battlefield ability, so the game looks back in time to the object's appearance immediately prior to it leaving the battlefield [CR 603.10a][CR 603.10]. At that moment Young Wolf still had its +1/+1 counter (the -1/-1 counter and the continuous -1/-1 effect only reduced its toughness to 0; they did not remove the +1/+1 counter) [CR 704.8]. Because the creature "had" a +1/+1 counter, the undying trigger condition fails, exactly as the Young Wolf example in [CR 704.8] illustrates.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No. Lightning Bolt will not damage the creature that Cloudshift returns.

Why: Cloudshift exiles the creature and then returns it as a new object on the battlefield; the returned card is not the target of any spell that targeted the original [C5]. When Lightning Bolt later resolves, its target is no longer in the zone it was in when targeted, making it illegal [CR 608.2b]. Because all of Lightning Bolt's targets are illegal, the spell doesn't resolve and is put into its owner's graveyard [CR 608.2b].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

Why: The equip ability is restricted to "Equip only as a sorcery" [C2], and the rules define that timing as your main phase with an empty stack [CR 117.1a]. Once Lightning Bolt is on the stack, the stack is no longer empty, so the sorcery-timing restriction prevents you from activating the equip ability [CR 702.6a]. Since no effect grants special activation permission (as you noted), there is no exception.

Review: **partial**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: Yes. You can tap that 3/3 creature to pay the Crew 1 cost of Smuggler's Copter even though it has no haste and was just cast.

Why: Crew is an activated ability of the Vehicle, not of the creature; the creature is simply tapped as part of the cost to activate the Vehicle's ability, so the "summoning sickness" restriction on a creature's own tap abilities doesn't apply. The Crew rule only requires that the creature be untapped, under your control, and have sufficient power [CR 702.122a]. The card-specific ruling confirms this directly: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. Haste is only needed for a creature to attack [CR 702.10b] or to activate its *own* tap/untap abilities [CR 702.10c], neither of which is what's happening here.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No. Because you cast Smuggler's Copter this turn, you have not controlled it continuously since your turn began, and it has no haste, so it cannot attack this turn.

Why: A Vehicle that becomes a creature "can't attack unless you've controlled it continuously since your turn began" [C10]. Haste is the ability that overrides that requirement [CR 702.10b], and Smuggler's Copter does not have haste [C1].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: Tapping the blocker does **not** remove it from combat and does **not** stop it from assigning combat damage. It will still deal 3 damage to the creature it is blocking.

Why: A creature remains a blocking creature until it is removed from combat or the combat phase ends [CR 509.1g]; tapping is not a removal from combat. A blocking creature assigns combat damage equal to its power as long as it is currently blocking [CR 510.1a][CR 510.1d]. The only listed conditions that prevent a blocker from assigning damage are that it is no longer blocking any creatures (e.g., they were destroyed or removed from combat) [CR 510.1d], neither of which is caused by tapping.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives as a 4/1. Double strike has no effect here.

Why: In a fight, each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Double strike is a static ability that modifies only the combat damage step [CR 702.4a], so it does not apply to a fight.

Review: **partial**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: Control Magic leaves the game, and the creature reverts to Alice's control.

Why: When a player leaves the game, all objects they own leave the game and any effects giving them control of objects end [CR 800.4a]. Since Bob owns the Control Magic, it leaves the game with him, and the creature returns to its owner, Alice. This is the exact scenario illustrated in the Mind Control example in [CR 800.4a]: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control."

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Ruling: No. Lightning Bolt does not resolve; it leaves the game when Bob leaves, so Alice is not dealt damage.

Why: When a player leaves the game, all objects owned by that player leave the game [CR 800.4a]. Because Bob owns the Lightning Bolt card, it is removed from the stack as part of that process and never reaches resolution. The separate clause about objects on the stack "not represented by cards" ceasing to exist does not apply here, since Lightning Bolt is a card; it simply leaves the game as an owned object [CR 800.4a].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Ruling: Yes. The 12 combat damage dealt while Alice controlled the commander and the 9 dealt while Bob controlled it add together. Since the total is 21, you lose the game as a state-based action.

Why: Rule 903.10a states that a player who has been dealt 21 or more combat damage "by the same commander over the course of the game" loses the game [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of zone or controller [CR 903.3], so the rule tracks damage dealt by that card, not by a particular controller of it. The rule contains no requirement that the same player have controlled the commander when the damage was dealt.

Review: **correct**. The answer meets both criteria: it sums 12+9 for the same commander and correctly says the player loses at 21 despite control changing. Rule 903.10a expressly tracks combat damage by the same commander over the game; citations to 903.10a and 903.3 support the explanation. AI-assisted review; not independent human validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand. That choice is a replacement effect, not a state-based action.

Why: Rule 903.9b explicitly states, "If a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead," and labels it "This replacement effect." [CR 903.9b] The state-based action in 903.9a applies only when the commander is already in a graveyard or exile, which is a different situation. [CR 903.9a] The "instead" language also aligns with the general definition of replacement effects. [CR 614.1a]

Review: **correct**. The answer remains correct under 903.9b and 903.9a; the additional 903.10a source is irrelevant but does not undermine the cited rule support. AI-assisted review; not independent human validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace of Rath: 3 → 5 → 10) or **8** (Furnace of Rath first, then Torbran: 3 → 6 → 8).

Why: When two or more replacement effects modify the same damage event, the affected player chooses which applies first [CR 616.1], a choice confirmed by both Torbran's ruling [C4] and Furnace of Rath's ruling [C6]. After the first effect is applied, the process repeats with the remaining effect [CR 616.1f]. Torbran adds 2 to the damage [C1]; Furnace of Rath doubles it [C5], so the order determines whether you get 3+2=5 then ×2=10, or 3×2=6 then +2=8.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having zero cards in your library is not, by itself, a state-based action that causes you to lose the game. You lose only if you *attempt to draw* a card from that empty library.

Why: The state-based action in [CR 704.5b] triggers specifically when "a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked." Rule [CR 121.4] confirms the same condition: "A player who attempts to draw a card from a library with no cards in it loses the game the next time a player would receive priority." Neither rule lists an empty library alone as a losing condition; the attempt to draw is the required trigger.

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Ruling: None. A blocked creature assigns all of its combat damage to the creature(s) blocking it, not to the player it was attacking. No damage gets through to your opponent.

Why: A blocked creature assigns its combat damage to the creatures blocking it [CR 510.1c]. Only an *unblocked* creature assigns its combat damage to the player, planeswalker, or battle it's attacking [CR 510.1b]. Since your attacker is blocked, its damage is directed at the blocker(s) exclusively.

Review: **incorrect**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: CR 702.19b

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No to both. Your copy does not get the counters on the original creature, and it does not get the bonus from the enchantment attached to it.

Why: When copying an object, "other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied" [CR 707.2]. An enchantment's bonus is an "other effect" applied to the original, not part of its printed or copiable values, so it is excluded from the copy. Once the copy exists, it is a fixed snapshot of copiable values and does not track ongoing effects on the original [CR 707.2b].

Review: **incorrect**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details: What are the two specific replacement effects (card names or their text), and what is the original effect creating the token? The number of tokens depends on what each replacement does (e.g., both doubling, one doubling and one adding a fixed number, one being a self-replacement effect, etc.) and the order in which you choose to apply them [CR 616.1, CR 616.1f].

Review: **correct**. Exact answer and packed source excerpts match the previously AI-assisted seed-42 review; the prior substantive grade is carried forward. This is not independent human judge validation.
Reviewer: Codex (AI-assisted; no independent human judge)

Missing reference groups: none

