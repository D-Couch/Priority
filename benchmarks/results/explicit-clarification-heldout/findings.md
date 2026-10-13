# Clarification-contract experiment findings

## Hypothesis

Two held-out questions omitted details that could change the ruling. The prior response contract told the model to ask for missing facts, but the model still assumed a blocked attacker lacked trample and treated an unspecified copy effect as ordinary copying. The experiment made the uncertainty policy explicit: unspecified characteristics and abilities are unknown, not absent, and no provisional ruling should be given when they could change the outcome.

## Result and decision

The change did not fix either target case. The model still gave definitive answers to h30 and h31 instead of asking clarifying questions. It also added an unsupported destination speculation to h25. Reviewed accuracy fell from 30/32 to 29/32, unsupported answers increased from two to three, citation-support failures increased from zero to one, and p95 latency increased from 12.17s to 14.04s. Median latency changed from 7.48s to 7.42s.

The answer-contract change failed the quality gate and was reverted. The answer-contract hash comparison and tests remain in the benchmark harness so future prompt experiments are explicitly declared and reproducible.

## Next investigation

The failure suggests that another broad instruction is not enough. A focused next experiment should detect missing card identities and answer-relevant abilities before generation, or add a separate answer-validation step that rejects an unconditional ruling when the question leaves a decisive characteristic unspecified. It should include positive controls where the user gives enough detail, and compare quality and latency before any default change.

## Review limits

The suite and review are AI-authored or AI-assisted and have not been validated by an independent Magic judge. This single-seed result is descriptive.
