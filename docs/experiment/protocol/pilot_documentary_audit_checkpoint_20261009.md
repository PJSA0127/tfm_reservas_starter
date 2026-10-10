# Auditoría documental de pausa — PILOT-PROP-01 — 2026-10-09

## Estado

**DOCUMENTAL / NO EXPERIMENTAL / NO BLOQUEANTE.**

Este registro documenta inconsistencias detectadas durante una revisión transversal posterior al checkpoint de MC-14. No constituye una nueva prueba, no modifica resultados observados, no reinicia actividades y no altera el protocolo ni los instrumentos congelados.

## Contexto

- Run: `PILOT-PROP-01`
- Estado del run al realizar la auditoría: `OPEN / IN_PROGRESS`
- P01: `IN_PROGRESS`
- MC-01..MC-14: `COMPLETED / PASS`
- `INC-P01-001`: `OPEN / NON-BLOCKING`
- siguiente paso formal: `P01_COMMON_TECHNICAL_REVIEW`
- D01–D05 introducidos: `NO`
- commit documental previo a esta auditoría: `4202feb17917c34273d8f2d4d501dba4d8f24d31`

## ERR-DOC-01 — prestart_revalidation_20261009.md

Artefacto original:

`evidence/PILOT-PROP-01/metadata/prestart_revalidation_20261009.md`

SHA-256 original preservado:

`23B33BC8D0E2838077C3353AF127BCC1714B87D816A2F774E35B2FB8B59F9CBC`

Defectos de serialización observados:

- variables PowerShell no expandidas en campos de metadatos (`$prestartRecordedAt`, `$documentalHead`, `$technicalCommit`, `$technicalTag`);
- tres caracteres NUL (`0x00`) en campos de salida;
- el contenido sustantivo de la revalidación permanece legible y el archivo conserva exactamente el hash registrado durante el pre-start.

Tratamiento:

- el artefacto original **NO se modifica**;
- no se reconstruyen retrospectivamente valores dentro del archivo hasheado;
- los valores operacionales relevantes se corroboran mediante registros independientes de reset, Git, run record y checkpoint documental;
- se clasifica como errata documental de evidencia pre-run, sin impacto experimental observado.

## ERR-DOC-02 — reset_execution_PILOT-CONV-02_to_PILOT-PROP-01.md

Artefacto original:

`evidence/PILOT-PROP-01/metadata/reset_execution_PILOT-CONV-02_to_PILOT-PROP-01.md`

SHA-256 original preservado:

`81F9E24D5FB94EBA862D866A92D5B498ABBF59C5C3DE44D9FED6D1C85E5CE3B2`

Defecto de serialización observado:

- dos caracteres `FORM FEED` (`0x0C`) sustituyen visualmente la letra inicial de `flask create-user` en dos líneas de recuperación R06.

Tratamiento:

- el artefacto original **NO se modifica**;
- la acción ejecutada está descrita por el resto del registro y por los resultados observados (`user_count final = 2`, U1/U2 creados, R06 final `PASS`);
- se clasifica como errata de formato sin cambio de resultado.

## Correcciones documentales aplicadas

Se actualizaron únicamente resúmenes operacionales vivos:

- `README.md`;
- `experiment/README.md`;
- `docs/experiment/protocol/README.md`.

Los cambios reflejan que `PILOT-PROP-01` está abierto, P01 está en progreso, P01-FUNC y MC-01..MC-14 ya fueron ejecutados y el siguiente paso es `P01_COMMON_TECHNICAL_REVIEW`.

No se modificaron protocolos, instrumentos, código, pruebas, configuraciones de seguridad ni evidencia histórica hasheada.

## Observaciones deliberadamente diferidas

### Versionado nominal de instrumentos

Existen archivos cuyo nombre conserva `v0.1` mientras su encabezado interno refleja revisiones `v0.2` o `v0.3`. No se renombran durante un run abierto porque sus nombres participan en referencias e hashes históricos. La normalización se realizará después del piloto y antes del freeze definitivo.

### Hashes de instrumentos propuestos

`proposed_instrument_hashes_v0.2.txt` corresponde al conjunto congelado del workspace propuesto. Antes de P02 debe verificarse el workspace real `D:\Repositorios\tfm_reservas_pilot_prop` contra ese conjunto. No se sustituyen instrumentos durante el run para hacerlos coincidir con copias documentales posteriores del repositorio principal.

### Esfuerzo documental no cronometrado

No se añaden estimaciones retrospectivas al esfuerzo. El total observado de P01 hasta este checkpoint permanece en `68.74 min-persona`. La frontera de cronometraje de documentación se tratará como lección del piloto antes del freeze definitivo.

## Resultado

```text
DOCUMENTARY_AUDIT        = PASS_WITH_ERRATA
ORIGINAL_EVIDENCE_EDITED = NO
TECHNICAL_BASELINE_EDITED= NO
RUN_INVALIDATED          = NO
P01                      = IN_PROGRESS
NEXT_FORMAL_STEP         = P01_COMMON_TECHNICAL_REVIEW
```
