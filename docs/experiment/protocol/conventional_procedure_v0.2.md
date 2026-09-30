# Procedimiento convencional — v0.2

## 1. Estado

**AJUSTADO TRAS PILOT-CONV-01 / PENDIENTE DE REVALIDACIÓN Y NUEVO FREEZE.**

La versión v0.2 incorpora únicamente correcciones de instrumentación derivadas de `INC-C03-001` e `INC-C03-002`.

## 2. Objetivo

Ejecutar el proceso convencional de referencia definido en `TFM - G7.docx` sin utilizar como guía explícita OWASP ASVS, trazabilidad requisito-prueba-evidencia ni los mecanismos SAST/DAST específicos del proceso propuesto.

## 3. Roles

- **I1 — Paulo:** ejecutor principal.
- **I2 — Carlos:** registro de esfuerzo/evidencia.
- **I3 — Jorge:** supervisor del protocolo.

Asignación formal: `investigator_role_assignment_v0.1.md`.

SHA-256 del registro: `219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631`.

Los mismos roles se mantienen en las actividades equivalentes del proceso propuesto.

## 4. Restricciones

Durante esta ejecución no se permite consultar:

- catálogo D01–D05;
- ubicación de defectos;
- mappings D01–D05 ↔ ASVS;
- resultados Semgrep;
- resultados ZAP;
- `tests/security/`;
- matriz requisito-prueba-evidencia como guía;
- búsquedas externas ad hoc.

Se permite documentación local previamente aprobada y congelada.

I1 puede utilizar capacidades normales del IDE, incluyendo navegación de referencias y búsqueda global de texto.

No se permite ejecutar analizadores automáticos de seguridad equivalentes a SAST/DAST.

No se permite construir solicitudes HTTP arbitrarias mediante `curl`, Postman, scripts, `fetch()` manual u otras herramientas equivalentes durante C03.

La única excepción de interacción cliente es la técnica controlada de modificación temporal del DOM definida de forma expresa en `manual_cases_v0.2.md`. Esta técnica:

- solo puede utilizarse en los casos allí enumerados;
- no permite explorar entradas o rutas adicionales;
- no modifica archivos fuente ni el servidor;
- conserva sesión, cookies y CSRF normales;
- forma parte del instrumento congelado una vez revalidado;
- debe registrarse como parte de la evidencia del caso.

## 5. Material permitido

- workspace convencional sanitizado;
- `app/`;
- `tests/functional/`;
- dependencias comunes;
- reglas de negocio;
- casos manuales congelados;
- navegador y sus herramientas de desarrollo únicamente en los casos autorizados por `manual_cases_v0.2.md`;
- IDE/editor;
- procedimiento convencional;
- run record;
- effort log;
- incident log.

## 6. Secuencia obligatoria

### C00 — Inicio

I3 verifica las condiciones iniciales.

I2 abre el run record e inicia el cronometraje de la primera actividad humana.

### C01 — Ejecución de pruebas funcionales

Ejecutar el conjunto fijado de `tests/functional/`.

Orden: **antes del recorrido manual**.

Si existen pruebas fallidas pero la aplicación sigue operativa:

- registrar resultado;
- conservar evidencia;
- continuar.

Solo se detiene por una incidencia bloqueante.

### C02 — Recorrido manual

Ejecutar en orden las funcionalidades aplicables:

1. autenticación;
2. listado/consulta;
3. creación;
4. detalle;
5. modificación;
6. cancelación;
7. control de acceso cuando corresponda.

### C03 — Casos manuales congelados

Utilizar exclusivamente los casos derivados previamente de BR-01–BR-12:

- válidos;
- vacíos cuando corresponda;
- inválidos;
- valores de frontera.

No se agregan casos nuevos durante una ejecución piloto ni durante una ejecución definitiva.

#### Técnica controlada para alcanzar el servidor

Cuando un caso congelado de `manual_cases_v0.2.md` lo indique expresamente, I1 puede modificar temporalmente un atributo del DOM desde las herramientas de desarrollo del navegador para permitir que la solicitud prevista alcance el servidor.

Esta técnica no cambia el criterio de comprobación y no constituye un reintento ad hoc porque:

- el caso y el valor están definidos antes del run;
- el atributo modificable está identificado de antemano;
- no se permite explorar valores distintos;
- el envío continúa mediante el formulario normal de la aplicación;
- se preservan sesión y CSRF;
- la modificación desaparece al recargar la página.

Si el caso no puede ejecutarse ni siquiera mediante la técnica congelada, se registra una incidencia de instrumentación y se aplica el criterio de continuidad de este procedimiento.

### C04 — Revisión técnica de código

I1 sigue obligatoriamente este orden:

1. autenticación y sesiones;
2. rutas/endpoints;
3. validación de entradas;
4. acceso a datos/persistencia;
5. templates y generación de respuestas;
6. operaciones que modifican estado y métodos HTTP.

La revisión es manual y puede usar:

- navegación del IDE;
- búsqueda global;
- búsqueda de referencias;
- lectura de código.

No puede usar Semgrep, ZAP, pruebas específicas de seguridad ni mappings del proceso propuesto.

### C05 — Registro de hallazgos

Cada hallazgo incluye:

- ID;
- descripción;
- flujo/ubicación observada;
- evidencia;
- criterio técnico;
- estado.

No se clasifica durante la ejecución como D01–D05.

### C06 — Cierre

1. completar todas las actividades obligatorias;
2. detener cronometraje;
3. cerrar hallazgos;
4. archivar evidencia;
5. registrar incidencias;
6. marcar el run como válido o invalidado;
7. no crear nueva evidencia después del cierre.

## 7. Actividades no previstas

Cada actividad del run record debe marcar:

```text
¿Actividad prevista en el protocolo? Sí / No
```

Una actividad `No` se registra como incidencia y se revisa antes de utilizar sus resultados.

La técnica controlada expresamente definida en `manual_cases_v0.2.md` se considera actividad prevista.

## 8. Tiempo

No existe límite máximo fijo.

La ejecución termina cuando C00–C06 han sido completados.

La espera pasiva no se contabiliza como esfuerzo humano.

## 9. Criterio de continuidad

Un fallo funcional no invalida automáticamente la ejecución.

Se continúa salvo que la incidencia:

- impida completar actividades obligatorias;
- rompa las condiciones experimentales;
- haga imposible producir evidencia válida.

## 10. Reintentos

El convencional no incorpora reintentos ad hoc para confirmar hallazgos.

Solo se permite repetir una operación cuando el procedimiento congelado ya la contempla o cuando sea necesario resolver una incidencia técnica documentada que no cambie el criterio de comprobación.

La técnica controlada de `manual_cases_v0.2.md` no se considera reintento: constituye el método predefinido de ejecución de las variantes afectadas.

## 11. Evidencia mínima

- reporte de pruebas funcionales;
- evidencia del recorrido manual;
- registro de casos manuales;
- registro de la técnica controlada cuando aplique;
- notas de revisión técnica;
- hallazgos;
- run record;
- effort log;
- incident log;
- metadatos del entorno.

## 12. Control de cambios

### Antecedente

El archivo previo `conventional_procedure_v0.1.md` contenía internamente el encabezado `Procedimiento convencional — v0.2`, aunque su nombre de archivo correspondía a v0.1.

La versión canónica post-piloto se normaliza como `conventional_procedure_v0.2.md`.

### v0.2

Cambios derivados de `PILOT-CONV-01`:

1. se incorpora la técnica controlada de modificación temporal del DOM para los casos expresamente definidos;
2. se prohíben solicitudes HTTP arbitrarias fuera de los formularios normales;
3. se declara la técnica controlada como actividad prevista y no como prueba/reintento ad hoc;
4. se exige registrar su uso como evidencia;
5. se mantiene sin cambios el alcance de C04 y C05;
6. no se modifican BR-01–BR-12 ni los criterios de continuidad.

La versión permanece pendiente de revalidación antes de un nuevo freeze.
