# Guardar, responder y dejar un draft en proposed

Procedimiento observado el 17-09-2026. Consultar primero la ficha y el
panel actuales: los textos de los botones y el límite de la cuenta pueden
cambiar. Esta guía documenta la operación; la autorización para editar o
responder procede de la tarea del usuario.

## Qué hace cada botón

| Acción | Efecto comprobado |
|---|---|
| `Save Changes` | Guarda el contenido; una modificación puede devolver la ficha a `editing` |
| `Add note to discussion.` | Publica la respuesta en la discusión y la comunica a los participantes; no sustituye el reenvío |
| `These changes are ready for review by an OEIS Editor.` | Envía la edición para revisión: debe pasar a `proposed` |
| `My Drafts (...)` | Permite comprobar el estado actual de cada solicitud |

**Guardar y responder no basta para dejar una ficha propuesta.** El cierre
requiere comprobar `proposed` en el panel después del último cambio.
`proposed` significa enviada a revisión; la aprobación sigue pendiente.

## Secuencia de trabajo

1. Abrir el panel del usuario y luego la ficha correspondiente. Leer las
   últimas intervenciones y registrar número, revisión y estado inicial.
   Conservar las aportaciones de los editores, aunque el repositorio tenga
   una copia anterior. No trabajar desde un texto histórico sin cotejarlo.
2. Preparar el texto y la respuesta localmente. Verificar las afirmaciones
   afectadas y la conservación de datos, offset, ejemplos y programa.
3. Abrir `edit` y después `edit internal format`. Capturar el valor completo
   del campo antes de sustituirlo: este formato conserva la indentación
   del programa. Los diffs de la discusión mezclan inserciones y supresiones
   y no representan por sí solos el texto vigente.
4. Introducir el texto preparado, enfocar el campo, volver a leerlo y
   cotejarlo. Normalizar únicamente CRLF/LF para esta comparación. Si el
   contenido no coincide, detener el guardado y resolver la diferencia.
5. Pulsar `Save Changes`. Volver a leer el contenido guardado en el servidor
   y compararlo con lo preparado; `%I` cambia al guardar la revisión.
   Abrir el formulario para leerlo no implica guardar otra modificación.
6. Regresar a la discusión. Introducir la respuesta en su campo, volver
   a leerla y cotejarla. Pulsar `Add note to discussion.` **una sola vez**.
   Comprobar que aparece con el autor y la hora correctos. Ante una demora,
   leer de nuevo antes de repetir el envío para evitar notas duplicadas.
7. Si la ficha está en `editing`, pulsar
   `These changes are ready for review by an OEIS Editor.`. Si ya está
   propuesta y sólo se añadió una nota, comprobar su estado sin editarla
   otra vez para provocar artificialmente la aparición del botón.
8. Volver a `My Drafts (...)` y comprobar la fila de esa ficha:
   **`proposed` y ausencia de `not yet proposed for review`**. Registrar la
   revisión final y conservar una captura textual del panel y la discusión.
   No basta buscar la palabra `proposed` en el historial: aparece también
   en revisiones antiguas de fichas que ahora están en `editing`.
9. Sincronizar el repositorio con el texto final del servidor. Mantener
   separadas la captura literal y la copia normalizada para los lectores
   locales. Actualizar el estado breve y la nota de entrega.

## Chrome y PowerShell: problemas ya resueltos

El ayudante está en el laboratorio compañero:
`depuracion/oeis20260917/chrome_uia.ps1`. Usa accesibilidad de Windows (UIA)
y selecciona una ventana cuyo título contiene OEIS. Ejecutarlo desde un
escritorio con Chrome abierto y la sesión OEIS del usuario disponible.
Si hay varias ventanas OEIS, identificar primero la que se está usando;
el ayudante toma la primera coincidencia. Restaurar la ventana si está
minimizada. No introducir ni recopilar credenciales.

- **Varias ventanas y monitores:** el ayudante antiguo `chrome.ps1`
  activaba Chrome por proceso y hacía clic en coordenadas fijas. Podía
  dirigirse a otra ventana. Preferir los enlaces y botones por nombre de UIA.
- **Valor obsoleto del campo:** `SetValue` puede cambiar el formulario sin
  actualizar inmediatamente la lectura accesible. `valor` y `obtener`
  enfocan el campo y esperan brevemente. Si aún se lee el texto anterior,
  enfocar y repetir la lectura; no asumir que el cambio falló ni enviar
  con una comparación fallida. El cotejo final es contra el servidor.
- **Finales de línea:** un texto LF puede volver como CRLF. Comparar
  normalizando `"\r\n"` a `"\n"`; preservar espacios e indentación.
- **Errores de PowerShell:** establecer `$ErrorActionPreference = 'Stop'`.
  Un error no terminante puede imprimir una excepción y acabar con código
  cero. En comandos nativos comprobar además `$LASTEXITCODE`; no encadenar
  guardar o publicar después de un cotejo fallido.
- **Salidas y campos:** usar `-Silencio` para guardar una captura sin
  imprimirla. El antiguo uso de `Out-Null` no suprimía `Console.WriteLine`.
  Ejecutar `-Accion controles` antes de escoger `-Indice`: en esta sesión
  el formato interno tenía índice 0, y la discusión índice 1 porque el
  buscador ocupaba el 0. Esos índices no son una garantía futura.
- **Carga de página:** tras navegar, comprobar documento y controles. Si
  todavía no aparecen, esperar y volver a leer antes de actuar. El texto
  `My Drafts (3)` también cambia con el número de solicitudes.

Ejemplo de inspección, desde la raíz de zootheorem:

```powershell
$ErrorActionPreference = 'Stop'
$ayudanteOeis = '..\conjeturadecollazpython\depuracion\oeis20260917\chrome_uia.ps1'
& $ayudanteOeis -Accion controles
& $ayudanteOeis -Accion leer -Archivo captura_actual.txt -Silencio
```

`-Archivo` se resuelve respecto a la carpeta del ayudante. Elegir un nombre
nuevo para cada captura que deba conservarse. Para un envío ya preparado,
los botones se invocan así, **en pasos separados y tras los cotejos**:

```powershell
& $ayudanteOeis -Accion boton -Valor 'Save Changes'
# Leer y comprobar el texto guardado; preparar y cotejar la respuesta.
& $ayudanteOeis -Accion boton -Valor 'Add note to discussion.'
# Comprobar la nota y el estado actual antes de reenviar.
& $ayudanteOeis -Accion boton -Valor 'These changes are ready for review by an OEIS Editor.'
# Abrir My Drafts (...) y comprobar la fila actual.
```

## Límite de ediciones y evidencia

El 17-09 la cuenta tenía tres ediciones pendientes. Abrir A398792 para
editar devolvió `You have too many active edits pending.`. Reenviar las
tres existentes como `proposed` no liberó un cupo: siguen activas hasta
que OEIS resuelva su estado. Se dejaron preparadas las otras correcciones
y se informó al editor; no se retiraron solicitudes para sortear el límite.

La entrega de referencia es [la revisión de la tarde](REVISION_20260917_TARDE.md):
A399819 #12, A399820 #13 y A399821 #11 quedaron propuestas.
Las capturas y el ayudante se conservan en el laboratorio compañero.
`verificar_tarde.py` coteja **esas capturas históricas**; no consulta OEIS
en vivo y no debe usarse para afirmar el estado actual de una sesión futura.
