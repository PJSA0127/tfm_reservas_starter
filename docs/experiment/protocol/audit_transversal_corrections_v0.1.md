# Correcciones derivadas de auditoría transversal — v0.2

## Propósito

Registrar de forma acumulativa las correcciones aplicadas como resultado de auditorías transversales y sincronizaciones documentales del laboratorio experimental.

Las secciones A–J conservan el contexto histórico de las correcciones realizadas en etapas anteriores. Las secciones posteriores registran cambios adicionales sin reescribir retroactivamente ese historial.

La jerarquía documental vigente es:

`TFM - G7 → PROTOCOLO EXPERIMENTAL → INSTRUMENTOS / DOCUMENTACIÓN TÉCNICA → CÓDIGO / AUTOMATIZACIÓN / EJECUCIONES / EVIDENCIAS`

La fuente de verdad del estado operacional vigente es `ESTADO_ACTUAL_TFM.md`.
## A — Workspace convencional

Se sustituyó una estrategia de exclusión genérica por una construcción mediante allowlist, se ampliaron las rutas sensibles excluidas (`docs/experiment/traceability/`, `scripts/ci/`, `.github/`, `security/`) y se definió la equivalencia mediante commit origen + hashes de componentes comunes.

## B — Referencias históricas de commits

Los hashes `d88d9d3`, `ee6eec7` y `48f429f` se etiquetaron explícitamente como referencias del repositorio de desarrollo anterior. No se presentarán como commits del repositorio experimental corregido actual.

## C — Ejecución técnica vs. resultado de seguridad

El workflow distingue ahora:

- error técnico del mecanismo;
- test/hallazgo de seguridad producido por una ejecución válida.

En `calibration` y `pilot` se exige baseline seguro. En `proposed-definitive`, findings/test failures pueden constituir evidencia y no invalidan por sí solos la ejecución técnica.

## D — Nombres neutrales de artifacts

Se normalizaron a:

- `semgrep-report.json`;
- `zap-report.json`;
- `zap-report.html`;
- `security/zap/zap-plan.yaml`.

La fase se registra en metadatos del run.

## E — Host local vs. runner GitHub

Se aclaró que las actividades equivalentes se ejecutan en el mismo host/laboratorio local, mientras GitHub Actions (`ubuntu-24.04`) es un componente automatizado adicional y exclusivo del proceso propuesto.

## F — Alcance histórico de Fase 9

Se documentó que el PASS de consistencia documental pre-GitHub correspondió al estado existente en aquel momento y no sustituye la auditoría metodológica transversal posterior.

## Alcance de la corrección

No se modificó la lógica funcional de Flask ni se introdujeron D01–D05.

## G — Cierre documental pre-piloto

Se sincronizaron el índice v0.5, el checklist de freeze y las plantillas de resultados/ejecución del piloto con las decisiones ya cerradas: roles I1/I2/I3, Run IDs, almacenamiento, retención y custodia.

## H — Tratamiento correcto del esfuerzo derivado del piloto

Se distinguió entre el tiempo de ejecución propiamente dicho del piloto, excluido del comparativo definitivo, y el trabajo adicional de ajuste/configuración específica que el piloto pueda revelar. Este último solo puede tratarse como configuración inicial si se registra separadamente como tiempo observado y sin doble contabilización.

## I — Dependabot para GitHub Actions

Se incorporó `.github/dependabot.yml` limitado al ecosistema `github-actions`, como mecanismo de apoyo durante desarrollo. Las referencias efectivamente utilizadas deberán fijarse por SHA antes del piloto/freeze.

## J — Limpieza pre-Git

La copia fuente distribuida después de esta corrección excluye `.env`, `artifacts/`, `.pytest_cache/`, `__pycache__/` y `.vscode/`.

## K — Sincronización documental pre-C00

Antes del inicio formal de `PILOT-CONV-01` se realizó una nueva revisión transversal entre:

- `TFM - G7.docx`;
- `ESTADO_ACTUAL_TFM.md`;
- documentación del protocolo;
- baseline técnico congelado;
- workspaces pre-piloto;
- evidencias y sellos de preparación;
- planificación temporal vigente.

La revisión confirmó que:

- el baseline técnico congelado sigue siendo `pre-pilot-freeze-v0.1`;
- el commit técnico congelado sigue siendo `32d27a04305617f8fea031704e24d7e68ce9c451`;
- CAL-01 y CAL-02 permanecen como validaciones técnicas pre-piloto;
- `PILOT-CONV-01` continúa en `READY_TO_START / NOT_STARTED`;
- C00 continúa en `NOT_STARTED`;
- el cronómetro experimental no ha iniciado;
- `PILOT-PROP-01` continúa en `PREPARED_NOT_STARTED`;
- el reset CONV → PROP continúa en `PREPARED_NOT_EXECUTED`;
- D01–D05 no han sido introducidos;
- no se han generado resultados experimentales del piloto.

Como resultado de esta sincronización se actualizaron documentalmente:

1. `docs/experiment/protocol/README.md`;
2. `docs/experiment/protocol/protocol_freeze_checklist_v0.1.md`;
3. `docs/experiment/protocol/conventional_workspace_sanitization_v0.1.md`;
4. `docs/experiment/protocol/evidence_archival_v0.1.md`;
5. `docs/experiment/protocol/pre_github_validation_plan_v0.1.md`;
6. `experiment/README.md`;
7. `README.md`.

Las correcciones realizadas incluyen:

- sustitución de referencias vigentes al anteproyecto por `TFM - G7.docx` cuando correspondía;
- reconocimiento explícito de `ESTADO_ACTUAL_TFM.md` como fuente de verdad operacional;
- actualización del estado de CAL-01 y CAL-02;
- actualización del estado del freeze técnico pre-piloto;
- actualización del workspace convencional ya preparado y validado;
- actualización de las rutas primaria y secundaria de evidencia;
- separación explícita entre baseline seguro del piloto y futura versión experimental definitiva con D01–D05;
- conservación de `PENDIENTE` para toda información que aún requiere observación experimental;
- preservación del carácter histórico de planes y validaciones anteriores;
- prohibición explícita de interpretar preparación, calibración o freeze técnico como inicio del piloto.

## L — Protección de artefactos ya cerrados

Durante esta sincronización no se modificaron:

- código funcional de la aplicación;
- baseline técnico congelado;
- tag `pre-pilot-freeze-v0.1`;
- commit técnico congelado;
- D01–D05;
- manifiestos SHA-256 ya cerrados;
- paquetes ZIP congelados;
- sellos de preparación;
- evidencia experimental cerrada;
- resultados de CAL-01 o CAL-02.

Tampoco se ejecutaron:

- C00;
- C01–C06;
- Semgrep experimental;
- OWASP ZAP experimental;
- pruebas específicas de seguridad como parte de un run;
- workflow de fase `pilot`;
- reset CONV → PROP;
- runtime de `PILOT-PROP-01`.

Por tanto, esta actualización constituye exclusivamente una **sincronización documental pre-C00**.

## M — Asignación nominal resuelta antes de C00

La correspondencia nominal entre los integrantes del equipo y los roles experimentales quedó formalizada antes del inicio de C00:

- I1 — Ejecutor principal: **Paulo**;
- I2 — Registrador de evidencia y esfuerzo: **Carlos**;
- I3 — Supervisor del protocolo: **Jorge**.

Registro: `investigator_role_assignment_v0.1.md`.

SHA-256 del registro:

`219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631`

La formalización de los roles no modifica retroactivamente metadatos, sellos, manifests, hashes ni evidencias de preparación cerradas antes de crear el registro. Por tanto, no se atribuyen retrospectivamente a Carlos o Jorge acciones históricas cuya identidad concreta no hubiese quedado registrada en el momento de su ejecución.

La resolución de este pendiente tampoco constituye el inicio del piloto:

- `PILOT-CONV-01`: `READY_TO_START / NOT_STARTED`;
- `C00`: `NOT_STARTED`;
- cronómetro experimental: `NO INICIADO`.

El siguiente paso experimental formal continúa siendo C00 únicamente cuando el equipo decida iniciar efectivamente el piloto.

## N — Discrepancia temporal del Gantt

La planificación temporal original ya no coincide con la ejecución real del proyecto:

- `H1.T1` estaba planificado para 2026-09-21 → 2026-09-24;
- las actividades posteriores dependían de ese cierre;
- `PILOT-CONV-01` continúa sin iniciar.

Esta desviación se considera de planificación y no modifica por sí misma el orden metodológico.

El Gantt deberá sincronizarse después de cerrar la actualización documental y establecer el nuevo punto temporal de ejecución, sin utilizar las fechas vencidas como justificación para saltar dependencias experimentales.
