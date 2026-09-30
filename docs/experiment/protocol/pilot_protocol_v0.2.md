# Protocolo piloto — v0.2

## 1. Estado

**CERRADO PARA EJECUCIÓN, FECHA PENDIENTE.**

## 2. Objetivo

Comprobar que el protocolo completo puede ejecutarse de manera clara, reproducible y medible antes del freeze.

## 3. Baseline

El piloto utiliza la aplicación segura sin D01–D05.

## 4. Secuencia

1. `PILOT-CONV-01`;
2. cierre/archivo;
3. reset completo;
4. `PILOT-PROP-01`;
5. cierre/archivo;
6. aplicación de instrumentos;
7. revisión de incidencias.

## 5. Roles

Los mismos roles previstos para la evaluación definitiva:

- I1 ejecutor;
- I2 evidencia/esfuerzo;
- I3 supervisor.

## 6. Equipo de cómputo

Un equipo experimental principal para actividades que puedan afectar al experimento.

Dispositivos auxiliares de I2/I3 solo para registro y checklist.

## 7. Qué debe validar el piloto

- claridad del convencional;
- claridad del propuesto;
- orden fijo;
- pruebas funcionales;
- casos manuales;
- revisión de código;
- ASVS explícito;
- pruebas de seguridad;
- Semgrep;
- ZAP;
- GitHub Actions;
- reintento técnico;
- run record;
- effort log;
- incident log;
- reset;
- workspace convencional;
- archivo y hash de evidencia;
- roles I1/I2/I3;
- ausencia de búsquedas externas ad hoc.

## 8. Cronometraje

I2 registra tiempos reales como `OBSERVADO`.

### Ejecución del piloto

Los minutos-persona empleados en ejecutar `PILOT-CONV-01`, el reset y `PILOT-PROP-01`:

- se conservan como evidencia de calibración;
- permiten revisar la aplicabilidad del instrumento de esfuerzo;
- no se incorporan a M2 definitivo.

### Ajustes derivados del piloto

Si una incidencia o resultado del piloto demuestra que un mecanismo específico necesita trabajo adicional de preparación/corrección para quedar operativo antes del freeze, ese trabajo se realiza y cronometra **fuera del run piloto**. Puede registrarse como configuración inicial del proceso correspondiente cuando sea específico, observado y trazable a la incidencia.

No se permite contabilizar el mismo tiempo como ejecución piloto y como configuración inicial.

## 9. Repetición

El piloto se repite únicamente si existe:

- incidencia bloqueante;
- ambigüedad relevante;
- fallo de reset;
- error de instrumentación;
- evidencia insuficiente;
- imposibilidad técnica de completar el procedimiento.

No se repite porque un resultado resulte desfavorable.

## 10. Ajustes posteriores

Antes del freeze pueden corregirse:

- instrucciones ambiguas;
- fallos técnicos;
- instrumentos;
- registro;
- reset;
- reproducibilidad.

No pueden introducirse ajustes orientados a favorecer un resultado.

## 11. Fecha

**PENDIENTE.**

## 12. Criterio de salida

El piloto queda aprobado cuando:

- ambas secuencias pueden completarse;
- no existen incidencias bloqueantes abiertas;
- el reset funciona;
- los roles son aplicables;
- el cronometraje funciona;
- las evidencias pueden cerrarse y hashearse;
- los mecanismos técnicos funcionan en el alcance definido.

## Antecedente PILOT-CONV-01

`PILOT-CONV-01` fue ejecutado y cerrado el 2026-09-29 con estado:

`INVALIDATED - EXCLUDED FROM FINAL COMPARISON`

La invalidación se debió a `INC-C03-001` e `INC-C03-002`, que demostraron problemas de instrumentación en cinco subcomprobaciones manuales.

Los ajustes permitidos fueron documentados en:

- `post_pilot_instrument_adjustments_v0.1.md`;
- `manual_cases_v0.2.md`;
- `conventional_procedure_v0.2.md`.

La secuencia vigente es:

1. revalidar los ajustes;
2. preparar y ejecutar `PILOT-CONV-02`;
3. cerrar y archivar `PILOT-CONV-02`;
4. ejecutar el reset CONV -> PROP;
5. ejecutar `PILOT-PROP-01`;
6. cerrar el piloto;
7. realizar el freeze definitivo.

La revalidación previa no constituye un nuevo run experimental y no se utiliza para calcular métricas.