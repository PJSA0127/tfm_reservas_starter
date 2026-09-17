# Correcciones derivadas de auditoría transversal — v0.1

## Propósito

Registrar las correcciones aplicadas después de auditar transversalmente el repositorio contra el anteproyecto rector.

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
