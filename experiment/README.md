# Control experimental

Este directorio contiene documentación de control relacionada con la construcción y gestión de las versiones utilizadas en el laboratorio experimental.

El estado operacional vigente de las ejecuciones se mantiene en `ESTADO_ACTUAL_TFM.md`.

## Estado operacional pospiloto verificado — 25 de octubre de 2026

- `PILOT-CONV-02`: **VALID / COMPLETED / ARCHIVED**; `PILOT-PROP-01`: **VALID_WITH_DOCUMENTED_LIMITATION / ARCHIVED / VERIFIED / SEALED**. El sello P10 fue aplicado el 14/10/2026.
- `PILOT-PROP-01`: 250 archivos, manifiesto de 248 entradas y ZIP de 250, todos íntegros en la copia primaria adjuntada. El último `PASS` de sincronización OneDrive fue reportado en el cierre del 14/10; **no** se ha comprobado OneDrive en vivo el 25/10.
- Esfuerzo humano de los pilotos: **146,71** y **604,22 minutos-persona**, ambos **solo calibración**. M1=cobertura, M2=esfuerzo humano, M3=detección; las métricas definitivas están pendientes.
- `INC-P01-001` cerrada mediante disposición P10 con limitación de medición, sin cambiar su registro histórico.
- D01–D05 **no estaban introducidos en el baseline del piloto**. Variante con los defectos, freeze definitivo, `DEF-CONV-01` y `DEF-PROP-01`: **pendientes y no autorizados por esta actualización documental**.
- `NEXT_FORMAL_STEP = POST_PILOT_REVIEW_AND_FREEZE_PREPARATION`; no repetir pilotaje ni iniciar tests definitivos.

**Procedencia:** estado contrastado con la evidencia final del piloto incluida en el ZIP del 25/10/2026. Este índice descriptivo no aprueba el freeze definitivo ni acredita por sí mismo un nuevo commit/push. Los datos del 10/10/2026 son checkpoints históricos, no el estado operativo vigente.

## Nomenclatura histórica y planificación de variantes

### Baseline seguro pre-piloto

La versión técnica que se congeló para la fase piloto (ya finalizada) fue:

- tag: `pre-pilot-freeze-v0.1`;
- commit técnico: `32d27a04305617f8fea031704e24d7e68ce9c451`;
- D01–D05 introducidos: **NO**;
- finalidad: ejecución de `PILOT-CONV-01` y, después del reset correspondiente, `PILOT-PROP-01`.

Este baseline fue validado técnicamente mediante CAL-01 y CAL-02 antes del inicio del piloto.

Su existencia y validación, por sí solas, no constituyen resultados experimentales. El estado de los runs se consulta en `ESTADO_ACTUAL_TFM.md`.

## Versión experimental definitiva

No consta una versión experimental definitiva construida, verificada y aprobada en las fuentes auditadas. La construcción y la validación controlada de D01–D05 forman parte de los preparativos posteriores al piloto, todavía pendientes de autorización y freeze.

Los tres primeros hitos (piloto convencional válido, reset CONV → PROP y piloto propuesto) **ya finalizaron**. Antes de iniciar los runs definitivos falta revisar las incidencias y lecciones aprendidas, autorizar los ajustes necesarios, incorporar y validar los cinco defectos controlados en la variante de laboratorio, y congelar código, instrumentos, datos, configuración y criterios mediante commit/tag y manifiestos verificables. El orden exacto de autorización y congelación depende del protocolo vigente; este README no lo reemplaza.

Esa misma versión constituirá el origen técnico de:

- `DEF-CONV-01`;
- `DEF-PROP-01`.

No se deberá crear una versión diferente para cada proceso definitivo.

## Nomenclatura histórica

En una etapa anterior de planificación se utilizaron los nombres previstos:

- `calibration-v1`: aplicación funcional sin D01–D05 destinada al pilotaje;
- `experiment-v1`: misma base funcional con D01–D05 destinada a la evaluación definitiva.

Estos nombres se conservan únicamente como referencia histórica.

`calibration-v1` no debe utilizarse como identificador del baseline vigente, porque el artefacto técnico efectivamente congelado quedó identificado como `pre-pilot-freeze-v0.1`.

`experiment-v1` tampoco debe presentarse como una versión ya existente. La versión experimental definitiva con D01–D05 continúa pendiente y su identificador final se fijará después de cerrar ambos pilotos y congelar el protocolo definitivo.

## Restricción del proceso convencional

El catálogo detallado D01–D05, sus ubicaciones o manifestaciones y su correspondencia con OWASP ASVS no deben estar disponibles como guía durante la ejecución del proceso convencional.

Durante `PILOT-CONV-01`, además:

- el baseline utilizado no contiene D01–D05;
- no se consulta la matriz requisito-prueba-evidencia;
- no se ejecutan Semgrep ni OWASP ZAP;
- no se ejecutan las pruebas específicas de seguridad del proceso propuesto;
- no se crean pruebas ad hoc para confirmar sospechas.

Durante la evaluación definitiva, el proceso convencional utilizará la misma versión experimental con D01–D05 que el proceso propuesto, pero continuará sujeto a las restricciones anteriores respecto del conocimiento y mecanismos exclusivos del proceso propuesto.

## Estado histórico del checkpoint P02 — 10 de octubre de 2026 (NO VIGENTE)

- `PILOT-CONV-01`: `INVALIDATED - EXCLUDED FROM FINAL COMPARISON` / archivado;
- `PILOT-CONV-02`: `VÁLIDO / COMPLETADO / ARCHIVADO`;
- reset CONV → PROP: `PASS`;
- revalidación metodológica pre-PROP: `PASS`;
- `PILOT-PROP-01`: `OPEN / IN_PROGRESS`;
- P01-FUNC: `PASS` — 18/18;
- P01-WALKTHROUGH: `COMPLETED_WITH_PROCEDURAL_DEVIATION` (`INC-P01-001`, no bloqueante);
- MC-01..MC-14: `COMPLETED / PASS`;
- P01: `COMPLETED`, revisión técnica común `NO_NEW_FINDINGS`;
- incidencias P01 preservadas: `INC-P01-001 = OPEN / NON-BLOCKING`; `INC-P01-002 = DOCUMENTED / NON-BLOCKING`;
- P02: `COMPLETED / SEALED`, revisión ASVS `6/6`, sin incidencias ni desviaciones de P02;
- P03–P06 y P08–P10: `NOT_STARTED`; P07: `CONDITIONAL / NOT_TRIGGERED`;
- esfuerzo observado: P01 `119.09`, P02 `127.05`, total `246.14 min-persona`; tiempo automático conocido `0.21 min`;
- siguiente paso formal: `PREPARE_P03_SECURITY_TESTS` (preflight de solo lectura);
- D01–D05 introducidos: `NO`;
- versión experimental definitiva: `NO CREADA`.

Los dos pilotos ya concluyeron; la revisión pospiloto y los controles del freeze definitivo siguen pendientes. La variante definitiva solo podrá prepararse mediante decisiones y validaciones autorizadas.

## Regla documental posterior a P02

P02 quedó sellado el `2026-10-10T18:30:42-05:00` con SHA-256 del sello `AF7EEC4DA51B40D7528F92CC452F760B8FEAA5E9AD0F48D48FCDA4924146F0C0`. No modificar sus evidencias. Los resultados posteriores se incorporaron como artefactos adicionales, sin reescribir la matriz P02. Las normalizaciones de nombres/versiones de instrumentos se difieren hasta después del piloto.
