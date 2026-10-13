# precise-conditions-heldout-seed42

Status: **complete** · implementation commit `f12fe9d244b9b285956cdc50c9dec54a4040476b`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | pending / n/a/0 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 81.1% |
| Cases retrieving every expected evidence group | 18/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | pending / n/a |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 0/0 reviewed |
| Reviewed accuracy | pending / n/a |
| Mean reviewed rubric score | pending / n/a |
| Median successful response | 8.10 s |
| p95 successful response | 13.81 s |
| Median first visible answer token | 6.50 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | pending | 9.66 |
| h02-intervening-if (r1) | 100.0% | pending | 6.25 |
| h03-independent-trigger (r1) | 50.0% | pending | 13.26 |
| h04-replacement-death (r1) | 100.0% | pending | 7.42 |
| h05-simultaneous-death (r1) | 100.0% | pending | 7.25 |
| h06-lifelink-prevented (r1) | 50.0% | pending | 5.18 |
| h07-infect-lifelink (r1) | 100.0% | pending | 7.64 |
| h08-protection-wrath (r1) | 100.0% | pending | 8.17 |
| h09-protection-aura (r1) | 100.0% | pending | 4.66 |
| h10-own-hexproof (r1) | 100.0% | pending | 5.57 |
| h11-ward-uncounterable (r1) | 66.7% | pending | 8.84 |
| h12-split-second (r1) | 100.0% | pending | 14.56 |
| h13-sacrifice-cost (r1) | 66.7% | pending | 9.71 |
| h14-flashback-countered (r1) | 66.7% | pending | 5.84 |
| h15-rebound-countered (r1) | 66.7% | pending | 6.95 |
| h16-persist-counter (r1) | 100.0% | pending | 6.96 |
| h17-undying-simultaneous-sba (r1) | 75.0% | pending | 11.81 |
| h18-blink-target (r1) | 50.0% | pending | 10.69 |
| h19-equip-timing (r1) | 75.0% | pending | 13.81 |
| h20-crew-new-creature (r1) | 66.7% | pending | 9.07 |
| h21-new-vehicle (r1) | 50.0% | pending | 7.99 |
| h22-tapped-blocker (r1) | 0.0% | pending | 8.00 |
| h23-fight-double-strike (r1) | 100.0% | pending | 8.05 |
| h24-leaving-controller (r1) | 100.0% | pending | 9.92 |
| h25-leaving-stack (r1) | 100.0% | pending | 8.75 |
| h26-commander-control (r1) | 100.0% | pending | 8.15 |
| h27-commander-hand (r1) | 100.0% | pending | 7.42 |
| h28-replacement-order (r1) | 80.0% | pending | 10.52 |
| h29-empty-library (r1) | 100.0% | pending | 7.79 |
| h30-ambiguous-combat (r1) | 100.0% | pending | 7.02 |
| h31-ambiguous-copy (r1) | 100.0% | pending | 9.59 |
| h32-ambiguous-replacements (r1) | 100.0% | pending | 9.76 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** Alice's ability goes on the stack first (bottom), then Bob's, then Charlie's (top). They resolve in reverse order: Charlie's first, Bob's second, Alice's last.

**Why:** In a multiplayer game, the active player puts their triggered abilities on the stack first, then each nonactive player in turn order does the same [CR 805.7]. Since Alice is active and turn order is Alice → Bob → Charlie, the stack (bottom to top) is Alice, Bob, Charlie. The top of the stack resolves first when all players pass [CR 608.1], so Charlie's ability resolves, then Bob's, then Alice's.

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and if you have 39 or less life at that time, it is removed from the stack and has no effect.

**Why:** Felidar Sovereign's ability uses an "intervening if clause," which means the condition is checked both when the ability triggers and again when it resolves. [CR 603.4] explicitly uses Felidar Sovereign as its example: if the player has 39 or less life at resolution, the ability does nothing. The card-specific ruling confirms this: "If you do, the ability will check again as it tries to resolve. If you don't have 40 or more life at that time, the ability won't do anything." [C2]

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. Once the ability is on the stack, it exists independently of the Simulacrum. Its effect—"you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle"—doesn't reference the Simulacrum or require it to be on the battlefield, so it resolves normally even if the Simulacrum is destroyed before it resolves.

**Why:** A triggered ability on the stack has the text of the ability that created it and no other characteristics [CR 405.4]. The "may" choice is made when the ability resolves [CR 603.5], and the effect simply instructs you to search your library—it doesn't attempt to do anything to the Simulacrum itself, so the Simulacrum's absence from the battlefield is irrelevant.

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exiling, so the card is never actually put into a graveyard [CR 614.6]. Since the trigger condition is never met, the ability doesn't trigger. This is confirmed by the official ruling: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Missing reference groups: none

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **three** times — once for itself dying and once for each of the two other creatures dying.

**Why:** Blood Artist's trigger condition is "whenever this creature or another creature dies," so each individual creature death is a separate trigger event. [CR 603.10a] establishes that leaves-the-battlefield abilities look back in time, meaning the ability triggers even though Blood Artist is no longer on the battlefield when the other creatures die. The card-specific ruling in [C2] confirms this directly: "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures." So with three total deaths (itself + two others), you get three triggers, each causing a target player to lose 1 life and you to gain 1 life.

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain based on damage *dealt* by the source. [CR 702.15b] If all 3 damage is prevented, no damage is dealt, so the condition for lifelink's life gain is never met.

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they gain 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the life-loss result on the damage recipient with poison counters instead [CR 702.90b]. Lifelink causes the source's controller to gain life equal to the damage dealt, "in addition to any other results that damage causes" [CR 702.15b]. These two abilities affect different players and different aspects of the same damage event, so they apply together without conflict.

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature. Protection from white does not prevent it.

**Why:** Protection from white prevents being *targeted* by white spells, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. Wrath of God says "Destroy all creatures" — it doesn't target any creature, so the targeting restriction in protection never applies [C1]. Since your creature has no indestructible, nothing stops the destruction.

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from white means the permanent can't be enchanted by Auras that have the stated quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action. [CR 702.16c]

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents *opponents* from targeting the creature, so you can freely target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you are not your own opponent, the restriction doesn't apply to you. Giant Growth simply requires "target creature" [C2], and your own creature is a legal target for your own spell.

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

**Why:** Abrupt Decay has "This spell can't be countered" printed on it [C1]. Ward's effect says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but a spell that can't be countered is not a valid object for that counter effect to apply to. The official ruling confirms this directly: "Abrupt Decay won't be countered even if you don't" pay the ward cost [C2]. The ward ability still triggers and you're still offered the choice to pay, but the "counter" portion simply has no effect on Abrupt Decay.

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up, and its triggered ability will resolve before Krosan Grip, redirecting it to your other artifact.

**Why:**

Turning a face-down permanent face up is a special action, and special actions are explicitly allowed while a spell with split second is on the stack [CR 702.61b] [C5]. Willbender's ability triggers when it is turned face up [C13], and triggered abilities are put on the stack as normal during split second [CR 702.61b] [C2]. Because the triggered ability is placed on top of Krosan Grip [CR 405.2], it resolves first. Willbender's text says "change the target of target spell or ability with a single target," and Krosan Grip has a single target, so it is a valid object for Willbender's ability. The new target must be legal for Krosan Grip [CR 115.7a] [CR 115.7b], and your other artifact qualifies.

**Practical sequence:**
1. Krosan Grip is on the stack targeting Artifact A.
2. You take the special action to turn Willbender face up (paying {1}{U}).
3. Willbender's triggered ability goes on the stack above Grip.
4. You target Krosan Grip with Willbender's ability.
5. Willbender's ability resolves: you change Grip's target to Artifact B.
6. Krosan Grip resolves: it destroys Artifact B.

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to destroy the creature, because the sacrifice is part of paying costs, which happens before the spell is cast and before anyone receives priority to respond.

**Why:** The casting process puts the spell on the stack first [CR 601.2a], then you pay all costs including the sacrifice [CR 601.2h], and only after those steps are complete does the spell become cast [CR 601.2i]. Players can only respond once the spell has been cast and all costs have been paid; no one can interfere with the creature you sacrificed to prevent the casting [C3]. By the time your opponent would get priority, the creature is already in the graveyard and the spell is on the stack.

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** When a spell is countered, it never resolves, so its "Draw a card" instruction is never carried out. Because the flashback cost was paid, the card is exiled instead of going to the graveyard when it leaves the stack [CR 702.34a]. This applies regardless of whether the spell resolves, is countered, or leaves the stack some other way [C2].

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not exile it. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The official ruling confirms this explicitly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist does not trigger and it stays in the graveyard.

**Why:** Persist's condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield, so any -1/-1 counters present at that moment prevent the ability from triggering [C6].

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When a state-based action causes a permanent to leave the battlefield at the same time other state-based actions are performed (such as removing opposing +1/+1 and -1/-1 counters), that permanent's last known information is derived from the game state *before* any of those state-based actions were performed. [CR 704.8] In your scenario, before state-based actions are checked, Young Wolf has a +1/+1 counter on it. Since undying's condition is "if it had no +1/+1 counters on it," and it did have one at the relevant moment, undying does not trigger. [CR 702.93a] This is the exact example given in [CR 704.8]: a Young Wolf with one +1/+1 counter that receives enough -1/-1 counters to die will not trigger undying because it had a +1/+1 counter when it was last on the battlefield.

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The original Lightning Bolt will fizzle and deal no damage.

**Why:** Cloudshift's ruling explicitly states that "the returned card won't be the target of any spells or abilities that targeted it before" [C5]. When the creature is exiled and returned, it's a new object on the battlefield, so the Bolt's target no longer exists. A spell with an illegal target won't resolve [C9].

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability can only be activated as a sorcery, meaning during your main phase when the stack is empty. Since Lightning Bolt is on the stack, you cannot activate the equip ability in response to it.

**Why:** The equip ability's text explicitly states "Activate only as a sorcery" [CR 702.6a]. A sorcery-speed activation requires the stack to be empty, so you cannot respond to a spell that is already on the stack with it. You could equip the hammer before your opponent casts Lightning Bolt (during your main phase with an empty stack), which would give the creature +10/+10 and let it survive the 3 damage [C2], but you cannot do so after the bolt is already on the stack.

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost even though it just came under your control and has no haste.

**Why:** The crew ability is an activated ability of the *Vehicle*, not of the creature being tapped. The creature is simply being tapped as part of the cost to activate the Vehicle's ability, which is not restricted by summoning sickness. The official ruling for Smuggler's Copter confirms this directly: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." [C12] The crew cost requires only that the creature be untapped and have sufficient power; it does not require the creature to have been under your control since your turn began. [CR 702.122a]

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No. Even after crewing it, Smuggler's Copter cannot attack this turn because you haven't controlled it continuously since your turn began, and it doesn't have haste.

**Why:** Once a Vehicle becomes a creature, it behaves exactly like any other artifact creature, which means it can't attack unless you've controlled it continuously since your turn began [C10]. Haste is the ability that overrides this restriction [CR 702.10b], but Smuggler's Copter doesn't have it. So even though it's a 3/3 creature with flying after crewing, the "summoning sickness" restriction still applies to its ability to attack.

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from assigning combat damage. It will still deal 3 damage as a blocker.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends; tapping is not a removal from combat [CR 509.1g]. In the combat damage step, each blocking creature assigns combat damage equal to its power [CR 510.1a], and a blocking creature assigns that damage to the creature(s) it is blocking [CR 510.1d]. Tapping has no effect on any of these conditions.

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it.

**Why:** A fight is a single simultaneous exchange where each creature deals damage equal to its power to the other [CR 701.14a]. The damage dealt in a fight is explicitly not combat damage [CR 701.14d], so double strike—which modifies the combat damage step [CR 702.4a]—has no effect here. The 3/3 (toughness 3) takes 4 damage and dies; the 4/4 (toughness 4) takes 3 damage and survives.

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects they own leave the game and any effects giving them control of objects end [CR 800.4a]. Since Bob owns Control Magic (he cast it), it leaves the game. The creature is owned by Alice, so it remains in the game and reverts to her control once Bob's control-changing effect ends. This is directly illustrated by the example in [CR 800.4a]: "Alex casts Mind Control… on Bianca's Assault Griffin. If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control." Additionally, gaining control of a creature does not cause you to gain control of attached Auras [C2], so Bob never owned the creature or the Aura's attachment relationship changed ownership.

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, the Lightning Bolt does not resolve. It leaves the game when Bob does.

**Why:** When a player leaves the game, all objects they own leave the game. [CR 800.4a] The Lightning Bolt on the stack is represented by a card that Bob owns, so it leaves the game as part of this process and never gets the chance to resolve. The fact that it targets Alice (who remains in the game) is irrelevant—the spell is gone before resolution.

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. Those 12 + 9 = 21 combat damage points add together, and the player loses the game.

**Why:** The commander damage rule tracks damage dealt "by the same commander" over the course of the game, not damage dealt by a specific controller [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of who controls it or what zone it's in [CR 903.3]. So as long as it's the same card dealing the combat damage, all of it counts toward the 21-damage threshold, no matter which player controlled it at the time.

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand. This is a replacement effect, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and it identifies this as a replacement effect [CR 903.9b]. The state-based action in rule 903.9a is a separate mechanism that applies when a commander is already in a graveyard or in exile [CR 903.9a]. Since your scenario involves the commander being returned to hand (not already in a graveyard or exile), the replacement effect in 903.9b is what applies.

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran).

**Why:** When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles it to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Each replacement effect gets only one opportunity to affect the event [CR 614.5].

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library is not, by itself, a losing condition. You only lose if you *attempt* to draw a card from it (or are required to draw more cards than it contains).

**Why:** The state-based action that causes a loss is specifically tied to an attempted draw from an empty library, not to the library being empty in general. [CR 704.5b] requires that the player "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] frames it the same way: "A player who attempts to draw a card from a library with no cards in it loses the game." So as long as no effect has caused you to draw (or attempt to draw) since your library became empty, you are not in a losing state.

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacker has **trample**, it must assign at least lethal damage to the blocking creature(s), and any excess damage can be assigned to the defending player. If it does **not** have trample, none of its damage gets through to the player — it assigns all its combat damage to the blocking creature(s).

**Why:** Trample modifies damage assignment so that once all blocking creatures have been assigned lethal damage (accounting for damage already marked on them and damage from other creatures in the same combat damage step), the controller may assign the remaining damage to the player [CR 702.19b]. Without trample, a blocked creature simply assigns its damage to the creatures blocking it [CR 510.1c].

**Example:** A 5/5 with trample is blocked by a 2/2. You must assign at least 2 damage to the blocker; the remaining 3 can go to your opponent.

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. Your copy does not get the counters on the original creature, and it does not get the bonus from the enchantment attached to it.

**Why:** When copying an object, only its copiable values are acquired—those are the values derived from the text printed on the object (name, mana cost, color, types, rules text, power, toughness, loyalty), as modified by other copy effects, face-down status, and "as it enters" abilities. Counters, status, and other effects (including type-changing and text-changing effects) are explicitly not copied. [CR 707.2]

For example, if a creature is a 5/5 because an enchantment gives it +2/+2, a Clone that copies it will only be whatever the creature's printed (or otherwise copiable) power and toughness are, not the boosted value. [CR 707.2]

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** You choose the order in which the two replacement effects are applied. Each effect modifies the event, and the next effect is then applied to the already-modified event. The final number of tokens depends on what each effect does and the order you choose.

**Why:** When two or more replacement effects attempt to modify the same event, the affected player chooses which one to apply first, then the process repeats with any remaining applicable effects [CR 616.1]. Once a chosen effect has been applied, the process is repeated taking into account only effects that would now be applicable [CR 616.1f]. For example, if both effects say "create twice as many tokens instead," you'd choose one to apply (doubling the count), then the other applies to that modified result (doubling again), yielding four times the original number. If the effects do different things (e.g., one doubles and one adds a fixed number), the order you choose can change the final result.

Missing reference groups: none

