# Control experimental

Este directorio contiene documentación de control relacionada con la construcción y gestión de las versiones utilizadas en el laboratorio experimental.

El estado operacional vigente de las ejecuciones se mantiene en `ESTADO_ACTUAL_TFM.md`.

## Nomenclatura vigente

### Baseline seguro pre-piloto

La versión técnica actualmente congelada para la fase piloto es:

- tag: `pre-pilot-freeze-v0.1`;
- commit técnico: `32d27a04305617f8fea031704e24d7e68ce9c451`;
- D01–D05 introducidos: **NO**;
- finalidad: ejecución de `PILOT-CONV-01` y, después del reset correspondiente, `PILOT-PROP-01`.

Este baseline fue validado técnicamente mediante CAL-01 y CAL-02 antes del inicio del piloto.

Su existencia y validación no implican que ningún run piloto haya comenzado.

## Versión experimental definitiva

La versión destinada a la evaluación definitiva todavía no ha sido creada.

Después de:

1. completar `PILOT-CONV-01`;
2. cerrar y archivar su evidencia;
3. ejecutar el reset CONV → PROP;
4. completar `PILOT-PROP-01`;
5. analizar las incidencias y lecciones de ambos pilotos;
6. aplicar únicamente los ajustes permitidos;
7. congelar el protocolo experimental definitivo;

se incorporarán de forma controlada D01–D05 y se fijará mediante commit/tag la versión experimental definitiva.

Esa misma versión constituirá el origen técnico de:

- `DEF-CONV-01`;
- `DEF-PROP-01`.

No se deberá crear una versión diferente para cada proceso definitivo.

## Nomenclatura histórica

En una etapa anterior de planificación se utilizaron los nombres previstos:

- `calibration-v1`: aplicación funcional sin D01–D05 destinada al pilotaje;
- `experiment-v1`: misma base funcional con D01–D05 destinada a la evaluación definitiva.

Estos nombres se conservan únicamente como referencia histórica.

`calibration-v1` no debe utilizarse como identificador del baseline vigente, porque el artefacto técnico efectivamente congelado quedó identificado como `pre-pilot-freeze-v0.1`.

`experiment-v1` tampoco debe presentarse como una versión ya existente. La versión experimental definitiva con D01–D05 continúa pendiente y su identificador final se fijará después de cerrar ambos pilotos y congelar el protocolo definitivo.

## Restricción del proceso convencional

El catálogo detallado D01–D05, sus ubicaciones o manifestaciones y su correspondencia con OWASP ASVS no deben estar disponibles como guía durante la ejecución del proceso convencional.

Durante `PILOT-CONV-01`, además:

- el baseline utilizado no contiene D01–D05;
- no se consulta la matriz requisito-prueba-evidencia;
- no se ejecutan Semgrep ni OWASP ZAP;
- no se ejecutan las pruebas específicas de seguridad del proceso propuesto;
- no se crean pruebas ad hoc para confirmar sospechas.

Durante la evaluación definitiva, el proceso convencional utilizará la misma versión experimental con D01–D05 que el proceso propuesto, pero continuará sujeto a las restricciones anteriores respecto del conocimiento y mecanismos exclusivos del proceso propuesto.

## Estado actual

- `PILOT-CONV-01`: `READY_TO_START / NOT_STARTED`;
- `PILOT-PROP-01`: `PREPARED_NOT_STARTED`;
- reset CONV → PROP: `PREPARED_NOT_EXECUTED`;
- D01–D05 introducidos: `NO`;
- versión experimental definitiva: `NO CREADA`.

No debe adelantarse la preparación de la versión experimental definitiva mientras no hayan concluido ambos pilotos y las actividades de cierre posteriores previstas por el protocolo.
