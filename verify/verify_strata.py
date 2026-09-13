"""Direct integer verification of A399819--A399821, n=1..20.

No laboratory modules or state-chain transitions are used. The terms beyond
20 are preserved from the earlier symbolic computation, not recomputed here.
Run from any directory. Python 3, standard library only.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEQUENCES = {8: 'A399819', 10: 'A399820', 12: 'A399821'}


def trajectory_pair(residue, horizon):
    left, right = [residue], [residue + 1]
    odd_left = odd_right = 0
    mixed = []
    for time in range(1, horizon + 1):
        x, y = left[-1], right[-1]
        if x % 2 != y % 2:
            mixed.append(time)
        odd_left += x % 2
        odd_right += y % 2
        left.append((3 * x + 1) // 2 if x % 2 else x // 2)
        right.append((3 * y + 1) // 2 if y % 2 else y // 2)
        if left[-1] == right[-1]:
            return time, odd_left, odd_right, mixed, left, right
    return None


def count_level(n):
    counts = dict.fromkeys(SEQUENCES, 0)
    witnesses = {k: [] for k in SEQUENCES}
    for residue in range(1 << n):
        x, y = residue, residue + 1
        sx = sy = mixed = 0
        for time in range(1, n + 1):
            px, py = x & 1, y & 1
            sx += px
            sy += py
            mixed += px != py
            x = (3 * x + 1) // 2 if px else x // 2
            y = (3 * y + 1) // 2 if py else y // 2
            if x == y:
                if time == n and sx == sy and mixed in counts:
                    counts[mixed] += 1
                    witnesses[mixed].append(residue)
                break
    return counts, witnesses


def read_data(number):
    rows = [tuple(map(int, line.split())) for line in
            (ROOT / 'seqs' / f'b{number[1:]}.txt').read_text().splitlines()
            if line.strip() and not line.startswith('#')]
    assert [n for n, _ in rows] == list(range(rows[0][0], 30))
    text = (ROOT / 'drafts' / f'{number}.txt').read_text(encoding='utf-8')
    data = ','.join(line.split(' ', 1)[1] for line in text.splitlines()
                    if line.startswith(('%S ', '%T ', '%U ')))
    assert list(map(int, data.split(','))) == [v for _, v in rows]
    offset = next(line[3:] for line in text.splitlines() if line.startswith('%O '))
    second = next(i for i, (_, v) in enumerate(rows, 1) if abs(v) >= 2)
    assert offset == f'{rows[0][0]},{second}'
    return dict(rows)


def main():
    expected = {k: read_data(number) for k, number in SEQUENCES.items()}
    wanted = {(9, 8): [65], (10, 8): [131, 193, 473],
              (11, 10): [769], (13, 12): [1025]}
    print('n e8 e10 e12', flush=True)
    for n in range(1, 21):
        counts, witnesses = count_level(n)
        for k in SEQUENCES:
            assert counts[k] == expected[k].get(n, 0), (n, k, counts[k], expected[k].get(n, 0))
            if (n, k) in wanted:
                assert witnesses[k] == wanted[n, k]
        print(n, *(counts[k] for k in SEQUENCES), flush=True)
    for (n, k), residues in wanted.items():
        for residue in residues:
            time, sx, sy, mixed, left, right = trajectory_pair(residue, n)
            assert time == n and sx == sy and len(mixed) == k
            # Shared odd steps also increase both counts; k/2 is only a minimum.
            assert sx >= k // 2
            print(f'n={n}, k={k}, r={residue}, meeting={left[-1]}, odd={sx},{sy}, mixed={mixed}')
    print('OK: all 60 counts through n=20; witnesses, b-files and draft offsets agree.')


if __name__ == '__main__':
    main()
