# zootheorem

Results on balanced merging of consecutive integers for
`T(x)=x/2` (even), `(qx+r)/2` (odd), with q,r odd.
Collatz uses q=3,r=1, OEIS A014682.

**Start with [PLAN_INVESTIGACION.md](PLAN_INVESTIGACION.md).**
Read only the paper or verifier needed for the task; do not preload
submission history or the companion laboratory's archives.

| Content | Location |
|---|---|
| Merging counts, doubling, density bound, mirror | [Paper 01](papers/01-merging-classes.md) |
| q=5,7 counts and prime obstruction | [Paper 02](papers/02-generalized-maps.md) |
| Fractional moments under explicit hypotheses | [Paper 03](papers/03-uniform-fractional-moment-bound.md) |
| Integer data | `seqs/` |
| Current OEIS checklist and history lookup | [drafts/ARSENAL.md](drafts/ARSENAL.md) |

```text
python verify/verify_merging_classes.py   # direct through n=20
python verify/verify_q_family.py         # q=5,7 through 18; obstruction through 14
python verify/verify_strata.py           # e8,e10,e12 through 20
python verify/verify_consistency.py      # stored lists and constants
lean lean/mirror_theorem.lean            # formal mirror theorem
```

Python verifiers need only the standard library. Run checks relevant
to the change; documentation edits do not require fresh large sweeps.
Distinguish written/formal proofs, exact finite counts and measurements.
Balanced merging alone does not prove convergence or equal finite heights.
The [previous README](archivo/contexto_20260913/README.md.txt) is preserved.
