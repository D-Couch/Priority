# Prototype retrieval priority findings

## Problem

The pre-change n04 answer asserted that a prototyped card kept its alternative power and toughness in the graveyard. The supplied context included the Prototype keyword definition and broad rules about static abilities, but omitted the governing Prototype Cards rules CR 718.3 and CR 718.4. This was a retrieval/packing failure that led to an unsupported answer.

## Change and result

The lexical topic map now prioritizes CR 718.3 and CR 718.4 when a question refers to prototype cards. The rule text itself is unchanged. Tests cover two differently phrased zone-characteristics questions and require both rules in the retrieved evidence.

On the frozen novel-v1 suite, the reviewed score improved from 19/20 to 20/20 and expected-evidence recall improved from 82.5% to 87.5%. The n04 evidence recall moved from 0% to 100%, and its answer changed to the supported ruling citing CR 718.4. Unsupported answers fell from one to zero. There were no request errors or truncated answers in either run. Median latency measured 6.36s before and 5.95s after; p95 moved from 9.85s to 8.11s.

The 20-case gameplay suite remained 20/20 with identical answers and evidence. The 32-case held-out suite remained 30/32 with identical answers and evidence; median latency measured 7.22s before and 7.51s after, a 0.29s single-run increase. Timing differences from one run are descriptive and may reflect normal local runtime variation.

The response contract already instructs the model to identify missing evidence rather than guess. No prompt wording change was made because the observed failure came from omission of directly applicable rules; supplying those rules corrected the answer.

## Review limits

The benchmark scenarios and answer reviews are AI-authored or AI-assisted and have not been validated by an independent Magic judge. These single-seed results are development checks, not an accuracy claim for unseen questions.
