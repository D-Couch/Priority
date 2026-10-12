# Commander damage retrieval change

The held-out case h26 previously abstained because lexical retrieval surfaced Commander rules 903.9 but omitted the governing rule 903.10a. The Commander topic now includes rules 903.10 and 903.10a. A retrieval regression test asserts that the exact held-out question returns CR 903.10a.

With the same local Qwen 3.8 27B Q4_K_M model, LM Studio configuration, frozen corpus, lexical mode, and seed 42, h26 now retrieves its expected evidence and answers correctly: the 12 and 9 damage amounts add for the same commander, and the player loses at 21 even though control changed. The related h27 answer remains correct; it also receives the additional Commander-damage sources, which are irrelevant to that answer.

The reviewed held-out score rose from 25/32 to 26/32, and expected-evidence recall rose from 17/32 to 18/32. Median latency increased from 10.30s to 10.50s and p95 from 16.94s to 17.42s. The run had no errors or truncations, and five existing answers remain flagged for unsupported or contradictory claims. One run is descriptive and cannot establish a reliable latency change.

The updated h26 answer and both changed Commander source sets were reviewed against the criteria and frozen Comprehensive Rules text. For the other 30 cases, prior AI-assisted grades were carried forward only where answers and packed source excerpts were byte-identical. No independent human judge reviewed this benchmark; results are not human-validated accuracy claims.
