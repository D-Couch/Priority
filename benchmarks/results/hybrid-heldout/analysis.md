# First hybrid vector experiment: failed adoption gate

This run used the frozen 20260925 rules (3,312 rules, 3,353 embedded chunks; 13.8 MB SQLite index) with local Nomic Embed Text v1.5 Q4_K_M, RRF k=60, top 24 semantic candidates and a 64-rule retrieval cap. Model settings, corpus, seeds, prompts, and suites matched the lexical reference runs.

Held-out accuracy rose from 25/32 to 29/32, evidence recall from 75.5% to 81.0%, and citation-support failures fell from 10 to 6. Median latency rose 4.1% (10.26→10.69s); p95 improved slightly (18.79→18.44s). The original suite regressed from 20/20 to 19/20, evidence recall 96.2%→93.8%, and one unsupported ruling appeared. Combined correctness is 48/52 compared with 45/52 for the lexical reference.

The vector run produced a serious new h07 error: it retrieved CR 704.5g but not adjacent CR 704.5f, then claimed a 0/0 creature with indestructible survives because no damage is marked. Zero toughness independently puts it into the graveyard under CR 704.5f. This violates the predeclared “no new unsupported answers” gate. The first hybrid configuration is therefore rejected as a default despite its held-out gain. It remains optional while one retrieval correction is tested.

Other gains included retrieving 800.4a for the control-change case and 903.10a for the Commander-damage case. h25 still abstained because its leaving-player rule did not make the final context. h23 correctly distinguished damage marked on toughness from remaining toughness. Full answers, candidate and final sources, per-case grades, and comparisons are in this directory.
