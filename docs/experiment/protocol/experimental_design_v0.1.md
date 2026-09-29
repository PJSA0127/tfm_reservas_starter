# Diseño experimental — v0.2

## 1. Estado

**CERRADO PARA PILOTAJE / PILOTO NO INICIADO / FREEZE DEFINITIVO PENDIENTE.**

Este documento operacionaliza el diseño definido en `TFM - G7.docx` y no lo sustituye. Las decisiones contenidas aquí quedan fijadas para el piloto. Cualquier ajuste posterior deberá derivarse de una incidencia documentada de claridad, instrumentación, reproducibilidad o funcionamiento técnico y deberá realizarse antes del freeze experimental definitivo.

## 2. Pregunta de investigación

¿Qué diferencias se observan, en términos de cobertura de requisitos de seguridad, esfuerzo requerido y defectos de seguridad detectados, entre un proceso convencional de referencia y un proceso de verificación continua basado en OWASP ASVS 5.0.0, trazabilidad requisito-prueba-evidencia y técnicas SAST y DAST, aplicados sobre una misma aplicación web en un entorno experimental controlado?

## 3. Objeto experimental

Aplicación web demostrativa de reservas desarrollada con Flask y PostgreSQL.

- El **piloto** utilizará un baseline seguro sin D01–D05.
- La **evaluación definitiva** utilizará una versión experimental que contenga D01–D05 de forma controlada.

## 4. Requisitos incluidos

Se fijan seis requisitos OWASP ASVS 5.0.0 L1:

- V1.2.1;
- V1.2.4;
- V2.2.1;
- V2.2.2;
- V3.5.1;
- V3.5.3.

## 5. Defectos controlados

| ID | Descripción | ASVS relacionado |
|---|---|---|
| D01 | Codificación de salida insuficiente | V1.2.1 |
| D02 | Consulta de datos no parametrizada | V1.2.4 |
| D03 | Validación insuficiente en servidor | V2.2.1 y V2.2.2 |
| D04 | Protección insuficiente de una operación sensible frente a solicitudes no autorizadas desde otro contexto | V3.5.1 |
| D05 | Método HTTP inadecuado para una operación que modifica estado | V3.5.3 |

D03 cuenta una sola vez para tasa de detección, mientras V2.2.1 y V2.2.2 se evalúan por separado para cobertura.

## 6. Procesos comparados

### 6.1. Proceso convencional

Incluye:

1. restauración y despliegue;
2. comprobación de aplicación y base de datos;
3. ejecución del conjunto fijado de pruebas funcionales;
4. recorrido manual de autenticación, creación, consulta, modificación y cancelación;
5. comprobaciones con datos válidos, vacíos, inválidos y de frontera;
6. revisión técnica sistemática del código;
7. registro de anomalías y evidencias.

No utiliza como guía explícita:

- OWASP ASVS;
- matriz requisito-prueba-evidencia;
- pruebas específicas de seguridad;
- Semgrep;
- OWASP ZAP;
- workflow del proceso propuesto.

### 6.2. Proceso propuesto

Parte del mismo estado funcional inicial, repite las actividades comunes del convencional con el mismo procedimiento y los mismos datos y añade:

1. criterios ASVS explícitos;
2. matriz requisito-prueba-evidencia;
3. pruebas específicas de seguridad;
4. Semgrep SAST;
5. OWASP ZAP DAST;
6. GitHub Actions;
7. conservación sistemática de evidencias;
8. determinación formal del estado de verificación.

## 7. Equipo investigador y roles

El mismo equipo investigador participa en ambos procesos y mantiene los mismos roles en las actividades equivalentes.

La asignación nominal vigente fue formalizada antes de C00:

- I1 = Paulo;
- I2 = Carlos;
- I3 = Jorge.

Registro: `investigator_role_assignment_v0.1.md`.

SHA-256: `219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631`.

### I1 — Paulo — Ejecutor principal

- opera la aplicación y el equipo experimental principal;
- ejecuta comandos y pruebas;
- realiza el recorrido manual;
- realiza las comprobaciones funcionales;
- lidera la revisión técnica del código;
- registra los hallazgos identificados.

I1 no puede incorporar nuevas comprobaciones dirigidas a confirmar un defecto concreto.

### I2 — Carlos — Registrador de evidencia y esfuerzo

- inicia y detiene el cronometraje;
- registra pausas;
- registra minutos activos;
- recopila y organiza evidencia;
- registra incidencias;
- verifica asociación entre evidencias y Run ID.

I2 no orienta la ejecución hacia defectos concretos.

### I3 — Jorge — Supervisor del protocolo

- verifica condiciones iniciales;
- verifica cumplimiento del procedimiento;
- controla que no se utilicen mecanismos no permitidos;
- autoriza el inicio posterior a un reset;
- supervisa el cierre formal de cada run.

I3 no incorpora nuevas comprobaciones ni dirige al ejecutor hacia defectos concretos.

### 7.1. Equipo de cómputo

Las operaciones que puedan afectar al experimento se realizan desde **un único equipo experimental principal**.

I2 e I3 pueden utilizar dispositivos auxiliares exclusivamente para:

- cronometraje;
- checklist;
- formularios;
- anotaciones de registro.

Los dispositivos auxiliares no se utilizan para:

- inspeccionar código;
- ejecutar herramientas;
- interactuar con la aplicación experimental;
- consultar D01–D05;
- buscar documentación externa.

La misma disposición se mantiene en convencional y propuesto.

### 7.2. Internet

Durante las actividades manuales no se realizan búsquedas externas ad hoc.

Se permite conectividad cuando sea parte necesaria de la infraestructura, por ejemplo GitHub Actions. La documentación local previamente aprobada y congelada sí puede consultarse cuando el procedimiento lo permita.

### 7.3. Runner CI

GitHub Actions (`ubuntu-24.04`) es un mecanismo adicional propio del proceso propuesto. No sustituye el host local común utilizado para las actividades equivalentes.

## 8. Conocimiento de los defectos

Los investigadores conocen la existencia general de cinco defectos por su participación en la construcción del laboratorio.

No existe cegamiento completo.

Durante el proceso convencional:

- no se consulta el catálogo D01–D05;
- no se consulta su ubicación;
- no se consulta su correspondencia con ASVS;
- no se consultan resultados de Semgrep, ZAP o pruebas específicas;
- no se agregan comprobaciones motivadas por sospechas sobre defectos concretos.

La clasificación definitiva se realiza después de concluir ambos procesos.

## 9. Orden definitivo

1. restaurar estado inicial;
2. ejecutar convencional;
3. cerrar y archivar convencional;
4. no modificar código;
5. ejecutar reset;
6. comprobar estado equivalente;
7. ejecutar propuesto;
8. cerrar y archivar propuesto;
9. aplicar instrumento independiente;
10. clasificar frente a D01–D05;
11. calcular métricas.

## 10. Número de ejecuciones definitivas

- 1 ejecución convencional;
- 1 ejecución propuesta.

Una ejecución invalidada no reemplaza ni sobrescribe su registro: se conserva como invalidada y el nuevo intento recibe un nuevo Run ID.

## 11. Estado inicial equivalente por fase

Cada par de ejecuciones de una misma fase debe derivarse del mismo origen técnico congelado.

### Piloto

El piloto utiliza el baseline seguro:

- tag: `pre-pilot-freeze-v0.1`;
- commit técnico: `32d27a04305617f8fea031704e24d7e68ce9c451`;
- D01–D05: no introducidos.

`PILOT-CONV-01` y `PILOT-PROP-01` deben derivarse de este mismo origen técnico, aplicando únicamente las diferencias de instrumentación permitidas para cada proceso.

### Evaluación definitiva

La evaluación definitiva utilizará un único commit experimental futuro con D01–D05 introducidos y validados.

`DEF-CONV-01` y `DEF-PROP-01` deberán derivarse exactamente de ese mismo commit experimental definitivo.

### Convencional

Utiliza un workspace sanitizado derivado del commit correspondiente a la fase:

- `app/` idéntico;
- `tests/functional/` idéntico;
- dependencias comunes idénticas;
- mismos D01–D05 durante la fase definitiva;
- instrumentación exclusiva del propuesto eliminada.

La equivalencia se valida mediante hashes y verificaciones reproducibles.

### Propuesto

Utiliza el mismo commit correspondiente a la fase como origen y conserva la instrumentación completa.

### Regla entre ejecuciones

Aunque el convencional detecte un defecto, **no se corrige el código antes de ejecutar el proceso propuesto**.

## 12. Piloto

Se ejecuta una secuencia piloto completa sobre baseline seguro:

1. `PILOT-CONV-01`;
2. cierre y archivo de su evidencia;
3. reset completo CONV → PROP;
4. comprobación de equivalencia del estado inicial;
5. `PILOT-PROP-01`.

El piloto:

- no contiene D01–D05;
- prueba procedimientos, roles, reset, instrumentos y evidencias;
- familiariza al equipo con las actividades comunes;
- no aporta tiempos ni resultados al comparativo definitivo.

Se repite únicamente si existe una incidencia bloqueante, ambigüedad relevante, fallo de reset, error de instrumentación, evidencia insuficiente o imposibilidad técnica de completar el protocolo.

## 13. Variables

### Cobertura

```text
Cobertura (%) =
(requisitos efectivamente verificados / 6) × 100
```

### Esfuerzo

Minutos-persona activos, desglosados en:

- configuración inicial;
- ejecución;
- análisis;
- documentación de evidencias;
- mantenimiento o recuperación.

El tiempo automático se registra aparte.

### Detección

```text
Tasa de detección (%) =
(defectos controlados correctamente detectados / 5) × 100
```

## 14. Evaluación posterior

### Aplicación inicial

I2 — Carlos aplica inicialmente el instrumento independiente usando solo evidencia cerrada y criterios congelados.

### Revisión

I3 — Jorge revisa la clasificación y comprueba consistencia y suficiencia de evidencia.

### Participación de I1

I1 — Paulo participa únicamente en la revisión final y puede aclarar hechos ya registrados. No puede:

- crear evidencia nueva;
- ejecutar nuevas pruebas;
- modificar registros retrospectivamente;
- sustituir evidencia inexistente mediante explicación posterior.

### Decisión

El resultado definitivo se aprueba por consenso I1 + I2 + I3.

Cuando la evidencia no es suficiente para demostrar que un requisito fue verificado, se clasifica conservadoramente como **no verificado**.

## 15. Grabación

La grabación de pantalla/video no es evidencia obligatoria.

Solo podrá utilizarse como evidencia suplementaria si:

- no altera el procedimiento;
- se prueba previamente en el piloto;
- se adopta de forma equivalente en las ejecuciones que se comparen;
- se congela la decisión antes de la fase definitiva.

## 16. Análisis

Se comparan:

- cobertura;
- detección;
- esfuerzo humano;
- desglose de esfuerzo;
- tiempo automático como complemento;
- hallazgos adicionales y falsos positivos.

El análisis se limita al escenario experimental definido.

## 17. Freeze

Antes de la evaluación definitiva se congelan:

- commit experimental;
- D01–D05 y ubicaciones;
- requisitos y criterios;
- pruebas funcionales;
- datos manuales;
- procedimientos;
- herramientas/configuraciones;
- dependencias y digests;
- roles;
- workspace convencional;
- reset;
- evidencia;
- Run IDs;
- workflow y referencias inmutables.

## 18. Estado operacional pre-C00

Al momento de esta sincronización documental:

- `PILOT-CONV-01`: `READY_TO_START / NOT_STARTED`;
- `C00`: `NOT_STARTED`;
- cronómetro experimental: `NO INICIADO`;
- `PILOT-PROP-01`: `PREPARED_NOT_STARTED`;
- reset CONV → PROP: `PREPARED_NOT_EXECUTED`;
- D01–D05 introducidos: `NO`;
- versión experimental definitiva: `NO CREADA`.

La preparación técnica, las calibraciones CAL-01/CAL-02 y el freeze técnico pre-piloto no constituyen una ejecución experimental.

La fuente de verdad del estado operacional vigente es `ESTADO_ACTUAL_TFM.md`.
