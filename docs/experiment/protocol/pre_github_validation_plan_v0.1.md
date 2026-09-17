# Plan de validación integral pre-GitHub — v0.1

## Estado

**COMPLETADO LOCALMENTE.**

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

## Pendiente posterior

- primer push;
- ejecución `calibration` real;
- revisión de artifacts;
- SHAs inmutables;
- pilotaje;
- freeze.
