# Merging of consecutive integers for the maps (qx+r)/2: first data and two theorems

*(zootheorem, paper 02 — 2026-08-09)*

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

## Data (first computation of these counts, to our knowledge)

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
**0.107** (nearly flat) · `q = 5`: **0.0044**. Neither sequence is in
the OEIS (checked 2026-08-09 with control). Terms `n ≤ 18` are
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

By Terras uniformity the two cases are equidistributed over residue
classes, so the shared-step multiplier `m` is a fair coin on
`{1/2, q/2}` and

> **E[m] = (1+q)/4, which equals 1 exactly when q = 3.**

Among all maps `(qx+1)/2` the Collatz map is the unique critical one:
for `q ≥ 5`, `E[log₂ m] = (log₂ q − 2)/2 > 0` and the difference
dynamics is supercritical in log — consistent with the collapse of the
measured merging densities above (0.409 vs 0.107 vs 0.0044). The
interpretation of the collapse is supported by the data; the displayed
expectation is an exact statement about shared steps.

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
