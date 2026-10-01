# Resultados del piloto — v0.2

## Estado

**PARCIAL — COMPONENTE CONVENCIONAL PILOTO CERRADO / PILOT-PROP-01 PENDIENTE.**

Este documento no constituye el cierre global del piloto.

## Resultados observados

| Componente | Resultado | Evidencia | Estado posterior |
|---|---|---|---|
| Procedimiento convencional — intento 1 | INVALIDADO | `evidence/PILOT-CONV-01/` | Ajustes de instrumentación requeridos |
| REV-INSTR-01 | 5/5 PASS | instrumentos v0.2 y evidencia de revalidación | Ajustes aprobados |
| Procedimiento convencional — intento 2 | VÁLIDO / COMPLETADO | `evidence/PILOT-CONV-02/` | Archivado y verificado |
| C01 funcional — CONV-02 | 18/18 PASS | evidencia C01 | Cerrado |
| C02 recorrido — CONV-02 | 7/7 PASS | evidencia C02 | Cerrado |
| C03 casos manuales — CONV-02 | 14/14 PASS | evidencia C03 | Cerrado |
| C04 revisión técnica — CONV-02 | COMPLETADA / 5 observaciones | evidencia C04 | Cerrado |
| C05 hallazgos — CONV-02 | 5 hallazgos | evidencia C05 | Cerrado |
| C06 cierre — CONV-02 | PASS | evidencia C06 | Run válido |
| Archivo/copia/hash — CONV-02 | PASS | manifest, sello y recibo | Cerrado |
| Reset CONV -> PROP | PASS | `evidence/PILOT-PROP-01/metadata/` | Estado inicial restaurado |
| Revalidación metodológica pre-PROP | PASS | sello pre-PROP v0.2 | PROP READY_TO_START |
| PILOT-PROP-01 | PENDIENTE | | READY_TO_START / NOT_STARTED |

## Lección de PILOT-CONV-01

El primer intento convencional detectó que cinco subcomprobaciones congeladas no podían ejecutarse completamente mediante interacción normal del navegador.

El problema fue de instrumentación:

- cuatro variantes requerían superar controles cliente para comprobar la validación server-side;
- la cancelación entre usuarios requería un POST controlado que preservara sesión y CSRF.

Los ajustes derivados fueron versionados en `manual_cases_v0.2.md`, `conventional_procedure_v0.2.md` y `post_pilot_instrument_adjustments_v0.1.md`, y posteriormente revalidados antes de `PILOT-CONV-02`.

## Resultado de PILOT-CONV-02

`PILOT-CONV-02` demostró que el procedimiento convencional ajustado puede completarse de forma ejecutable y auditable sobre el baseline seguro.

Esfuerzo humano observado: **146.71 min-persona**.

Tiempo automático válido conocido: **0.14 min**.

Estos valores son evidencia de calibración y no entran en las métricas definitivas.

## Estado del piloto global

- [x] `PILOT-CONV-01` ejecutado e invalidado de forma trazable;
- [x] ajustes permitidos derivados del primer intento documentados;
- [x] ajustes revalidados;
- [x] `PILOT-CONV-02` ejecutado y cerrado como válido;
- [x] reset CONV -> PROP ejecutado y verificado;
- [x] workspace PROP revalidado con instrumentos comunes v0.2;
- [ ] ejecutar `PILOT-PROP-01`;
- [ ] cerrar resultados globales del piloto;
- [ ] aprobar piloto y avanzar a freeze definitivo.

No se extraen todavía conclusiones comparativas definitivas de cobertura, detección o esfuerzo entre procesos.
