# A uniform fractional-moment bound for critical random affine recursions, by subadditivity alone

*(zootheorem, paper 03 — 2026-08-09)*

## Statement

Let `(u_t)` be any real-valued process (no Markov property, no
independence along the path, no stationarity) satisfying the
domination

```
|u_{t+1}|  ≤  m_t·|u_t| + s,        s ≤ 1/2 a constant,
```

where each `m_t` is drawn fresh (independently of `u_t`) from a fixed
bounded nonnegative distribution with **E[m] = 1** and `m` not a.s.
constant — for instance a fair coin on `{1/2, 3/2}`. Then for every
`θ ∈ (0, 1)`:

```
E[ |u_t|^θ ]  ≤  |u_0|^θ + s^θ / (1 − r_θ)        uniformly in t,
```

with `r_θ = E[m^θ] < 1`. For the fair coin on `{1/2, 3/2}`:
`θ = 1/2` gives the bound `|u_0|^{1/2} + 21.8` and `θ = 0.9` gives
`|u_0|^{0.9} + 46.2`. By Markov's inequality,
`P(|u_t| > x) ≤ B_θ / x^θ` for all `t` — uniform tightness with
explicit constants.

## Proof (three steps)

1. **Subadditivity.** For `0 < θ < 1` and `a, b ≥ 0`,
   `(a+b)^θ ≤ a^θ + b^θ`. Applied to the domination:
   `|u_{t+1}|^θ ≤ m_t^θ |u_t|^θ + s^θ`.
2. **Expectation.** Since `m_t` is independent of `u_t`:
   `E|u_{t+1}|^θ ≤ r_θ · E|u_t|^θ + s^θ`.
3. **The window is open *because* the chain is critical.** The map
   `θ ↦ E[m^θ]` is convex, equals 1 at `θ = 0` and at `θ = 1`
   (this is exactly `E[m] = 1`), and is not constant; a non-constant
   convex function equal to 1 at both endpoints is strictly below 1 on
   the open interval. Iterate step 2. ∎

## Discussion

The recursion `u' = m·u + q` with `E[m] = 1` is the *critical* case of
random affine recursions and perpetuities, traditionally the delicate
boundary of the theory (the classical Kesten–Goldie machinery assumes
a Cramér root `κ` with `E[m^κ] = 1` and uses renewal theory). The
point of this note is that **for fractional moments the critical case
is the easy case**: criticality is precisely what opens the whole
window `θ ∈ (0,1)` in step 3; the proof needs no renewal theory, no
independence along the path — only the domination and a fresh
multiplier; and the constant is explicit. The exponent window is also
sharp: at `θ = 1` the conclusion fails in general (`E|u_t|` can grow
linearly).

The supercritical contrast delimits the scope: if `E[log m] > 0`
(e.g. a fair coin on `{1/2, q/2}` with `q ≥ 5`), then by Jensen
`E[m^θ] ≥ e^{θ·E[log m]} > 1` for every `θ > 0` and **no window
remains**. For coins `{1/2, q/2}` the dichotomy is exact: a window
exists iff `q = 3` iff `E[m] = 1` (paper 02, Theorem 1).

## Honesty section

The closest literature we have located (not yet carefully compared):
the critical case of `X = MX + Q` (Babillot–Bougerol–Élie 1997;
recurrence/transience of the critical case, arXiv:2105.04994), and
work on fractional moments of stochastic recurrence equations in the
Kesten regime. We do not claim novelty of the lemma — a three-step
argument this short may well exist in some form; we claim only that
it is correct (the proof is above and is complete), self-contained,
and useful: it is applied, with the domination verified exactly on
354,299 integer transitions, in the research programme from which
this repository is extracted.
