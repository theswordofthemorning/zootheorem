# zootheorem

Theorems, integer sequences and verification scripts from an ongoing
study of the pairwise dynamics of Collatz-type maps — how the
trajectories of two nearby integers merge under maps of the family

```
T(x) = x/2            if x is even
T(x) = (q*x + r)/2    if x is odd        (q, r odd; q = 3, r = 1 is Collatz)
```

This repository publishes **results** (statements, self-contained
proofs, sequence data, and independent brute-force verification
scripts). The research programme behind them is not published here.

## Contents

| path | what it is |
|---|---|
| `papers/01-merging-classes.md` | The sequences a(n), b(n): merging classes of consecutive integers under the shortcut Collatz map. Definition, the doubling theorem, the proven density lower bound 0.435658, the mirror theorem (3x−1 gives the identical sequence), and the verification provenance of every term. |
| `papers/02-generalized-maps.md` | The same count for (5x+1)/2 and (7x+1)/2 — measured for the first time — plus two theorems: the criticality E[m] = (1+q)/4 (q = 3 is the unique critical map of the family) and the obstruction theorem (if an odd prime divides r but not q, consecutive pairs never merge; verified as a falsifiable prediction on three maps). |
| `papers/03-uniform-fractional-moment-bound.md` | A self-contained lemma: uniform-in-time fractional moment bounds for critical random affine recursions (E[multiplier] = 1), with explicit constants, by subadditivity alone. |
| `seqs/` | Sequence data in b-file format (`n a(n)` per line). |
| `verify/` | Stand-alone brute-force verification scripts (Python 3, no dependencies). They recompute the sequences from the raw definition and exit with an error on any mismatch. |
| `lean/mirror_theorem.lean` | The mirror theorem (a₊(n) = a₋(n) for all n) formally proved in Lean 4, core only (no Mathlib), zero `sorry`. Comments in Spanish; the statement and proof are machine-checked. |

## How to verify

```
python verify/verify_merging_classes.py     # a(1)..a(20) by brute force
python verify/verify_q_family.py            # q = 5, 7 and the obstruction tests
lean lean/mirror_theorem.lean               # needs Lean 4 (elan); no output = proved
```

## Status of each claim

Every claim in `papers/` carries one of three labels, and the labels
are part of the text: **proved** (with the proof, or machine-checked in
Lean), **computed exactly** (integer computation, no sampling, with the
range stated), or **measured** (with the range and the estimator
stated). Nothing is extrapolated.
