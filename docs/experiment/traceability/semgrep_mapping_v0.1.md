# Correspondencia SAST — ASVS 5.0.0 v0.1

| ASVS | Prueba específica | Regla(s) Semgrep | Rol del SAST |
|---|---|---|---|
| `v5.0.0-1.2.1` | `SEC-V121-01` | `SEM-V121-01`, `SEM-V121-02` | Detectar mecanismos explícitos que desactiven el escape contextual. |
| `v5.0.0-1.2.4` | `SEC-V124-01` | `SEM-V124-01`, `SEM-V124-02` | Detectar construcción evidente de SQL dinámico no parametrizado. |
| `v5.0.0-2.2.1` | `SEC-V221-01` | — | La semántica de reglas de negocio se comprueba mediante pruebas específicas. |
| `v5.0.0-2.2.2` | `SEC-V222-01` | — | La aplicación en capa confiable se comprueba mediante solicitudes directas al servidor. |
| `v5.0.0-3.5.1` | `SEC-V351-01` | `SEM-V351-01` | Evidencia complementaria para detectar exclusiones explícitas de CSRF. |
| `v5.0.0-3.5.3` | `SEC-V353-01` | `SEM-V353-01` | Detectar una ruta GET que persista modificación de estado. |

## Interpretación

Un resultado de `0 findings` en el baseline seguro demuestra únicamente que **las reglas SAST definidas fueron ejecutadas y no encontraron los patrones inseguros especificados**. No debe interpretarse aisladamente como cumplimiento completo de un requisito ASVS.

La determinación final de “verificado / no verificado” se realizará usando el conjunto de mecanismos y la evidencia mínima fijada para cada requisito.
