# Casting-sequence rule retrieval

Implementation under test: `7c10de4` (`fix: retrieve spell casting cost sequence rules`). Questions that mention an additional casting cost now prioritize CR 601.2a, 601.2h, 601.2i, 117.2e, and 117.3c. A frozen-corpus check confirmed all five survive the actual LM Studio context packer for h13.

The h13 answer now correctly distinguishes putting the spell on the stack at the start of casting from paying its costs before the spell becomes cast. It explains that no opponent receives priority between cost payment and completion, and its citations are supported by packed rules and the Fling ruling. h13 improved from partial to fully correct versus `leave-game-phrase-heldout`.

The full seed-42 held-out run scored 27/32 fully correct, compared with 26/32 in the preceding lexical retrieval run. Unsupported-claim answers fell 4→3. Expected evidence recall rose 78.6%→79.7%; median latency was 10.40 s and p95 17.38 s. These single runs are descriptive; only the h13 transition is directly attributed to this retrieval change. There were no request errors or truncations.

Review: Codex, AI-assisted manual against the frozen criteria and excerpts. The h13 answer and its five packed rules were checked directly. Other rubric grades were checked against current wording; no independent human judge.
