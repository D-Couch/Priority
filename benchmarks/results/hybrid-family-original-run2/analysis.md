# Candidate-family expansion: original-suite result

The 20-case run completed all requests at seed 42: 19/20 fully correct, versus 19/20 for the prior RRF hybrid and 20/20 for the lexical baseline. Expected-evidence recall was 89.6%, median latency 11.73 s, and p95 17.70 s. There were no request errors or truncated outputs, but the unsupported 0/0 ruling remains. This fails the no-new-unsupported-answer gate.

Although CR 704.5f exists in the full 96-rule retrieval candidate list, context packing omits it. CR 704.5g is packed and the model repeats the earlier incorrect conclusion that a 0/0 creature survives. The lexical retrieval set contains CR 704.5f. The next controlled implementation will preserve every lexical rule candidate and append vector-only candidates after it, rather than combining the lists with reciprocal-rank fusion.

Reviews are AI-assisted and not independent human rulings. See both comparison reports for case-level outcomes.
