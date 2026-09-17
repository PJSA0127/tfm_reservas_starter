# GitHub Actions — proceso propuesto v0.1

## Estado

La lógica del workflow fue simulada localmente con éxito. La ejecución real en GitHub Actions permanece pendiente.

## Workflow

`.github/workflows/proposed-security-verification.yml`

Solo se dispara mediante `workflow_dispatch`.

## Fases

- `calibration`
- `pilot`
- `proposed-definitive`

No existe fase convencional.

## Jobs

| Job | Mecanismo | Evidencia |
|---|---|---|
| `functional-tests` | pytest funcional | JUnit + metadatos |
| `security-tests` | pytest ASVS | JUnit + metadatos |
| `sast` | Semgrep | JSON + versión/digest |
| `dast` | ZAP autenticado | JSON, HTML, recursos, URLs, logs, clasificación |
| `verification-summary` | consolidación | estado final |

## Checkout limpio

Cada job crea `.env` desde `.env.example`.

## Semgrep

Baseline local validado:

- 6 reglas;
- 14 targets reales;
- 0 findings;
- 0 errores.

Validación sintética:

- 6 fixtures;
- 6/6 reglas detectadas exactamente una vez.

## ZAP

Versión calibrada: `2.17.0`.

Se valida:

- autenticación;
- rutas protegidas;
- spider;
- active scan;
- reportes;
- clasificación;
- ausencia de 5xx no controlados.

IDs mapeados experimentalmente:

| ID | Defecto | ASVS |
|---:|---|---|
| 40012 | D01 | v5.0.0-1.2.1 |
| 40014 | D01 | v5.0.0-1.2.1 |
| 40018 | D02 | v5.0.0-1.2.4 |
| 10202 | D04 | v5.0.0-3.5.1 |

Hallazgos fuera de este mapeo se conservan como adicionales y no modifican automáticamente la tasa D01–D05.

## Simulación local validada

- funcional: 18/18;
- seguridad: 22/22;
- Semgrep: 0 findings / 14 targets;
- ZAP: `exit code 2` esperado por hallazgos Medium adicionales;
- clasificador: PASS;
- web DAST: 0 HTTP 5xx;
- jobs simulados en proyectos Compose aislados;
- sin contenedores residuales al cierre.

## GitHub Actions references

Actualmente:

- `actions/checkout@v7`;
- `actions/upload-artifact@v7`;
- `ubuntu-24.04`.

Antes del freeze:

- fijar Actions por SHA completo;
- ejecutar calibración real;
- conservar artifacts;
- documentar `GITHUB_SHA` / `GITHUB_RUN_ID`.

## Dependabot

Durante desarrollo se utiliza `.github/dependabot.yml` limitado al ecosistema `github-actions` para identificar actualizaciones disponibles de las Actions utilizadas por el workflow.

Dependabot es un mecanismo de apoyo de desarrollo y **no modifica automáticamente el protocolo experimental**. Antes del piloto/freeze, las referencias efectivamente utilizadas por el workflow deben fijarse por SHA completo y permanecer inmutables durante las ejecuciones experimentales.

## Tiempo

Tiempo de jobs = automático.

El tiempo humano de disparo, análisis y archivo = esfuerzo humano.

## Pendientes

- ejecución real en GitHub;
- SHAs inmutables;
- validación de artifacts en runner real;
- ejecución `pilot`;
- ejecución `proposed-definitive`.

## Semántica de ejecución frente a resultado de seguridad

El workflow distingue dos dimensiones:

1. **estado de ejecución técnica**: la herramienta/prueba pudo ejecutarse y producir evidencia válida;
2. **resultado de seguridad**: se observaron o no fallos/hallazgos dentro de la ejecución.

En `calibration` y `pilot`, que utilizan el baseline seguro, se exige que las suites y clasificadores permanezcan sin hallazgos experimentales esperados. En `proposed-definitive`, un test fallido o un hallazgo Semgrep/ZAP puede constituir **evidencia de detección** y no debe confundirse automáticamente con un error de infraestructura.

Para pytest se acepta exit code `1` en `proposed-definitive` como resultado de tests fallidos, mientras que códigos `>=2` se consideran errores técnicos. Semgrep genera un reporte y una clasificación separada; los findings no fuerzan un fallo técnico. ZAP conserva su exit code, clasifica los hallazgos mapeados y ejecuta siempre la comprobación de robustez y la carga de evidencias.

Los artifacts usan nombres neutrales (`semgrep-report.json`, `zap-report.json`, `zap-report.html`) y la fase se identifica mediante metadatos, `GITHUB_SHA`, `GITHUB_RUN_ID` y el nombre del artifact.
