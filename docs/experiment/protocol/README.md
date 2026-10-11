# Protocolo experimental — índice documental v0.8

**Estado general:** PILOT-CONV-01 INVALIDADO Y ARCHIVADO / REV-INSTR-01 5/5 PASS / PILOT-CONV-02 VÁLIDO Y ARCHIVADO / RESET CONV→PROP PASS / PILOT-PROP-01 OPEN / IN_PROGRESS / P01 COMPLETED / P02 COMPLETED SEALED / NEXT PREPARE_P03_SECURITY_TESTS
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

La preparación técnica, por sí sola, no determina el estado de ejecución de los runs. El estado operacional vigente se consulta en `ESTADO_ACTUAL_TFM.md`.

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
| `conventional_procedure_v0.2.md` | Procedimiento convencional ajustado tras el piloto | Revalidado en REV-INSTR-01; utilizado en PILOT-CONV-02 y activo para actividades comunes de PILOT-PROP-01 |
| `proposed_procedure_v0.1.md` | Procedimiento propuesto fijo | Cerrado para pilotaje |
| `metrics_definition_v0.1.md` | Cobertura, esfuerzo y detección | Cerrado para pilotaje |
| `independent_coverage_instrument_v0.1.md` | Asociación posterior evidencia–requisito | Cerrado para pilotaje |
| `reset_procedure_v0.1.md` | Restauración del estado experimental | Cerrado para pilotaje |
| `conventional_workspace_sanitization_v0.2.md` | Construcción y validación del workspace convencional | Workspace PILOT-CONV-02 reconstruido, verificado y congelado |
| `pilot_protocol_v0.2.md` | Piloto previo a medición definitiva | Vigente y congelado para el piloto; PILOT-PROP-01 actualmente abierto |
| `run_record_template_v0.1.md` | Registro por ejecución | Cerrado como plantilla |
| `effort_log_v0.1.md` | Minutos-persona y tiempos automáticos | Instrumento cerrado; PILOT-PROP-01 contiene datos observados parciales |
| `incident_log_v0.1.md` | Incidencias | Cerrado como instrumento; `INC-P01-001` e `INC-P01-002` preservadas en PILOT-PROP-01 |
| `pilot_execution_log_v0.2.md` | Registro de runs piloto y reset | PILOT-CONV-01 invalidado; PILOT-CONV-02 válido y archivado; reset PASS; PILOT-PROP-01 `OPEN / IN_PROGRESS` |
| `pilot_results_v0.2.md` | Consolidación parcial de resultados del piloto | Archivo de checkpoint anterior; P01/P02 posteriores constan en los registros vivos y sello P02 |
| `evidence_archival_v0.1.md` | Conservación de evidencias | Estructura definida; rutas primaria/secundaria preparadas y verificadas |
| `ci_execution_v0.1.md` | Ejecución CI del proceso propuesto | CAL-01/CAL-02 validadas; pilot y proposed-definitive pendientes |
| `environment_manifest_v0.1.md` | Versiones, dependencias, host y digests | Freeze técnico pre-piloto validado; versión experimental definitiva pendiente |
| `pre_github_validation_plan_v0.1.md` | Validación técnica pre-GitHub | Histórico; validación local completada y calibración remota realizada posteriormente |
| `protocol_freeze_checklist_v0.2.md` | Condiciones de preparación y congelación | Convencional piloto válido cerrado; reset PASS; PROP preparado y revalidado |
| `audit_transversal_corrections_v0.1.md` | Registro de correcciones metodológicas transversales | Histórico vigente; debe conservar trazabilidad de las correcciones |
| `pilot_documentary_audit_checkpoint_20261009.md` | Auditoría documental de pausa durante PILOT-PROP-01 | Checkpoint histórico; documenta erratas sin alterar evidencia histórica |
| `p02_postseal_documentary_checkpoint_20261010.md` | Estado documental posterior al sello P02 | Nuevo checkpoint de actualización de índices y reglas de continuidad hacia P03, sin modificar instrumentos congelados |

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

| `manual_cases_v0.2.md` | Casos manuales comunes | Revalidados en REV-INSTR-01; utilizados en PILOT-CONV-02 y activos para P01 de PILOT-PROP-01 |
| `post_pilot_instrument_adjustments_v0.1.md` | Trazabilidad de ajustes derivados de PILOT-CONV-01 | Documentado; ajustes revalidados en REV-INSTR-01 5/5 PASS |

## Estado histórico previo a PILOT-PROP-01

`PILOT-CONV-01` fue ejecutado el 2026-09-29 y quedó `INVALIDATED - EXCLUDED FROM FINAL COMPARISON` por `INC-C03-001` e `INC-C03-002`. Su evidencia permanece cerrada, sellada y archivada.

Los ajustes derivados fueron revalidados en `REV-INSTR-01` con resultado `5/5 PASS`. Posteriormente, `PILOT-CONV-02` se ejecutó completamente sobre el mismo baseline seguro, quedó **VÁLIDO / COMPLETADO** y su evidencia fue archivada y verificada.

El reset CONV → PROP fue ejecutado y finalizó `PASS`. La incidencia técnica R06 quedó resuelta antes del inicio del proceso propuesto. La revalidación metodológica del overlay v0.2 también finalizó `PASS`, conservando intacto el baseline técnico de 87 archivos.

Estado operacional de ese checkpoint histórico (superado por la actualización posterior a P02; consultar el bloque vigente añadido abajo):

1. `PILOT-CONV-02`: cerrado y archivado;
2. reset CONV → PROP: `PASS`;
3. `PILOT-PROP-01`: `OPEN / IN_PROGRESS`;
4. P01-FUNC: `PASS` — 18/18;
5. P01-WALKTHROUGH: `COMPLETED_WITH_PROCEDURAL_DEVIATION`;
6. `INC-P01-001`: `OPEN / NON-BLOCKING`;
7. MC-01..MC-14: `COMPLETED / PASS`;
8. P01: `IN_PROGRESS`;
9. siguiente paso formal: `P01_COMMON_TECHNICAL_REVIEW`;
10. P02–P10: `NOT_STARTED`;
11. freeze experimental definitivo: pendiente hasta cerrar el piloto completo.


## Actualización operacional posterior al sello P02 — 2026-10-10 (VIGENTE)

- `PILOT-PROP-01 = OPEN / IN_PROGRESS`; baseline seguro sin D01–D05.
- `P01 = COMPLETED`; revisión técnica común terminada con `NO_NEW_FINDINGS`. Se conservan sin reclasificación retrospectiva `INC-P01-001` e `INC-P01-002`, ambas no bloqueantes.
- `P02 = COMPLETED / SEALED`; 6/6 requisitos ASVS revisados; 0 incidencias y 0 desviaciones en P02.
- Esfuerzo humano observado: P01 `119.09`, P02 `127.05`, acumulado `246.14 min-persona`; automático conocido `0.21 min`.
- Sello P02: `evidence/PILOT-PROP-01/metadata/p02_closure_seal_20261010.md`, SHA-256 `AF7EEC4DA51B40D7528F92CC452F760B8FEAA5E9AD0F48D48FCDA4924146F0C0`.
- Manifiesto P02: `evidence/PILOT-PROP-01/hashes/p02_closure_manifest_20261010.txt`, SHA-256 `CC5A8998D23FE89BED2C7DFD933E4C08C201598862BB14440A8F49A24D958BFB`.
- Los registros de P02 son inmutables; P03 y fases posteriores deben generar nuevos artefactos para proseguir la trazabilidad sin editar la matriz sellada.
- `P03 = NOT_STARTED`, `P04–P06 = NOT_STARTED`, P07 condicional no activado, `P08–P10 = NOT_STARTED`.
- `NEXT_FORMAL_STEP = PREPARE_P03_SECURITY_TESTS`: preflight de solo lectura del workspace `D:\Repositorios\tfm_reservas_pilot_prop`, de la batería congelada y del aislamiento `db_test`.
- Los ajustes de nomenclatura `v0.1` frente a versiones internas quedan diferidos hasta después del piloto.

La referencia histórica del commit Git anterior a esta actualización es `8fa2451c414376139ecfe331a33201a385f6c846`. La actualización de este índice solo adquirirá condición de checkpoint Git una vez instalada y verificada; no se atribuye un nuevo commit anticipadamente.
