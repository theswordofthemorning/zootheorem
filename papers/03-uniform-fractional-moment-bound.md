# A uniform fractional-moment bound when the mean multiplier is one

*(zootheorem, paper 03 — 2026-08-09; hypotheses corrected 2026-09-13)*

## Statement

Let `(u_t)` start at a deterministic real u_0 (no Markov property, no
independence along the path, no stationarity) satisfying the
domination

```
|u_{t+1}|  ≤  m_t·|u_t| + s,        0 ≤ s ≤ 1/2 a constant,
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
3. **Strict Jensen inequality.** Since x -> x^theta is strictly
   concave on the nonnegative reals and m is not almost surely constant,
   `r_theta=E[m^theta] < (E[m])^theta=1`. Iteration gives
   `E|u_t|^theta <= r_theta^t |u_0|^theta + s^theta*(1-r_theta^t)/(1-r_theta)`.
   This implies the stated bound. The argument includes distributions
   with an atom at zero. ∎

For a random initial value with finite theta moment, replace
`|u_0|^theta` on the right by `E|u_0|^theta`.

## Discussion and scope

For the coin {1/2,3/2}, E[m]=1 but
`E[log m]=(1/2)log(3/4)<0`. This is different from the logarithmically
critical case E[log m]=0 studied in the Babillot–Bougerol–Élie setting;
see [Brofferio, Buraczewski and Damek](https://arxiv.org/abs/0809.1864).
No novelty or stationary-tail theorem is claimed here.

The two numerical constants above are loose upper bounds for
`s^theta/(1-r_theta)` at s=1/2 (approximately 20.752 and 45.192).
At theta=1 no uniform first-moment bound holds in general: in the
nonnegative affine recursion with additive term s>0 the expectation
can grow linearly.

If E[log m]>0, Jensen gives E[m^theta]>=exp(theta E[log m])>1 for
all theta>0. For coins {1/2,q/2} with positive odd q>=3, a fractional
window exists exactly for q=3. If q=1 is admitted, it too has a window.

The lemma concerns deterministic times under its specified law.
Applying it at an exit time, after survival conditioning, or to a
reversed excursion requires a separate argument. The laboratory's
354,299-transition check is finite evidence for the application, not
a proof of the domination on every integer state. See the
[current research plan](../PLAN_INVESTIGACION.md) for those obligations.
