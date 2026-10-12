# Citation presentation correction

The verified seed-42 original-suite answer 16 used `Rule 510.1c` and `(702.19d)` instead of bracketed citations. The frontend now links those rule numbers when the exact source ID is supplied with the answer. Existing bracketed references remain unchanged; unknown numbers are never promoted to verified sources. Stored answers and model prompts are unchanged, so this does not improve semantic evidence support or alter benchmark grades.

Validation: `node test_citations.mjs` covers the historical failure, existing citations, unknown sources and number-boundary collisions. No additional inference run is needed for this presentation-only change. CI also validates the new frozen suite.
