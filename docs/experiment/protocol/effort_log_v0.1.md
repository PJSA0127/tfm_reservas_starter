# Registro de esfuerzo — v0.2

## 1. Estado

**INSTRUMENTO CERRADO PARA PILOTAJE. DATOS DEFINITIVOS PENDIENTES DE OBSERVACIÓN.**

## 2. Objetivo

Registrar de forma trazable:

- esfuerzo humano;
- tiempo automático;
- categoría de actividad;
- evidencia temporal;
- incidencias asociadas.

## 3. Unidad

```text
minutos-persona activos
```

El tiempo automático se registra por separado.

## 4. Estados del tiempo

### OBSERVADO

Medido durante una actividad real mediante el instrumento formal.

Puede incorporarse a M2 si la actividad pertenece al comparativo.

### ESTIMADO

Valor aproximado usado para planificación o referencia histórica.

**No se incorpora a M2.**

### PLANIFICADO

Tiempo reservado para una actividad futura.

**No se incorpora a M2.**

## 5. Categorías de esfuerzo

- configuración inicial;
- ejecución;
- análisis;
- documentación de evidencias;
- mantenimiento/recuperación.

## 6. Reglas de cronometraje

I2 — **Carlos** es responsable de:

- inicio;
- fin;
- pausas;
- minutos activos.

La asignación nominal vigente está registrada en `investigator_role_assignment_v0.1.md`.

SHA-256 del registro: `219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631`.

Cuando varios investigadores están activos, se registra cada tiempo individual.

Espera pasiva = 0 minutos-persona para el investigador en espera.

## 7. Registro experimental

| ID | Run ID | Proceso | Categoría | Actividad | Investigador | Inicio | Fin | Pausas | Min activos | Min-persona | Tiempo automático | Estado temporal | Evidencia |
|---|---|---|---|---|---|---|---|---|---:|---:|---:|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | | | | | | | OBSERVADO | PENDIENTE |

## 8. Registro histórico conocido

Existe un registro previo de aproximadamente:

```text
1.800 minutos-persona
```

asociado con selección/análisis/operacionalización inicial de los seis requisitos ASVS.

Tratamiento:

- se conserva como histórico;
- no se incorpora a M2;
- pertenece a construcción/preparación general del experimento según `TFM - G7.docx`;
- no se desagrega retrospectivamente sin evidencia.

## 9. Estimaciones de planificación histórica

Los siguientes valores son **ESTIMADOS**, no mediciones observadas. Se documentan para planificación y revisión del equipo y no se incorporan a M2.

| ID | Actividad | Bloque | Personas consideradas | Duración cronológica estimada | Esfuerzo estimado | Tratamiento |
|---|---|---|---:|---:|---:|---|
| EST-01 | Definición del procedimiento convencional | Convencional | 3 | 120 min | 360 min-persona | Excluido de M2 por ser estimado |
| EST-02 | Casos manuales válidos/vacíos/inválidos/frontera | Convencional | 3 | 90 min | 270 min-persona | Excluido |
| EST-03 | Checklist e instrumentos convencionales | Convencional | 2 | 60 min | 120 min-persona | Excluido |
| EST-04 | Pruebas específicas de seguridad | Propuesto | 2 | 240 min | 480 min-persona | Excluido |
| EST-05 | Configuración inicial Semgrep | Propuesto | 2 | 90 min | 180 min-persona | Excluido |
| EST-06 | Diseño de 6 reglas Semgrep | Propuesto | 2 | 180 min | 360 min-persona | Excluido |
| EST-07 | Calibración Semgrep y fixtures 6/6 | Propuesto | 2 | 120 min | 240 min-persona | Excluido |
| EST-08 | Configuración inicial ZAP | Propuesto | 2 | 180 min | 360 min-persona | Excluido |
| EST-09 | Autenticación ZAP | Propuesto | 2 | 150 min | 300 min-persona | Excluido |
| EST-10 | Spider y active scan | Propuesto | 2 | 90 min | 180 min-persona | Excluido |
| EST-11 | Mapping/clasificador DAST | Propuesto | 2 | 120 min | 240 min-persona | Excluido |
| EST-12 | Calibración del mecanismo ZAP | Propuesto | 2 | 90 min | 180 min-persona | Excluido |
| EST-13 | Matriz requisito-prueba-evidencia | Propuesto | 3 | 150 min | 450 min-persona | Excluido |
| EST-14 | Catálogo/mappings operativos | Propuesto | 2 | 90 min | 180 min-persona | Excluido |
| EST-15 | Workflow CI | Propuesto | 2 | 180 min | 360 min-persona | Excluido |
| EST-16 | Artifacts y metadatos CI | Propuesto | 2 | 90 min | 180 min-persona | Excluido |
| EST-17 | Simulación local CI — trabajo humano | Propuesto | 2 | 120 min | 240 min-persona | Excluido |
| EST-18 | Diseño de archivo de evidencias | Experimental común | 3 | 90 min | 270 min-persona | Excluido |
| EST-19 | Adecuación específica del laboratorio para mecanismos | Propuesto | 2 | 120 min | 240 min-persona | Excluido |
| EST-20 | Mantenimiento de mecanismos Semgrep/ZAP/CI | Propuesto | 2 | 180 min | 360 min-persona | Excluido |

### Nota sobre correcciones de la aplicación

La corrección funcional derivada del HTTP 500 detectado durante calibración ZAP se considera construcción/corrección general del escenario experimental y **no se contabiliza como esfuerzo del proceso propuesto**.

## 10. Planificación del piloto

También son valores `PLANIFICADO`, no experimentales:

| Actividad | Duración cronológica prevista |
|---|---:|
| Preparación inicial | 20–30 min |
| `PILOT-CONV-01` | 120–150 min |
| Cierre convencional | 20–30 min |
| Reset | 30–45 min |
| `PILOT-PROP-01` | 180–240 min |
| Cierre propuesto | 30–45 min |
| Revisión de instrumentos/evidencias | 60–90 min |
| Revisión de incidencias | 30–60 min |

Los tiempos reales correspondientes a la **ejecución propiamente dicha del piloto** se registran como `OBSERVADO`, pero no entran en el comparativo definitivo.

### Ajustes/configuración derivados del piloto

Si durante el piloto se identifica que un mecanismo específico necesita trabajo adicional para quedar operativo antes del freeze, ese trabajo se registra **fuera del Run ID piloto** en una actividad independiente. Puede contabilizarse como configuración inicial del proceso correspondiente únicamente cuando:

- existe tiempo `OBSERVADO`;
- el trabajo es específico del proceso convencional o propuesto;
- deriva de una incidencia o necesidad identificada durante el piloto;
- no constituye ejecución del piloto;
- no corresponde a construcción general de la aplicación/experimento;
- no se contabiliza dos veces.

Plantilla:

| ID | Incidencia origen | Proceso | Mecanismo | Actividad de ajuste | Investigador | Min activos | Min-persona | Estado | Evidencia |
|---|---|---|---|---|---|---:|---:|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | OBSERVADO | PENDIENTE |

## 11. Resumen definitivo

Se completa solo con tiempos observados de runs válidos.

| Proceso | Configuración | Ejecución | Análisis | Documentación | Mantenimiento | Total humano | Tiempo automático |
|---|---:|---:|---:|---:|---:|---:|---:|
| Convencional | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| Propuesto | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

## 12. Runs invalidados

Los tiempos de runs invalidados:

- permanecen documentados;
- se marcan `EXCLUDED FROM FINAL COMPARISON`;
- no se suman a M2 definitivo.
