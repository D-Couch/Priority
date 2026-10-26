# focused-heldout-retrieval-check-2026-10-26-3

Status: **complete** · implementation commit `1ce5d2185b8bed03fdb7e154914bb2778fd96134`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | pending / n/a |
| Correct and normally completed | pending / n/a/0 reviewed |
| Unknown finish reason | 32 |
| Mean expected-evidence recall | 88.5% |
| Cases retrieving every expected evidence group | 22/32 |
| Answers with citations | 0/32 |
| Citation ID validity (not semantic support) | pending / n/a |
| Answers with unsupported/contradictory claims | pending / n/a |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 0/0 reviewed |
| Reviewed accuracy | pending / n/a |
| Mean reviewed rubric score | pending / n/a |
| Median successful response | 0.05 s |
| p95 successful response | 0.06 s |
| Median first visible answer token | pending / n/a s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 66.7% | pending | 0.17 |
| h02-intervening-if (r1) | 100.0% | pending | 0.05 |
| h03-independent-trigger (r1) | 100.0% | pending | 0.05 |
| h04-replacement-death (r1) | 100.0% | pending | 0.05 |
| h05-simultaneous-death (r1) | 100.0% | pending | 0.05 |
| h06-lifelink-prevented (r1) | 50.0% | pending | 0.03 |
| h07-infect-lifelink (r1) | 100.0% | pending | 0.04 |
| h08-protection-wrath (r1) | 100.0% | pending | 0.03 |
| h09-protection-aura (r1) | 100.0% | pending | 0.02 |
| h10-own-hexproof (r1) | 100.0% | pending | 0.04 |
| h11-ward-uncounterable (r1) | 66.7% | pending | 0.05 |
| h12-split-second (r1) | 100.0% | pending | 0.06 |
| h13-sacrifice-cost (r1) | 100.0% | pending | 0.05 |
| h14-flashback-countered (r1) | 66.7% | pending | 0.05 |
| h15-rebound-countered (r1) | 66.7% | pending | 0.05 |
| h16-persist-counter (r1) | 100.0% | pending | 0.04 |
| h17-undying-simultaneous-sba (r1) | 75.0% | pending | 0.06 |
| h18-blink-target (r1) | 50.0% | pending | 0.06 |
| h19-equip-timing (r1) | 75.0% | pending | 0.06 |
| h20-crew-new-creature (r1) | 66.7% | pending | 0.05 |
| h21-new-vehicle (r1) | 50.0% | pending | 0.04 |
| h22-tapped-blocker (r1) | 100.0% | pending | 0.04 |
| h23-fight-double-strike (r1) | 100.0% | pending | 0.04 |
| h24-leaving-controller (r1) | 100.0% | pending | 0.04 |
| h25-leaving-stack (r1) | 100.0% | pending | 0.06 |
| h26-commander-control (r1) | 100.0% | pending | 0.05 |
| h27-commander-hand (r1) | 100.0% | pending | 0.05 |
| h28-replacement-order (r1) | 100.0% | pending | 0.06 |
| h29-empty-library (r1) | 100.0% | pending | 0.03 |
| h30-ambiguous-combat (r1) | 100.0% | pending | 0.03 |
| h31-ambiguous-copy (r1) | 100.0% | pending | 0.03 |
| h32-ambiguous-replacements (r1) | 100.0% | pending | 0.04 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

(No answer.)

Missing reference groups: CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

(No answer.)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

(No answer.)

Missing reference groups: none

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

(No answer.)

Missing reference groups: none

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

(No answer.)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

(No answer.)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

(No answer.)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

(No answer.)

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

(No answer.)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

(No answer.)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

(No answer.)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

(No answer.)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

(No answer.)

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

(No answer.)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

(No answer.)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

(No answer.)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

(No answer.)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

(No answer.)

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

(No answer.)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

(No answer.)

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

(No answer.)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

(No answer.)

Missing reference groups: none

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

(No answer.)

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

(No answer.)

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

(No answer.)

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

(No answer.)

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

(No answer.)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

(No answer.)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

(No answer.)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

(No answer.)

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

(No answer.)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

(No answer.)

Missing reference groups: none

