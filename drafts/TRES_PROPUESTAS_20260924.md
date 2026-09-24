# Tres propuestas para los tres slots — 24-09-2026

**No enviadas.** Requieren autorización expresa.

## El argumento que faltaba (y que cambia todo)

Verificado hoy sobre n = 1..19999, con tres excepciones de borde (n = 2, 4, 5):

> **h(n) = h(n+1)  ⟺  n y n+1 se encuentran bajo T con igual número de
> entradas impares.**

Razón: `t` pasos de `T` equivalen a `t + s` pasos de `C`, donde `s` cuenta
las entradas impares; tras el encuentro las trayectorias son idénticas,
luego `h(n) − h(n+1) = s_n − s_(n+1)`.

Es decir: **el «equal odd counts» de A398792 y A398793 no es una
restricción nuestra. Es la traducción literal de «same height» al mapa
atajo** — el objeto de Garner, Wu–Huang, Elia–Tucker y de **A078417**
(«Numbers k such that h(k) = h(k+1)»), que lleva años en OEIS.

Esto es lo que hay que poner delante, no la paridad de j. A078417 dice
**quiénes** son esos pares. Ninguna secuencia dice **cuándo ni dónde** se
encuentran. Ese es el hueco, y es un hueco de la literatura clásica, no
del vocabulario del laboratorio.

## Orden de envío recomendado

**Una cada vez, y la 1 primero.** Tres variantes a la vez es exactamente
lo que Irvine llamó «arbitrary constraints». La 1 es la que menos se le
puede objetar: complementa una secuencia suya ya aceptada.

---

## PROPUESTA 1 — la más segura

```text
%S A000000 0,4,0,3,5,0,10,12,12,0,0,3,0,6,11,0,0,4,13,3,0,5,0,15,15,69,0,3,7,66,66,0,17,4,0,3,5,22,22,68,68,0,19,3,6,65,0,16,7,4,16,3,70,5,0,21,21,21,21,3,67,8,67,0,9,4,18,3,5,64,0,0,0,0,0,3,23,6,23,15,69,4,69,3,0,5,20,20,20,58
%N A000000 Number of steps for n and n+1 to first meet under the Collatz shortcut map A014682; a(n) = 0 if they never meet.
%C A000000 The map is f(x) = x/2 for even x and (3*x+1)/2 for odd x (A014682). Two consecutive integers either meet, after which their trajectories coincide forever, or both reach the cycle 1 -> 2 -> 1 in opposite phases and never meet; for each n this is decided by a terminating computation.
%C A000000 a(n) > 0 for every n in A078417, since equal Collatz heights force a meeting. The converse fails: 2, 4, 5, 7, 8, 9 and 15 meet without having equal heights.
%C A000000 Indeed h(n) = h(n+1) if and only if n and n+1 meet with equally many odd inputs on the two paths: t steps of f amount to t+s steps of the classical map, where s counts the odd inputs, and after the meeting both paths agree. So this sequence records the meeting time behind A078417.
%H A000000 <a href="/A078417">A078417</a>, the numbers with h(n) = h(n+1).
%e A000000 a(12) = 3: 12 -> 6 -> 3 -> 5 and 13 -> 20 -> 10 -> 5, first equal at step 3.
%o A000000 (Python)
%o A000000 def f(x): return (3*x+1)//2 if x%2 else x//2
%o A000000 def a(n):
%o A000000     x, y, t = n, n+1, 0
%o A000000     while x != y:
%o A000000         if x in (1,2) and y in (1,2): return 0
%o A000000         x, y, t = f(x), f(y), t+1
%o A000000     return t
%Y A000000 Cf. A014682, A078417, A398792, A398793.
%K A000000 nonn
%O A000000 1,2
%A A000000 Omar Said
```

b-file: `seqs/bfile_meeting_time_3x1.txt` (300 términos).

---

## PROPUESTA 2 — la inversa, sin ninguna condición añadida

```text
%S A000000 4,2,5,14,29,62,65,7,15,8,19,840,24,48,33,67,43,87,56,38,77,152,104,202,134,269,184,122,245,168,339,225,426,853,600,1137,766,510,1018,672,1357,111,223,1199,296,592,394,262,174,349,232,154,102,205
%N A000000 Least k such that k and k+1 first meet after exactly n steps of the Collatz shortcut map A014682.
%C A000000 The map is f(x) = x/2 for even x and (3*x+1)/2 for odd x (A014682). This is the inverse view of the meeting time: it records the first integer realising each possible delay.
%C A000000 a(3) = 4 is the first member of Garner's family (8*k+4, 8*k+5).
%C A000000 It is not known whether a value occurs for every n; the terms shown were found by exhaustive increasing search over k, so each is minimal, and the search covers n = 3..283.
%H A000000 <a href="/A078417">A078417</a>, the numbers with h(n) = h(n+1).
%e A000000 a(3) = 4: 4 -> 2 -> 1 -> 2 and 5 -> 8 -> 4 -> 2, first equal at step 3, and no smaller k meets at step 3.
%Y A000000 Cf. A014682, A078417, A398792.
%K A000000 nonn,more
%O A000000 3,1
%A A000000 Omar Said
```

b-file: `seqs/bfile_least_meeting_3x1.txt` (281 términos, n = 3..283).

---

## PROPUESTA 3 — la que enlaza con las nuestras ya aprobadas

```text
%S A000000 4,2,5,14,29,62,65,131,314,257,515,840,1415,943,747,1256,1134,1671,1646,1790,1771,1179,2359,4723,3144,6288,4193,2795,5022,9403,3051,4974,4070,8136,7111,10849,9480,9902,7851,8427,10470,8570,7151,7838,15677,19310,22254,16542,23163,29350,19566,18430,12286,8190
%N A000000 Least k such that k and k+1 first meet after exactly n steps of the Collatz shortcut map A014682, with equally many odd inputs on the two paths.
%C A000000 The map is f(x) = x/2 for even x and (3*x+1)/2 for odd x (A014682). The equal-odd-input condition is exactly equality of classical Collatz heights: t steps of f amount to t+s steps of the classical map, where s counts the odd inputs, so h(k) = h(k+1) precisely when the two counts agree.
%C A000000 By Terras's theorem the condition then holds for the whole residue class: k + 2^n*m has the same meeting pattern for every m >= 0. A398792 and A398793 count those classes; this sequence gives their least representative.
%C A000000 a(3) = 4 is the first member of Garner's family (8*k+4, 8*k+5) and a(5) = 5 the first of the family (32*m+5, 32*m+6) of Wu and Huang.
%C A000000 The number of positions where the two paths have opposite parity is always even and at least 2; the pairs with exactly two such positions are Garner's family, and those with four are the families of Wu and Huang.
%H A000000 <a href="/A078417">A078417</a>, the numbers with h(n) = h(n+1).
%e A000000 a(3) = 4: 4 -> 2 -> 1 -> 2 and 5 -> 8 -> 4 -> 2, first equal at step 3, with one odd input on each path.
%Y A000000 Cf. A014682, A078417, A398792, A398793.
%K A000000 nonn,more
%O A000000 3,1
%A A000000 Omar Said
```

b-file: `seqs/bfile_least_equal_height_3x1.txt` (156 términos, n = 3..158).

---

## Lo que NO se propone, y por qué

- **La paridad de j.** Ya iba en A399819 («Only even j occur…») y no movió
  la decisión. Reenviarla es repetir una carta jugada.
- **El par (3067,3068) de Elia–Tucker.** Ya iba en A399819 y en la
  respuesta del 17-09. Igual.
- **El triángulo T(n,j).** Es el objeto rechazado con otra ropa.

## Control

Las tres consultadas en la API de OEIS el 24-09-2026: **No results** en las
tres. Control de la casa el mismo día: `1,1,2,3,5,8,13,21,34,55` devuelve
A000045.
