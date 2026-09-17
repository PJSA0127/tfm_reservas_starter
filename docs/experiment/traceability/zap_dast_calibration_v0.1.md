# Calibración OWASP ZAP DAST autenticado — baseline seguro v0.1

**Clasificación:** desarrollo/calibración; no corresponde a la evaluación experimental definitiva.

## Implementación asociada

Referencia histórica del flujo autenticado en el **repositorio de desarrollo anterior**: `48f429f` (`feat: calibrate authenticated OWASP ZAP DAST workflow`). Esta referencia se conserva únicamente como trazabilidad histórica y **no corresponde al historial Git del repositorio experimental corregido actual**. La validación pre-GitHub añadió posteriormente un control de robustez de la aplicación y una regresión para IDs fuera de rango, sin cambiar los IDs D01–D05 ni los criterios de clasificación experimental. El commit definitivo del repositorio experimental se registrará cuando el nuevo historial sea inicializado y congelado.

## Herramienta

- OWASP ZAP: `2.17.0`.
- Imagen: `zaproxy/zap-stable:2.17.0`.
- Automation Framework autenticado.

## Resultado de autenticación

La ejecución final de calibración registró:

- `stats.auth.success >= 1`: PASS;
- `stats.auth.state.loggedin >= 1`: PASS;
- `stats.auth.browser.passed >= 1`: PASS;
- `/reservations/`: HTTP 200;
- `/reservations/new`: HTTP 200;
- `/reservations/1`: HTTP 200;
- `/reservations/1/edit`: HTTP 200.

## Exploración y active scan

- spider autenticado: 12 URLs descubiertas;
- active scan: completado;
- reglas activas relevantes: 40012, 40014 y 40018;
- reportes JSON/HTML generados;
- listado de URLs generado;
- HTTP 5xx durante DAST: 0;
- excepciones no controladas en `web_dast`: 0.

## Hallazgos observados

| ID | Riesgo | Resultado | Clasificación |
|---:|---|---|---|
| 10020 | Medium | Missing Anti-clickjacking Header | adicional, fuera de D01–D05 |
| 10021 | Low | X-Content-Type-Options Header Missing | adicional, fuera de D01–D05 |
| 10036 | Low | Server Leaks Version Information | adicional, fuera de D01–D05 |
| 10038 | Medium | CSP Header Not Set | adicional, fuera de D01–D05 |
| 10111 | Informational | Authentication Request Identified | informativo |
| 10112 | Informational | Session Management Response Identified | informativo |

No se observaron los IDs experimentales:

- 40012;
- 40014;
- 40018;
- 10202.

## Clasificador experimental

Comando:

```powershell
python .\scripts\ci\check_zap_relevant_findings.py `
  .\artifacts\zap\zap-report.json `
  .\artifacts\zap\zap-relevant-findings.json
```

Resultado observado:

```text
Safe-baseline DAST expectation: PASS (no mapped D01/D02/D04 alerts).
```

## Interpretación

La calibración confirma que ZAP puede autenticarse, explorar las rutas protegidas, ejecutar el active scan y producir evidencia clasificable sin provocar errores HTTP 5xx no controlados en la aplicación. La ausencia de alertas relevantes en el baseline seguro no constituye, de forma aislada, verificación completa de los requisitos ASVS.

En la ejecución `proposed-definitive`, la presencia de alertas mapeadas se conserva como resultado de seguridad y no se confunde con un fallo técnico del motor ZAP. Las fases seguras `calibration` y `pilot` mantienen una validación separada que exige 0 alertas mapeadas.
