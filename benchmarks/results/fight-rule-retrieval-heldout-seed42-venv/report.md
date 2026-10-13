# fight-rule-retrieval-heldout-seed42-venv

Status: **complete** · implementation commit `96180d5652abe5e64476e4b7db4705521432d3df`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | pending / n/a/0 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 82.2% |
| Cases retrieving every expected evidence group | 19/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | pending / n/a |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 0/0 reviewed |
| Reviewed accuracy | pending / n/a |
| Mean reviewed rubric score | pending / n/a |
| Median successful response | 7.59 s |
| p95 successful response | 11.73 s |
| Median first visible answer token | 5.92 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | pending | 7.18 |
| h02-intervening-if (r1) | 100.0% | pending | 5.82 |
| h03-independent-trigger (r1) | 50.0% | pending | 10.72 |
| h04-replacement-death (r1) | 100.0% | pending | 6.48 |
| h05-simultaneous-death (r1) | 100.0% | pending | 6.33 |
| h06-lifelink-prevented (r1) | 50.0% | pending | 5.43 |
| h07-infect-lifelink (r1) | 100.0% | pending | 9.13 |
| h08-protection-wrath (r1) | 100.0% | pending | 6.86 |
| h09-protection-aura (r1) | 100.0% | pending | 4.58 |
| h10-own-hexproof (r1) | 100.0% | pending | 6.61 |
| h11-ward-uncounterable (r1) | 66.7% | pending | 7.16 |
| h12-split-second (r1) | 100.0% | pending | 9.31 |
| h13-sacrifice-cost (r1) | 100.0% | pending | 10.63 |
| h14-flashback-countered (r1) | 66.7% | pending | 5.72 |
| h15-rebound-countered (r1) | 66.7% | pending | 6.15 |
| h16-persist-counter (r1) | 100.0% | pending | 6.80 |
| h17-undying-simultaneous-sba (r1) | 75.0% | pending | 10.34 |
| h18-blink-target (r1) | 50.0% | pending | 14.60 |
| h19-equip-timing (r1) | 75.0% | pending | 10.23 |
| h20-crew-new-creature (r1) | 66.7% | pending | 7.59 |
| h21-new-vehicle (r1) | 50.0% | pending | 7.80 |
| h22-tapped-blocker (r1) | 0.0% | pending | 7.77 |
| h23-fight-double-strike (r1) | 100.0% | pending | 7.53 |
| h24-leaving-controller (r1) | 100.0% | pending | 10.21 |
| h25-leaving-stack (r1) | 100.0% | pending | 10.12 |
| h26-commander-control (r1) | 100.0% | pending | 7.68 |
| h27-commander-hand (r1) | 100.0% | pending | 7.59 |
| h28-replacement-order (r1) | 80.0% | pending | 8.95 |
| h29-empty-library (r1) | 100.0% | pending | 7.18 |
| h30-ambiguous-combat (r1) | 100.0% | pending | 6.30 |
| h31-ambiguous-copy (r1) | 100.0% | pending | 9.25 |
| h32-ambiguous-replacements (r1) | 100.0% | pending | 11.73 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** Alice's ability goes on the stack first (bottom), then Bob's, then Charlie's (top). They resolve in reverse order: Charlie's first, then Bob's, then Alice's.

**Why:** At the beginning of upkeep, all triggered abilities are put on the stack before the active player gets priority [CR 503.1a]. The order is determined by CR 805.7: the active player (Alice) puts her triggered abilities on the stack first, then each nonactive player in turn order (Bob, then Charlie) does the same. Since the stack resolves top-down [CR 608.1], Charlie's ability resolves first, followed by Bob's, then Alice's.

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and if you have 39 or less life at that time, it is removed from the stack and has no effect.

**Why:** Felidar Sovereign's ability uses an "intervening if clause," which means the condition is checked both when the ability triggers and again as it resolves. [CR 603.4] The specific ruling confirms this: "If you do, the ability will check again as it tries to resolve. If you don't have 40 or more life at that time, the ability won't do anything." [C2] So in your scenario—triggering at 40 life but dropping to 39 before resolution—the ability fails its second check and does nothing.

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. You may still search for a basic land. Once the triggered ability is on the stack, it exists independently of the Simulacrum.

**Why:** A triggered ability on the stack has the text of the ability that created it and no other characteristics [CR 405.4]. The Simulacrum's ETB effect—"you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle"—directs the player to act on their library and the battlefield; it never references the Simulacrum itself. The zone-change rule about looking for the object in the zone it moved to [CR 603.6] only applies when the ability attempts to do something *to* the object that changed zones, which is not the case here. Destroying the Simulacrum has no effect on the ability already on the stack.

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exiling the card instead [C1], so the card is never put into a graveyard and the trigger condition is never met. This is confirmed by the official ruling: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Missing reference groups: none

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **three times** — once for itself dying and once for each of the two tokens dying.

**Why:** Blood Artist's trigger condition is "whenever this creature or another creature dies," so it triggers for each creature that dies, including itself. The official ruling confirms this: "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures." [C2] This works because leaves-the-battlefield abilities look back in time, so the ability triggers even though Blood Artist is no longer on the battlefield when the triggers go on the stack. [CR 603.10a]

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain based on damage that is actually *dealt*, not damage that is assigned. [CR 702.15b] states that "damage dealt by a source with lifelink causes that source's controller…to gain that much life." If all 3 damage is prevented, no damage is dealt, so no life is gained.

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they get 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result of damage dealt to a player with gaining poison counters instead [CR 702.90b]. Lifelink causes the controller of the damage source to gain life "in addition to any other results that damage causes" [CR 702.15b]. These two abilities operate on different players and don't conflict: infect changes what happens to the opponent (poison counters instead of life loss), while lifelink causes you to gain life. Both apply simultaneously.

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature.

**Why:** Protection from white prevents being *targeted* by white spells and prevents *damage* from white sources, but Wrath of God does neither — it's a global "destroy all creatures" effect with no targeting and no damage. [CR 702.16b], [CR 702.16e], [C1]. The only ability that would save it from a "destroy" effect is indestructible, which your creature doesn't have. [CR 702.12b]

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality means the protected permanent can't be enchanted by Auras with that quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action. [CR 702.16c]

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. You can target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. It only restricts opponents from targeting the creature; it does not prevent you from targeting it with your own spells. Since Giant Growth simply says "Target creature gets +3/+3 until end of turn" [C2], and you are the controller of both the spell and the creature, hexproof is irrelevant to your own targeting.

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

**Why:** Abrupt Decay has "This spell can't be countered," which is a static restriction that prevents any effect from countering it. Ward's ability says "counter that spell or ability unless that player pays [cost]," but since Abrupt Decay can't be countered, that counter effect simply doesn't apply. The ruling confirms this directly: "Abrupt Decay won't be countered even if you don't [pay the ward cost]." [C1][C2][CR 702.21a]

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up during split second, and its triggered ability will resolve before Krosan Grip, redirecting the target to your other artifact.

**Why:** Turning a face-down permanent face up is a special action, not an activated ability, so split second doesn't prevent it [CR 702.37e, CR 702.61b]. The triggered ability goes on top of the stack above Krosan Grip [CR 405.2], resolves first, and changes Grip's target to your second artifact. This is explicitly confirmed by the card's ruling: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5].

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice. By the time anyone gets priority to respond, the creature is already in the graveyard and the spell is fully cast.

**Why:** The sacrifice is part of paying the total cost, which happens during the casting process (601.2h). No player receives priority during that process; the spell only becomes "cast" after all cost steps are complete (601.2i). Players can only respond once the spell has been cast and all its costs have been paid, at which point the sacrificed creature is already gone [C3]. The opponent's only window to act is after Fling is on the stack with its costs fully paid.

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice goes to exile, and you do not draw a card.

**Why:** Flashback creates a static ability that says "exile this card instead of putting it anywhere else any time it would leave the stack" [CR 702.34a]. This applies regardless of how the spell leaves the stack—whether it resolves, is countered, or is removed some other way [C2]. Since the spell was countered, it never resolved, so the "Draw a card" instruction was never carried out.

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not trigger. The spell goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never happens. The official ruling confirms this explicitly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard" [C5].

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist does not trigger and it stays in the graveyard.

**Why:** Persist's condition is "if it had no -1/-1 counters on it" — the check happens just before the creature leaves the battlefield, and if it has even one -1/-1 counter at that moment, the condition fails and the ability doesn't trigger. [CR 702.79a] [C6]

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When a state-based action causes a permanent to leave the battlefield at the same time other state-based actions are performed (such as removing opposite counters), the permanent's last known information is derived from the game state *before* any of those state-based actions were performed. [CR 704.8] In your scenario, before state-based actions are checked, Young Wolf still has a +1/+1 counter on it, so undying's condition ("if it had no +1/+1 counters on it") is not met. [CR 702.93a] This is the exact situation described in the example under rule 704.8: a Young Wolf with one +1/+1 counter and enough -1/-1 counters to bring its toughness to 0 dies, and because it had a +1/+1 counter when last on the battlefield, undying does not trigger. [CR 704.8]

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The original Lightning Bolt will fizzle and deal no damage.

**Why:** Cloudshift exiles the creature and returns it to the battlefield as a new object. The returned card is not the target of Lightning Bolt — Lightning Bolt's target is the original object, which is now in exile and therefore not a legal target. A spell with no legal target when it tries to resolve won't resolve and its effect won't happen. [C5] [C9]

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

**Why:** Equip is an activated ability that can only be activated as a sorcery [CR 702.6a]. "Activate only as a sorcery" means the ability may only be activated when the stack is empty and it is a main phase. Since Lightning Bolt is on the stack, the stack is not empty, so the equip ability is not legal to activate at that time. Even if you could equip it, the +10/+10 would help the creature survive the 3 damage, but the timing restriction prevents you from doing so in response.

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost even though it just came under your control.

**Why:** The crew ability simply requires you to tap any number of untapped creatures you control with total power N or greater as a cost. It does not require those creatures to have been under your control since the beginning of your turn. The "summoning sickness" restriction only prevents a creature from attacking or activating tap abilities that include the tap symbol in their cost — it does not prevent a creature from being tapped to pay a cost for another permanent's ability. [CR 702.122a] [C12]

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No. Since you cast Smuggler's Copter this turn, it hasn't been under your control continuously since your turn began, and it has no haste, so it cannot attack this turn.

**Why:** Once a Vehicle becomes a creature via crew, it behaves exactly like any other artifact creature, including the restriction that it can't attack unless you've controlled it continuously since your turn began. [C10] Haste is the ability that overrides this restriction, and Smuggler's Copter doesn't have it. [CR 702.10b]

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from dealing combat damage. It remains a valid blocker and will deal 3 combat damage as normal.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends, whichever comes first [CR 509.1g]. Tapping is not a removal from combat—only effects that specifically say "remove from combat" do that. Combat damage is assigned based on the creature's power, not its tapped or untapped status [CR 510.1a], [CR 510.1d].

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 toughness remaining.

**Why:** When creatures fight, each deals damage equal to its power to the other [CR 701.14a]. This damage is not combat damage [CR 701.14d]. Double strike is a static ability that modifies the combat damage step [CR 702.4a], so it has no effect on fight interactions. Both creatures deal their power as damage simultaneously, and the 3/3's toughness is exceeded by the 4 damage it receives.

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature remains on the battlefield under Alice's control.

**Why:** When Bob leaves the game, all objects he owns leave the game, and any effects giving him control of objects end [CR 800.4a]. Since Bob cast and owns Control Magic, it leaves the game. The creature is owned by Alice, so it stays, and with the control-changing effect gone, it reverts to her control. This is directly analogous to the example in [CR 800.4a]: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control." Note that gaining control of a creature does not cause you to gain control of Auras attached to it [C2], so the Aura was always Bob's to begin with.

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, Lightning Bolt does not resolve. It leaves the game when Bob does.

**Why:** When a player leaves the game, all objects they own leave the game. Lightning Bolt is a card owned by Bob, so it leaves the game immediately and never gets the chance to resolve. [CR 800.4a] The rule's separate clause about objects on the stack "not represented by cards" ceasing to exist applies to things like spell copies or abilities without a card; since Lightning Bolt *is* represented by a card, it simply leaves the game (to Bob's graveyard) rather than ceasing to exist. [CR 800.4a]

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 + 9 = 21 combat damage adds together, and you lose the game.

**Why:** Commander damage is tracked per player per commander, not per controller. The rule states that a player who has been dealt 21 or more combat damage "by the same commander over the course of the game" loses the game [CR 903.10a]. The identity of the commander (the card) is what matters, not who is controlling it at the time the damage is dealt. So even though Alice controlled it for the first 12 and Bob for the last 9, it's still the same commander dealing damage to you, and the total reaches the 21 threshold.

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand. This is a **replacement effect**, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and labels this a replacement effect. The state-based action in rule 903.9a applies to a different situation—when the commander is already in a graveyard or in exile and was put there since the last state-based action check. Since your case involves the commander going to your hand (not to a graveyard or exile), the replacement effect in 903.9b is what applies. [CR 903.9b] [CR 903.9a]

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** The player being dealt damage (your opponent) chooses the order. The possible totals are **8** or **10**.

**Why:** When multiple replacement effects modify how much damage a source would deal, the player who would be dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first (3 + 2 = 5, then doubled to 10) or Furnace of Rath first (3 × 2 = 6, then +2 = 8) gives the two possible outcomes. Your opponent will naturally choose the order that minimizes the damage (8). Each replacement effect applies only once and does not re-trigger itself [CR 614.5].

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library by itself is not a losing condition. You only lose if you *attempt to draw* a card from a library that has no cards in it.

**Why:** The state-based action that causes a loss is specifically triggered by an attempted draw from an empty library, not by the library being empty. [CR 704.5b] states the loss occurs when "a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] confirms this is the condition. None of the listed ways to lose the game ([CR 104.3b], [CR 104.3d]) include simply having zero cards in your library.

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacker has trample, you must assign at least lethal damage to the blocking creature(s) first, and any excess damage can be assigned to your opponent. If your attacker does *not* have trample, all of its damage goes to the blocker(s) and nothing gets through.

**Why:** Trample modifies damage assignment so that once all blocking creatures have been assigned lethal damage (accounting for damage already on them and other damage being assigned in the same step), the controller may assign the remaining damage to the defending player. [CR 702.19b]

**Example:** A 5/5 with trample is blocked by a 2/2. You must assign at least 2 damage to the blocker; the remaining 3 can go to your opponent.

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. Your copy does not get the counters on the original creature, and it does not get the bonus from the enchantment attached to it.

**Why:** When copying an object, only its *copiable values* are acquired—those are the values derived from the text printed on the object (name, mana cost, color, types, rules text, power, toughness, loyalty), as modified by other copy effects, face-down status, and "as it enters" abilities. Counters, status, and other effects (including type-changing and text-changing effects) are explicitly not copied. [CR 707.2]

For example, if a creature is a 5/5 because an enchantment gives it +2/+2, a Clone that copies it will only be its base 3/3 (or whatever its printed/copiable power and toughness are), not 5/5. [CR 707.2]

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** You (as the affected player) choose which replacement effect to apply first. After that effect modifies the event, the process repeats with any remaining applicable effects. The final number of tokens depends on what each effect does to the (possibly already-modified) event.

**Why:** When two or more replacement effects attempt to modify the same event, the affected player chooses the order they're applied [CR 616.1]. Once one is applied, the process is repeated with any effects still applicable to the modified event [CR 616.1f]. Importantly, replacement effects that apply "if an effect would create one or more tokens" also apply if another replacement effect is the one creating them [CR 614.16]. So if both effects say "create twice as many," you'd get four times the original (double, then double again). If one says "create twice as many" and the other says "create three instead," the order you choose matters: doubling first then replacing with three gives three; replacing with three first then doubling gives six.

If you share the specific card texts, I can work out the exact result.

Missing reference groups: none

