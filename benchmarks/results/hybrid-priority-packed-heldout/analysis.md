# Lexical-preserving hybrid: held-out result

At seed 42, this 32-case run scored 28/32 fully correct versus 25/32 lexical (+3 cases). Mean expected-evidence recall was unchanged at 75.5%; median latency was 10.96 s versus 10.91 s (+0.4%), p95 19.42 s versus 21.88 s. All requests completed without truncation. One answer had an unsupported claim versus five in lexical, and there were no new unsupported cases. The tapped-blocker evidence was absent in both this run and the lexical baseline, so its 0/3 evidence score is not a regression.

The new held-out run still abstains on h25 and h26 because CR 800.4a and CR 903.10a are missing from packed context, and it repeats the known casting-step error in h13. The three accuracy gains were h07 infect/lifelink, h20 summoning-sickness/crew, and h23 fight/double-strike. This is a single seeded measurement, so the protocol requires replication on both suites at seed 43 before changing the default.

Review was AI-assisted and not independently checked by a human judge. Full per-answer results and source passages are retained in `run.json` and `review.json`.
