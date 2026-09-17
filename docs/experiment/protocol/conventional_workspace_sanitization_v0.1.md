# Sanitización del workspace convencional — v0.1

## Objetivo

Construir un workspace convencional que permita ejecutar exactamente las actividades previstas por el anteproyecto sin exponer mecanismos, resultados o documentación exclusivos del proceso propuesto.

La sanitización **no pretende crear cegamiento completo** respecto de la existencia general de D01–D05, porque el anteproyecto reconoce que el equipo investigador conoce su existencia. Su finalidad es impedir que durante la ejecución convencional se consulte información que revele la naturaleza concreta, ubicación o correspondencia de los defectos con ASVS o con las herramientas del proceso propuesto.

## Principio de construcción

El workspace convencional se construirá mediante una **allowlist de contenidos permitidos**. No se utilizará como estrategia principal copiar el repositorio completo y borrar selectivamente algunos archivos, porque esa aproximación aumenta el riesgo de contaminación accidental.

La copia convencional debe derivarse de la misma revisión experimental utilizada por el proceso propuesto y conservar sin modificaciones el código de aplicación, los defectos controlados, las dependencias comunes y las pruebas funcionales fijadas.

## Contenido permitido

Como mínimo, el paquete convencional podrá incluir:

```text
app/
tests/functional/
pyproject.toml
Dockerfile
.env.example
```

Además podrá incluir únicamente la documentación e instrumentos necesarios para ejecutar el procedimiento convencional, por ejemplo:

```text
docs/experiment/protocol/business_rules_v0.1.md
docs/experiment/protocol/conventional_procedure_v0.1.md
docs/experiment/protocol/run_record_template_v0.1.md
docs/experiment/protocol/effort_log_v0.1.md
docs/experiment/protocol/incident_log_v0.1.md
```

El archivo Compose utilizado por el proceso convencional deberá contener únicamente los servicios necesarios para la aplicación y las pruebas funcionales comunes. No debe exponer servicios Semgrep, ZAP ni otros mecanismos exclusivos del proceso propuesto.

## Contenido excluido

El workspace convencional no debe incluir, como mínimo:

```text
tests/security/
security/
scripts/ci/
.github/
docs/experiment/traceability/
artifacts/
```

También se excluirá cualquier otro archivo que revele de forma explícita:

- el catálogo detallado D01–D05;
- la ubicación o manifestación concreta de los defectos;
- la correspondencia D01–D05 ↔ ASVS;
- la matriz requisito-prueba-evidencia utilizada como guía del proceso propuesto;
- reglas, configuraciones o resultados Semgrep;
- planes, configuraciones o resultados ZAP;
- pruebas específicas de seguridad;
- clasificadores de hallazgos experimentales;
- resultados de ejecuciones previas del proceso propuesto;
- artifacts de calibración o de evaluación;
- fixtures sintéticos de validación de herramientas.

## README convencional

El paquete convencional utilizará un README mínimo específico para esa ejecución. No se copiará sin revisión el README raíz del repositorio completo si este describe ASVS, Semgrep, ZAP, CI o el catálogo experimental de manera que pueda orientar indebidamente la ejecución convencional.

## Pruebas funcionales

`tests/functional/` **forma parte del proceso convencional**, de acuerdo con el anteproyecto, y debe estar disponible en la versión congelada correspondiente.

No se modificará la suite funcional entre la ejecución convencional y la propuesta.

## Equivalencia con la versión experimental

La sanitización no crea una versión funcional distinta de la aplicación.

Se deberá demostrar que el workspace convencional deriva del mismo commit experimental y conserva exactamente los componentes comunes relevantes. Como mínimo se comprobará:

- hash del contenido de `app/`;
- hash del contenido de `tests/functional/`;
- dependencias comunes;
- reglas de negocio;
- datos iniciales;
- configuración funcional común;
- presencia de los mismos defectos D01–D05 en la aplicación experimental.

El hecho de excluir instrumentación exclusiva del proceso propuesto significa que el árbol completo del workspace sanitizado no será idéntico al árbol Git original. Por ello, la equivalencia se demostrará mediante la referencia al commit origen y hashes de los componentes comunes, no mediante la afirmación de que ambos árboles son idénticos.

## Comprobación de contaminación

Antes de entregar el workspace convencional se realizará una búsqueda transversal de términos y rutas sensibles, incluyendo como mínimo:

```text
ASVS
D01
D02
D03
D04
D05
Semgrep
ZAP
security_test
zap_mapping
semgrep_mapping
```

Cada coincidencia deberá revisarse. Una coincidencia solo podrá permanecer si es estrictamente necesaria para una actividad convencional permitida y no revela información exclusiva del proceso propuesto.

## Validación técnica previa

Antes de utilizar el paquete se comprobará:

1. que la aplicación construye y arranca;
2. que PostgreSQL y la inicialización funcionan;
3. que `tests/functional/` puede ejecutarse;
4. que no existen servicios o comandos exclusivos del proceso propuesto;
5. que no existen artifacts previos;
6. que la equivalencia de los componentes comunes ha sido registrada.

## Registro

| Campo | Valor |
|---|---|
| Commit experimental origen | PENDIENTE |
| Paquete/branch/worktree convencional | PENDIENTE |
| Responsable de preparación | PENDIENTE |
| Responsable de revisión | PENDIENTE |
| Hash `app/` origen | PENDIENTE |
| Hash `app/` convencional | PENDIENTE |
| Hash `tests/functional/` origen | PENDIENTE |
| Hash `tests/functional/` convencional | PENDIENTE |
| Resultado de búsqueda de contaminación | PENDIENTE |
| Resultado de validación funcional | PENDIENTE |
| Hash del paquete final | PENDIENTE |

## Regla de freeze

Una vez validado y congelado el workspace convencional, no se añadirán ni eliminarán contenidos durante la ejecución definitiva salvo que una incidencia bloquee el experimento y obligue a invalidar el run conforme al protocolo.
