# Casting-order response-contract check

Implementation under test: `f4b8711` (`fix: clarify casting order in rulings`). The shared response contract states that a spell goes onto the stack at 601.2a, costs are paid while it is there at 601.2h, it becomes cast at 601.2i, and players receive no priority during casting.

The seed-42 held-out run scored 25/32 fully correct, compared with 27/32 on the preceding retrieval-only run. Unsupported-claim answers increased 3→5; expected evidence recall was 78.1%, median latency 10.74 s, and p95 17.20 s. h13 remained fully correct with all five relevant casting/priority rules supplied. h01 regressed with an incorrect “put on the stack at the same time” claim, and h30 failed to ask for missing combat details. Because this is a single stochastic run, the aggregate does not establish the contract caused those regressions; it does not show an aggregate improvement either.

The original gameplay-v1 suite remained 20/20 fully correct, with no request errors or truncations. Separately, a two-turn chat through a fresh server running this commit returned complete streams, no warnings, and consistent h13 rulings: the first answer correctly said there is no response window; the follow-up explicitly said Fling is put on the stack before the sacrifice cost is paid. Both answers supplied the relevant CR 601.2 and priority sources.

Review: Codex, AI-assisted manual against frozen rubrics and excerpts; no independent human judge. Semantic citation support is marked unavailable where not directly rechecked.
