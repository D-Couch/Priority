# General rules questions v1

This one-case frozen suite checks the assistant's behavior on conceptual questions about paper play. It must give a useful general answer without requiring card identity or a particular game state, while separating general advice from exact-card exceptions. Its random-selection case also checks legal-target handling and physical randomization guidance.

The expected answer, criteria, and reference passages are fixed before inference. The case and rubric are AI-authored and have not been independently reviewed by a Magic judge. Treat the result as a behavioral regression check, not an accuracy estimate.

Run it with the same locally served model as other full benchmarks:

```bash
.venv/bin/python benchmark.py validate --suite benchmarks/general-questions-v1/scenarios.json
.venv/bin/python benchmark.py run --suite benchmarks/general-questions-v1/scenarios.json --label general-questions-v1 --output benchmarks/results/general-questions-v1
```

The tournament-rule excerpt is a concise paraphrase of the official February 27, 2026 Magic Tournament Rules, section 3.9. It applies to die-roll game actions in tournaments; it does not claim that tournament policy defines every casual random-selection procedure.
