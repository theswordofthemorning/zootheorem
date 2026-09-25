# Propuesta única — tiempo de encuentro de los pares de A078417 (24-09-2026)

**No enviada.** Sustituye a la «Propuesta 1» de `TRES_PROPUESTAS_20260924.md`:
aquella contaba también encuentros *dentro del ciclo trivial* (p. ej. 7 y 8 bajo
A014682 «se encuentran» en el paso 10 dando vueltas en 1 -> 2), que un editor
leería como artefacto. Aquí sólo hay encuentros reales: los de A078417.

Duplicados buscados el 24-09-2026 en la API de OEIS: esta secuencia, la
variante con ceros para todo n, la Propuesta 1 antigua y el texto
«coalesce collatz consecutive»: **No results** en las cuatro. Control:
Fibonacci devuelve A000045.

Verificación: `conjeturadecollazpython/depuracion/oeis20260924/encuentro.py`.
A078417 recalculada = b-file oficial (10 000 términos); conjunto de Gao
literal = {m de A078417 con a <= log2 m} para m = 2..199999, 0 discrepancias;
a = 3 sólo y siempre en m == 4 (mod 8). El programa de la ficha se ejecutó
tal cual y coincide con la b-file. b-file: `seqs/bfile_meeting_equal_height_3x1.txt`
(n = 1..10000), renombrar a bNNNNNN.txt con el número asignado.

Demostración de `a >= 3` con igualdad sii m == 4 (mod 8): si C(x) = C(y) con
x != y, entonces {x, y} = {2v, (v-1)/3}. Un par consecutivo nunca es de esa
forma (5v+1 = ±3), lo que descarta a = 1; los dos casos del paso 1 dan
ecuaciones sin solución, lo que descarta a = 2; y en el paso 3 los cuatro
casos de m mod 4 dejan sólo m == 0 (mod 4) con m/4 impar.

## Texto (formato interno)

```text
%S A000000 3,9,5,3,7,3,10,5,3,6,3,8,9,5,3,7,3,13,12,5,3,6,3,9,5,3,7,3,11,5,10,3,6,3,8,5,3,7,3,14,5,13,3,6,3,9,11,5,3,7,3,10,5,3,6,3,8,9,5,3,7,3,12,14,5,3,6,3,9,13,5,3,7,3,11,5,3,6,3,8,13,5,3,7,3,17,17,5,3,6,3,9,5,3,7,3,10,5,12,3,6,3,8,9,5,3,7,15,15,3,13,5,3,6,3,9,5,3,7,3
%N A000000 Number of steps after which the Collatz trajectories of A078417(n) and A078417(n)+1 first coincide.
%C A000000 With f(x) = x/2 for even x and 3*x+1 for odd x (A006370), a(n) is the least k such that f^k(m) = f^k(m+1), where m = A078417(n). Such a k exists because m and m+1 reach 1 after the same number of steps, so a(n) <= A006577(m).
%C A000000 Gao (1993) conjectured that the set of m such that f^k(m) = f^k(m+1) for some k <= log_2(m) has natural density 1, and proved that its density is at least 0.389 (as summarized by Lagarias). For m >= 2 a meeting that early occurs before either trajectory reaches 1, so this set consists exactly of the numbers m = A078417(n) with a(n) <= log_2(m). Gao's conjecture is thus the statement that these numbers have natural density 1.
%C A000000 For every j, A398792(j)/2^j is a lower bound for the lower density of the set in Gao's conjecture: the pairs of a class counted there meet within j steps of A014682, that is, within at most 2*j steps of f, which is at most log_2(m) for every member m >= 4^j of the class. A398792(32)/2^32 = 0.4356..., above Gao's 0.389.
%C A000000 a(n) >= 3, with equality exactly when A078417(n) == 4 (mod 8). These are Garner's pairs (8*k+4, 8*k+5), k >= 1, which meet at 6*k+4 after three steps.
%D A000000 G.-G. Gao, On consecutive numbers of the same height in the Collatz problem, Discrete Math. 112 (1993), 261-267.
%H A000000 Omar Said, <a href="/A000000/b000000.txt">Table of n, a(n) for n = 1..10000</a>
%H A000000 Lynn E. Garner, <a href="https://doi.org/10.1016/S0012-365X(85)80020-0">On heights in the Collatz 3n+1 problem</a>, Discrete Math, 55 (1985), 57-64.
%H A000000 Jeffrey C. Lagarias, <a href="https://arxiv.org/abs/math/0309224">The 3x+1 problem: An annotated bibliography (1963-1999) (sorted by author)</a>, arXiv:math/0309224 [math.NT], 2003-2011.
%e A000000 a(1) = 3: A078417(1) = 12, and 12 -> 6 -> 3 -> 10, 13 -> 40 -> 20 -> 10.
%e A000000 a(2) = 9: A078417(2) = 14, and the trajectories 14, 7, 22, 11, 34, 17, 52, 26, 13, 40 and 15, 46, 23, 70, 35, 106, 53, 160, 80, 40 first agree at step 9.
%o A000000 (Python)
%o A000000 def f(x): return 3*x+1 if x % 2 else x//2
%o A000000 def h(m):
%o A000000     k = 0
%o A000000     while m > 1: m, k = f(m), k+1
%o A000000     return k
%o A000000 def a_list(limit):
%o A000000     out = []
%o A000000     for m in range(1, limit):
%o A000000         if h(m) == h(m+1):
%o A000000             x, y, k = m, m+1, 0
%o A000000             while x != y: x, y, k = f(x), f(y), k+1
%o A000000             out.append(k)
%o A000000     return out
%o A000000 print(a_list(200))
%Y A000000 Cf. A006370, A006577, A078417, A277109, A398792.
%K A000000 nonn
%O A000000 1,1
%A A000000 Omar Said
```

## Por qué una sola

Tras un NOGI, dos altas a la vez vuelven a parecer variantes. Esta es la más
fuerte: complemento natural de A078417 (que dice *quiénes*; esta dice
*cuándo*), la conjetura de Gao se vuelve un enunciado literal sobre ella, y
lo único propio que afirma está demostrado. La segunda (testigo mínimo o
comentarios a A398793) espera a que esta se acepte.
