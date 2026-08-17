# Merging classes of consecutive integers under the shortcut Collatz map

*(zootheorem, paper 01 — 2026-08-09)*

## Definition

Let `T` be the shortcut Collatz map (OEIS A014682, the function usually
denoted `T` in the 3x+1 literature): `T(x) = x/2` for even `x`,
`T(x) = (3x+1)/2` for odd `x`. For `n ≥ 1` and a residue
`r ∈ [0, 2^n)`, write `S_n(r)` for the number of odd iterates among
`r, T(r), …, T^{n-1}(r)`.

> **a(n)** = number of residues `r ∈ [0, 2^n)` with
> `T^n(r) = T^n(r+1)` and `S_n(r) = S_n(r+1)`.
>
> **b(n)** = `a(n+1) − 2·a(n)` (the classes that merge for the first
> time at level `n+1`).

By Terras' theorem (1976) the first `n` parities of a trajectory are
determined by the residue mod `2^n`, and
`T^n(2^n·m + r) = 3^{S_n(r)}·m + T^n(r)`. Consequently the condition
above is decided by the residue class: **for every counted class, all
pairs `(2^n·m + r, 2^n·m + r + 1)` with `m ≥ 1` merge** — their
trajectories coincide from the merge index on — and therefore have
equal Collatz height (equal total number of steps to reach 1) whenever
the common trajectory reaches 1, which is unconditionally true for all
starting values below `2^71` (Barina 2025).

**The `m ≥ 1` hypothesis is necessary.** For `m = 0` the counted
property can fail (the trajectory may reach the attractor before step
`n`); exactly three classes are exceptional (`r = 2, 4, 5`), stable
from `n = 5` to at least `n = 22`. The counts a(n) are unaffected.

## Data

`a(n)`, `n = 1 … 36` (b-file: `seqs/bfile_merging_classes_3x1.txt`):

```
0, 0, 1, 3, 8, 18, 39, 82, 170, 351, 721, 1476, 3012, 6130, 12450,
25241, 51105, 103358, 208840, 421643, 850737, 1715546, 3457791,
6966495, 14030369, 28247507, 56854178, 114400435, 230136995,
462857658, 930718308, 1871137623, 3761106610, 7558807251,
15188796435, 30516174184
```

`b(n)`, `n = 1 … 35` (b-file: `seqs/bfile_new_classes_3x1.txt`):

```
0, 1, 1, 2, 2, 3, 4, 6, 11, 19, 34, 60, 106, 190, 341, 623, 1148,
2124, 3963, 7451, 14072, 26699, 50913, 97379, 186769, 359164, 692079,
1336125, 2583668, 5002992, 9701007, 18831364, 36594031, 71181933,
138581314
```

Neither sequence is in the OEIS (checked 2026-08-09, with a Fibonacci
control query returning A000045).

## Theorems (proved)

**Doubling.** `a(n+1) ≥ 2·a(n)` for all `n`. *Proof.* If `r` is
counted at level `n`, then both `r` and `r + 2^n` are counted at level
`n+1`: by Terras' identity with `m = 1`,
`T^n(2^n + r) = 3^{S_n(r)} + T^n(r)` and likewise for `r+1`, so if the
outputs for `r, r+1` coincided they still coincide, and the parities
(hence `S`) are unchanged; and a counted `r` stays counted one level
up because its two iterates are already the same number. ∎

**Corollary (proven density bound).** `a(n)/2^n` is non-decreasing,
and every value is a proven lower bound for the lower asymptotic
density of consecutive integer pairs with equal Collatz height. At
`n = 32`: **density ≥ 0.435658**, by exact integer computation over
all `2^32` residues — no sampling. (For comparison, Gao (1993-style
counts pushed to `10^8`) *measures* a density around 0.51; the value
here is smaller but proven.)

**Mirror theorem.** Define `a₋(n)` identically for the map
`T₋(x) = x/2 / (3x−1)/2`. Then `a₋(n) = a(n)` for **all** `n`. The
reason is one line: `T₋(−x) = −T(x)` on all of ℤ, so negation
conjugates the two maps and the block reflection `r ↦ 2^n − 1 − r`
is a bijection between the two counted sets. Machine-checked proof in
`lean/mirror_theorem.lean` (Lean 4, core only, no `sorry`).
Consequence worth stating: a(n) is blind to the sign of the `±1`, so
it cannot by itself be evidence about convergence — it is a
well-defined combinatorial count, and that is all this note claims.

## Provenance of the terms

| terms | how computed | independent check |
|---|---|---|
| `a(1)…a(20)` | brute force over all pairs | re-verified by `verify/verify_merging_classes.py` (this repo) |
| `a(3)…a(32)` | exact sweep over residue classes | second, independently written parallel sweep; identical |
| `a(33)…a(36)` | exact coalesced-state computation | an exact integer identity with independently computed summands; identical |

All computations are integer-exact; no floating point is involved in
any counted quantity.

## References

- R. Terras, *A stopping time problem on the positive integers*, Acta
  Arith. 30 (1976), 241–252.
- L. E. Garner, *On heights in the Collatz 3n+1 problem*, Discrete
  Math. 55 (1985), 57–64. (The class `r = 4 mod 8` here is Garner's
  pair `(8k+4, 8k+5)`.)
- G.-G. Gao, *On consecutive numbers of the same height in the Collatz
  problem*, Discrete Math. 112 (1993), 261–267. (The lifting lemma
  behind the doubling theorem.)
- Wu Jia-Bang and Huang Guo-Lin, *Family of consecutive integer pairs
  of the same height in the Collatz conjecture*, Mathematica Applicata
  (Wuhan) 14 (2001), suppl., 21–25. MR 1885838. (The class
  `r = 5 mod 32` here is their family `(32m+5, 32m+6)`.)
- M. Elia and C. Tucker, INTEGERS 15 (2015), #A54.
- D. Barina, *Convergence verification of the Collatz problem*,
  J. Supercomputing (2025). (Source of the `2^71` bound.)
- Related OEIS entries: A014682 (the map `T` itself), A076227
  (surviving Collatz residues mod 2^n), A006877, A100982.
