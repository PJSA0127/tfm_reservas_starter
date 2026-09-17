# TFM Reservas — laboratorio experimental de seguridad

Aplicación web demostrativa y laboratorio reproducible para el TFM sobre **trazabilidad de requisitos de seguridad y verificación continua basada en OWASP ASVS 5.0.0 L1**.

## Estado actual

La rama de trabajo representa el **baseline seguro de calibración**. Todavía no contiene los defectos controlados D01–D05 y no constituye aún el protocolo experimental congelado.

Componentes implementados y calibrados localmente:

- Flask + Jinja2 + Bootstrap 5.
- Flask-Login.
- Flask-WTF / CSRFProtect.
- SQLAlchemy + Psycopg 3.
- PostgreSQL 18 mediante Docker.
- CRUD reducido de reservas.
- Validación de servidor documentada mediante reglas BR-01–BR-12.
- Autoescape de Jinja2 como baseline de codificación de salida.
- Acceso a datos mediante ORM/consultas parametrizadas.
- Operaciones de cambio de estado mediante métodos HTTP no seguros.
- 18 pruebas funcionales `pytest`.
- 22 pruebas específicas de seguridad `pytest`.
- 40 pruebas totales ejecutadas satisfactoriamente durante calibración.
- Semgrep CE 1.177.0 con 6 reglas locales versionadas y validación positiva 6/6 mediante fixtures sintéticos.
- OWASP ZAP 2.17.0 con DAST autenticado, laboratorio aislado y control de robustez sin HTTP 5xx no controlados.
- Workflow manual de GitHub Actions para el **proceso propuesto**.

Los resultados anteriores son evidencia de **desarrollo/calibración**, no resultados de la evaluación experimental definitiva.

## Estructura relevante

```text
app/                         Aplicación Flask

tests/functional/            Pruebas funcionales comunes

tests/security/              Pruebas específicas del proceso propuesto

security/semgrep/            Reglas y documentación SAST

security/zap/                Planes y documentación DAST

docs/experiment/protocol/    Procedimiento, reglas y documentación de ejecución

docs/experiment/traceability/ Matrices y registros de calibración

scripts/                     Utilidades de laboratorio/CI

.github/workflows/           CI manual exclusiva del proceso propuesto
```

## Preparación local

1. Copiar `.env.example` a `.env`:

   ```powershell
   Copy-Item .env.example .env
   ```

2. Construir y levantar la aplicación:

   ```powershell
   docker compose up -d --build web
   ```

   Compose espera a `db`, ejecuta automáticamente `db_init` y solo después inicia `web`. `db_init` debe finalizar con código `0`; no es necesario ejecutar `init-db` manualmente.

3. Crear un usuario local cuando sea necesario:

   ```powershell
   docker compose exec web flask --app app:create_app create-user
   ```

4. Abrir `http://localhost:5000`.

## Pruebas

### Funcionales

```powershell
docker compose --profile test run --rm test
```

### Seguridad específica

```powershell
docker compose --profile test run --rm test pytest -v tests/security
```

### Suite completa de calibración

```powershell
docker compose --profile test run --rm test pytest -v tests
```

## Semgrep

```powershell
docker compose --profile security run --rm semgrep semgrep --version
docker compose --profile security run --rm semgrep
```

El reporte local se escribe en `artifacts/semgrep/semgrep-report.json`. El nombre es deliberadamente neutro para que la misma ruta pueda utilizarse en `calibration`, `pilot` y `proposed-definitive`; la fase se registra en los metadatos del run.

## OWASP ZAP

El DAST utiliza un laboratorio separado (`db_dast`, `dast_init`, `web_dast`, `zap`) para no modificar la base principal ni la base de pruebas.

```powershell
docker compose --profile dast down --remove-orphans
docker compose --profile dast up -d web_dast
docker compose --profile dast run --rm zap
```

`web_dast` depende de `db_dast` healthy y de `dast_init` completado correctamente, por lo que el seed se ejecuta automáticamente. Durante calibración se confirmó además que el scan no provoca respuestas HTTP 5xx ni excepciones no controladas.

La configuración final de calibración exige autenticación satisfactoria antes de ejecutar spider y active scan. Los reportes se generan como `artifacts/zap/zap-report.json` y `artifacts/zap/zap-report.html`; la fase experimental se identifica mediante metadatos y no mediante el nombre del archivo.

## GitHub Actions

Solo existe el workflow experimental:

```text
.github/workflows/proposed-security-verification.yml
```

Durante desarrollo, `.github/dependabot.yml` revisa únicamente actualizaciones del ecosistema `github-actions`. Es un mecanismo de apoyo; antes del piloto/freeze las Actions usadas experimentalmente se fijarán por SHA completo.

Se ejecuta exclusivamente mediante `workflow_dispatch` y ofrece las fases:

- `calibration`
- `pilot`
- `proposed-definitive`

**No debe ejecutarse durante la evaluación definitiva del proceso convencional.** No existe un workflow automático en `push`/`pull_request` para evitar contaminación experimental.

## Seguridad de archivos locales

No deben versionarse:

- `.env`
- `artifacts/`
- reportes diagnósticos de autenticación ZAP
- caches locales

El archivo `.dockerignore` evita además que estos elementos entren accidentalmente al contexto de construcción Docker.

## Estrategia experimental

No introducir D01–D05 todavía.

Antes de construir la versión experimental con defectos controlados deben completarse, entre otros:

1. validación exhaustiva local completada y validación remota de CI pendiente;
2. procedimiento convencional fijo;
3. instrumento independiente de cobertura;
4. protocolo piloto;
5. manifiesto reproducible del entorno;
6. workspace convencional sanitizado;
7. ejecución piloto sobre baseline seguro;
8. congelación del protocolo y de versiones/digests.

Después se generará `experiment-v1`, usado de forma idéntica por ambos procesos en la evaluación definitiva.
