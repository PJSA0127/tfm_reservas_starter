# Resultados del piloto — v0.2

## Estado

**PARCIAL — PILOT-CONV-01 CERRADO E INVALIDADO / PILOT-CONV-02 Y PILOT-PROP-01 PENDIENTES.**

Este documento no constituye el cierre global del piloto.

## Resultado parcial

| Componente | Resultado | Evidencia | Ajuste requerido |
|---|---|---|---|
| Procedimiento convencional — intento 1 | INVALIDADO | `evidence/PILOT-CONV-01/` | Sí |
| Pruebas funcionales C01 | 18/18 PASS | evidencia C01 | No |
| Recorrido manual C02 | 7/7 PASS | evidencia C02 | No |
| Casos manuales C03 | COMPLETADO CON INCIDENCIAS | `manual/c03_manual_cases.md` | Sí |
| Revisión técnica C04 | COMPLETADA | `manual/c04_code_review.md` | No para repetir C03 |
| Registro de hallazgos C05 | COMPLETADO | `review/c05_findings.md` | No |
| Cierre C06 | INVALIDADO POR CONSENSO I1+I2+I3 | `evaluation/c06_closure.md` | Repetición convencional |
| Archivo/copia/hash | PASS | manifest y recibo | No |
| PILOT-CONV-02 | PENDIENTE | | |
| PILOT-PROP-01 | PENDIENTE | | |

## Lección principal

El primer intento convencional detectó que cinco subcomprobaciones congeladas no podían ejecutarse completamente mediante interacción normal del navegador.

El problema fue de instrumentación:

- cuatro variantes requerían superar controles cliente para comprobar la validación server-side;
- la cancelación entre usuarios requería un POST controlado que preservara sesión y CSRF.

## Ajustes derivados

- `manual_cases_v0.2.md`;
- `conventional_procedure_v0.2.md`;
- `post_pilot_instrument_adjustments_v0.1.md`.

Estado: **PENDIENTES DE REVALIDACIÓN**.

## Decisión parcial

- [x] repetir el proceso convencional piloto por incidencia objetiva;
- [x] aplicar ajustes permitidos y versionados;
- [ ] revalidar ajustes;
- [ ] ejecutar `PILOT-CONV-02`;
- [ ] ejecutar reset;
- [ ] ejecutar `PILOT-PROP-01`;
- [ ] cerrar resultados globales del piloto;
- [ ] aprobar piloto y avanzar a freeze definitivo.

No se extraen todavía conclusiones comparativas de cobertura, detección o esfuerzo entre procesos.
Esfuerzo humano observado del intento invalidado: **115.30 min-persona**.
Tiempo automático registrado: **0.19 min**.
Estos valores son de calibración y no entran en las métricas definitivas.
