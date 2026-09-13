# Merging of consecutive integers for the maps (qx+r)/2: data and two theorems

*(zootheorem, paper 02 — 2026-08-09; scope corrected 2026-09-13)*

## Definition

For odd `q, r`, let `T_{q,r}(x) = x/2` (x even), `(qx+r)/2` (x odd).
Define `a_{q,r}(n)` exactly as in paper 01: residues `r₀ ∈ [0, 2^n)`
with `T^n(r₀) = T^n(r₀+1)` and equal odd-step counts.

Two remarks make this well-defined and interesting beyond Collatz:

1. **No convergence is assumed anywhere.** Merging at the same step
   index with equal odd count is a finite event, decidable per residue
   class (Terras' argument only uses the parity structure, which holds
   for every odd `q, r`). So `a_{5,1}` is well-defined even though
   `5x+1` trajectories are believed to diverge.
2. The count is again class-exact: each counted class contains
   infinitely many merging pairs.

## Data (exact finite counts)

`a_{5,1}(n)`, `n = 1…22` (first nonzero at `n = 11`):

```
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 11, 28, 70, 161, 370, 835, 1840,
4021, 8621, 18401
```

`a_{7,1}(n)`, `n = 1…22`:

```
0, 0, 0, 1, 2, 5, 11, 23, 48, 99, 203, 413, 838, 1694, 3419, 6881,
13843, 27811, 55818, 111980, 224511, 449933
```

Densities at `n = 22`: `q = 3`: **0.409** (rising) · `q = 7`:
**0.107** · `q = 5`: **0.0044** (rounded finite-level ratios). These
sequences are [A398794](https://oeis.org/A398794) and
[A398795](https://oeis.org/A398795). Terms `n ≤ 18` are
re-verified by brute force in `verify/verify_q_family.py`; terms
19–22 come from an exact class computation that matches the brute
force on the whole common range.

And `a_{3,-1}(n) = a_{3,1}(n)` for all `n` — the mirror theorem of
paper 01, which holds at the level of the counted sets.

## Theorem 1 (criticality; proved for shared steps)

Consider a pair `(x, x+d)` evolving under `T_{q,1}`. On a step where
both elements have the same parity ("shared step") the difference `d`
transforms exactly:

- both even: `d → d/2`;
- both odd: `d → q·d/2`.

Condition on a fixed finite parity history for which the next step
is shared. The next unused Terras bit is fair under the uniform
residue-class law (or its Haar limit), so the multiplier `m` is a coin on
`{1/2, q/2}` and

> **E[m] = (1+q)/4, which equals 1 exactly when q = 3.**

Here “critical” refers only to the first moment E[m]=1. For positive
odd q>=5, `E[log_2 m]=(log_2 q-2)/2>0`; for q=3 it is negative.
The logarithmic statement requires q>0. These are shared-step
identities under the declared law, not conclusions about the limiting
merging densities or about conditioning on future survival. Among
positive odd q>=3, only q=3 has a positive fractional-moment window;
q=1 also has such a window and is outside that restricted claim.

## Theorem 2 (obstruction; proved)

> Let `p` be an odd prime with `p | r` and `p ∤ q`. Then **no pair of
> consecutive integers ever merges with equal odd count** under
> `T_{q,r}`: `a_{q,r}(n) = 0` for all `n`.

*Proof.* Modulo `p`, since `p | r`, the map acts multiplicatively:
`T(x) ≡ 2⁻¹·x` (x even) or `2⁻¹·q·x` (x odd). Hence after `t` steps
with `s` odd ones, `x_t ≡ 2⁻ᵗ qˢ · x₀ (mod p)`. If two trajectories
merge at the same index `t` with equal odd counts `s`, the accumulated
units are equal, so `x_t = y_t` forces `x₀ ≡ y₀ (mod p)` — false for
consecutive integers. ∎

Falsifiable prediction, tested: `(5x+3)/2`, `(7x+3)/2` and `(3x+5)/2`
all give `a(n) = 0` for every `n ≤ 14` by brute force
(`verify/verify_q_family.py`), as the theorem demands. Note the
theorem also covers pairs at any distance `d` with `p ∤ d`.

## References

- R. Terras, Acta Arith. 30 (1976), 241–252.
- See paper 01 for the Collatz-case references and the mirror theorem.
