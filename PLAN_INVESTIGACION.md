# Current plan — 2026-09-17

**Target:** `phi=lim a(n)/2^n=1`, where a(n) counts balanced merging
classes by step n for T=A014682. For their union F,
`lower natural density(F)>=phi`. Equality of those limits needs another
argument; finite equal heights additionally require convergence and
control of first arrival at 1. This is not a proof of Collatz.

## Work queue

| Step | Status and completion criterion |
|---|---|
| P0: coherence | Repository corrections and verifiers completed; four OEIS corrections prepared, pending an edit slot |
| **P1: full clock, next** | Add k=0,1 boundary segments to the interior excursion bound; specify entrance, exit and restart times and prove a global bound |
| P2: exit window | For `u_tau=Pi_tau*u0+W_tau`, u0=c/9, prove `P(abs(W_tau)<=M given tau>T(c))>=p>0` uniformly on a declared domain, with fixed M and declared logarithmic horizon; or exhibit a family refuting uniformity |
| P3: absorption | Control actual starts and prove divergence of conditional success probabilities; justify strong Markov and conditional Borel–Cantelli without circularity |
| P4: publish | Update both plans and the laboratory registry when a piece closes or fails |

The laboratory has a written bound
`P_(2,c)(tau>t)<=C sqrt(log(t+2)/(t+1))`, uniform in integer c;
tau is first arrival at k=1, not fusion. Boundary times remain open.
The product Pi is controlled; W at exit is not. Fixed-time moments
and a forward harmonic change of law do not settle this conditioning.
Erizas excludes uniform contraction over all scales and late times;
local review 12's suggested O(n) clock is not adopted as a theorem.

Detailed proofs and next action live in the separate laboratory's
`ESTADO_INVESTIGACION.md` and `depuracion/coherencia20260913/Matematica.md`,
§3–4. Do not load its historical summaries to start. P2 experiments must
separate survival, exit and censoring, and include signed and adversarial starts.

## Publication handoff

A398792–A398795 are published. A399819–A399821 were checked **proposed**
after the 17-09 afternoon replies to Howroyd and Marcus, revisions
#12, #13, #11. Direct titles, local definitions and article links were
added; data, offsets, examples and programs were preserved. Approval is
pending. [Analysis and delivery](drafts/REVISION_20260917_TARDE.md).
[Corrections to the four published entries](drafts/CORRECCIONES_PUBLICADAS_20260917.md)
are prepared but unsubmitted: OEIS refused to open A398792 because the
account has three active edits. They concern density qualifications,
the ratio argument, the Conejas meeting value and the shared-step law.
Submit when a slot becomes available; no pending draft was withdrawn.
OEIS acceptance does not establish the asymptotic argument.

Keep this plan short: replace outdated status and link detailed work.
The [previous full plan](archivo/contexto_20260913/PLAN_INVESTIGACION.md.txt)
is preserved for lookup. Both repos matched origin/main at session start.
The user requested commit and push to close this review. Future OEIS work
uses [the documented submission procedure](drafts/PROCEDIMIENTO_OEIS.md).
