# Sanitización del workspace convencional — v0.2

## Estado

**WORKSPACE PRE-PILOTO PREPARADO Y VALIDADO / PILOTO NO INICIADO**

Este documento describe las reglas de construcción y sanitización del workspace convencional y registra la preparación realizada para `PILOT-CONV-01`.

El estado operacional vigente de la ejecución debe consultarse en `ESTADO_ACTUAL_TFM.md`.

La preparación y validación del workspace no implica que el piloto haya comenzado.

## Objetivo

Construir un workspace convencional que permita ejecutar exactamente las actividades previstas por `TFM - G7.docx` sin exponer mecanismos, resultados o documentación exclusivos del proceso propuesto.

La sanitización no pretende crear cegamiento completo respecto de la existencia general de D01–D05, porque el TFM reconoce que el equipo investigador conoce su existencia.

Su finalidad es impedir que durante la ejecución convencional se consulte información que revele:

- la naturaleza concreta de los defectos;
- su ubicación o manifestación;
- su correspondencia con los requisitos OWASP ASVS;
- resultados o mecanismos exclusivos del proceso propuesto.

## Principio de construcción

El workspace convencional se construye mediante una **allowlist de contenidos permitidos**.

No se utilizará como estrategia principal copiar el repositorio completo y eliminar selectivamente archivos, porque esa aproximación aumenta el riesgo de contaminación accidental.

La copia convencional debe derivarse del mismo origen técnico que corresponda a la fase experimental ejecutada y conservar sin modificaciones los componentes comunes relevantes.

## Distinción entre piloto y evaluación definitiva

Existen dos contextos diferentes para la construcción del workspace convencional.

### Piloto

`PILOT-CONV-01` utiliza el baseline seguro pre-piloto:

- tag: `pre-pilot-freeze-v0.1`;
- commit técnico: `32d27a04305617f8fea031704e24d7e68ce9c451`;
- D01–D05 introducidos: **NO**.

Por tanto, durante el piloto **no corresponde exigir la presencia de D01–D05** como condición de equivalencia.

La equivalencia debe comprobarse respecto del baseline seguro utilizado también como origen del workspace propuesto pre-piloto.

### Evaluación definitiva

Después de completar ambos pilotos, analizar sus incidencias, aplicar únicamente los ajustes permitidos y congelar el protocolo definitivo, se preparará la versión experimental definitiva con D01–D05.

El workspace convencional destinado a `DEF-CONV-01` deberá derivarse de esa misma versión experimental definitiva utilizada posteriormente por `DEF-PROP-01`.

En ese contexto sí deberá verificarse que los componentes comunes conservan los mismos D01–D05 controlados.

El workspace preparado actualmente para `PILOT-CONV-01` **no debe describirse como el workspace definitivo de `DEF-CONV-01`**.

## Contenido permitido

Como mínimo, el paquete convencional puede incluir los componentes comunes necesarios, entre ellos:

- `app/`
- `tests/functional/`
- `pyproject.toml`
- `Dockerfile`
- `.env.example`

Además puede incluir únicamente la documentación e instrumentos necesarios para ejecutar el procedimiento convencional, por ejemplo:

- `docs/experiment/protocol/business_rules_v0.1.md`
- `docs/experiment/protocol/conventional_procedure_v0.2.md`
- `docs/experiment/protocol/run_record_template_v0.1.md`
- `docs/experiment/protocol/effort_log_v0.1.md`
- `docs/experiment/protocol/incident_log_v0.1.md`

El archivo Compose utilizado por el proceso convencional debe contener únicamente los servicios necesarios para:

- aplicación;
- PostgreSQL;
- inicialización;
- pruebas funcionales comunes.

No debe exponer servicios Semgrep, OWASP ZAP ni otros mecanismos exclusivos del proceso propuesto.

## Contenido excluido

El workspace convencional no debe incluir, como mínimo:

- `tests/security/`
- `security/`
- `scripts/ci/`
- `.github/`
- `docs/experiment/traceability/`
- `artifacts/`

También debe excluir cualquier otro archivo que revele de forma explícita:

- catálogo detallado D01–D05;
- ubicación o manifestación concreta de los defectos;
- correspondencia D01–D05 ↔ ASVS;
- matriz requisito-prueba-evidencia utilizada como guía del proceso propuesto;
- reglas, configuraciones o resultados Semgrep;
- planes, configuraciones o resultados OWASP ZAP;
- pruebas específicas de seguridad;
- clasificadores de hallazgos experimentales;
- resultados de ejecuciones previas del proceso propuesto;
- artifacts de calibración o evaluación;
- fixtures sintéticos de validación de herramientas.

## README convencional

El paquete convencional utiliza un README mínimo específico.

No debe copiarse sin revisión el README raíz del repositorio completo cuando este describa ASVS, Semgrep, ZAP, CI o el catálogo experimental de una forma que pueda orientar indebidamente la ejecución convencional.

## Pruebas funcionales

`tests/functional/` forma parte del proceso convencional y debe estar disponible en la revisión congelada correspondiente.

La suite funcional común no puede modificarse entre el proceso convencional y el proceso propuesto de una misma fase experimental.

## Equivalencia técnica

La sanitización no crea una versión funcional diferente de la aplicación.

La equivalencia debe demostrarse mediante:

- referencia al mismo commit origen;
- manifiesto SHA-256 de los archivos permitidos;
- equivalencia de `app/`;
- equivalencia de `tests/functional/`;
- mismas dependencias comunes;
- mismas reglas de negocio;
- mismos datos iniciales;
- misma configuración funcional común.

En el piloto se verifica equivalencia respecto del baseline seguro.

En la evaluación definitiva se verificará equivalencia respecto de la versión experimental definitiva con D01–D05.

El árbol completo del workspace sanitizado no será idéntico al repositorio original porque excluye intencionalmente mecanismos exclusivos del proceso propuesto.

Por tanto, la equivalencia se demuestra mediante el origen técnico y los hashes de los componentes comunes, no mediante identidad completa entre árboles.

## Comprobación de contaminación

Antes de habilitar el workspace convencional se debe realizar una búsqueda transversal de términos y rutas sensibles, incluyendo como mínimo:

- `ASVS`
- `D01`
- `D02`
- `D03`
- `D04`
- `D05`
- `Semgrep`
- `ZAP`
- `security_test`
- `zap_mapping`
- `semgrep_mapping`

Cada coincidencia debe revisarse.

Una coincidencia únicamente puede permanecer cuando sea estrictamente necesaria para una actividad convencional permitida y no revele información exclusiva del proceso propuesto.

## Validación técnica previa

Antes de utilizar el paquete se comprueba:

1. que la aplicación construye y arranca;
2. que PostgreSQL y la inicialización funcionan;
3. que `tests/functional/` está presente y corresponde a la suite funcional congelada; la ejecución experimental se reserva para C01;
4. que no existen servicios o comandos exclusivos del proceso propuesto;
5. que no existen artifacts previos dentro del workspace de ejecución;
6. que la equivalencia de los componentes comunes queda registrada;
7. que el contenido del paquete coincide con su manifiesto;
8. que los hashes de preparación son reproducibles.

## Registro de preparación de PILOT-CONV-01

| Campo | Valor |
|---|---|
| Fase | Piloto |
| Run ID | `PILOT-CONV-01` |
| Estado del artefacto de preparación | `PASS` |
| Estado operacional actual | `READY_TO_START / NOT_STARTED` |
| Tag técnico origen | `pre-pilot-freeze-v0.1` |
| Commit técnico origen | `32d27a04305617f8fea031704e24d7e68ce9c451` |
| Workspace sanitizado de preparación | `D:\Repositorios\tfm_reservas_pilot_conv` |
| Workspace de ejecución | `D:\Repositorios\tfm_reservas_pilot_conv_run` |
| Cantidad de archivos congelados | `31` |
| Manifest SHA-256 | `bdd96f0aef922b90442d6ab24740f9d6e36d0de644db5525ed4ab862e7df2bd2` |
| Paquete | `conventional_workspace_PILOT-CONV-01.zip` |
| SHA-256 del paquete | `f06736398a1aafc8cd3052e4fedea8d469b2af29cffac8e6b9e4821e012fe459` |
| Verificación del contenido del paquete | `PASS` |
| Equivalencia del workspace | `PASS` |
| Verificación de rutas prohibidas | `PASS` |
| Validación Compose | `PASS` |
| Casos manuales | `v0.1` |
| Commit documental casos manuales | `a540595666d1a2ca88429dd1a732cfdd266d3477` |
| SHA-256 casos manuales | `f83c2252ea1b77acc6f9bfe6d391b3cbae3a198b4d3f9a2cd177cd5dd0092ef1` |
| Responsable operativo de preparación para futuras ejecuciones | I2 — Carlos |
| Responsable operativo de revisión para futuras ejecuciones | I3 — Jorge |
| Piloto iniciado | `NO` |

La asignación nominal vigente es:

- I1 — Ejecutor principal: **Paulo**;
- I2 — Registrador de evidencia y esfuerzo: **Carlos**;
- I3 — Supervisor del protocolo: **Jorge**.

Registro: `investigator_role_assignment_v0.1.md`.

SHA-256: `219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631`.

Esta asignación aplica a las ejecuciones posteriores a su formalización. No se atribuyen retroactivamente a Carlos o Jorge las acciones de preparación histórica ya cerradas antes de crear el registro.

Los valores anteriores describen la preparación ya realizada y no constituyen resultados experimentales del piloto.

## Estado funcional observado durante la preparación

Durante la validación pre-piloto quedó registrado:

| Control | Resultado |
|---|---|
| Base de datos | `healthy` |
| Aplicación web | `healthy` |
| Inicialización de BD | `exit 0` |
| Endpoint `/health` | `HTTP 200` |
| Usuarios piloto | `2` |
| Reservas iniciales | `0` |
| Servicio `db_test` | inactivo |

Estos datos forman parte de la validación de preparación.

Antes de C00 solo deberá realizarse la revalidación mínima del estado volátil establecida en el protocolo y en `ESTADO_ACTUAL_TFM.md`.

No se repetirán freezes, hashes o reconstrucciones ya cerradas salvo evidencia real de inconsistencia.

## Regla de freeze

El workspace convencional preparado para `PILOT-CONV-01` está congelado como artefacto de preparación.

No se añadirán ni eliminarán contenidos durante el run.

Si una incidencia técnica impide mantener las condiciones experimentales y obliga a invalidar la ejecución, se aplicará el procedimiento previsto por el protocolo.

La evidencia ya cerrada y protegida mediante SHA-256 no debe modificarse retroactivamente.

La preparación futura del workspace de `DEF-CONV-01` deberá realizarse después del piloto y utilizar como origen la versión experimental definitiva congelada con D01–D05.

## Instrumentos convencionales vigentes para la reconstrucción

- `docs/experiment/protocol/business_rules_v0.1.md`
- `docs/experiment/protocol/manual_cases_v0.2.md`
- `docs/experiment/protocol/conventional_procedure_v0.2.md`
## Preparación requerida para PILOT-CONV-02

Antes de generar el nuevo workspace convencional:

1. `manual_cases_v0.2.md` debe superar la revalidación controlada;
2. `conventional_procedure_v0.2.md` debe quedar aprobado;
3. debe reconstruirse el workspace sanitizado desde el mismo baseline técnico seguro `pre-pilot-freeze-v0.1`;
4. deben incorporarse únicamente los instrumentos convencionales vigentes;
5. debe repetirse la comprobación de contaminación;
6. debe generarse un nuevo manifiesto SHA-256;
7. debe verificarse nuevamente la equivalencia de `app/` y `tests/functional/`;
8. debe generarse un nuevo paquete específico para `PILOT-CONV-02`;
9. la preparación de `PILOT-CONV-01` permanece únicamente como antecedente histórico.

El workspace y paquete de `PILOT-CONV-01` no se reutilizan como artefacto congelado de `PILOT-CONV-02`.

## Control de cambios post-piloto

La presente versión se normaliza canónicamente como `conventional_workspace_sanitization_v0.2.md`.

Los cambios responden únicamente a la invalidación de `PILOT-CONV-01` y al versionado de los instrumentos convencionales. No modifican el baseline técnico ni introducen D01–D05.