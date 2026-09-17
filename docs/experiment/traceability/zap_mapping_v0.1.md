# Correspondencia DAST — ASVS 5.0.0 v0.1

| ASVS | Defecto | Mecanismo ZAP | Rol |
|---|---|---|---|
| `v5.0.0-1.2.1` | D01 | Active rules 40012 y 40014 | Buscar manifestaciones dinámicas de XSS; complementa SEC-V121-01 y Semgrep. |
| `v5.0.0-1.2.4` | D02 | Active rule 40018 | Buscar manifestaciones dinámicas de SQL injection; complementa SEC-V124-01 y Semgrep. |
| `v5.0.0-2.2.1` | D03 | — | Las reglas funcionales se verifican con SEC-V221-01. |
| `v5.0.0-2.2.2` | D03 | — | La validación server-side se verifica con SEC-V222-01. |
| `v5.0.0-3.5.1` | D04 | Passive alert 10202 cuando aplique | Evidencia dinámica complementaria sobre ausencia de anti-CSRF; la prueba determinante es SEC-V351-01. |
| `v5.0.0-3.5.3` | D05 | — | El cambio de estado por método HTTP se verifica con SEC-V353-01 y SAST/revisión de rutas. |

## Criterio de interpretación

Los hallazgos ZAP deben revisarse y clasificarse frente a los criterios
preestablecidos. Hallazgos ajenos a D01–D05 se registrarán por separado como
hallazgos adicionales válidos o falsos positivos y no modificarán la tasa de
detección de los cinco defectos controlados.
