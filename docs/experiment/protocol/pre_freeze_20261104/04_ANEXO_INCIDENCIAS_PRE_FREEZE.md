# Anexo candidato — registro y disposición de incidencias definitivas

**Estado:** `CANDIDATO DOCUMENTAL PRE-FREEZE / REV-01..11 APROBADOS POR INTERLOCUTOR / TEXTO NO CONGELADO`. Complementa `incident_log_v0.1.md`, P07 de `proposed_procedure_v0.1.md` y el protocolo; REV-06.

## Clasificación sin alterar severidades originales

- **Tipo:** fallo técnico de infraestructura/lanzador, desviación procedimental, hallazgo de aplicación o seguridad, anomalía documental. El tipo no establece por sí solo severidad ni invalidez.
- **Severidad:** `BLOQUEANTE`, `MAYOR`, `MENOR`, `DOCUMENTAL`, aplicando las definiciones existentes.
- **Estado:** detectada, tratada, recuperada, no bloqueante, pendiente de decisión o cerrada, con procedencia; no falsear el estado histórico.
- **Reintento P07:** únicamente cuando el mecanismo tuvo fallo técnico y se cumplen restricciones congeladas, sin cambiar prueba/regla/criterio/configuración. El resultado de seguridad desfavorable no activa reintento. Preservar ambos intentos.

## Registro por incidencia

| Campo | Valor a registrar durante el run |
|---|---|
| ID y Run ID | PENDIENTE |
| Momento de detección ISO 8601 con offset | PENDIENTE |
| Fase/actividad/mecanismo | PENDIENTE |
| Tipo / severidad | PENDIENTE |
| Hecho técnico observable (sin reinterpretación) | PENDIENTE |
| Evidencia del intento original y hashes cuando proceda | PENDIENTE |
| Impacto en reproducibilidad, registro y continuidad | PENDIENTE |
| ¿Resultado de seguridad o fallo del mecanismo? | PENDIENTE |
| ¿Reintento P07 elegible? Justificación y autorización | PENDIENTE |
| Acción concreta y fecha/hora | PENDIENTE |
| Evidencia del intento recuperado / resultado | PENDIENTE |
| ¿Hay condición bloqueante? | PENDIENTE |
| Decisión I3 documentada | PENDIENTE |
| Consenso I1/I2/I3 para invalidez/cierre, si aplica | PENDIENTE |
| Estado final e impacto sobre el run | PENDIENTE |

## Criterio de continuidad y archivo

- Ante condición que impida completar el procedimiento, rompa las condiciones experimentales o comprometa evidencia esencial: escalar a I3 y decidir por consenso conforme al protocolo.
- Un run invalidado conserva su carpeta, registros, evidencias y tiempos; se excluye del comparativo definitivo y un nuevo intento utiliza otro Run ID.
- Un resultado de seguridad puede existir aun cuando la prueba o escaneo termine con señal distinta de `PASS`. No reejecutar para «confirmar» hallazgos.
- El anexo **no** cambia el número de reintentos ni crea nuevos tipos de test o condiciones de aprobación.
