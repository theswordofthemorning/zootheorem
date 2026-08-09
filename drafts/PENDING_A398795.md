# A398795 — pendiente de envío (bloqueada por el límite de drafts)

**Estado (2026-08-09):** el A-number **A398795** está reservado para
Omar Said, pero OEIS limita a **3 drafts activos** las cuentas nuevas
y los tres slots están ocupados por A398792, A398793 y A398794
(las tres propuestas, esperando revisión). La reserva dura
aproximadamente un mes; si expira, se pide otro número en
<https://oeis.org/edit/allocate> y se ajustan las referencias cruzadas.

## Cómo enviarla cuando se libere un slot

1. Comprobar en <https://oeis.org/draft?user=Omar%20Said> que alguna de
   las tres quedó aprobada (o rechazada).
2. Ir a **<https://oeis.org/edit?seq=A398795&internal=1>** (formato
   interno: una sola caja de texto).
3. Sustituir el contenido de la caja por el bloque de abajo, **dejando
   la línea `%I` que OEIS ya trae** (tiene su timestamp propio).
4. `Save Changes`, y en la página del draft, botón
   **"These changes are ready for review by an OEIS Editor."**
5. Verificar en la lista de drafts que el estado dice **proposed**
   (no «editing») — la lista es la fuente de verdad, no el botón.

## El contenido, listo para pegar (todo menos la línea %I)

```
%S 0,0,0,1,2,5,11,23,48,99,203,413,838,1694,3419,6881,13843,27811,
%T 55818,111980,224511,449933
%N Number of residues r in [0, 2^n) such that the trajectories of r and r+1 under the map x -> x/2 if x is even, (7x+1)/2 if x is odd, satisfy T^n(r) = T^n(r+1) and contain the same number of odd terms among the first n iterates.
%C The analog of A398792 for the 7x+1 map; see A398794 for why the count is well defined without any convergence assumption. The density a(n)/2^n at n = 22 is 0.107, nearly flat on the computed range, against 0.409 (and rising) for the Collatz map.
%C For maps (q*x+r)/2 with an odd prime p dividing r but not q, the corresponding count is 0 for every n: mod p the map is multiplication by units (2^-1 or 2^-1*q), and merging at equal step and odd counts equalizes the accumulated factors, forcing r == r+1 (mod p), which is impossible. (Tested on (5x+3)/2, (7x+3)/2 and (3x+5)/2: all identically zero.)
%H Omar Said, <a href="https://github.com/theswordofthemorning/zootheorem">Statements, proofs, sequence data and verification scripts</a>
%e a(4) = 1: the residue r = 8 satisfies T^4(8) = T^4(9) = 4 with one odd step on each side (8 -> 4 -> 2 -> 1 -> 4 and 9 -> 32 -> 16 -> 8 -> 4).
%o (Python)
%o def a(n):
%o     c = 0
%o     for r in range(2**n):
%o         x, y, sx, sy = r, r+1, 0, 0
%o         for _ in range(n):
%o             sx += x & 1; sy += y & 1
%o             x = (7*x+1)//2 if x & 1 else x//2
%o             y = (7*y+1)//2 if y & 1 else y//2
%o             if x == y:
%o                 c += sx == sy
%o                 break
%o     return c
%Y Cf. A398792, A398793, A398794.
%K nonn,more
%O 1,5
%A _Omar Said_, Aug 09 2026
```

## Verificación del contenido

- Los 22 términos están recalculados por fuerza bruta independiente en
  `verify/verify_q_family.py` (n <= 18) y por el cálculo exacto de
  clases (n <= 22, coincidentes en todo el rango común).
- El ejemplo `a(4) = 1` con testigo `r = 8` está calculado, no citado
  de memoria: `T^4(8) = T^4(9) = 4`, un paso impar por lado.
- El teorema de la obstrucción del segundo comentario es el Theorem 2
  de `papers/02-generalized-maps.md`, con su prueba de cinco líneas.
- Offset `1,5`: el primer término mayor que 1 es a(5) = 2.
