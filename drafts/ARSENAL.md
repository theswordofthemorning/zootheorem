# EL ARSENAL — sucesiones verificadas listas para OEIS (09-08-2026)

## El flujo de OEIS, en cinco líneas (pillarle la mano)

1. `allocate` A-number → draft (**editing**) → botón «ready for review»
   (**proposed**) → un editor revisa → o comenta (caja rosa, vuelve a
   editing — responder RÁPIDO y re-proponer) → o **aprueba** =
   PUBLICADA (visible en búsquedas). Semanas típicas para cuentas
   nuevas; el intercambio con Michel Marcus en minutos es buena señal.
2. **El límite cuenta drafts ACTIVOS (editing + proposed) = 3 para
   cuentas nuevas.** Era 7 hasta 2019; lo bajaron por saturación de
   editores. Cada aprobación LIBERA su slot al instante.
3. **El límite se puede subir** pidiéndolo a los editores con
   historial de submissions bien formateadas. La estrategia: que las
   tres primeras aterricen impecables y luego pedir el aumento.
4. El cuello de botella es humano (revisión), no nuestro: la táctica
   correcta es GOTEO DE CALIDAD, no ráfaga — cada entrada con su
   programa reproducible, sus referencias con MR, y su b-file.

## En el aire (3/3 slots ocupados)

| A-number | qué | estado |
|---|---|---|
| A398792 | a(n) fusión Collatz, 36 términos | proposed (2ª ronda, correcciones de Marcus aplicadas) |
| A398793 | b(n) las nuevas, 35 términos | proposed (respondido «more terms») |
| A398794 | (5x+1)/2, 22 términos | proposed |

## En recámara (texto listo, esperando slot)

- **A398795** — (7x+1)/2, 22 términos. Texto completo en
  `PENDING_A398795.md`. Primera en recargar.

## El cargador de reserva (verificadas, NO catalogadas — comprobado
## contra OEIS con control durante las sesiones del repo)

| # | sucesión | términos conocidos | historia |
|---|---|---|---|
| 1 | primeros retornos del par a gap 1 (catálogo extendido a largo 30) | 1,0,0,1,1,3,5,6,11,19,31,55,98,176,313,578,1099,2047,3847,… | extiende las tablas de la tesis LaTourette 2007 y corrige su L11 (errata ya comunicada a Moravian) — la mejor historia editorial del lote |
| 2 | b₄(m) = 7·2^{m−7} − m + 4 (estrato mínimo del piso g) | 3,7,15,30,60,121,… (m ≥ 7) | su hermana c₄ ES A079583 — el cruce da confianza; b₄ no está |
| 3 | b-reducida del piso g | 1,4,11,28,66,149 | afirmación #51 del repo; no está en OEIS |
| 4 | c-reducida del piso h **= H(k) de la identidad de renovación** | 1,3,9,24,58,134,300,659,1426 | afirmación del repo (gérmenes, `identidadexacta.py`); no está en OEIS. **FUSIONADA con la ex-#9 (12-08-2026): son LA MISMA serie** — la H de la identidad ES la c-reducida del piso h, con offset 3 (H(3)=H(4)=H(5)=0, H(6..14) = la serie; verificado término a término re-corriendo `identidadexacta.py`). Cross-reference valiosa para la entrada: un slot cubre ambas. `flecosr.py` extiende: c(15)=3053, c(16)=6487 |
| 5 | las nuevas de c | 1,3,6,10,18,32,59,108 | afirmación #52; no está |
| 6 | retornos de la cadena modificada (primeros retornos a (0,1) con el vórtice rebotado) | 0,1,0,0,1,2,5,7,10,18,29,49,86,151,271,480,881,1661,3093,5828 | la prima de la #1; retorno11.py |
| 7 | perfil diferencial a_2(k) (fusión de {n, n+2}) | de diferenciales.py | familia entera Δ = 2,3,… disponible |
| 8 | G(k) de la identidad de renovación | 0,0,0,0,1,5,16,44,110,259,588,1302 | identidadexacta.py |
| 9 | e8: estrato \|M\|=8 de las clases nuevas de la cadena (k,c) | 3,7,15,27,45,73,111,166,237,330,451,605,797,1033,1316,1655,2054,2517,3051,3665 (desde N=10) | `estratoscadena.py`; consultada OEIS 09-08-2026 («No results», control Fibonacci OK). NO admite forma cuasi-polinomial (grado ≤ 8, periodo ≤ 8) — a diferencia de e6 = 3+(N−7)(N−8)/2, que ES cerrada cuadrática y por eso va como posible comentario en entrada ajena, no slot propio |
| 10 | e10: estrato \|M\|=10 de las clases nuevas de la cadena (k,c) | 0,1,4,12,30,65,131,247,447,761,1242,1953,3003,4485,6570,9410,13204,18164,24596,32753 (desde N=10) | ídem `estratoscadena.py`; «No results» 09-08-2026; sin forma cuasi-polinomial |
| 11 | e12: estrato \|M\|=12 de las clases nuevas de la cadena (k,c) | 0,0,0,1,5,18,52,134,315,681,1393,2698,4947,8712,14818,24465,39278,61513,94110,140829 (desde N=10) | ídem `estratoscadena.py`; «No results» 09-08-2026; sin forma cuasi-polinomial |

**Total: ~15 balas fabricadas y verificadas** (4 en juego + 11 en
reserva — 12-08-2026: entraron los tres estratos e8/e10/e12 y se
fusionaron la ex-#4 y la ex-#9, que eran la misma serie). Regla antes de cargar cualquiera: re-consultar OEIS ESE DÍA
con control (Fibonacci → A000045), definición sin revelar el método
interno, programa de fuerza bruta en la entrada, y b-file.
