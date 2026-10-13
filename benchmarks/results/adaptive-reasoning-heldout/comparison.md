# Adaptive reasoning held-out quality check

The adaptive run scored **29/32** after review, with 0 request errors. The prior reviewed low-effort run scored 29/32 and the prior off-effort run scored 26/32.

This is a **quality check, not a direct latency comparison**. The adaptive run used parallel=1, while both historical effort runs used parallel=4 (low) and parallel=4 (off); the implementation and runtime telemetry also differ. The adaptive run’s median (4.26s) and p95 (12.33s) are recorded in its report but are not attributed as improvements against those historical timings.

Rubric labels are AI-assisted and the suite is a frozen development set, not independent judge validation.
