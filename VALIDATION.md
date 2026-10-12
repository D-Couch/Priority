# Validation

Validated against the local LM Studio endpoint and model `qwen/qwen3.8-27b` on October 11, 2026 (America/Chicago).

- Six Python parser/retrieval regression tests passed.
- HTTP checks passed for the homepage, rule lookup, invalid messages, external Host/Origin rejection, and keeping the knowledge database outside the static file root.
- Chromium desktop (1440 × 1000) and mobile (390 × 844) checks passed. Tested card search, attachment, removal, source panels, conversation storage/reload, and navigation. No JavaScript errors or horizontal mobile overflow. A mocked streaming response was used to exercise frontend citation and persistence behavior; real model calls were tested separately.
- Three real model responses were manually checked against retrieved official rules. All gave the expected ruling with recognized citations and no citation warnings:
  - Responding to tapping a basic Forest for mana: no; cites 605.3b. About 34 seconds.
  - Commander dying, then moving to the command zone: allowed as a state-based action; dies triggers still occur. Cites 903.9a and 700.4. About 29 seconds.
  - A 6/6 trampler blocked by an undamaged 2/2 with indestructible: may assign 2 to the blocker and 4 to the defending player. Cites 702.19b and 702.12b. About 31 seconds.

This small smoke test is not a general ruling-accuracy benchmark. Citation checks detect missing/unrecognized citation IDs, not whether a cited passage logically supports every claim. Retrieval is lexical with topic expansion and can miss relevant rules in complex interactions.
