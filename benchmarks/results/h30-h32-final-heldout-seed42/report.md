# h30-h32-final-heldout-seed42

Status: **complete** · implementation commit `33b8429a85867b385e2030f3d3971845f32b5b3c`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 31/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 83.9% |
| Cases retrieving every expected evidence group | 20/32 |
| Answers with citations | 31/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 31/32 reviewed |
| Reviewed accuracy | 96.9% |
| Mean reviewed rubric score | 96.9% |
| Median successful response | 8.08 s |
| p95 successful response | 12.87 s |
| Median first visible answer token | 6.31 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 66.7% | correct | 10.82 |
| h02-intervening-if (r1) | 100.0% | correct | 6.41 |
| h03-independent-trigger (r1) | 100.0% | correct | 5.68 |
| h04-replacement-death (r1) | 100.0% | correct | 6.58 |
| h05-simultaneous-death (r1) | 100.0% | correct | 6.44 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 5.98 |
| h07-infect-lifelink (r1) | 100.0% | correct | 7.01 |
| h08-protection-wrath (r1) | 100.0% | correct | 8.20 |
| h09-protection-aura (r1) | 100.0% | correct | 5.00 |
| h10-own-hexproof (r1) | 100.0% | correct | 7.51 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 8.03 |
| h12-split-second (r1) | 100.0% | correct | 12.87 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 9.68 |
| h14-flashback-countered (r1) | 66.7% | correct | 5.88 |
| h15-rebound-countered (r1) | 66.7% | correct | 7.67 |
| h16-persist-counter (r1) | 50.0% | correct | 7.31 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 16.77 |
| h18-blink-target (r1) | 50.0% | correct | 11.68 |
| h19-equip-timing (r1) | 75.0% | correct | 10.80 |
| h20-crew-new-creature (r1) | 66.7% | correct | 9.97 |
| h21-new-vehicle (r1) | 50.0% | correct | 11.86 |
| h22-tapped-blocker (r1) | 0.0% | correct | 10.03 |
| h23-fight-double-strike (r1) | 100.0% | correct | 10.38 |
| h24-leaving-controller (r1) | 100.0% | correct | 10.61 |
| h25-leaving-stack (r1) | 100.0% | correct | 8.16 |
| h26-commander-control (r1) | 100.0% | correct | 8.75 |
| h27-commander-hand (r1) | 100.0% | correct | 7.20 |
| h28-replacement-order (r1) | 100.0% | correct | 12.58 |
| h29-empty-library (r1) | 100.0% | correct | 8.12 |
| h30-ambiguous-combat (r1) | 100.0% | correct | 5.67 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 7.41 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 7.98 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** The abilities go on the stack in the order Alice, Bob, Charlie (bottom to top), and resolve in the order Charlie, Bob, Alice (top to bottom).

**Why:** All three abilities trigger at the beginning of the upkeep, so they are all placed on the stack in the first part of the process. Each player, in APNAP order, puts their triggered ability on the stack. Alice is the active player, so she goes first, then Bob, then Charlie. [CR 603.3b] Each ability becomes the topmost object on the stack when placed. [CR 603.3] After all triggered abilities are on the stack, the active player (Alice) receives priority. [CR 117.3a] If all players pass in succession, the top of the stack resolves. [CR 117.4] Since Charlie's ability is on top, it resolves first, then Bob's, then Alice's.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 405.2

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability checks your life total again as it resolves, and since you have 39 life at that time, it does nothing.

Why: Felidar Sovereign's ability uses an "intervening 'if' clause." The condition is checked twice: first when the trigger event occurs (your upkeep begins), and again as the ability resolves. If the condition isn't true at resolution, the ability is removed from the stack and has no effect. [CR 603.4] The card-specific ruling confirms this: "If you do [have 40 or more life], the ability will check again as it tries to resolve. If you don't have 40 or more life at that time, the ability won't do anything." [C2]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes. Once the triggered ability is on the stack, it exists independently of its source. Destroying the Simulacrum does not remove or counter the ability already on the stack, so it will still resolve and you may search for a basic land.

Why: A triggered ability, once on the stack, is unaffected by the destruction or removal of its source. [CR 113.7a]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

Why: "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exiling the card instead [C1]. Since the card is never put into a graveyard, the creature never dies, and the trigger condition is never met [C2].

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **three** times — once for itself dying and once for each of the two other creatures dying.

**Why:** Blood Artist's trigger condition is "whenever this creature or another creature dies." Each creature dying is a separate trigger event. The card-specific ruling confirms this: "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures." [C2] This is consistent with the general rule that leaves-the-battlefield triggers look back in time and trigger for each matching event. [CR 603.10a]

So you'll have three instances of "target player loses 1 life and you gain 1 life" on the stack.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain only when damage is actually *dealt* by the source. [CR 702.15b] states: "Damage dealt by a source with lifelink causes that source's controller… to gain that much life." If all 3 damage is prevented, no damage is dealt, so the condition for lifelink's effect is never met.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, your opponent gets 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result of damage dealt to a player with giving that player poison counters instead [CR 702.90b]. Lifelink causes the source's controller to gain that much life "in addition to any other results that damage causes" [CR 702.15b]. Since infect already replaced the life-loss result, lifelink still functions independently and you gain 3 life.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature. Protection from white does not save it.

**Why:** Wrath of God says "Destroy all creatures" without targeting any specific creature and without dealing damage. [C1] Protection from white prevents being *targeted* by white spells [CR 702.16b] and prevents *damage* from white sources [CR 702.16e], but "destroy" is neither targeting nor damage. Since Wrath of God does neither, protection from white has no effect on it.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from white means the permanent can't be enchanted by Auras that have the stated quality. Any such Auras already attached are put into their owners' graveyards as a state-based action. [CR 702.16c]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes, you can target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof means "This permanent can't be the target of spells or abilities **your opponents** control." [CR 702.11b] Since you are not an opponent of yourself, hexproof does not prevent you from targeting your own creature with your own spell. It only blocks targeting by the other player's spells and abilities.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No, ward does not counter Abrupt Decay. The ward ability triggers, but its effect to counter the spell fails because Abrupt Decay has "This spell can't be countered."

Why: Ward is a triggered ability that says "counter that spell or ability unless that player pays [cost]" [CR 702.21a]. The ability triggers when Abrupt Decay targets the creature, but when it resolves, its effect attempts to counter a spell that has protection from being countered. The card-specific ruling confirms this directly: "Abrupt Decay won't be countered even if you don't" [C2]. So the ward ability triggers, but its counter effect has no legal effect on Abrupt Decay, and the spell resolves normally.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will resolve before Grip, letting you redirect Grip to your other artifact.

**Why:**

- Turning a face-down permanent face up is a special action, and special actions are allowed while a spell with split second is on the stack. [CR 702.37e] [CR 702.61b] [C5]
- Willbender's triggered ability triggers when it is turned face up. [C13]
- Triggered abilities trigger and are put on the stack as normal while a spell with split second is on the stack. [CR 702.61b]
- The trigger goes on top of the stack (above Grip) and resolves first. Willbender's ability says "change the target of target spell or ability with a single target." Krosan Grip has a single target, so it qualifies. [CR 115.7b]
- You change Grip's target to your other artifact, which is a legal target. [CR 115.7a]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice. The creature is sacrificed as part of paying the cost, which happens during the casting process before the spell is fully cast. No player receives priority until after all costs have been paid and the spell is on the stack.

**Why:** Paying costs (including sacrificing a creature as an additional cost) is part of the casting process under [CR 601.2h]. The spell only becomes "cast" once all steps through 601.2h are completed, at which point the controller receives priority [CR 601.2i]. Since no player has priority during the casting process, there is no window for your opponent to respond to the sacrifice. This is confirmed by the card-specific ruling: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." [C3]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** Flashback includes a static ability that says "If the flashback cost was paid, exile this card instead of putting it anywhere else any time it would leave the stack" [CR 702.34a]. This applies whether the spell resolves, is countered, or leaves the stack in any other way [C2]. Since the spell was countered, it never resolved, so its "Draw a card" effect never happened.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not apply. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound is a static ability that functions while the spell is on the stack and creates a delayed triggered ability only if the spell resolves. Its replacement effect says "instead of putting it into your graveyard **as it resolves**, exile it." If the spell is countered, it never resolves, so the replacement effect never applies and the delayed triggered ability is never created. The card goes to its owner's graveyard as normal. [CR 702.88a] [C5]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist does not trigger and it does not return to the battlefield.

Why: The persist ability's trigger condition is "if it had no -1/-1 counters on it." The game checks the creature's state just before it leaves the battlefield, and if a -1/-1 counter is present at that moment, the condition is not met, so the ability never triggers. [C1] [C6]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 702.79a

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When a state-based action causes a permanent to leave the battlefield at the same time other state-based actions are performed (such as the +1/+1 and -1/-1 counter cancellation under [CR 704.5q]), that permanent's last known information is derived from the game state **before** any of those state-based actions were performed [CR 704.8]. In your scenario, before the state-based action check, Young Wolf had one +1/+1 counter on it. Undying's condition—"if it had no +1/+1 counters on it"—is evaluated against that last known information, so the condition is not met and undying does not trigger.

This is directly supported by the example in [CR 704.8], which describes the same situation with Young Wolf having a +1/+1 counter and concluding that "undying will not trigger."

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 702.93a

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The Lightning Bolt will fizzle and deal no damage.

**Why:** Cloudshift exiles the creature and returns it to the battlefield as a new object [C3]. The returned card is not the target of any spell that targeted the original object [C5]. When the Lightning Bolt tries to resolve, its target is the original object, which is now in exile. Since Lightning Bolt doesn't specify it can target objects in another zone, only permanents are legal targets [CR 115.2]. With an illegal target, the spell doesn't resolve and its effect doesn't happen.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

**Why:** The equip ability states "Equip only as a sorcery." Under [CR 307.5], this means the player must have priority, it must be during the main phase of their turn, **and the stack must be empty**. Since Lightning Bolt is on the stack, the stack is not empty, so the equip ability cannot be activated at that time.

Additionally, even if you could equip it, Colossus Hammer grants +10/+10 and removes flying [C2]—it does not prevent or redirect damage, so it would not stop Lightning Bolt's 3 damage [C1].

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 702.6a

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost of Smuggler's Copter, even though it just came under your control and has no haste.

**Why:** The "summoning sickness" restriction (a creature can't attack or activate its own tap abilities unless it's been under your control since your turn began) does not prevent a creature from being tapped to pay a cost for another permanent's activated ability. The official ruling for Smuggler's Copter explicitly confirms this: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." [C12] The crew ability's cost is "Tap any number of other untapped creatures you control with total power N or greater" [CR 702.122a], and your 3/3 meets the power requirement and is untapped, so it's a legal part of the cost.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** Once a Vehicle becomes a creature, it behaves like any other creature, including the restriction that it can't attack unless you've controlled it continuously since your turn began [C10]. Since you cast it this turn, that condition isn't met. Haste would override this restriction [CR 702.10b], but Smuggler's Copter doesn't have haste. The timing rule about when you can crew it (beginning of combat step at the latest) [C13] is irrelevant here because the summoning-sickness restriction still applies regardless of when you crew it.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a blocker does not remove it from combat and does not stop it from dealing combat damage. It still assigns combat damage equal to its power to the creature it's blocking.

**Why:** A creature remains a blocking creature until it's removed from combat or the combat phase ends [CR 509.1g]. Tapping is not one of the ways a creature is removed from combat. In the combat damage step, each blocking creature assigns combat damage equal to its power [CR 510.1a], and a blocking creature assigns that damage to the creature(s) it's blocking [CR 510.1d]. There is no requirement that a creature be untapped to assign combat damage.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives. Double strike has no effect here.

**Why:** When creatures fight, each deals damage equal to its power to the other [CR 701.14a]. That damage is not combat damage [CR 701.14d]. Double strike is a static ability that modifies the combat damage step [CR 702.4a], so it does not apply to fight damage. The 3/3 has 4 damage marked on it against a toughness of 3, so it dies. The 4/4 has 3 damage marked on it against a toughness of 4, so it survives.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects owned by that player leave the game, and any effects that give that player control of objects end. [CR 800.4a] Bob owns Control Magic (he cast it), so it leaves the game. The creature is owned by Alice, so it remains on the battlefield. The control-changing effect from Control Magic ends, and the creature reverts to its owner, Alice. This is directly illustrated by the example in [CR 800.4a]: "Alex casts Mind Control, an Aura that reads, 'You control enchanted creature,' on Bianca's Assault Griffin. If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control."

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, Lightning Bolt does not resolve. It leaves the game.

**Why:** When a player leaves the game, all objects owned by that player leave the game. Lightning Bolt is a card on the stack owned by Bob, so it leaves the game as part of this process. It does not resolve, and it does not go to a graveyard—it simply leaves the game. [CR 800.4a]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together, totaling 21, which meets the loss threshold.

**Why:** The rule tracks combat damage dealt "by the same commander over the course of the game" [CR 903.10a]. The tracking unit is the commander card itself, not the player who controls it. The commander designation is an attribute of the card that persists regardless of zone or controller [CR 903.3]. So all combat damage that card deals to you across the game accumulates toward the 21-damage loss condition, no matter who controls it when the damage is dealt.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and it identifies this as a replacement effect. The state-based action in rule 903.9a is a separate mechanism that applies when the commander is already in a graveyard or exile. [CR 903.9b] [CR 903.9a]

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The possible damage totals are **10** or **8**.

**Why:** When multiple replacement effects modify how damage is dealt, the affected player chooses the order in which to apply them [CR 616.1]. This is confirmed by both card-specific rulings [C4] and [C6].

The two possible orders:

- **Torbran first, then Furnace of Rath:** 3 + 2 = 5, then 5 × 2 = **10**
- **Furnace of Rath first, then Torbran:** 3 × 2 = 6, then 6 + 2 = **8**

Your opponent picks whichever order they prefer.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No. Having an empty library is not itself a losing condition. You only lose if you attempt to draw a card from a library that has no cards in it.

Why: The state-based action that causes a loss is specifically tied to the act of attempting a draw from an empty library, not to the library being empty. [CR 704.5b] states the loss occurs "if a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] confirms it is the player who "attempts to draw a card from a library with no cards in it" who loses. Simply having zero cards in your library, without a draw attempt, does not trigger any losing condition.

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** I can't determine the amount without more details.

**Need details:**
- Does your attacker have trample?
- What is its power?
- How many creatures are blocking it, and what is each one's toughness?
- Is any damage already marked on the blockers?
- Are there any relevant abilities or effects (e.g., protection, damage prevention, damage redirection)?

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No. A copy does not get the counters on the original creature, nor does it get the bonus from an enchantment attached to it.

**Why:** When copying an object, the copy acquires only the copiable values (name, mana cost, color, types, rules text, power, toughness, etc.) as modified by other copy effects and certain "as it enters" abilities. Counters, status, and other effects (including type-changing and text-changing effects) are explicitly not copied. [CR 707.2]

So if the original creature has +1/+1 counters on it or an Aura giving it +2/+0, the copy enters without those counters and without that bonus. The copy only has whatever power and toughness are printed (or set by its own copiable values).

Review: **incorrect**. The substantive general copy rule and citation are correct, but the frozen rubric requires a clarification and rejects a definitive answer to this underspecified copy question. This rubric miss is separated from product alignment.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Ruling: You (as the affected player) choose which replacement effect to apply first. Once that effect is applied, the process is repeated with any remaining applicable replacement effects. The final number of tokens depends on the specific effects and the original event.

Why: When two or more replacement effects attempt to modify the same event, the affected player chooses which one to apply [CR 616.1]. If any of them are self-replacement effects, one of those must be chosen first [CR 616.1a]. After the chosen effect is applied, the process is repeated, taking into account only replacement effects that would now be applicable [CR 616.1f].

Need details: What is the exact text of each replacement effect, and how many tokens would the original event create before any replacements are applied?

Review: **correct**. The answer meets the frozen criteria and makes no unsupported or contradictory material claim; reviewed against the supplied rule or card excerpts.
Reviewer: Codex

Missing reference groups: none

