# conditional-heldout-seed42

Status: **complete** · implementation commit `5abb9f298a24b44994aeaf5ef28b19ecd0b417b0`

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
| Median successful response | 7.78 s |
| p95 successful response | 10.64 s |
| Median first visible answer token | 6.25 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | pending | 10.39 |
| h02-intervening-if (r1) | 100.0% | pending | 5.87 |
| h03-independent-trigger (r1) | 50.0% | pending | 10.64 |
| h04-replacement-death (r1) | 100.0% | pending | 6.06 |
| h05-simultaneous-death (r1) | 100.0% | pending | 7.33 |
| h06-lifelink-prevented (r1) | 50.0% | pending | 4.62 |
| h07-infect-lifelink (r1) | 100.0% | pending | 8.09 |
| h08-protection-wrath (r1) | 100.0% | pending | 7.82 |
| h09-protection-aura (r1) | 100.0% | pending | 4.86 |
| h10-own-hexproof (r1) | 100.0% | pending | 5.56 |
| h11-ward-uncounterable (r1) | 66.7% | pending | 7.07 |
| h12-split-second (r1) | 100.0% | pending | 10.28 |
| h13-sacrifice-cost (r1) | 66.7% | pending | 9.58 |
| h14-flashback-countered (r1) | 66.7% | pending | 5.30 |
| h15-rebound-countered (r1) | 66.7% | pending | 6.59 |
| h16-persist-counter (r1) | 100.0% | pending | 6.82 |
| h17-undying-simultaneous-sba (r1) | 75.0% | pending | 10.53 |
| h18-blink-target (r1) | 50.0% | pending | 9.87 |
| h19-equip-timing (r1) | 75.0% | pending | 9.28 |
| h20-crew-new-creature (r1) | 66.7% | pending | 16.93 |
| h21-new-vehicle (r1) | 50.0% | pending | 8.09 |
| h22-tapped-blocker (r1) | 0.0% | pending | 9.92 |
| h23-fight-double-strike (r1) | 100.0% | pending | 7.55 |
| h24-leaving-controller (r1) | 100.0% | pending | 7.74 |
| h25-leaving-stack (r1) | 100.0% | pending | 8.73 |
| h26-commander-control (r1) | 100.0% | pending | 7.88 |
| h27-commander-hand (r1) | 100.0% | pending | 7.15 |
| h28-replacement-order (r1) | 80.0% | pending | 7.89 |
| h29-empty-library (r1) | 100.0% | pending | 6.43 |
| h30-ambiguous-combat (r1) | 100.0% | pending | 6.44 |
| h31-ambiguous-copy (r1) | 100.0% | pending | 8.23 |
| h32-ambiguous-replacements (r1) | 100.0% | pending | 7.71 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** Alice's ability goes on the stack first (bottom), then Bob's, then Charlie's (top). They resolve in reverse order: Charlie's first, then Bob's, then Alice's.

**Why:** When multiple triggered abilities are waiting, the active player puts theirs on the stack first, then each nonactive player in turn order does the same [CR 805.7]. Each new object is placed on top of all objects already on the stack [CR 405.2], so the stack from bottom to top is Alice, Bob, Charlie. The top of the stack resolves first [CR 608.1], giving the resolution order Charlie → Bob → Alice.

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and if you have 39 or less life at that time, it does nothing.

**Why:** Felidar Sovereign's ability uses an "intervening 'if' clause," which means the condition is checked both when the ability triggers and again as it resolves. If the condition isn't met at resolution, the ability is removed from the stack and has no effect. [CR 603.4] [C2]

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. You may still search for a basic land. The ability's effect doesn't reference the Simulacrum itself, so it doesn't need to find the card in the graveyard.

**Why:** Zone-change triggers that "attempt to do something to that object" must find it in the zone it moved to, or that part fails [CR 603.6]. Solemn Simulacrum's ETB ability only instructs you to search your library, put a land onto the battlefield, and shuffle — it never tries to do anything *to* the Simulacrum [C1]. Since the effect doesn't depend on the Simulacrum's location, the ability resolves normally even though the Simulacrum is now in the graveyard.

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exiling the card instead [C1], so the card is never put into a graveyard and the trigger condition is never met [C2].

Missing reference groups: none

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **three** times — once for itself dying and once for each of the two other creatures dying.

**Why:** Each creature dying is a separate trigger event that matches the condition "whenever this creature or another creature dies." [CR 603.10a] establishes that leaves-the-battlefield triggers look back in time and trigger for each matching event, even if the source itself also leaves the battlefield simultaneously. The card-specific ruling confirms this: "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures." [C2]

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain only when damage is *dealt* by a source with lifelink [CR 702.15b]. Prevented damage is not dealt, so the condition for lifelink's life gain is never met.

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they get 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result with gaining poison counters, so the opponent does not lose life [CR 702.90b]. Lifelink causes its controller to gain life equal to the damage dealt "in addition to any other results that damage causes," meaning it functions independently of whether the damage actually caused life loss [CR 702.15b]. Both effects apply simultaneously to the same damage event.

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature.

**Why:** Protection from white prevents being targeted by white spells, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. None of these apply to a non-targeting "destroy all creatures" effect. Wrath of God simply says "Destroy all creatures" without targeting [C1], so protection offers no defense against it. Indestructible would have prevented the destruction [CR 702.12b], but since your creature lacks it, the destruction proceeds normally.

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality means the protected permanent can't be enchanted by Auras that have that quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action [CR 702.16c]. This happens automatically the next time state-based actions are checked; no player needs to do anything.

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents *opponents* from targeting the creature, so you can freely target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you are not your own opponent, the restriction doesn't apply to you. Giant Growth simply requires "target creature" [C2], and your own creature is a legal target for your own spell.

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost. The spell resolves and destroys the target.

**Why:** Ward's effect is "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but Abrupt Decay's text states "This spell can't be countered" [C1]. An effect that cannot legally be applied simply doesn't happen, so the ward's counter effect is impossible. The official ruling confirms this directly: "Abrupt Decay won't be countered even if you don't" [C2].

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will go on the stack above the Grip, allowing you to redirect it to your other artifact.

**Why:**

Turning a face-down permanent face up is a special action that doesn't use the stack [CR 702.37e], and split second explicitly permits special actions while it's on the stack [CR 702.61b]. This is also confirmed by the card-specific ruling: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5].

Once Willbender is turned face up, its triggered ability goes on the stack as normal [CR 702.61b], placing it above Krosan Grip. When it resolves, you choose a new legal target for the Grip — your other artifact qualifies [CR 115.7b].

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice. The sacrifice is part of the atomic casting process, and no one receives priority until the spell is fully cast with all costs paid.

**Why:** When you cast Fling, the spell is put on the stack, then you pay all costs (including the sacrifice) as a single uninterrupted action [CR 601.2a], [CR 601.2h]. Only after those steps complete does the spell become cast and players get priority [CR 601.2i]. The official ruling confirms this directly: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell" [C3]. Additionally, even if the creature were somehow removed after the spell is cast, Fling would still deal 4 damage, since it uses the power as it last existed on the battlefield [C2].

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** Flashback creates a static ability that says "exile this card instead of putting it anywhere else any time it would leave the stack" [CR 702.34a]. This applies whether the spell resolves, is countered, or leaves the stack for any other reason [C2]. Since the spell was countered, it never resolved, so the "Draw a card" instruction was never carried out.

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not apply. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The official ruling confirms this explicitly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard from the battlefield, persist does not trigger and the card does not return.

**Why:** Persist's trigger condition includes the intervening "if" clause: "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks that condition at the moment the creature is put into the graveyard; if the condition isn't met, the ability simply doesn't trigger [CR 603.4]. This is confirmed by the Kitchen Finks ruling, which notes that persist checks the creature's state just before it leaves the battlefield [C6].

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When a state-based action causes a permanent to leave the battlefield at the same time other state-based actions are performed (such as removing opposing +1/+1 and −1/−1 counters), the permanent's last known information is derived from the game state *before* any of those state-based actions were performed. [CR 704.8] In your scenario, before the check Young Wolf had a +1/+1 counter on it, so undying's condition ("if it had no +1/+1 counters on it") is not met. [CR 702.93a] This is the exact example given in the rule: a Young Wolf with one +1/+1 counter that receives enough −1/−1 counters to die will not trigger undying because it had a +1/+1 counter when last on the battlefield. [CR 704.8]

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The original Lightning Bolt will not damage the returned creature.

**Why:** When Cloudshift resolves, it exiles the creature and returns it to the battlefield as a new object. The original object that Lightning Bolt was targeting no longer exists, so the Bolt has no legal target and won't resolve. The Cloudshift ruling explicitly confirms this: "The returned card won't be the target of any spells or abilities that targeted it before." [C5] Since only permanents are legal targets for spells like Lightning Bolt [CR 115.2], and the original permanent is gone, the Bolt fizzles.

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability can only be activated as a sorcery, so it cannot be activated while Lightning Bolt is on the stack.

**Why:** The equip ability's timing restriction ("Equip only as a sorcery") means it may only be activated during your main phase when the stack is empty. [CR 702.6a] [C2] Since Lightning Bolt is an instant on the stack when you'd want to respond, the equip ability is not legally activatable at that time. Even if you could equip it, the +10/+10 would only matter if the creature survived the 3 damage, but the timing restriction prevents the activation entirely.

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost of Smuggler's Copter even though it was just cast and has no haste.

**Why:** The summoning sickness restriction (that a creature can't be tapped to activate *its own* abilities with the tap symbol) does not apply when the creature is being tapped as part of the cost of another object's ability. Crew is an activated ability of the Vehicle, and the creature is simply being tapped to pay that cost. [CR 702.122a] defines crew as "Tap any number of other untapped creatures you control with total power N or greater," and the official ruling confirms: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." [C12]

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** Once a Vehicle becomes a creature, it can't attack unless you've controlled it continuously since your turn began [C10]. Since you cast it this turn, that condition isn't met, and without haste to override the restriction [CR 702.10b], it's subject to summoning sickness. Crewing it doesn't change this — it simply makes it a creature; it doesn't grant haste or remove the continuous-control requirement.

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from assigning combat damage. It will still deal its combat damage in the combat damage step.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends; tapping is not a form of removal from combat [CR 509.1g]. In the combat damage step, a blocking creature assigns combat damage to the creatures it is blocking, with no condition requiring it to be untapped [CR 510.1d]. Tapping is simply a status change (tapped/untapped) and has no bearing on whether a creature is in combat or deals damage.

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 damage marked on it. Double strike has no effect here.

**Why:** Fight damage is not combat damage [CR 701.14d], and double strike only modifies the combat damage step [CR 702.4a]. In a fight, each creature simply deals damage equal to its power to the other [CR 701.14a], so the 3/3 takes 4 damage (exceeding its toughness of 3) and the 4/4 takes 3 damage (below its toughness of 4).

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects they own leave the game and any effects giving them control of objects end [CR 800.4a]. Since Bob owns Control Magic (he cast it), it leaves the game along with him. The creature, which Alice owns, simply reverts to her control once the control-changing effect ends. This is exactly the example given in the rule: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a].

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No. Lightning Bolt leaves the game and does not resolve.

**Why:** When a player leaves the game, all objects they own leave the game [CR 800.4a]. Since Bob owns the Lightning Bolt card, it leaves the game at that moment. It does not go to a graveyard or any other zone—it simply leaves the game. The clause about objects on the stack "ceasing to exist" applies only to objects not represented by cards (such as copies or tokens) [CR 800.4a], which doesn't apply here since Lightning Bolt is a card.

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together to 21, and you lose the game.

**Why:** Commander damage is tracked per commander (the card), not per controller. The rule states that a player who has been dealt 21 or more combat damage "by the same commander over the course of the game" loses [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of zone or controller changes [CR 903.3]. So all combat damage dealt by that same commander card accumulates toward the threshold, no matter who was controlling it when the damage was dealt.

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may choose to put your commander into the command zone instead of your hand. This is a **replacement effect**, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and identifies this as a replacement effect [CR 903.9b]. The state-based action in rule 903.9a applies to a different situation—when the commander is already in a graveyard or in exile [CR 903.9a]. Since your scenario involves the commander moving from the battlefield to your hand, the replacement effect is what applies.

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The two possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran). Your opponent will choose 10.

**Why:** When multiple effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran's "+2" first gives 3 + 2 = 5, which Furnace then doubles to 10. Applying Furnace's "double" first gives 3 × 2 = 6, to which Torbran then adds 2 for 8. Since your opponent chooses, they select the order that produces the greater result.

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library is not itself a losing condition. You only lose if you *attempt to draw* a card from a library that has no cards in it.

**Why:** The state-based action that causes a loss specifically requires that a player "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked" [CR 704.5b]. Rule 121.4 confirms the same condition: "A player who attempts to draw a card from a library with no cards in it loses the game" [CR 121.4]. Simply having zero cards in your library, without a draw attempt, does not trigger this loss.

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacking creature has trample, you must assign at least lethal damage to the blocking creature(s), and any excess damage can be assigned to the defending player. If it does *not* have trample, all of its combat damage is assigned to the blocker(s) and none reaches your opponent.

**Why:** Trample modifies damage assignment so that once all blocking creatures have been assigned lethal damage (accounting for damage already marked on them and damage from other creatures in the same combat damage step), the controller may assign the remaining damage to the player or planeswalker being attacked [CR 702.19b]. Without trample, a blocked creature assigns all its combat damage to the creatures blocking it [CR 510.1c].

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. Your copy does not get the counters on the original creature, and it does not get the bonus from an enchantment attached to it.

**Why:** When copying an object, only its copiable values are acquired—those derived from the text printed on the object (name, mana cost, color, types, rules text, power, toughness, loyalty), as modified by other copy effects and certain "as it enters" abilities. "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An enchantment's bonus is an "other effect," and counters are explicitly excluded, so neither transfers to the copy.

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** You (the affected player) choose which replacement effect to apply first, then the process is repeated with the remaining effect. The final number of tokens depends on what each effect does and the order you choose.

**Why:** When two or more replacement effects attempt to modify the same event, the affected player chooses one to apply, then the process repeats with any remaining applicable effects [CR 616.1], [CR 616.1f]. For example, if one effect doubles the token count and another adds a fixed number, applying the doubling first yields a different result than applying the addition first. If you share the specific effects, I can walk through the exact outcome.

Missing reference groups: none

