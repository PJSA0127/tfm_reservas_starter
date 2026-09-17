# Semgrep Community Edition — configuración SAST v0.1

**Estado:** mecanismo implementado y calibrado localmente; pendiente de piloto y congelación definitiva.

## Versión utilizada

- Semgrep Community Edition: `1.177.0`
- Imagen Docker: `semgrep/semgrep:1.177.0-nonroot`
- Reglas locales: `security/semgrep/rules/`
- Objetivo: `app/`
- Métricas: desactivadas con `--metrics=off`
- Exclusiones explícitas: `**/__pycache__/**` y `**/*.pyc`
- Fixtures de validación positiva: `security/semgrep/fixtures/`

El uso de reglas locales evita que cambios posteriores en configuraciones remotas modifiquen silenciosamente el conjunto experimental.

## Reglas incluidas

| Regla | ASVS | Defecto | Propósito |
|---|---|---|---|
| `tfm.asvs.v121.jinja-safe-filter` | v5.0.0-1.2.1 | D01 | Detectar desactivación explícita del escape Jinja mediante `safe`. |
| `tfm.asvs.v121.explicit-markup` | v5.0.0-1.2.1 | D01 | Detectar usos de `Markup()` que requieran revisión. |
| `tfm.asvs.v124.raw-sql-fstring` | v5.0.0-1.2.4 | D02 | Detectar SQL construido mediante f-string en `text()`/`execute()`. |
| `tfm.asvs.v124.raw-sql-concatenation` | v5.0.0-1.2.4 | D02 | Detectar SQL construido por concatenación en `text()`/`execute()`. |
| `tfm.asvs.v351.csrf-exempt-route` | v5.0.0-3.5.1 | D04 | Detectar exclusiones explícitas de CSRF. |
| `tfm.asvs.v353.get-route-commits-state` | v5.0.0-3.5.3 | D05 | Detectar rutas GET que persisten cambios. |

## Ejecución

```powershell
docker compose --profile security run --rm semgrep semgrep --version
docker compose --profile security run --rm semgrep
```

## Calibración observada

Sobre el baseline seguro se comprobó:

- Semgrep `1.177.0`;
- 6 reglas ejecutadas;
- 14 archivos Git-tracked analizados;
- aproximadamente 100 % de líneas parseadas;
- `0 findings`;
- generación de `artifacts/semgrep/semgrep-report.json`;
- validación positiva 6/6: cada regla detectó exactamente una vez su fixture sintético;
- 0 errores del motor durante la validación;
- baseline posterior nuevamente en 0 findings.

El registro consolidado está en `docs/experiment/traceability/semgrep_calibration_v0.1.md`. Los fixtures son instrumentación de calibración/proceso propuesto y deben permanecer fuera del workspace convencional sanitizado.

## Alcance

Semgrep es complementario; no demuestra autónomamente cumplimiento ASVS.

- V1.2.1: `SEC-V121-01` + Semgrep + ZAP complementario.
- V1.2.4: `SEC-V124-01` + Semgrep + ZAP complementario.
- V2.2.1: prueba específica.
- V2.2.2: prueba específica.
- V3.5.1: `SEC-V351-01` es determinante; Semgrep/ZAP complementan.
- V3.5.3: `SEC-V353-01` + Semgrep/revisión de rutas.

`0 findings` significa únicamente que las reglas configuradas no encontraron sus patrones definidos. No equivale a una certificación ASVS.

## Reproducibilidad pendiente

Antes de la evaluación definitiva se registrará/fijará el digest exacto de la imagen Semgrep utilizada.

## Semántica de findings y ejecución

La ejecución normal del servicio Semgrep genera `artifacts/semgrep/semgrep-report.json` **sin utilizar `--error`**, para que un finding de `proposed-definitive` se conserve como resultado de seguridad y no se confunda con un fallo técnico del job. La fase `calibration`/`pilot` valida por separado que el baseline seguro permanezca en 0 findings.

La validación positiva con fixtures sintéticos sí puede utilizar `--error` porque su finalidad es comprobar deliberadamente que las seis reglas disparan sobre patrones conocidos; ese comportamiento pertenece a calibración del mecanismo y no a la semántica de la ejecución experimental definitiva.
