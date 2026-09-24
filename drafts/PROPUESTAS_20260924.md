# Propuestas preparadas — 24-09-2026

**No enviadas.** Requieren autorización expresa del usuario; el estado
vigente prohíbe enviar a OEIS o contactar personas sin ella. La cuenta
tiene los tres slots libres desde el rechazo de esta mañana.

Documentación con demostraciones y verificadores en
`conjeturadecollazpython/depuracion/oeis20260924/Garzas.md`.

## Qué es nuevo y qué no (leer antes de decidir)

Comprobado contra las fichas rechazadas, para no reenviar cartas ya
jugadas:

| material | estado |
|---|---|
| «Only even j occur» | **ya iba en A399819**, comentario 10, con la misma razón |
| par (3067,3068) y Elia–Tucker | **ya iba en A399819** y en la respuesta del 17-09 |
| `sum_j e_j(n) = A398793(n-1)` | **ya iba** en las tres fichas |
| lema del punto de encuentro (`m == 2 mod 3`) | no aparece en ninguna ficha |
| `e_2(n) = 1` y su forma cerrada | no aparece en ninguna ficha |
| recursión `j(r) = 2 + j((3r+1)/4)` | no aparece en ninguna ficha |
| testigos mínimos de cada nivel | no aparece en ninguna ficha |

Irvine leyó lo de la izquierda y rechazó igual. Así que **no proponer de
nuevo la paridad de `j` ni el contraejemplo de Elia–Tucker**: eso ya se
envió, ya se argumentó el 17-09 y no movió la decisión. Lo que se puede
defender es lo de abajo, que es lo que no ha visto nadie.

Orden recomendado: **primero la 1, y sólo después la 2.** La 1 enriquece
una ficha ya aprobada y no arriesga nada; la 2 abre número nuevo a siete
días de un NOGI y conviene que llegue con la primera ya aceptada detrás.

---

## 1. Comentarios nuevos para A398793 (entrada aprobada)

Añadir a los comentarios de A398793. No tocan datos, offset, ejemplos ni
programas. Ninguno repite lo ya enviado.

El lema que fija el punto de encuentro:

```text
If x <> y and f(x) = f(y) = m, then {x,y} = {2*m, (2*m-1)/3} and m == 2 (mod 3): a value has two f-preimages exactly when it is 2 mod 3, one even and one odd. So every meeting value of a counted pair is 2 mod 3, and the last step before meeting always has opposite parity.
```

Un segundo, con la columna extrema resuelta:

```text
The stratum j = 2 contains exactly one pair at every level n >= 4, namely r = 2^(n-2)-2 for even n and r = 3*2^(n-2)-2 for odd n. Proof sketch: with j = 2 the opposite-parity positions are forced to be the first and the last, so the difference is even in between and odd at the end, giving r+2 = 2^(n-2)*q with q odd, and the range leaves only q = 1 and q = 3. Both trajectories then have the closed form 3^a*2^b-1, so one step before meeting the pair is (x, 3*x+1) with x = (3^k-1)/2 in A003462; such a pair meets at the next step exactly when x is odd, which holds for one candidate and fails for the other. The meeting values are the base-9 repdigits 2, 20, 182, 1640, ... of A125857.
```

Un tercero, que es el que de verdad responde a «general value», porque lo
hace con literatura y no con opinión:

```text
The two extreme strata are the classical families. Stratum j = 2 is Garner's family (8*k+4, 8*k+5), and by the previous comment it is the only pair of its stratum at each level; stratum j = 4 gives the families of Wu and Huang, (32*m+5, 32*m+6), (64*m+45, 64*m+46) and (128*m+29, 128*m+30). The parameter j is therefore not an arbitrary label: its first two values recover exactly the families already isolated in the literature, and the strata with larger j continue that classification.
```

Y un cuarto, el más estructural: la recursión.

```text
The residues with r == 1 (mod 4) satisfy an exact recursion. For r = 4*k+1 the first two positions are forced: f(r) = 6*k+2 is even while f(r+1) = 2*k+1 is odd, and then f^2(r) = 3*k+1, f^2(r+1) = 3*k+2, so the pair is consecutive again after two steps, having spent two opposite-parity positions of opposite signs. Hence, writing r' = (3*r+1)/4, the meeting index and the stratum both drop by two, n(r) = 2 + n(r') and j(r) = 2 + j(r'), and r is balanced if and only if r' is. Since r -> (3*r+1)/4 maps {r == 1 (mod 4)} bijectively onto {r' == 1 (mod 3)}, this determines one third of each row from the row two levels earlier.
```

Comprobado sobre los $2^n$ residuos completos para n = 3..26 (barrido
vectorizado, ninguna excepción), contra los 24 primeros términos no nulos
de A398793 tal como está publicada, y la recursión en 54 623 pares.

---

## 2. Entrada nueva: testigo mínimo de cada nivel

Objeto distinto del rechazado: **no tiene ningún parámetro fijado**, que
era la objeción literal de Irvine («arbitrary constraints like "exactly 12
positions"»). Sus dos primeros términos son de Garner y de Wu–Huang, ambos
ya citados en A398792 por los propios editores.

```text
%S A000000 4,2,5,14,29,62,65,131,314,257,515,840,1415,943,747,1256,1134,1671,1646,1790,1771,1179,2359,4723,3144,6288,4193,2795,5022,9403,3051,4974,4070,8136,7111,10849,9480,9902,7851,8427,10470,8570,7151,7838,15677,19310,22254,16542,23163,29350,19566,18430,12286,8190
%N A000000 Least k such that k and k+1 first meet after exactly n steps of the Collatz shortcut map A014682, with both trajectories having the same number of odd inputs.
%C A000000 The map is f(x) = x/2 for even x and (3*x+1)/2 for odd x (A014682). A pair (k,k+1) is counted when n is the least index with f^n(k) = f^n(k+1) and the two trajectories receive equally many odd inputs in those n steps; a(n) is the least such k.
%C A000000 By Terras's theorem the first n input parities depend only on the residue modulo 2^n, so a(n) also selects an entire class: k + 2^n*m has the same meeting pattern for every m >= 0.
%C A000000 The number j of positions where the two trajectories have opposite parity is always even and at least 2 (see A398793). The meeting value is always congruent to 2 mod 3, since a value has two f-preimages, one even and one odd, exactly when it is 2 mod 3.
%C A000000 a(3) = 4 is the first member of Garner's family (8*k+4, 8*k+5) and a(5) = 5 the first of the family (32*m+5, 32*m+6) of Wu and Huang, both cited in A398792. More generally the terms with j = 2 give Garner's family and those with j = 4 give the families of Wu and Huang, including (64*m+45, 64*m+46) and (128*m+29, 128*m+30).
%C A000000 It is not known whether a witness exists for every n; the terms given were found by exhaustive increasing search, so each is minimal, but the search covers n = 3..132 only.
%H A000000 <a href="/A014682">A014682</a>, the shortcut map used here.
%e A000000 a(3) = 4: the trajectories of 4 and 5 are 4 -> 2 -> 1 -> 2 and 5 -> 8 -> 4 -> 2, first equal at step 3, with one odd input each (5, and 1).
%o A000000 (Python)
%o A000000 def f(x): return (3*x+1)//2 if x%2 else x//2
%o A000000 def a(n):
%o A000000     k = 0
%o A000000     while True:
%o A000000         x, y, sx, sy = k, k+1, 0, 0
%o A000000         for t in range(1, n+1):
%o A000000             sx += x%2; sy += y%2; x, y = f(x), f(y)
%o A000000             if x == y: break
%o A000000         if x == y and t == n and sx == sy: return k
%o A000000         k += 1
%Y A000000 Cf. A003462, A014682, A125857, A398792, A398793.
%K A000000 nonn,more
%O A000000 3,1
%A A000000 Omar Said
```

Consultada la API de OEIS el 24-09-2026 con los doce primeros términos
(`4,2,5,14,29,62,65,131,314,257,515,840`): **No results**. Control de la
casa el mismo día: la consulta de `1,1,2,3,5,8,13,21,34,55` devuelve
A000045, así que el «No results» es del buscador, no del método.

Nota sobre Elia–Tucker: el laboratorio ya la tenía localizada y verificada
desde agosto, y la ficha A399819 la enlazaba. Al citarla, **usar el enlace
de arXiv**: `sucesiones.txt` la registra como *Integers* 15 (2015) #A54 y
la web la da como 16 (2016) #A80; esa discrepancia está sin resolver y no
conviene afirmar un volumen concreto. Su Teorema 2.1 (n == 4 (mod 8),
n > 4, coinciden en el tercer paso) hay que citarlo como suyo: es lo mismo
que sale del cálculo de las clases pares, y no es observación nuestra.

b-file preparado con los 130 términos en
`seqs/bfile_minimal_witness_3x1.txt` (n = 3..132); se renombra al
A-number real si la entrada llega a abrirse.

### Riesgo honesto de la 2

El objeto es nuevo y sin parámetros, pero sigue siendo del mismo tema y
llega muy pronto tras el NOGI. Si se envía y vuelve a rechazarse, la vía
OEIS queda cerrada para este material durante bastante tiempo. Por eso el
orden importa: la 1 no tiene ese riesgo y, si se acepta, cambia el contexto
en que se lee la 2.

---

## Lo que NO se propone

El triángulo T(n,j). Aunque el teorema de la libélula le quita lo
arbitrario —la mitad de las columnas son nulas por demostración, y las dos
primeras no nulas parecen constantes— sigue siendo el mismo objeto
rechazado hace siete días. Reenviarlo ahora gasta lo único que no se
recupera.
