# Protocolo experimental — índice documental v0.5

**Estado general:** CERRADO PARA PILOTAJE / PRE-FREEZE
**Documento rector:** Anteproyecto TFM E3 Borrador vigente
**Marco:** OWASP ASVS 5.0.0 L1

## Jerarquía documental

En caso de discrepancia, se aplica el siguiente orden:

1. anteproyecto académico aprobado/vigente;
2. protocolo experimental;
3. instrumentos de registro y evaluación;
4. configuraciones y artefactos técnicos.

El protocolo no redefine el diseño académico: lo operacionaliza.

## Diseño vigente derivado del anteproyecto

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

Los investigadores conocen la existencia general de cinco defectos controlados por haber participado en la construcción del laboratorio. No existe cegamiento completo. Para reducir el sesgo, durante el proceso convencional no se consulta:

- catálogo D01–D05;
- ubicación concreta de los defectos;
- correspondencia defecto–ASVS;
- resultados de Semgrep;
- resultados de ZAP;
- pruebas específicas del proceso propuesto.

## Piloto

El piloto se ejecuta sobre el baseline seguro sin D01–D05 mediante:

1. `PILOT-CONV-01`;
2. reset completo;
3. `PILOT-PROP-01`.

Los tiempos correspondientes a la **ejecución propiamente dicha del piloto** se conservan como evidencia de calibración y no forman parte de la comparación definitiva.

Si el piloto revela la necesidad de ajustar o corregir mecanismos específicos de alguno de los procesos, el trabajo humano adicional realizado fuera de la ejecución del run piloto podrá registrarse separadamente como **configuración inicial**, siempre que exista medición observada y no se produzca doble contabilización.

## Documentos

| Documento | Finalidad | Estado pre-piloto |
|---|---|---|
| `experimental_design_v0.1.md` | Operacionalización del diseño del anteproyecto | Cerrado para pilotaje |
| `business_rules_v0.1.md` | Reglas funcionales | Definido |
| `conventional_procedure_v0.1.md` | Procedimiento convencional fijo | Cerrado para pilotaje |
| `proposed_procedure_v0.1.md` | Procedimiento propuesto fijo | Cerrado para pilotaje |
| `metrics_definition_v0.1.md` | Cobertura, esfuerzo y detección | Cerrado para pilotaje |
| `independent_coverage_instrument_v0.1.md` | Asociación posterior evidencia–requisito | Cerrado para pilotaje |
| `reset_procedure_v0.1.md` | Restauración del estado experimental | Cerrado para pilotaje |
| `conventional_workspace_sanitization_v0.1.md` | Construcción del workspace convencional | Criterios definidos; workspace real pendiente |
| `pilot_protocol_v0.1.md` | Piloto previo a medición definitiva | Cerrado; fecha pendiente |
| `run_record_template_v0.1.md` | Registro por ejecución | Cerrado como plantilla |
| `effort_log_v0.1.md` | Minutos-persona y tiempos automáticos | Instrumento cerrado; datos observados pendientes |
| `incident_log_v0.1.md` | Incidencias | Cerrado como instrumento |
| `pilot_execution_log_v0.1.md` | Registro de ambos runs piloto y reset | Plantilla cerrada |
| `pilot_results_v0.1.md` | Consolidación de resultados del piloto | Plantilla; datos pendientes |
| `evidence_archival_v0.1.md` | Conservación de evidencias | Cerrado; rutas absolutas pendientes |
| `ci_execution_v0.1.md` | Ejecución CI del proceso propuesto | Validación GitHub real pendiente |
| `environment_manifest_v0.1.md` | Versiones y digests | Parcial hasta freeze |
| `pre_github_validation_plan_v0.1.md` | Validación técnica pre-GitHub | Histórica/completada localmente |
| `protocol_freeze_checklist_v0.1.md` | Condiciones de congelación | Abierto hasta piloto/freeze |

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

Los datos aún no observados permanecen como `PENDIENTE`.
