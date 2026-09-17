# Registro de ejecución piloto — v0.1

> Se completa únicamente durante la ejecución piloto real.

## Identificación general

| Campo | Valor |
|---|---|
| Fecha | PENDIENTE |
| Equipo investigador | PENDIENTE |
| I1 | PENDIENTE |
| I2 | PENDIENTE |
| I3 | PENDIENTE |
| Baseline | Calibración sin D01–D05 |
| Commit/tag baseline | PENDIENTE |

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

Si el piloto revela la necesidad de realizar posteriormente trabajo adicional de ajuste/configuración específica de un mecanismo, dicho trabajo se registra fuera de los Run IDs del piloto, con su propia actividad/registro observado, y puede clasificarse como **configuración inicial** del proceso correspondiente conforme al anteproyecto. No se permite doble contabilización.

## Incidencias y repetición

Si un run piloto es invalidado, se conserva con la marca:

```text
INVALIDATED — EXCLUDED FROM FINAL COMPARISON
```

y el nuevo intento recibe un identificador incremental, por ejemplo `PILOT-CONV-02` o `PILOT-PROP-02`.
