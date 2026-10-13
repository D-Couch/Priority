# CR 800.4a retrieval fix

Implementation under test: `00e3a79bc7006f3527bfd6dfbd997cc4113806f1` (`fix: match abbreviated player-elimination wording`). The h25 phrasing “Bob loses and leaves” now triggers CR 800.4a retrieval. On the frozen corpus, the rule appears in both candidate and packed evidence. The answer correctly says Lightning Bolt leaves with Bob and does not resolve, citing CR 800.4a. The earlier attempt (`c8c6510`) failed because it required “leaves the game”; its negative result remains under `leave-game-rule-heldout`.

The seed-42 held-out suite scored 26/32 fully correct, compared with 25/32 in the reviewed baseline; evidence recall rose 75.5%→78.6%, unsupported-claim answers fell 5→4, and median latency was 9.94 s. The direct h25 outcome improved from abstained to correct. Other outcomes also varied (h19 regressed; h20 improved), so this single-run aggregate is descriptive and does not establish that retrieval caused every difference. There were no request errors or truncations.

The seed-42 original suite remained 20/20 fully correct, with 0 errors and 0 truncations. Its answers and packed evidence matched previously reviewed answers; semantic citation support is marked unavailable because those earlier reviews predated that rubric field. The extra topic does not match any original-suite question.

Review: Codex, AI-assisted manual. Reused prior frozen-rubric grades only for byte-identical answers and complete packed evidence; manually checked the changed h24/h25 answers against frozen rule excerpts. No independent human judge.
