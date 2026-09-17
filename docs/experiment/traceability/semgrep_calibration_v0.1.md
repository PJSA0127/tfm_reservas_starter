# Calibración Semgrep — baseline seguro v0.1

**Clasificación:** desarrollo/calibración; no corresponde a la evaluación experimental definitiva.

## Implementación asociada

Referencia histórica del **repositorio de desarrollo anterior**: `ee6eec7` (`feat: add reproducible Semgrep SAST baseline`). Esta referencia se conserva únicamente para documentar el origen del mecanismo y **no corresponde al historial Git del repositorio experimental corregido actual**. La configuración pre-GitHub actual incorpora correcciones posteriores a dos reglas, fixtures sintéticos versionados y exclusiones explícitas de archivos generados. El commit definitivo del repositorio experimental se registrará cuando el nuevo historial sea inicializado y congelado.

## Configuración

- Semgrep CE: `1.177.0`.
- Imagen: `semgrep/semgrep:1.177.0-nonroot`.
- Reglas locales: 6.
- Objetivo: `app/`.
- Métricas: desactivadas.
- Exclusiones reproducibles: `**/__pycache__/**` y `**/*.pyc` mediante argumentos explícitos de Compose.

## Comandos de calibración

```powershell
docker compose --profile security pull semgrep
docker compose --profile security run --rm semgrep semgrep --version
docker compose --profile security run --rm semgrep
```

## Resultado observado

- versión reportada: `1.177.0`;
- 6 reglas ejecutadas;
- 14 archivos Git-tracked analizados;
- aproximadamente 100 % de líneas parseadas;
- 0 findings;
- scan completado correctamente;
- reporte generado: `artifacts/semgrep/semgrep-report.json`;
- validación positiva: 6 fixtures sintéticos, 6 findings, 6 reglas únicas, 0 errores;
- gate sintético: `PASS (6/6 rules detected exactly once)`;
- baseline repetido después de los fixtures: 0 findings.

## Interpretación

`0 findings` significa que las reglas SAST definidas fueron ejecutadas y no encontraron los patrones inseguros especificados. La validación positiva independiente demuestra además que las seis reglas disparan frente a sus patrones sintéticos controlados. No constituye por sí solo una certificación ni una demostración completa de cumplimiento ASVS.

La ejecución experimental normal no utiliza `--error` para convertir findings en fallos técnicos; el baseline seguro se valida mediante una comprobación de fase separada. La validación sintética 6/6 conserva su finalidad exclusiva de calibración.
