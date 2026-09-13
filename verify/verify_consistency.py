"""Check stored data and the numerical bounds quoted by the papers."""

import ast
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def stored_list(script, name):
    tree = ast.parse((ROOT / 'verify' / script).read_text(encoding='utf-8'))
    return next(ast.literal_eval(node.value) for node in tree.body
                if isinstance(node, ast.Assign) and
                any(isinstance(t, ast.Name) and t.id == name for t in node.targets))


def bfile(name):
    rows = [tuple(map(int, line.split())) for line in
            (ROOT / 'seqs' / name).read_text().splitlines()
            if line.strip() and not line.startswith('#')]
    assert [n for n, _ in rows] == list(range(1, len(rows)+1))
    return [v for _, v in rows]


def paper_lists(name):
    text = (ROOT / 'papers' / name).read_text(encoding='utf-8')
    blocks = re.findall(r'```\s*\n([\s\S]*?)\n```', text)
    return [list(map(int, block.replace('\n', '').split(',')))
            for block in blocks if re.fullmatch(r'[\d,\s]+', block)]


def main():
    a3 = stored_list('verify_merging_classes.py', 'A_TERMS')
    b3 = [a3[i+1] - 2*a3[i] for i in range(len(a3)-1)]
    a5 = stored_list('verify_q_family.py', 'A5_TERMS')
    a7 = stored_list('verify_q_family.py', 'A7_TERMS')
    for name, values in [('merging_classes_3x1', a3), ('new_classes_3x1', b3),
                         ('merging_classes_5x1', a5), ('merging_classes_7x1', a7)]:
        assert bfile('bfile_' + name + '.txt') == values, name
    assert paper_lists('01-merging-classes.md') == [a3, b3]
    assert paper_lists('02-generalized-maps.md') == [a5, a7]
    assert Fraction(a3[31], 2**32) > Fraction(435658, 10**6)
    with localcontext() as ctx:
        ctx.prec = 60
        for theta, upper in [(Decimal('0.5'), Decimal('21.8')),
                             (Decimal('0.9'), Decimal('46.2'))]:
            r = (Decimal('0.5')**theta + Decimal('1.5')**theta)/2
            value = Decimal('0.5')**theta/(1-r)
            assert value < upper
            print(f'theta={theta}: additive bound {value:.12f} < {upper} (60-digit Decimal evaluation)')
    print('OK: all four stored b-files agree with scripts and papers; density bound is exact.')
    print('This checks consistency beyond the direct ranges, not a new enumeration there.')


if __name__ == '__main__':
    main()
