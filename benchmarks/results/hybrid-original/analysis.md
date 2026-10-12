# First hybrid vector experiment: original-suite regression

Hybrid scored 19/20 correct and complete compared with 20/20 for lexical retrieval. The only regression is h07: it claims a 0/0 indestructible creature survives if no damage is marked. This is false because the separate zero-toughness state-based action puts it into its owner's graveyard (CR 704.5f). The vector run retrieved CR 704.5g instead and omitted adjacent CR 704.5f, creating a new unsupported answer.

Mean evidence recall fell from 96.2% to 93.8%; median latency increased 3.5% and p95 increased 11.3%, within the protocol's 20% latency bound. Full answers and the review are retained here. The no-new-unsupported-answer gate fails, so this configuration is not enabled by default.
