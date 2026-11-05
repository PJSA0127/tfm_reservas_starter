# Anexo candidato — registro contemporáneo de esfuerzo definitivo

**Estado:** `CANDIDATO DOCUMENTAL PRE-FREEZE / REV-01..11 APROBADOS POR INTERLOCUTOR / TEXTO NO CONGELADO`. Complementa, sin modificar, `effort_log_v0.1.md` (encabezado original `v0.2`), `run_record_template_v0.1.md`, `metrics_definition_v0.1.md` y TFM §1.3.7. Justificación: REV-03 y REV-08.

## Reglas preservadas

- **M2 = suma de minutos-persona activos observados**, desagregados por las categorías: configuración inicial, ejecución, análisis, documentación de evidencias y mantenimiento/recuperación.
- I2 — Carlos registra; I1 — Paulo ejecuta; I3 — Jorge supervisa. Cada participante se atribuye únicamente el intervalo activo de la actividad que tiene asignada; participantes asignados activos durante el intervalo declarado salvo pausa/inactividad expresamente registrada.
- El tiempo automático de pytest/Semgrep/ZAP/CI u otros mecanismos se registra **por separado**; la espera pasiva y las pausas personales son cero esfuerzo humano.
- Si un investigador trabaja junto a otro, se suman sus tiempos activos. Redondeo por investigador a dos decimales y suma de cantidades redondeadas según criterio del proyecto, conservando duración observada sin redondear cuando exista.
- `OBSERVADO` puede ser elegible; `ESTIMADO` y `PLANIFICADO` no se suman a M2. Tiempos de piloto, corrección general del escenario, incorporación D01–D05 y redacción académica se excluyen.
- Preparación específica fuera del piloto solo es elegible si está permitida por el protocolo, tiene trazabilidad causal y cronometraje **contemporáneo** y no está duplicada.

## Registro de actividad (crear una copia **vacía** por tramo al iniciar la medición, nunca completarla retrospectivamente)

| Campo obligatorio | Valor al ejecutar |
|---|---|
| ID de registro / Run ID / ID de actividad | PENDIENTE / PENDIENTE / PENDIENTE |
| Proceso y fuente del procedimiento congelado | PENDIENTE |
| Categoría M2 | PENDIENTE |
| Objetivo y evidencia que debe generarse | PENDIENTE |
| Investigador y rol | PENDIENTE |
| Inicio observado ISO 8601 con offset | PENDIENTE |
| Fin observado ISO 8601 con offset | PENDIENTE |
| Duración transcurrida real (segundos) | PENDIENTE |
| Pausas personales / ajenas: comienzo-fin-motivo | PENDIENTE (usar **0** solo si se constató) |
| Minutos humanos activos | PENDIENTE |
| Minutos-persona atribuibles a este investigador | PENDIENTE |
| Estado temporal | `OBSERVADO / ESTIMADO / PLANIFICADO` (seleccionar observado) |
| ¿Elegible M2? / justificación | PENDIENTE |
| Evidencia contemporánea (archivo, ruta, referencia) | PENDIENTE |
| Incidencia, recuperación o reintento relacionado | PENDIENTE / NO APLICA |
| Verificación I2 | PENDIENTE |

**Operación temporal:** abrir el registro **antes** de la intervención humana elegible; anotar inicio cuando arranca, pausa/reanudación cuando ocurren, cierre al finalizar. Si falta medición, marcar `NO OBSERVADO`, documentar la limitación y excluir ese tramo no probado del valor observado; no inferir segundos mediante logs de herramienta salvo instrumento explícito que los mida.

## Tiempo autónomo — registro distinto, sin suma a M2

| Run ID / mecanismo | ID intento | Inicio/fin observados con offset | Duración automática medida | Referencia a reporte/metadata |
|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

## Consolidación y control de doble conteo

| Registro fuente | Persona | Categoría | Min activos observados | Min-persona a sumar | Excluido y motivo |
|---|---|---|---:|---:|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

No se suma un mismo intervalo dos veces bajo ejecución y documentación. El trabajo documental **posterior** que forme parte de la aplicación de un proceso requiere tramo medido propio; si un único tramo continuo abarca ambas categorías, definir los límites observados de cada subtramo antes de totalizar. Para runs invalidados, preservar esfuerzos como evidencia pero excluir del comparativo definitivo conforme al protocolo.
