# OWASP ZAP DAST — configuración de calibración

**Estado:** DAST autenticado implementado y calibrado localmente; pendiente de piloto y congelación definitiva.

## Versión

- OWASP ZAP Core: `2.17.0`
- Imagen Docker: `zaproxy/zap-stable:2.17.0`
- Plan principal reutilizable: `security/zap/zap-plan.yaml`

Digest observado durante validación local pre-GitHub: `sha256:781a2bdaea47324e7bab583e2263f21d257b0aee61ed51521a5be45f5f5081ef`. Se volverá a confirmar antes del freeze definitivo.

## Arquitectura del laboratorio DAST

El perfil `dast` está aislado del entorno principal y de pytest:

- `db_dast`: PostgreSQL exclusivo;
- `dast_init`: reinicia el esquema y crea datos conocidos;
- `web_dast`: instancia Flask exclusiva;
- `zap`: Automation Framework.

`dast_init` crea un usuario de laboratorio y una reserva semilla. El active scan no debe apuntarse a entornos externos o productivos.

## Autenticación final calibrada

La configuración vigente se obtuvo a partir del Authentication Helper de ZAP y posteriormente se comprobó dentro del plan DAST:

- método: **Browser Authentication**;
- navegador: `firefox-headless`;
- pasos: `AUTO_STEPS`;
- login: `/auth/login`;
- verificación: `poll` contra `/reservations/`;
- autenticado: `200 OK`;
- no autenticado: `302 FOUND`;
- sesión: **Header-Based Session Management**.

Antes del spider se exigen cuatro solicitudes autenticadas con `HTTP 200`:

- `/reservations/`
- `/reservations/new`
- `/reservations/1`
- `/reservations/1/edit`

También deben pasar:

- `stats.auth.success >= 1`;
- `stats.auth.state.loggedin >= 1`;
- `stats.auth.browser.passed >= 1`.

Si falla la autenticación, el plan no debe continuar al active scan.

## Reglas dinámicas activas

| ID | Regla | Relación experimental |
|---:|---|---|
| 40012 | Cross Site Scripting (Reflected) | V1.2.1 / D01 |
| 40014 | Cross Site Scripting (Persistent) | V1.2.1 / D01 |
| 40018 | SQL Injection | V1.2.4 / D02 |

El alert pasivo `10202` (Absence of Anti-CSRF Tokens), cuando aplique, es evidencia complementaria para V3.5.1 / D04.

## Ejecución

```powershell
docker compose --profile dast pull zap
docker compose --profile dast run --rm --no-deps zap zap.sh -version

docker compose --profile dast down --remove-orphans
docker compose --profile dast up -d web_dast
docker compose --profile dast run --rm zap
```

## Evidencias esperadas

- `artifacts/zap/zap-report.json`
- `artifacts/zap/zap-report.html`
- directorio de recursos generado para el HTML moderno
- `artifacts/zap/zap-discovered-urls.txt`
- `artifacts/zap/web-dast.log` en CI
- directorio de recursos `artifacts/zap/zap-report*/**`

El clasificador del alcance experimental se ejecuta mediante:

```powershell
python .\scripts\ci\check_zap_relevant_findings.py `
  .\artifacts\zap\zap-report.json `
  .\artifacts\zap\zap-relevant-findings.json
```

## Calibración final observada

La ejecución final de calibración comprobó:

- autenticación: PASS;
- estado autenticado observado: PASS;
- Browser Authentication completado: PASS;
- spider: 12 URLs;
- active scan completado;
- reportes generados;
- clasificador experimental: PASS;
- HTTP 5xx no controlados durante DAST: 0;
- excepciones no controladas en `web_dast`: 0.

Hallazgos adicionales observados: 10020, 10021, 10036 y 10038. Informativos: 10111 y 10112. No se observaron 40012, 40014, 40018 ni 10202.

Estos hallazgos adicionales no forman parte de D01–D05 y no modifican la tasa de detección experimental. Durante calibración, un ID sintético fuera del rango de PostgreSQL reveló inicialmente un HTTP 500; se corrigió para responder 404 y quedó cubierto por una prueba funcional de regresión.

## Seguridad de credenciales

El Authentication Report diagnóstico puede incluir la contraseña de laboratorio en `afEnv`. No debe versionarse. Los reportes diagnósticos se mantienen dentro de rutas ignoradas por Git.

## Interpretación

La ausencia de alertas XSS/SQLi/CSRF no constituye por sí sola cumplimiento ASVS. ZAP es un mecanismo complementario dentro de la matriz requisito-prueba-evidencia.

## Nombres de evidencia y fase

Los nombres de los reportes son neutrales (`zap-report.json`, `zap-report.html`) porque el mismo plan se reutiliza en `calibration`, `pilot` y `proposed-definitive`. La fase concreta no se infiere del nombre del archivo: se registra en `zap-metadata.txt`, en el nombre del artifact de GitHub y en los metadatos del run.

Un hallazgo D01/D02/D04 clasificado durante `proposed-definitive` es evidencia experimental y no se interpreta como fallo técnico de ZAP. En `calibration` y `pilot` el workflow sí exige 0 hallazgos mapeados porque ambas fases utilizan el baseline seguro.
