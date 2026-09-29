# Protocolo experimental — índice documental v0.6

**Estado general:** PREPARADO PARA PILOTAJE / PILOTO NO INICIADO
**Documento rector:** `TFM - G7.docx`
**Fuente de verdad del estado operacional:** `ESTADO_ACTUAL_TFM.md`
**Marco:** OWASP ASVS 5.0.0 L1

## Jerarquía documental

En caso de discrepancia, se aplica el siguiente orden:

1. `TFM - G7.docx`;
2. protocolo experimental;
3. instrumentos y documentación técnica;
4. código, automatización, ejecuciones y evidencias.

Un artefacto de nivel inferior no puede redefinir una decisión establecida por un nivel superior.

El protocolo no redefine el diseño académico: lo operacionaliza.

`Diagrama de Gantt - TFM - G7B-1.md` se utiliza para planificación y seguimiento temporal, pero no sustituye al protocolo ni al estado operacional vigente.

## Estado de preparación

El baseline técnico pre-piloto fue validado mediante CAL-01 y CAL-02 y quedó congelado para la fase piloto.

También fueron preparados y validados:

- el workspace convencional sanitizado;
- el workspace del proceso propuesto;
- la suite funcional común;
- los instrumentos de registro;
- las rutas de evidencia primaria y secundaria;
- los mecanismos de integridad mediante SHA-256;
- las configuraciones de Semgrep y OWASP ZAP;
- el workflow del proceso propuesto;
- las dependencias, imágenes y GitHub Actions necesarias para el freeze técnico pre-piloto.

Los valores operacionales vigentes, hashes, commits, tags, sellos de preparación y estado exacto de los runs deben consultarse en `ESTADO_ACTUAL_TFM.md` y en las evidencias correspondientes.

La preparación técnica no implica que el piloto haya comenzado.

## Diseño vigente derivado del TFM

La evaluación compara:

1. un proceso convencional de referencia;
2. el proceso de verificación continua propuesto.

Ambos se aplican sobre la misma versión experimental y bajo condiciones comparables.

La ejecución definitiva contempla:

- una ejecución completa del proceso convencional;
- reset completo del entorno;
- una ejecución completa del proceso propuesto.

El proceso convencional se ejecuta primero.

Las ejecuciones serán realizadas por el **mismo equipo investigador**, utilizando un único equipo experimental principal para las operaciones que puedan afectar al experimento y manteniendo los mismos roles en las actividades equivalentes:

- **I1 — Ejecutor principal**;
- **I2 — Registrador de evidencia y esfuerzo**;
- **I3 — Supervisor del protocolo**.

I2 e I3 pueden utilizar dispositivos auxiliares únicamente para cronometraje, checklist y registro. Esos dispositivos no se utilizan para analizar código, ejecutar herramientas, interactuar con la aplicación experimental ni realizar búsquedas externas ad hoc.

La correspondencia nominal entre los roles y los integrantes del equipo fue registrada antes de C00:

- I1 — Ejecutor principal: **Paulo**;
- I2 — Registrador de evidencia y esfuerzo: **Carlos**;
- I3 — Supervisor del protocolo: **Jorge**.

Registro: `investigator_role_assignment_v0.1.md`.

SHA-256 del registro: `219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631`.

La asignación entra en vigor para la ejecución experimental y no atribuye retroactivamente identidades a evidencias de preparación ya cerradas o hasheadas.

Los investigadores conocen la existencia general de cinco defectos controlados por haber participado en la construcción del laboratorio. No existe cegamiento completo.

Para reducir el sesgo, durante el proceso convencional no se consulta:

- catálogo D01–D05;
- ubicación concreta de los defectos;
- correspondencia defecto–ASVS;
- resultados de Semgrep;
- resultados de ZAP;
- pruebas específicas del proceso propuesto.

## Piloto

El piloto se ejecuta sobre el baseline seguro sin D01–D05 mediante:

1. `PILOT-CONV-01`;
2. cierre y archivo de su evidencia;
3. reset completo;
4. `PILOT-PROP-01`.

Los tiempos correspondientes a la **ejecución propiamente dicha del piloto** se conservan como evidencia de calibración y no forman parte de la comparación definitiva.

Si el piloto revela la necesidad de ajustar o corregir mecanismos específicos de alguno de los procesos, el trabajo humano adicional realizado fuera de la ejecución del run piloto podrá registrarse separadamente como **configuración inicial**, siempre que exista medición observada y no se produzca doble contabilización.

Los resultados del piloto no se utilizan para calcular las métricas definitivas.

## Documentos

| Documento | Finalidad | Estado actual |
|---|---|---|
| `experimental_design_v0.1.md` | Operacionalización del diseño del TFM | Cerrado para pilotaje |
| `business_rules_v0.1.md` | Reglas funcionales | Definido |
| `conventional_procedure_v0.1.md` | Procedimiento convencional fijo | Cerrado para pilotaje |
| `proposed_procedure_v0.1.md` | Procedimiento propuesto fijo | Cerrado para pilotaje |
| `metrics_definition_v0.1.md` | Cobertura, esfuerzo y detección | Cerrado para pilotaje |
| `independent_coverage_instrument_v0.1.md` | Asociación posterior evidencia–requisito | Cerrado para pilotaje |
| `reset_procedure_v0.1.md` | Restauración del estado experimental | Cerrado para pilotaje |
| `conventional_workspace_sanitization_v0.1.md` | Construcción y validación del workspace convencional | Workspace real preparado y validado; piloto no iniciado |
| `pilot_protocol_v0.1.md` | Piloto previo a medición definitiva | Cerrado para pilotaje; ejecución no iniciada |
| `run_record_template_v0.1.md` | Registro por ejecución | Cerrado como plantilla |
| `effort_log_v0.1.md` | Minutos-persona y tiempos automáticos | Instrumento cerrado; datos observados pendientes |
| `incident_log_v0.1.md` | Incidencias | Cerrado como instrumento; datos observados pendientes |
| `pilot_execution_log_v0.1.md` | Registro de ambos runs piloto y reset | Plantilla cerrada; ejecución no iniciada |
| `pilot_results_v0.1.md` | Consolidación de resultados del piloto | Plantilla cerrada; resultados pendientes |
| `evidence_archival_v0.1.md` | Conservación de evidencias | Estructura definida; rutas primaria/secundaria preparadas y verificadas |
| `ci_execution_v0.1.md` | Ejecución CI del proceso propuesto | CAL-01/CAL-02 validadas; pilot y proposed-definitive pendientes |
| `environment_manifest_v0.1.md` | Versiones, dependencias, host y digests | Freeze técnico pre-piloto validado; versión experimental definitiva pendiente |
| `pre_github_validation_plan_v0.1.md` | Validación técnica pre-GitHub | Histórico; validación local completada y calibración remota realizada posteriormente |
| `protocol_freeze_checklist_v0.1.md` | Condiciones de preparación y congelación | Preparación pre-piloto completada; piloto y freeze definitivo pendientes |
| `audit_transversal_corrections_v0.1.md` | Registro de correcciones metodológicas transversales | Histórico vigente; debe conservar trazabilidad de las correcciones |

## Estado experimental

Los documentos de ejecución deben reflejar únicamente datos observados.

Mientras un run no haya comenzado:

- los registros de ejecución permanecen pendientes;
- los tiempos experimentales permanecen pendientes;
- las incidencias permanecen pendientes;
- los resultados permanecen pendientes;
- no se registran hallazgos experimentales;
- no se introduce información inferida o simulada como si fuera observada.

La existencia de preparación técnica, calibraciones previas o evidencia de freeze no equivale al inicio de un run piloto.

## Regla de cambios

Una vez iniciado el experimento definitivo no se modificarán, como consecuencia de los resultados:

- actividades permitidas;
- datos de prueba;
- reglas;
- defectos;
- herramientas;
- configuraciones;
- pruebas;
- criterios de clasificación;
- instrumentos.

Durante el piloto solo podrán realizarse ajustes permitidos por el protocolo y deberán quedar justificados y documentados.

No se modificará retroactivamente evidencia ya cerrada o hasheada.

Los datos aún no observados permanecen como `PENDIENTE`.
