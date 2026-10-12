# novel-v1 additional evaluation protocol

This 20-case set covers mechanics and interactions absent from the original gameplay-v1 and heldout-v1 case IDs. The scenarios, expected answers, criteria, and rule excerpts were written and frozen before the first inference run. No labels are sent to the answering model. The source is the project’s frozen Comprehensive Rules snapshot 20260925.

The cases and rubrics are AI-authored. They are not independently validated by a human Magic judge, so this is an exploratory evaluation, not a certified accuracy estimate. Before using the results to claim general accuracy or change defaults, have an independent judge review each scenario, expected ruling, rubric criterion, and reference excerpt. Preserve this first run and any corrections as append-only addenda; do not silently edit frozen labels.

Run with the frozen corpus and record model, seed, generation settings, retrieval mode, request errors, truncations, evidence recall, citation support, and reviewed rubric results. Keep this suite separate from regression tuning. Any change prompted by its answers converts it into regression data; create another untouched suite before making broader performance claims.

First baseline: [novel-v1-baseline](../results/novel-v1-baseline/report.md), seed 42. It scored 17/20 fully correct (85%), had one request error, and retrieved 82.5% of expected evidence groups. The n03 reference-label addendum is recorded separately. These are AI-assisted exploratory grades pending independent Magic judge validation.
