# Afternoon editorial follow-up — 2026-09-17

The live review covered all seven entries and both repositories. Four
entries are published; A399819–A399821 remain proposed. Michel Marcus
requested article links on A399820 at 17:30–17:32 EDT; Andrew Howroyd
requested explicit definitions of the local terminology on A399819 at
18:47–18:49 EDT. These requests do not dispute the numerical counts.

The three pending entries now have direct counting definitions in their
titles, explicit definitions of the two local phrases, and input indices
0..n-1 distinguished from iteration numbers 1..n. Gao and Terras are linked
in all three; A399819 also links Garner and Elia–Tucker. Marcus's addition
was retained. Data, offsets, examples and programs were preserved.

| Entry | Reply and resubmission, EDT | Final revision | Checked state |
|---|---|---|---|
| A399819 | 20:10 | #12 | proposed |
| A399820 | 20:11 | #13 | proposed |
| A399821 | 20:08 | #11 | proposed |

The laboratory preserves the replies, browser captures, analysis and
checks in `depuracion/oeis20260917/ANALISIS_TARDE.md`. The local draft files
match the final server texts, with DATA wrapping normalized for the parser.
The bounded direct/symbolic check through 13 passed, as did preservation
checks against all seven live entries and the stored b-files. For q=5,7,
the local range is through 22; Irvine's public extensions go through 29.

The review also found older published assertions requiring correction:
the convergence qualification in A398792, an unsupported ratio/density
equivalence and an incorrect meeting value in A398793, and the probability
law and conditioning in A398794–A398795. These are our audit findings,
not claims made by the editors this afternoon.

[Exact prepared corrections](CORRECCIONES_PUBLICADAS_20260917.md) remain
unsubmitted: opening A398792 for editing returned the site's active-edit
limit. Marcus was told this in the reply. No existing draft was withdrawn.
The Conejas meeting value was checked with integer iteration and Lean
4.32.2, with no sorryAx. The laboratory registry and generated database
now distinguish that terminal value from the preceding ternary repunit.
The paper bibliography corrects Barina's 2025 title and Tucker's initial.

At session start both repos matched origin/main; earlier same-day work had
already been committed externally. This session's local changes have not
been committed or pushed. P1–P3 remain open. Editorial follow-up is to
respond to new comments and submit the prepared corrections when a slot
becomes available.

After this report the user requested commit and push in both repositories,
plus documentation of resubmission. The [operating procedure](PROCEDIMIENTO_OEIS.md)
records the successful flow and the Chrome UIA issues encountered.
