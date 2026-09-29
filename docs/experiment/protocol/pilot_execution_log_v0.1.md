# Registro de ejecución piloto — v0.2

> Los datos observacionales de ejecución se completan únicamente durante el piloto real. Los metadatos estables conocidos antes de C00 pueden quedar preidentificados sin que ello constituya inicio del run.

## Identificación general

| Campo | Valor |
|---|---|
| Fecha | PENDIENTE |
| Equipo investigador | Jorge, Carlos y Paulo |
| I1 | Paulo — Ejecutor principal |
| I2 | Carlos — Registrador de evidencia y esfuerzo |
| I3 | Jorge — Supervisor del protocolo |
| Baseline | Baseline seguro pre-piloto sin D01–D05 |
| Commit/tag baseline | `32d27a04305617f8fea031704e24d7e68ce9c451` / `pre-pilot-freeze-v0.1` |
| Registro de roles | `investigator_role_assignment_v0.1.md` |
| SHA-256 registro de roles | `219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631` |

## Runs previstos

| Etapa | Run ID | Inicio | Fin | Estado | Esfuerzo observado | Tiempo automático | Incidencias | Evidencia |
|---|---|---|---|---|---:|---:|---|---|
| Convencional piloto | `PILOT-CONV-01` | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| Reset | N/A | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| Propuesto piloto | `PILOT-PROP-01` | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| Revisión de instrumentos | N/A | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | N/A | PENDIENTE | PENDIENTE |

## Resultado del reset

| Verificación | Resultado | Evidencia |
|---|---|---|
| cierre y archivo de `PILOT-CONV-01` | PENDIENTE | PENDIENTE |
| contenedores/volúmenes recreados | PENDIENTE | PENDIENTE |
| commit/tag restaurado | PENDIENTE | PENDIENTE |
| BD/datos iniciales restaurados | PENDIENTE | PENDIENTE |
| perfil de navegador limpio | PENDIENTE | PENDIENTE |
| healthcheck/operación mínima | PENDIENTE | PENDIENTE |
| autorización I3 para iniciar `PILOT-PROP-01` | PENDIENTE | PENDIENTE |

## Tratamiento del tiempo

Los tiempos observados correspondientes a la **ejecución de `PILOT-CONV-01`, el reset experimental y `PILOT-PROP-01`** se conservan como evidencia de calibración y no forman parte de M2 definitivo.

Si el piloto revela la necesidad de realizar posteriormente trabajo adicional de ajuste/configuración específica de un mecanismo, dicho trabajo se registra fuera de los Run IDs del piloto, con su propia actividad/registro observado, y puede clasificarse como **configuración inicial** del proceso correspondiente conforme a `TFM - G7.docx`. No se permite doble contabilización.

## Incidencias y repetición

Si un run piloto es invalidado, se conserva con la marca:

```text
INVALIDATED — EXCLUDED FROM FINAL COMPARISON
```

y el nuevo intento recibe un identificador incremental, por ejemplo `PILOT-CONV-02` o `PILOT-PROP-02`.
