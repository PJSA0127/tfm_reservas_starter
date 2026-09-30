# Registro de ejecución piloto — v0.2

## Estado

**PARCIAL / PILOT-CONV-01 INVALIDADO Y ARCHIVADO / PILOT-CONV-02 PENDIENTE.**

## Identificación general

| Campo | Valor |
|---|---|
| Fecha primera ejecución convencional | 2026-09-29 |
| Equipo investigador | Jorge, Carlos y Paulo |
| I1 | Paulo — Ejecutor principal |
| I2 | Carlos — Registrador de evidencia y esfuerzo |
| I3 | Jorge — Supervisor del protocolo |
| Baseline | Baseline seguro pre-piloto sin D01–D05 |
| Commit/tag baseline | `32d27a04305617f8fea031704e24d7e68ce9c451` / `pre-pilot-freeze-v0.1` |

## Runs y etapas

| Etapa | Run ID | Estado | Evidencia |
|---|---|---|---|
| Convencional piloto — intento 1 | `PILOT-CONV-01` | `INVALIDATED - EXCLUDED FROM FINAL COMPARISON` | `evidence/PILOT-CONV-01/` |
| Ajuste de instrumentos | N/A | EN CURSO | `post_pilot_instrument_adjustments_v0.1.md` |
| Convencional piloto — intento 2 | `PILOT-CONV-02` | NO INICIADO | PENDIENTE |
| Reset CONV -> PROP | N/A | NO EJECUTADO | PENDIENTE |
| Propuesto piloto | `PILOT-PROP-01` | NO INICIADO | PENDIENTE |

## Tratamiento de PILOT-CONV-01

`PILOT-CONV-01` permanece conservado íntegramente como evidencia de calibración.

- no se sobrescribe;
- no se utiliza para métricas definitivas;
- no se clasifica frente a D01–D05;
- su invalidación se atribuye a problemas de instrumentación;
- su manifiesto SHA-256 y copia secundaria fueron verificados.

## Próximo paso

Revalidar las cinco correcciones de instrumentación. Solo después se reconstruye y congela el workspace de `PILOT-CONV-02`.
Esfuerzo humano observado de PILOT-CONV-01: 115.30 min-persona.
Tiempo automático registrado: 0.19 min.
Cierre documental observado: 2026-09-29 15:45:15 -05:00.
