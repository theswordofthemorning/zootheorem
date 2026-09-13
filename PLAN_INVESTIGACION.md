# Current plan — 2026-09-13

**Target:** `phi=lim a(n)/2^n=1`, where a(n) counts balanced merging
classes by step n for T=A014682. For their union F,
`lower natural density(F)>=phi`. Equality of those limits needs another
argument; finite equal heights additionally require convergence and
control of first arrival at 1. This is not a proof of Collatz.

## Work queue

| Step | Status and completion criterion |
|---|---|
| P0: coherence | Local corrections and verifiers completed; remote publication pending |
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

A398792–A398795 are published. A399819–A399821 were last observed
**proposed** after resubmission on 13-09; approval remains unconfirmed.
Local text, offsets, ranges and the prepared but unposted A398792
clarification: [revision note](drafts/REVISION_20260913.md).
OEIS acceptance does not establish the asymptotic argument.

Keep this plan short: replace outdated status and link detailed work.
The [previous full plan](archivo/contexto_20260913/PLAN_INVESTIGACION.md.txt)
is preserved for lookup. Current changes are local, without commit/push.
