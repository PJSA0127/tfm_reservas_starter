# Plan de validación integral pre-GitHub — v0.2

## Estado

**HISTÓRICO — VALIDACIÓN LOCAL COMPLETADA / CAL-01 Y CAL-02 COMPLETADAS / PILOTAJE PENDIENTE**

Este documento registra la estrategia usada para validar el repositorio corregido antes de GitHub. Sus resultados pertenecen a calibración/desarrollo, no al experimento definitivo.

## Resultado consolidado

| Fase | Resultado |
|---|---|
| Entorno y estructura | PASS |
| Build + PostgreSQL + Flask | PASS |
| Flujo manual | PASS |
| pytest | PASS |
| Semgrep | PASS |
| ZAP | PASS |
| Regresión integrada | PASS |
| Simulación CI local | PASS |
| Consistencia documental | PASS |

## pytest

- 18/18 funcionales;
- 22/22 seguridad;
- 40/40 total.

## Semgrep

- 6 reglas;
- 14 targets;
- baseline 0 findings;
- fixtures 6/6;
- post-baseline 0 findings.

## ZAP

- autenticación PASS;
- spider PASS;
- active scan PASS;
- reportes generados;
- clasificación experimental PASS;
- 0 hallazgos mapeados D01/D02/D04 en baseline;
- 0 HTTP 5xx no controlados.

Durante esta validación se detectó y corrigió una respuesta 500 provocada por un ID de reserva fuera del rango PostgreSQL `INTEGER`; se incorporó una regresión que exige 404.

## CI local

Los cuatro jobs se simularon en workspaces/proyectos Compose aislados con resultado satisfactorio.

Esto no equivale a validar GitHub Actions real.

## Alcance histórico de la Fase 9 documental

La fase de «Consistencia documental» marcada como PASS verificó la coherencia técnica y documental del repositorio corregido **en el estado existente en ese momento**. Posteriormente se realizó una auditoría metodológica transversal tomando el anteproyecto como documento rector y se realinearon los documentos del protocolo. Por tanto, el PASS histórico de Fase 9 no sustituye esta auditoría posterior ni debe interpretarse como validación definitiva del protocolo experimental congelado.

## Pendiente posterior al cierre local — estado histórico

En el momento en que finalizó la validación exclusivamente local, permanecían pendientes:

- primer push;
- ejecución `calibration` real;
- revisión de artifacts;
- SHAs inmutables;
- pilotaje;
- freeze.

Esta lista se conserva como registro histórico del estado existente al cerrar la validación pre-GitHub y no representa el estado operacional vigente.

## Seguimiento posterior

Después del cierre de la validación local se completaron las actividades siguientes:

| Actividad | Estado posterior |
|---|---|
| Primer push al repositorio remoto | COMPLETADO |
| Primera ejecución real `calibration` — CAL-01 | PASS |
| `GITHUB_RUN_ID` CAL-01 | `35247019707` |
| `GITHUB_SHA` CAL-01 | `7cfa55bc7bc96d67112f37d19e681007ec19d425` |
| Revisión y conservación de artifacts CAL-01 | COMPLETADO |
| GitHub Actions fijadas por SHA completo | COMPLETADO |
| Dependencias transitivas congeladas mediante `requirements.lock` | COMPLETADO |
| Imágenes técnicas relevantes fijadas por digest | COMPLETADO |
| Freeze técnico pre-piloto | COMPLETADO |
| Tag técnico | `pre-pilot-freeze-v0.1` |
| Commit técnico congelado | `32d27a04305617f8fea031704e24d7e68ce9c451` |
| Segunda calibración — CAL-02 | PASS |
| `GITHUB_RUN_ID` CAL-02 | `35251661421` |
| Artifacts CAL-02 conservados y verificados mediante SHA-256 | COMPLETADO |
| `PILOT-CONV-01` | `READY_TO_START / NOT_STARTED` |
| `PILOT-PROP-01` | `PREPARED_NOT_STARTED` |
| Freeze experimental definitivo posterior al piloto | PENDIENTE |

CAL-02 confirmó que la inmovilización de dependencias, imágenes y referencias GitHub Actions no alteró el comportamiento esperado del baseline seguro.

Los resultados de CAL-01 y CAL-02 corresponden a calibración y validación técnica pre-piloto. No constituyen resultados experimentales de los runs piloto ni de las ejecuciones definitivas.

La fuente de verdad del estado operacional vigente es `ESTADO_ACTUAL_TFM.md`.

## Pendiente vigente

A partir del estado actual permanecen pendientes en esta línea de trabajo:

- ejecución real de `PILOT-CONV-01`;
- cierre y archivo de su evidencia;
- reset formal CONV → PROP;
- ejecución real de `PILOT-PROP-01`;
- análisis de incidencias y lecciones de ambos pilotos;
- ajustes permitidos derivados del piloto, si existieran;
- freeze del protocolo experimental definitivo;
- preparación de la versión experimental definitiva con D01–D05.

No deben confundirse estos pendientes con actividades técnicas pre-GitHub que ya fueron completadas.
