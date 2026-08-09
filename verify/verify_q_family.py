# verify_q_family.py
#
# Independent brute-force computation of the merging-class sequences
# for the generalized maps T_q(x) = x/2 (x even), (q*x+1)/2 (x odd),
# for q = 5 and q = 7. Same definition as verify_merging_classes.py
# with 3 replaced by q. Note that convergence of trajectories is NOT
# assumed anywhere: merging at the same step index with equal odd
# count is a finite, class-decidable event even for maps (like 5x+1)
# whose trajectories are believed to diverge.
#
# Checks the stored terms (computed by an independent method) against
# direct simulation for n <= N_DIRECT. SystemExit on any mismatch.

N_DIRECT = 18

A5_TERMS = [
    # n = 1 .. 22   (first nonzero term at n = 11)
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 3, 11, 28, 70, 161, 370, 835, 1840, 4021, 8621, 18401,
]
A7_TERMS = [
    # n = 1 .. 22
    0, 0, 0, 1, 2, 5, 11, 23, 48, 99, 203, 413, 838, 1694, 3419, 6881,
    13843, 27811, 55818, 111980, 224511, 449933,
]


def a_direct_q(n, q):
    count = 0
    for r in range(2 ** n):
        x, y = r, r + 1
        sx = sy = 0
        merged = False
        for _ in range(n):
            if x % 2:
                sx += 1
            if y % 2:
                sy += 1
            x = (q * x + 1) // 2 if x % 2 else x // 2
            y = (q * y + 1) // 2 if y % 2 else y // 2
            if x == y:
                merged = (sx == sy)
                break
        if merged:
            count += 1
    return count


for q, stored in ((5, A5_TERMS), (7, A7_TERMS)):
    for n in range(1, N_DIRECT + 1):
        got = a_direct_q(n, q)
        if got != stored[n - 1]:
            raise SystemExit("MISMATCH: q=%d a(%d) direct=%d stored=%d"
                             % (q, n, got, stored[n - 1]))
    print("OK: q=%d, a(1)..a(%d) recomputed by brute force, all match."
          % (q, N_DIRECT))

print()
print("Densities at n = 22: q=5: %.6f   q=7: %.6f   (q=3 gives 0.409018)"
      % (A5_TERMS[-1] / 2.0 ** 22, A7_TERMS[-1] / 2.0 ** 22))
# ---------------------------------------------------------------------------
# The obstruction theorem (papers/02, Theorem 2), tested as a falsifiable
# prediction: for the map (q*x + r)/2 with an odd prime p dividing r but
# not q, consecutive pairs NEVER merge with equal odd count. Reason: mod
# p the map is multiplication by units (2^-1 or 2^-1 q), equal step count
# and equal odd count equalize the accumulated factors, so merging forces
# x0 = y0 (mod p) -- false for consecutive integers. Tested here on
# (5x+3)/2, (7x+3)/2 and (3x+5)/2: a(n) must be 0 for every n.
# ---------------------------------------------------------------------------

def a_direct_qr(n, q, r):
    count = 0
    for r0 in range(2 ** n):
        x, y = r0, r0 + 1
        sx = sy = 0
        merged = False
        for _ in range(n):
            if x % 2:
                sx += 1
            if y % 2:
                sy += 1
            x = (q * x + r) // 2 if x % 2 else x // 2
            y = (q * y + r) // 2 if y % 2 else y // 2
            if x == y:
                merged = (sx == sy)
                break
        if merged:
            count += 1
    return count


print()
for (q, r) in ((5, 3), (7, 3), (3, 5)):
    for n in range(1, 15):
        if a_direct_qr(n, q, r) != 0:
            raise SystemExit("OBSTRUCTION FAILS: q=%d r=%d n=%d" % (q, r, n))
    print("OK: (%dx+%d)/2 -- a(n) = 0 for n <= 14, as the obstruction"
          " theorem predicts." % (q, r))

print()
print("The one-line criticality statement (see papers/02): writing each")
print("step of the pair-difference dynamics as c -> m*c + shift, the")
print("multiplier m is a fair coin on {1/2, q/2}, so E[m] = (1+q)/4.")
print("E[m] = 1 exactly iff q = 3: among all maps (qx+1)/2 the Collatz")
print("case is the unique critical one.")
