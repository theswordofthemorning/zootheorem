# Correcciones preparadas para A398792–A398795 — 17-09-2026

**No enviadas.** Al intentar editar A398792, OEIS respondió
«You have too many active edits pending». Las tres solicitudes actuales
ocupan el límite de la cuenta. No retirar ninguna para sortearlo.
La auditoría se apoya en las fichas e historiales leídos en vivo el 17-09,
conservados en el laboratorio, `depuracion/oeis20260917/*_tarde.txt`.
Los datos, programas, ejemplos y atribuciones de las cuatro fichas se conservan.

## A398792: densidad y enlaces

Sustituir el primer comentario por:

```text
By Terras's theorem, the first n input parities depend only on the residue modulo 2^n, and f^n(2^n*m+r) = 3^s*m+f^n(r), where s counts the odd inputs f^i(r), 0 <= i < n. Thus every counted residue represents pairs (2^n*m+r,2^n*m+r+1) meeting with equal odd-input counts for every m >= 0. For m >= 1, neither path reaches 1 before step n; if the common tail reaches 1, their finite classical total stopping times are equal. Barina verified convergence for positive starting values below 2^71; this finite verification does not prove convergence for all lifts.
```

Sustituir el comentario que empieza `a(n+1) >= 2*a(n)` por:

```text
a(n+1) >= 2*a(n): both r and r+2^n inherit the counted property. Let F_n be the periodic set of positive integers x such that x and x+1 have equal images after n iterations and equal odd-input counts. Then F_n is contained in F_(n+1) and has density a(n)/2^n. For F = union_n F_n, its lower natural density is at least phi = lim_n a(n)/2^n. In particular a(32)/2^32 = 1871137623/4294967296 > 0.435658 is an unconditional bound for this merging set. A bound for pairs with equal finite total stopping times requires the separate convergence qualification.
```

Sustituir el comentario `Relation to the 3x+1 problem` por:

```text
The sequence counts finite meeting patterns of consecutive pairs, including the families of Garner and Wu--Huang. The density statement concerns these meetings. If phi=1, F has natural density one. Equality between the density of F and phi for an arbitrary phi is not asserted, and these statements do not prove the Collatz conjecture.
```

Corregir la referencia de Barina de 2025: el título es
*Improved verification limit for the convergence of the Collatz conjecture*.
Añadir a LINKS, en orden de apellido, conservando los enlaces existentes:

```text
David Barina, <a href="https://doi.org/10.1007/s11227-025-07337-0">Improved verification limit for the convergence of the Collatz conjecture</a>, J. Supercomputing 81 (2025), 810.
Guo-Gang Gao, <a href="https://doi.org/10.1016/0012-365X(93)90240-T">On consecutive numbers of the same height in the Collatz problem</a>, Discrete Mathematics 112 (1993), 261-267.
Lynn E. Garner, <a href="https://doi.org/10.1016/S0012-365X(85)80020-0">On heights in the Collatz 3n+1 problem</a>, Discrete Mathematics 55 (1985), 57-64.
Jeffrey C. Lagarias, <a href="https://arxiv.org/abs/math/0608208">The 3x+1 Problem: An Annotated Bibliography, II (2000-2009)</a>, entry 125 discusses the cited paper of Wu and Huang.
Riho Terras, <a href="https://doi.org/10.4064/aa-30-3-241-252">A stopping time problem on the positive integers</a>, Acta Arithmetica 30 (1976), 241-252.
```

No se localizó un enlace directo verificable al artículo de Wu–Huang;
el de Lagarias está identificado como bibliografía, no como artículo original.

## A398793: punto de encuentro, índice y razón

Sustituir el comentario de la familia `(2^j-2,2^j-1)` por:

```text
For every even j >= 2, the pair (2^j-2,2^j-1) first meets after j+2 iterations at (3^j-1)/4, with j odd inputs on each path. At the preceding step its two values are (3^(j-1)-1)/2 and (3^j-1)/2. Thus a(j+1) >= 1 for every even j >= 2, and new classes occur at infinitely many levels.
```

El repunit `(3^(j-1)-1)/2` es el menor valor **anterior** al encuentro.
En j=2, las rutas `2,1,2,1,2` y `3,5,8,4,2` se encuentran en 2,
no en el repunit 1. La prueba escrita usa las dos escaleras descritas en
`conejas.lean`; determinismo y desigualdad en j+1 excluyen encuentros
anteriores. Lean certifica los caminos y el valor terminal, no contiene
todavía toda esta deducción sobre primer encuentro y conteo.

Sustituir el comentario sobre `a(n+1)/a(n)` por:

```text
The last ratio in the displayed data is a(35)/a(34) = 138581314/71181933, approximately 1.94686. The existence or value of a limiting ratio is not established by these data. Writing A(n) = A398792(n), the identity A(N)/2^N = sum_{k=1}^{N-1} a(k)/2^(k+1) follows by telescoping. A limiting ratio of 2 would not by itself determine the value of this sum or a natural density.
```

El n=35 antiguo también estaba desplazado: el último cociente disponible
es `a(35)/a(34)`, no `a(36)/a(35)`. Contraejemplo a la inferencia general:
`b_n=floor(2^n/(n+1)^2)` tiene razón límite 2, pero
`sum b_n/2^(n+1) < (1/2) sum 1/(n(n+1)) = 1/2`.
Esto refuta la inferencia, no un posible resultado adicional para Collatz.

## A398794 y A398795: ley del promedio

En A398794, conservar la comparación numérica en n=22 y reemplazar su
interpretación de la esperanza por:

```text
For positive odd q, when both inputs have the same parity their difference is multiplied by 1/2 (both even) or q/2 (both odd). Under the uniform residue-class law, conditioned on a finite parity history for which the next inputs have the same parity, the next unused parity bit is fair, so the conditional expected multiplier is (1+q)/4. This identity concerns only such steps, without conditioning on future meetings or survival.
```

Sustituir `Relation to the 3x+1 problem` en ambas fichas por:

```text
These counts compare finite meeting patterns for q=3,5,7. On steps with equal input parity under the law specified in A398794, q=3 is the unique positive odd q with expected difference multiplier 1. This does not describe the mean change over arbitrary steps or prove a statement about limiting merging densities. The observed densities are not ordered by q: at n=22 the value for q=7 exceeds that for q=5.
```

En A398795, precisar dominio y evitar reutilizar `r` para el término
constante del mapa y para el representante de la clase:

```text
For the map f(x)=x/2 for even x and (q*x+c)/2 for odd x, with q and c odd integers, suppose an odd prime p divides c but not q. Then no consecutive pair can meet with equal odd-input counts: modulo p, a path with n steps and s odd inputs maps x to 2^(-n)*q^s*x. Equal n and s give the same invertible factor for x and x+1, so meeting would force x == x+1 (mod p), a contradiction.
```

## Alcance y respaldo

Los argumentos de densidad, razón y ley condicionada ya están corregidos
en los papers y en el registro del laboratorio desde el 13-09. Esta
propuesta lleva esas correcciones a las fichas públicas. El valor terminal
de Conejas se cotejó otra vez con iteración entera y Lean 4.32.2 el 17-09.
Las extensiones de Irvine en A398794 y A398795 hasta n=29 están publicadas;
los b-files locales de esos dos mapas conservan su rango propio hasta n=22.
No se atribuye a nuestra verificación directa el rango añadido por Irvine.
