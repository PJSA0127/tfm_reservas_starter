# TFM Reservas — laboratorio experimental de seguridad

Aplicación web demostrativa y laboratorio reproducible para el TFM **Trazabilidad de requisitos de seguridad y verificación continua basada en OWASP ASVS**.

El proyecto utiliza un subconjunto de seis requisitos OWASP ASVS 5.0.0 L1 y compara un proceso convencional de referencia con un proceso de verificación continua propuesto.

El documento académico rector es `TFM - G7.docx`.

El estado operacional vigente de las ejecuciones se mantiene en `ESTADO_ACTUAL_TFM.md`.

## Estado actual

El repositorio se encuentra en estado **pre-piloto**.

Baseline técnico congelado:

- tag: `pre-pilot-freeze-v0.1`;
- commit técnico: `32d27a04305617f8fea031704e24d7e68ce9c451`;
- D01–D05 introducidos: **NO**;
- CAL-01: `PASS`;
- CAL-02: `PASS`.

Estado operacional:

- `PILOT-CONV-01`: `READY_TO_START / NOT_STARTED`;
- `C00`: `NOT_STARTED`;
- cronómetro experimental: `NO INICIADO`;
- `PILOT-PROP-01`: `PREPARED_NOT_STARTED`;
- reset CONV → PROP: `PREPARED_NOT_EXECUTED`;
- versión experimental definitiva con D01–D05: `NO CREADA`.

La preparación técnica, las calibraciones y el freeze pre-piloto no constituyen resultados experimentales.

## Componentes implementados

El baseline seguro incluye:

- Flask + Jinja2 + Bootstrap 5;
- Flask-Login;
- Flask-WTF / CSRFProtect;
- SQLAlchemy + Psycopg 3;
- PostgreSQL 18 mediante Docker;
- CRUD reducido de reservas;
- reglas funcionales BR-01–BR-12;
- autoescape de Jinja2 como baseline de codificación de salida;
- acceso a datos mediante ORM y consultas parametrizadas;
- operaciones de cambio de estado mediante métodos HTTP apropiados al baseline seguro;
- 18 pruebas funcionales `pytest`;
- 22 pruebas específicas de seguridad utilizadas por el proceso propuesto;
- 40 pruebas totales ejecutadas satisfactoriamente durante calibración;
- Semgrep Community Edition 1.177.0 con 6 reglas locales versionadas y validación positiva 6/6 mediante fixtures sintéticos;
- OWASP ZAP 2.17.0 con DAST autenticado, laboratorio aislado y control de robustez sin HTTP 5xx no controlados;
- workflow manual de GitHub Actions exclusivo del proceso propuesto.

Durante la calibración técnica se ejecutaron satisfactoriamente las suites y mecanismos necesarios para validar el laboratorio.

Esos resultados corresponden a desarrollo y calibración y no forman parte de las métricas experimentales definitivas.

## Estructura relevante

- `app/` — aplicación Flask.
- `tests/functional/` — pruebas funcionales comunes.
- `tests/security/` — pruebas específicas del proceso propuesto.
- `security/semgrep/` — reglas y documentación SAST.
- `security/zap/` — planes y documentación DAST.
- `docs/experiment/protocol/` — protocolo, procedimientos e instrumentos.
- `docs/experiment/traceability/` — matrices y documentación de trazabilidad.
- `scripts/` — utilidades del laboratorio y CI.
- `.github/workflows/` — workflow manual del proceso propuesto.
- `evidence/` — evidencia experimental y metadatos de preparación.

## Preparación local de desarrollo

Estas instrucciones corresponden al entorno de desarrollo y mantenimiento del laboratorio.

No deben utilizarse para reconstruir arbitrariamente un workspace experimental ya congelado durante una ejecución.

### Variables de entorno

Crear `.env` a partir de `.env.example` cuando corresponda:

`Copy-Item .env.example .env`

### Construcción y arranque

`docker compose up -d --build web`

Compose espera a `db`, ejecuta `db_init` y posteriormente inicia `web`.

`db_init` debe finalizar correctamente con código `0`.

### Usuario local

Cuando sea necesario en un entorno de desarrollo:

`docker compose exec web flask --app app:create_app create-user`

Aplicación local:

`http://localhost:5000`

## Pruebas

### Pruebas funcionales comunes

`docker compose --profile test run --rm test`

Estas pruebas forman parte de las actividades comunes, pero durante un run experimental deben ejecutarse únicamente en el paso previsto por el protocolo.

### Pruebas específicas de seguridad

`docker compose --profile test run --rm test pytest -v tests/security`

Estas pruebas pertenecen al proceso propuesto.

**No deben ejecutarse durante `PILOT-CONV-01` ni durante la evaluación definitiva del proceso convencional.**

### Suite completa de calibración

`docker compose --profile test run --rm test pytest -v tests`

Este comando pertenece a actividades de desarrollo/calibración.

No debe utilizarse como sustituto de los pasos definidos por el protocolo durante un run experimental.

## Semgrep

Comandos de desarrollo/calibración:

- `docker compose --profile security run --rm semgrep semgrep --version`
- `docker compose --profile security run --rm semgrep`

El reporte se genera en:

`artifacts/semgrep/semgrep-report.json`

La ruta utiliza una denominación neutral y la fase correspondiente se registra mediante metadatos.

Semgrep pertenece al proceso propuesto y **no debe ejecutarse durante el proceso convencional**.

## OWASP ZAP

El DAST utiliza un entorno separado compuesto por:

- `db_dast`;
- `dast_init`;
- `web_dast`;
- `zap`.

Comandos de desarrollo/calibración:

- `docker compose --profile dast down --remove-orphans`
- `docker compose --profile dast up -d web_dast`
- `docker compose --profile dast run --rm zap`

Los reportes se generan en:

- `artifacts/zap/zap-report.json`;
- `artifacts/zap/zap-report.html`.

La configuración validada requiere autenticación satisfactoria antes de spider y active scan. Durante la calibración también se verificó que el DAST no produjera respuestas HTTP 5xx ni excepciones no controladas.

OWASP ZAP pertenece al proceso propuesto y **no debe ejecutarse durante el proceso convencional**.

## GitHub Actions

El workflow experimental del proceso propuesto es:

`.github/workflows/proposed-security-verification.yml`

Su ejecución es exclusivamente manual mediante `workflow_dispatch`.

Fases definidas:

- `calibration`;
- `pilot`;
- `proposed-definitive`.

No existe un workflow automático experimental en `push` o `pull_request`, para evitar contaminación de las ejecuciones.

Las GitHub Actions utilizadas por el workflow fueron fijadas por SHA completo antes del piloto.

Las dependencias Python relevantes se encuentran congeladas mediante `requirements.lock` y las imágenes técnicas utilizadas por el laboratorio fueron inmovilizadas mediante digest cuando corresponde.

`.github/dependabot.yml` se utiliza únicamente como apoyo durante desarrollo para revisar actualizaciones del ecosistema `github-actions`.

Una actualización sugerida por Dependabot no modifica automáticamente el baseline experimental congelado.

## Calibraciones remotas

Se completaron dos validaciones remotas previas al piloto.

### CAL-01

Objetivo: comprobar el funcionamiento real del workflow y sus artifacts en GitHub Actions.

Resultado: `PASS`.

### CAL-02

Objetivo: verificar que la inmovilización técnica de dependencias, imágenes y GitHub Actions mantuviera el comportamiento esperado del baseline seguro.

Resultado: `PASS`.

El commit técnico validado por CAL-02 es:

`32d27a04305617f8fea031704e24d7e68ce9c451`

CAL-01 y CAL-02 son calibraciones técnicas.

**No son ejecuciones de `PILOT-CONV-01` ni `PILOT-PROP-01`.**

## Seguridad de archivos locales

No deben versionarse archivos o resultados locales que no formen parte deliberadamente del repositorio, entre ellos:

- `.env`;
- artifacts temporales;
- reportes diagnósticos locales;
- caches;
- archivos de ejecución no destinados a Git.

`.dockerignore` evita que elementos locales innecesarios entren accidentalmente al contexto de construcción Docker.

La evidencia experimental se gestiona conforme a `docs/experiment/protocol/evidence_archival_v0.1.md`.

## Proceso convencional

El proceso convencional utiliza un workspace sanitizado construido mediante allowlist.

Para `PILOT-CONV-01` existen:

- workspace sanitizado de preparación: `D:\Repositorios\tfm_reservas_pilot_conv`;
- workspace de ejecución: `D:\Repositorios\tfm_reservas_pilot_conv_run`.

Este workspace procede del baseline seguro sin D01–D05.

Durante el proceso convencional está prohibido utilizar como guía:

- OWASP ASVS explícito;
- catálogo D01–D05;
- ubicación o mappings de defectos;
- matriz requisito-prueba-evidencia;
- pruebas específicas de seguridad;
- Semgrep;
- OWASP ZAP;
- workflow del proceso propuesto;
- pruebas ad hoc destinadas a confirmar sospechas.

## Proceso propuesto

El workspace pre-piloto del proceso propuesto está preparado, pero su runtime no se inicia antes del cierre de `PILOT-CONV-01` y del reset formal correspondiente.

El proceso propuesto incorpora, además de las actividades comunes:

- requisitos OWASP ASVS seleccionados de forma explícita;
- matriz requisito-prueba-evidencia;
- pruebas específicas de seguridad;
- Semgrep;
- OWASP ZAP;
- GitHub Actions;
- conservación sistemática de evidencias.

## Secuencia del piloto

La secuencia vigente es:

`revalidación mínima → C00 → C01 → C02 → C03 → C04 → C05 → C06 → cierre y archivo → reset → PILOT-PROP-01`

Antes de C00 no deben repetirse freezes, hashes, calibraciones o reconstrucciones ya cerradas salvo evidencia concreta de inconsistencia.

Los resultados y tiempos de ejecución propiamente dichos del piloto no forman parte de la comparación experimental definitiva.

## Versión experimental definitiva

D01–D05 **todavía no han sido introducidos**.

La versión experimental definitiva se preparará únicamente después de:

1. completar ambos pilotos;
2. analizar sus incidencias y lecciones;
3. aplicar únicamente los ajustes permitidos;
4. versionar los instrumentos modificados, si corresponde;
5. congelar el protocolo experimental definitivo;
6. introducir de forma controlada D01–D05;
7. validar la funcionalidad y correspondencia de los defectos;
8. fijar el commit/tag experimental definitivo.

La misma versión experimental definitiva será utilizada como origen técnico para:

- `DEF-CONV-01`;
- `DEF-PROP-01`.

No se modificará el código entre ambas evaluaciones definitivas.

## Jerarquía documental

La jerarquía vigente es:

`TFM - G7 → PROTOCOLO EXPERIMENTAL → INSTRUMENTOS / DOCUMENTACIÓN TÉCNICA → CÓDIGO / AUTOMATIZACIÓN / EJECUCIONES / EVIDENCIAS`

Un artefacto inferior no puede redefinir una decisión establecida por un nivel superior.

`ESTADO_ACTUAL_TFM.md` constituye la fuente de verdad del estado operacional vigente.

El Gantt se utiliza para planificación y seguimiento temporal, no para determinar automáticamente qué paso experimental puede ejecutarse.
