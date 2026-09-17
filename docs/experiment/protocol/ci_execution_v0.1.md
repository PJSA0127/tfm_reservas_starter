# GitHub Actions — proceso propuesto v0.1

## Estado

La lógica del workflow fue validada mediante CAL-01 y, tras inmovilizar dependencias, imágenes y GitHub Actions, mediante CAL-02. CAL-02 (Run ID 35251661421) terminó correctamente sobre el commit 32d27a04305617f8fea031704e24d7e68ce9c451, identificado por el tag pre-pilot-freeze-v0.1.

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

- `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` (`v7`);
- `actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` (`v7`);
- `ubuntu-24.04`.

CAL-01 validó las referencias `v7` utilizadas originalmente. Antes del freeze, esas mismas revisiones quedan fijadas por SHA completo. Los artifacts de CAL-01 fueron conservados y se registraron `GITHUB_SHA=7cfa55bc7bc96d67112f37d19e681007ec19d425` y `GITHUB_RUN_ID=35247019707`.


## CAL-02 - validación del freeze técnico

- Run ID: `35251661421`;
- commit: `32d27a04305617f8fea031704e24d7e68ce9c451`;
- tag técnico: `pre-pilot-freeze-v0.1`;
- funcional: 18/18 PASS;
- seguridad ASVS: 22/22 PASS;
- total pytest: 40/40 PASS;
- Semgrep: 0 findings / 0 errors;
- ZAP autenticado: PASS;
- ZAP: 0 tipos de hallazgo mapeados a D01/D02/D04;
- ZAP: 6 tipos de hallazgo adicionales conservados;
- aplicación durante DAST: 0 HTTP 5xx / excepciones no controladas;
- summary job: PASS.

Artifacts:

- functional: `c724040f70c24bf9fd9dacfe9501e575abf8016145b7fe4d8762cf1665b58d73`;
- security-tests: `9189dafc41b1081eac13641e783e53fa3bfc30f990b63a54cf7294eeca3d9a50`;
- Semgrep: `009079eaad1ccb282be6b7eae56d31168d0857d2c8288118c739e3b393ea43de`;
- ZAP: `c24df1add7d495352591a7e00c2521fc3d60c04c970c20e7e87f4bc05f50b5a0`.

El resultado confirma que la inmovilización técnica no alteró el comportamiento esperado del baseline seguro.

## Dependabot

Durante desarrollo se utiliza `.github/dependabot.yml` limitado al ecosistema `github-actions` para identificar actualizaciones disponibles de las Actions utilizadas por el workflow.

Dependabot es un mecanismo de apoyo de desarrollo y **no modifica automáticamente el protocolo experimental**. Antes del piloto/freeze, las referencias efectivamente utilizadas por el workflow deben fijarse por SHA completo y permanecer inmutables durante las ejecuciones experimentales.

## Tiempo

Tiempo de jobs = automático.

El tiempo humano de disparo, análisis y archivo = esfuerzo humano.

## Pendientes


- ejecución `pilot`;
- ejecución `proposed-definitive`.

## Semántica de ejecución frente a resultado de seguridad

El workflow distingue dos dimensiones:

1. **estado de ejecución técnica**: la herramienta/prueba pudo ejecutarse y producir evidencia válida;
2. **resultado de seguridad**: se observaron o no fallos/hallazgos dentro de la ejecución.

En `calibration` y `pilot`, que utilizan el baseline seguro, se exige que las suites y clasificadores permanezcan sin hallazgos experimentales esperados. En `proposed-definitive`, un test fallido o un hallazgo Semgrep/ZAP puede constituir **evidencia de detección** y no debe confundirse automáticamente con un error de infraestructura.

Para pytest se acepta exit code `1` en `proposed-definitive` como resultado de tests fallidos, mientras que códigos `>=2` se consideran errores técnicos. Semgrep genera un reporte y una clasificación separada; los findings no fuerzan un fallo técnico. ZAP conserva su exit code, clasifica los hallazgos mapeados y ejecuta siempre la comprobación de robustez y la carga de evidencias.

Los artifacts usan nombres neutrales (`semgrep-report.json`, `zap-report.json`, `zap-report.html`) y la fase se identifica mediante metadatos, `GITHUB_SHA`, `GITHUB_RUN_ID` y el nombre del artifact.
