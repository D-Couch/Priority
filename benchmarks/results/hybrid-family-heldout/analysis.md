# Candidate-family expansion: held-out result

The 32-case run completed all requests at seed 42: 28/32 fully correct, versus 29/32 for the prior RRF hybrid and 25/32 for the lexical held-out baseline. Expected-evidence recall was 77.9%, median latency 11.11 s, and p95 20.92 s. There were no request errors or truncated outputs; three answers contained unsupported claims. The run is therefore not adopted.

The result exposed two retrieval failures. First, the 0/0 rules exception CR 704.5f was absent from the candidate list because earlier sibling expansions consumed the 32-rule expansion allowance before CR 704.5g was processed. Second, the expanded candidate list altered context packing enough that the fight/double-strike case incorrectly treated a fight as two combat-damage steps. This is one case fewer fully correct than the prior hybrid run. The implementation kept the original 64 primary candidates in candidate metadata, but the prompt packer still gave the appended expansion rules context ahead of later primary rules because it groups excerpts by rule section.

Reviews are AI-assisted and not independent human rulings. Every case and source list was inspected; the frozen corpus and rubric were unchanged. See `from-hybrid64.md` and `from-lexical.md` for per-case comparisons.
