# Lexical-preserving candidate order: held-out result

At seed 42 this intermediate candidate-only implementation scored 27/32 fully correct against the lexical baseline's 25/32. It improved expected evidence recall from 75.5% to 78.6%, with median latency 10.65 s and p95 19.58 s. There were no request failures or truncation.

The run kept CR 903.10a in packed context, allowing a correct ruling on h26. However, it repeated the false marked-damage detail on h23, and the ambiguity case h30 answered conditionally rather than asking the frozen required clarification. h25 abstained because CR 800.4a remained absent. Subsequent work prioritized lexical rules during context packing; see the later matched two-suite results for the adoption decision. Review was AI-assisted, not independent human evaluation.
