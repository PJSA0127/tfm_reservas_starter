# Protocolo experimental — índice documental v0.8

**Estado pospiloto verificado (evidencias del 14/10/2026; auditadas en ZIP del 25/10/2026):** `PILOT-CONV-02 = VALID / COMPLETED / ARCHIVED`; `PILOT-PROP-01 = VALID_WITH_DOCUMENTED_LIMITATION / COMPLETED / ARCHIVED / VERIFIED / SEALED`; `P10 = COMPLETED`; `NEXT_FORMAL_STEP = POST_PILOT_REVIEW_AND_FREEZE_PREPARATION`.

**Checkpoint histórico 10/10/2026, SUPERADO:** PILOT-CONV-01 INVALIDADO Y ARCHIVADO / REV-INSTR-01 5/5 PASS / PILOT-CONV-02 VÁLIDO Y ARCHIVADO / RESET CONV→PROP PASS / PILOT-PROP-01 OPEN / IN_PROGRESS / P01 COMPLETED / P02 COMPLETED SEALED / NEXT PREPARE_P03_SECURITY_TESTS
**Documento rector vigente:** `TFM - 7B.docx` (ratificado el 25/10/2026). Copia de continuidad recibida como `TFM - 7B(5).docx` el 04/11/2026, SHA-256 `8A601A7D54A8D28E5DAE7D2B1D44507EF107B196172D1105F2B85F760CBFAB7A`. Los hashes anteriores del 25/10/2026 permanecen como referencias históricas, no como hashes de esta copia.
**Fuente de verdad del estado operacional:** `ESTADO_ACTUAL_TFM.md`
**Marco:** OWASP ASVS 5.0.0 L1

## Resumen operativo y procedencia — 25/10/2026

- P01–P06, P08–P10 cerradas y documentadas; P07 fue un reintento técnico condicionado de ZAP (uno consumido y documentado).
- Cuatro incidencias del propuesto registradas. `INC-P01-001 = CLOSED_WITH_MEASUREMENT_LIMITATION` mediante disposición adicional, mientras el archivo original `INC-P01-001.md` permanece históricamente abierto e íntegro. Estimación retrospectiva de ~44 segundos excluida del esfuerzo observado.
- Esfuerzo de calibración: `PILOT-CONV-02 = 146,71 min-persona` y `PILOT-PROP-01 = 604,22 min-persona` (P10: `70,48`). **No** registrar como M2 definitivo.
- Sello final propuesto: `evidence/PILOT-PROP-01/metadata/final_seal.txt`, SHA-256 `0D4EB7D54ACBA33F3B47FF54149748A967098390BC58DB17609BB82EDA3793B9`; manifiesto `8BF199916349628D544DFBDDC6B9E338218E91F0229F432C97C36B81B973E372`; ZIP externo `C957E841C57A5925B6AFE2B4A04B06E2E6A9A05D787922FCB16CE3C12BBCCB04` (250/250 verificados en el ZIP adjunto).
- `PILOT-CONV-01 = INVALIDATED / ARCHIVED` y `PILOT-CONV-02 = VALID / ARCHIVED` conservan su historia propia.
- No existe confirmación de introducción de D01–D05 en la variante definitiva, aprobación de freeze definitivo o inicio de `DEF-CONV-01`/`DEF-PROP-01`. El baseline pilotado fue deliberadamente seguro.
- El equipo confirmó el nombre canónico **`TFM - 7B.docx`**. La mención a `TFM - 7B(2).docx` corresponde al checkpoint histórico del 25/10/2026, no a la copia de continuidad del 04/11/2026; `TFM - G7.docx` se mantiene exclusivamente como denominación histórica.
- Los archivos históricos `pilot_execution_log_v0.2.md`, `pilot_results_v0.2.md`, `p02_postseal_documentary_checkpoint_20261010.md` y el checklist `v0.2` reflejan checkpoints anteriores: **no deben reescribirse para aparentar que siempre registraron P10**. La conciliación descriptiva se registra en `post_pilot_documentary_reconciliation_20261025.md`.
- Este índice no constituye prueba de instalación o publicación Git, firma de investigador, aprobación de freeze ni ejecución experimental. Es necesario verificar por separado cualquier cambio aplicado al checkout y al remoto.

## Jerarquía documental

En caso de discrepancia, se aplica el siguiente orden:

1. `TFM - 7B.docx`;
2. protocolo experimental;
3. instrumentos y documentación técnica;
4. código, automatización, ejecuciones y evidencias.

Un artefacto de nivel inferior no puede redefinir una decisión establecida por un nivel superior.

El protocolo no redefine el diseño académico: lo operacionaliza.

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

Los pilotos se ejecutaron sobre el baseline seguro sin D01–D05. La secuencia histórica de referencia fue:

1. `PILOT-CONV-01`;
2. invalidación y archivo histórico del primer intento, revisión de instrumentos y repetición convencional válida `PILOT-CONV-02`;
3. reset controlado CONV → PROP;
4. `PILOT-PROP-01`, cerrado con limitación documental y sellado en P10.

Los tiempos correspondientes a la **ejecución propiamente dicha del piloto** se conservan como evidencia de calibración y no forman parte de la comparación definitiva.

Si el piloto revela la necesidad de ajustar o corregir mecanismos específicos de alguno de los procesos, el trabajo humano adicional realizado fuera de la ejecución del run piloto podrá registrarse separadamente como **configuración inicial**, siempre que exista medición observada y no se produzca doble contabilización.

Los resultados del piloto no se utilizan para calcular las métricas definitivas.

## Documentos

| Documento | Finalidad | Estado en el último checkpoint verificado |
|---|---|---|
| `experimental_design_v0.1.md` | Operacionalización del diseño del TFM | Cerrado para pilotaje |
| `business_rules_v0.1.md` | Reglas funcionales | Definido |
| `conventional_procedure_v0.2.md` | Procedimiento convencional ajustado tras el piloto | Revalidado en REV-INSTR-01; utilizado en PILOT-CONV-02 y en las actividades comunes de PILOT-PROP-01 (ambos ya finalizados) |
| `proposed_procedure_v0.1.md` | Procedimiento propuesto fijo | Cerrado para pilotaje |
| `metrics_definition_v0.1.md` | Cobertura, esfuerzo y detección | Cerrado para pilotaje |
| `independent_coverage_instrument_v0.1.md` | Asociación posterior evidencia–requisito | Cerrado para pilotaje |
| `reset_procedure_v0.1.md` | Restauración del estado experimental | Cerrado para pilotaje |
| `conventional_workspace_sanitization_v0.2.md` | Construcción y validación del workspace convencional | Workspace PILOT-CONV-02 reconstruido, verificado y congelado |
| `pilot_protocol_v0.2.md` | Protocolo congelado del piloto | Aplicado a ambos pilotos históricos ya cerrados; no modificar retrospectivamente |
| `run_record_template_v0.1.md` | Registro por ejecución | Cerrado como plantilla |
| `effort_log_v0.1.md` | Minutos-persona y tiempos automáticos | Instrumento histórico conservado; esfuerzo final PILOT-PROP-01: 604,22 minutos-persona |
| `incident_log_v0.1.md` | Incidencias | Instrumento conservado; cuatro incidencias registradas, y disposición P10 para INC-P01-001 |
| `pilot_execution_log_v0.2.md` | Registro histórico de runs piloto y reset | Snapshot de etapa previa a P10; no es el estado operativo vigente, conservado sin modificar |
| `pilot_results_v0.2.md` | Consolidación histórica parcial de resultados del piloto | Registro previo al cierre global de P10, preservado como checkpoint; usar sellos finales para situación vigente |
| `evidence_archival_v0.1.md` | Conservación de evidencias | Estructura definida; rutas primaria/secundaria preparadas y verificadas |
| `ci_execution_v0.1.md` | Instrumento histórico de CI propuesto | CAL-01/CAL-02 completadas; fase `pilot` P06 éxito, run `38474365033`; fase definitiva pendiente |
| `environment_manifest_v0.1.md` | Versiones, dependencias, host y digests | Freeze técnico pre-piloto validado; versión experimental definitiva pendiente |
| `pre_github_validation_plan_v0.1.md` | Validación técnica pre-GitHub | Histórico; validación local completada y calibración remota realizada posteriormente |
| `protocol_freeze_checklist_v0.2.md` | Checklist congelado histórico | Casillas P03–P10/GitHub `pilot` no actualizadas en esta versión; ver evidencias P10 y preparar revisión nueva, sin retroeditar v0.2 |
| `audit_transversal_corrections_v0.1.md` | Registro de correcciones metodológicas transversales | Histórico vigente; debe conservar trazabilidad de las correcciones |
| `pilot_documentary_audit_checkpoint_20261009.md` | Auditoría documental de pausa durante PILOT-PROP-01 | Checkpoint histórico; documenta erratas sin alterar evidencia histórica |
| `p02_postseal_documentary_checkpoint_20261010.md` | Estado documental posterior al sello P02 | Checkpoint **histórico** de actualización hacia P03, previo al cierre global P10; sin modificar instrumentos congelados |

## Estado experimental

Los documentos de ejecución deben reflejar únicamente datos observados.

Mientras un run no haya comenzado:

- los registros de ejecución permanecen pendientes;
- los tiempos experimentales permanecen pendientes;
- las incidencias permanecen pendientes;
- los resultados permanecen pendientes;
- no se registran hallazgos experimentales;
- no se introduce información inferida o simulada como si fuera observada.

La preparación técnica, la calibración y el freeze prepiloto no equivalen a la ejecución definitiva ni al freeze definitivo.

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

Durante los pilotos solo se realizaron los ajustes y reintentos documentados conforme al protocolo; para los runs definitivos no podrán aplicarse cambios no autorizados.

No se modificará retroactivamente evidencia ya cerrada o hasheada.

Los datos aún no observados permanecen como `PENDIENTE`.

Estos documentos adicionales también son parte del inventario histórico:

| Documento | Finalidad | Estado |
|---|---|---|
| `manual_cases_v0.2.md` | Casos manuales comunes | Revalidados en REV-INSTR-01; ejecutados en ambos pilotos válidos y cerrados |
| `post_pilot_instrument_adjustments_v0.1.md` | Trazabilidad de ajustes derivados de PILOT-CONV-01 | Documentado; ajustes revalidados en REV-INSTR-01 5/5 PASS |
| `post_pilot_documentary_reconciliation_20261025.md` | Conciliación del estado pospiloto con los índices descriptivos | Documento derivado nuevo, sin modificación de evidencia sellada |

## Estado histórico previo a PILOT-PROP-01

`PILOT-CONV-01` fue ejecutado el 2026-09-29 y quedó `INVALIDATED - EXCLUDED FROM FINAL COMPARISON` por `INC-C03-001` e `INC-C03-002`. Su evidencia permanece cerrada, sellada y archivada.

Los ajustes derivados fueron revalidados en `REV-INSTR-01` con resultado `5/5 PASS`. Posteriormente, `PILOT-CONV-02` se ejecutó completamente sobre el mismo baseline seguro, quedó **VÁLIDO / COMPLETADO** y su evidencia fue archivada y verificada.

El reset CONV → PROP fue ejecutado y finalizó `PASS`. La incidencia técnica R06 quedó resuelta antes del inicio del proceso propuesto. La revalidación metodológica del overlay v0.2 también finalizó `PASS`, conservando intacto el baseline técnico de 87 archivos.

Estado operacional de aquel checkpoint histórico, posteriormente superado por P02 y por el cierre P10 (consultar la sección inicial vigente):

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


## Actualización operacional posterior al sello P02 — 2026-10-10 (CHECKPOINT HISTÓRICO, NO VIGENTE)

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

La referencia histórica del commit Git anterior a esta actualización es `8fa2451c414376139ecfe331a33201a385f6c846`. Los commits de futuras correcciones documentales deben registrarse exclusivamente después de su instalación y verificación; no se atribuye un identificador de Git no observado.
