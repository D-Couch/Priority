# Response-contract experiment: rejected

Implementation under test: `3f38dd4` (`fix: omit unrelated card outcomes from rulings`). The response contract prohibited unasked follow-on effects and numerical outcomes. The seed-42 run scored 24/32 fully correct, compared with 26/32 in the immediately preceding reviewed retrieval run. Unsupported-claim answers increased 4→6. The h13 answer still incorrectly placed cost payment before the spell is on the stack; CR 601.2a and 601.2h were not packed. h23 added an incorrect damage-mark total, and h25 misrepresented the Bribery example in CR 800.4a. The experiment did not resolve the diagnosed failures and was rejected.

The original suite remained 20/20 fully correct. Both full runs had zero request errors and zero truncations. These single seeded runs are descriptive; h25 and h13 remain the main targeted cases.

Review: Codex, AI-assisted manual; prior criterion grades reused only where the same ruling remained. Newly incorrect h01/h13/h23/h25 details were individually checked against the frozen rule excerpts. No independent human judge.
