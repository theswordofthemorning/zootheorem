# verify_merging_classes.py
#
# Independent brute-force verification of the sequences a(n) and b(n)
# (merging classes of consecutive integers under the shortcut Collatz
# map), by direct simulation of integer pairs. No shared code with the
# programs that produced the stored terms.
#
# Definitions (T is the shortcut Collatz map: T(x) = x/2 for even x,
# T(x) = (3x+1)/2 for odd x):
#
#   a(n) = number of residues r in [0, 2^n) such that
#          T^n(r) = T^n(r+1)  and  the first n steps of r and r+1
#          contain the same number of odd iterates.
#
#   By Terras' theorem (1976) the first n parities depend only on
#   r mod 2^n, so a(n) counts entire residue classes: every pair
#   (2^n*m + r, 2^n*m + r + 1) with m >= 1 in a counted class merges
#   and has equal total stopping time. Hence a(n)/2^n is a proven
#   lower bound for the lower density of consecutive pairs with equal
#   Collatz height.
#
#   b(n) = a(n+1) - 2*a(n)   (classes that merge "for the first time"
#          at level n+1; b(n) >= 0 because a(n+1) >= 2*a(n), proved).
#
# This script recomputes a(1)..a(N_DIRECT) by brute force and checks
# them against the stored terms. Terms above N_DIRECT were computed by
# two independent methods each (see papers/01); they are stored here
# for the b-files but NOT re-verified by this script.
#
# Exits with SystemExit on any mismatch. Runs in a few minutes.

N_DIRECT = 20

A_TERMS = [
    # n = 1 .. 36
    0, 0,
    1, 3, 8, 18, 39, 82, 170, 351, 721, 1476, 3012, 6130, 12450, 25241,
    51105, 103358, 208840, 421643, 850737, 1715546, 3457791, 6966495,
    14030369, 28247507, 56854178, 114400435, 230136995, 462857658,
    930718308, 1871137623, 3761106610, 7558807251, 15188796435,
    30516174184,
]


def T(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def a_direct(n):
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
            x, y = T(x), T(y)
            if x == y:
                merged = (sx == sy)
                break
        if merged:
            count += 1
    return count


for n in range(1, N_DIRECT + 1):
    got = a_direct(n)
    if got != A_TERMS[n - 1]:
        raise SystemExit("MISMATCH: a(%d) direct=%d stored=%d"
                         % (n, got, A_TERMS[n - 1]))
print("OK: a(1)..a(%d) recomputed by brute force, all match." % N_DIRECT)

# b(n) = a(n+1) - 2 a(n) must be >= 0 for every stored term
for n in range(1, len(A_TERMS)):
    b = A_TERMS[n] - 2 * A_TERMS[n - 1]
    if b < 0:
        raise SystemExit("MISMATCH: b(%d) = %d < 0" % (n, b))
print("OK: b(n) = a(n+1) - 2a(n) is nonnegative for all stored terms")
print("    (the doubling theorem a(n+1) >= 2a(n) holds on the data).")

print()
print("b(n) = a(n+1) - 2a(n), n = 1..35:")
print([A_TERMS[n] - 2 * A_TERMS[n - 1] for n in range(1, len(A_TERMS))])
