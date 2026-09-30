# Casos manuales funcionales — v0.2

## 1. Estado

**AJUSTADO TRAS PILOT-CONV-01 / PENDIENTE DE REVALIDACIÓN Y NUEVO FREEZE.**

Este instrumento fija los casos manuales utilizados durante el proceso convencional y las actividades funcionales comunes del piloto.

La versión v0.2 deriva de las incidencias `INC-C03-001` e `INC-C03-002` observadas en `PILOT-CONV-01`.

No se agregan, eliminan ni modifican casos durante una ejecución abierta.

## 2. Referencia

Los casos se derivan exclusivamente de las reglas BR-01 a BR-12 de `business_rules_v0.1.md`.

## 3. Datos comunes

### Usuarios de laboratorio

| ID | Correo | Contraseña | Uso |
|---|---|---|---|
| U1 | `pilot.user1@tfm.local` | `PilotLocal123!` | usuario principal |
| U2 | `pilot.user2@tfm.local` | `PilotLocal123!` | comprobación entre usuarios |

Estas credenciales son exclusivamente locales para el laboratorio experimental.

### Fecha de referencia

Al iniciar la ejecución se registra:

`T0 = fecha actual del servidor`

A partir de T0 se utilizan:

- `T0-1`: día anterior;
- `T0`: día actual;
- `T0+10`: diez días después;
- `T0+365`: 365 días después;
- `T0+366`: 366 días después.

### Datos base de reserva válida

- nombre: `Ana Torres`
- correo: `ANA@example.com`
- fecha: `T0+10`
- personas: `3`
- notas: `Mesa cerca de la ventana`

### Técnica controlada para alcanzar validación de servidor

Por defecto, todos los casos se ejecutan mediante la interfaz normal del navegador.

Únicamente en `MC-04E`, `MC-05D`, `MC-07F`, `MC-08C` y en la subcomprobación de cancelación de `MC-12` se permite utilizar las herramientas de desarrollo del navegador para modificar temporalmente atributos del DOM definidos expresamente en este instrumento.

La finalidad exclusiva de esta técnica es permitir que una entrada o solicitud ya congelada alcance el servidor cuando un control del navegador impide hacerlo por la interfaz normal.

Reglas:

1. no modificar archivos fuente de la aplicación;
2. no modificar código del servidor;
3. no utilizar `curl`, Postman, scripts HTTP, `fetch()` manual ni solicitudes construidas fuera del formulario;
4. no introducir valores diferentes de los especificados en el caso;
5. no crear rutas ni casos adicionales;
6. conservar la sesión, cookies y token CSRF generados normalmente por la aplicación;
7. modificar únicamente el atributo indicado para el caso;
8. registrar que se aplicó la técnica controlada y qué atributo fue modificado;
9. la modificación del DOM es local, temporal y termina al recargar la página.

Esta técnica forma parte del procedimiento congelado cuando la versión v0.2 sea revalidada y aprobada; por tanto, su uso en los casos indicados no constituye una prueba ad hoc.

## 4. Casos manuales

### MC-01 — Acceso sin autenticación

1. Abrir el listado de reservas sin sesión iniciada.
2. Verificar que la aplicación no permita acceder al listado y redirija al inicio de sesión.

Resultado esperado: acceso al listado no permitido sin autenticación.

### MC-02 — Autenticación

Ejecutar:

1. U1 con contraseña válida;
2. U1 con contraseña incorrecta.

Resultados esperados:

- credenciales válidas permiten iniciar sesión;
- credenciales inválidas no permiten iniciar sesión y muestran el error correspondiente.

### MC-03 — Creación válida

Con U1 crear una reserva usando los datos base.

Resultado esperado:

- operación aceptada;
- reserva persistida;
- estado inicial `ACTIVE`;
- personas = 3.

### MC-04 — Nombre

Comprobar creación con:

| Variante | Valor | Esperado |
|---|---|---|
| MC-04A | vacío | rechazado |
| MC-04B | `A` | rechazado |
| MC-04C | `AB` | aceptado |
| MC-04D | `A` repetida 100 veces | aceptado |
| MC-04E | `A` repetida 101 veces | rechazado por validación de servidor |

Cada variante se ejecuta con los demás campos válidos.

#### Ejecución especial de MC-04E

Si el atributo cliente `maxlength="100"` impide introducir 101 caracteres:

1. abrir las herramientas de desarrollo del navegador;
2. localizar el campo `guest_name`;
3. eliminar únicamente el atributo `maxlength`;
4. introducir exactamente 101 caracteres `A`;
5. enviar el formulario mediante su botón normal;
6. verificar la respuesta de la aplicación.

Resultado esperado: el servidor rechaza la operación y la reserva no se persiste.

### MC-05 — Correo

Comprobar:

| Variante | Valor | Esperado |
|---|---|---|
| MC-05A | vacío | rechazado |
| MC-05B | `correo-invalido` | rechazado |
| MC-05C | `cliente@example.com` | aceptado |
| MC-05D | cadena de 256 caracteres con estructura mínima de correo aceptada por la aplicación | rechazado por validación de servidor |

Cada variante se ejecuta con los demás campos válidos.

#### Valor congelado de MC-05D

Utilizar exactamente:

- 244 caracteres `a`;
- seguidos de `@example.com`.

Longitud total: **256 caracteres**.

La finalidad es comprobar el límite de 255 caracteres definido por BR-02 y no la conformidad completa con RFC de correo electrónico.

#### Ejecución especial de MC-05D

Si los controles del navegador impiden enviar el valor:

1. abrir las herramientas de desarrollo;
2. localizar el campo `guest_email`;
3. eliminar únicamente `maxlength`;
4. si `type="email"` impide el envío antes de llegar al servidor, cambiar únicamente `type="email"` por `type="text"`;
5. introducir el valor congelado de 256 caracteres;
6. enviar mediante el botón normal del formulario;
7. verificar la respuesta de la aplicación.

Resultado esperado: el servidor rechaza la operación y la reserva no se persiste.

### MC-06 — Fecha

Comprobar:

| Variante | Valor | Esperado |
|---|---|---|
| MC-06A | vacío | rechazado |
| MC-06B | `T0-1` | rechazado |
| MC-06C | `T0` | aceptado |
| MC-06D | `T0+365` | aceptado |
| MC-06E | `T0+366` | rechazado |

Cada variante se ejecuta con los demás campos válidos.

### MC-07 — Número de personas

Comprobar:

| Variante | Valor | Esperado |
|---|---|---|
| MC-07A | vacío | rechazado |
| MC-07B | `0` | rechazado |
| MC-07C | `1` | aceptado |
| MC-07D | `12` | aceptado |
| MC-07E | `13` | rechazado |
| MC-07F | `abc` | rechazado por validación de servidor |

Cada variante se ejecuta con los demás campos válidos.

#### Ejecución especial de MC-07F

Si `type="number"` impide introducir `abc`:

1. abrir las herramientas de desarrollo;
2. localizar el campo `party_size`;
3. cambiar únicamente `type="number"` por `type="text"`;
4. introducir exactamente `abc`;
5. enviar mediante el botón normal del formulario;
6. verificar la respuesta.

Resultado esperado: el servidor rechaza la operación y la reserva no se persiste.

### MC-08 — Notas

Comprobar:

| Variante | Valor | Esperado |
|---|---|---|
| MC-08A | vacío | aceptado |
| MC-08B | `N` repetida 500 veces | aceptado |
| MC-08C | `N` repetida 501 veces | rechazado por validación de servidor |

Cada variante se ejecuta con los demás campos válidos.

#### Ejecución especial de MC-08C

Si `maxlength="500"` impide introducir 501 caracteres:

1. abrir las herramientas de desarrollo;
2. localizar el campo `notes`;
3. eliminar únicamente el atributo `maxlength`;
4. introducir exactamente 501 caracteres `N`;
5. enviar mediante el botón normal del formulario;
6. verificar la respuesta.

Resultado esperado: el servidor rechaza la operación y la reserva no se persiste.

### MC-09 — Edición válida

1. Crear una reserva válida con U1.
2. Editar el nombre a `Nombre Actualizado`.
3. Cambiar personas a `5`.

Resultado esperado:

- operación aceptada;
- cambios persistidos;
- nombre actualizado;
- personas = 5.

### MC-10 — Edición inválida

1. Partir de una reserva válida.
2. Intentar editarla estableciendo personas = `99`.

Resultado esperado:

- operación rechazada;
- los datos inválidos no se persisten.

La respuesta puede producirse por control cliente o servidor. Este caso no sustituye la comprobación server-side específica de BR-07 realizada mediante las variantes especiales anteriores.

### MC-11 — Normalización de correo

Crear una reserva utilizando:

`ANA@example.com`

Resultado esperado:

el correo persistido queda normalizado como:

`ana@example.com`

### MC-12 — Acceso entre usuarios

#### Preparación

1. Iniciar sesión como U1.
2. Crear una reserva válida y registrar su ID como `R-U1`.
3. Confirmar que `R-U1` se encuentra `ACTIVE`.
4. Cerrar la sesión de U1.
5. Iniciar sesión como U2.

#### Consulta y edición

6. Intentar consultar directamente `R-U1`.
7. Intentar editar directamente `R-U1`.

Resultados esperados:

- U2 no puede consultar `R-U1`;
- U2 no puede editar `R-U1`.

#### Cancelación mediante POST controlado

8. Con U2 crear una reserva válida propia y registrar su ID como `R-U2`.
9. Abrir el detalle de `R-U2`.
10. Verificar que existe el formulario normal de cancelación de `R-U2`.
11. Abrir las herramientas de desarrollo.
12. Localizar exclusivamente el formulario de cancelación.
13. Cambiar únicamente su atributo `action`, reemplazando el ID `R-U2` por el ID `R-U1`.
14. No modificar `method="post"`, el token CSRF, cookies, sesión ni ningún otro campo.
15. Enviar el formulario mediante el botón normal de cancelación.
16. Volver a comprobar `R-U1` con U1 al finalizar la prueba.

Resultados esperados:

- el POST ejecutado bajo la sesión de U2 no permite cancelar `R-U1`;
- la aplicación responde con control de acceso equivalente al utilizado para consulta/edición;
- `R-U1` permanece almacenada;
- `R-U1` permanece `ACTIVE`.

La modificación temporal del `action` se utiliza únicamente para comprobar BR-08 sobre la operación POST de cancelación y no constituye una ruta o caso adicional.

### MC-13 — Cancelación

1. U1 crea una reserva válida.
2. Cancelar utilizando el flujo normal de la aplicación.

Resultado esperado:

- la reserva permanece almacenada;
- su estado cambia a `CANCELLED`.

### MC-14 — Acceso directo a cancelación mediante GET

1. Crear una reserva válida.
2. Intentar acceder mediante GET a la URL de cancelación.

Resultado esperado:

- la operación no modifica la reserva;
- el método no es aceptado para efectuar la cancelación.

## 5. Reglas de ejecución

- ejecutar los casos en el orden definido;
- registrar resultado observado y evidencia;
- no agregar casos ad hoc durante el run;
- un resultado inesperado se registra como hallazgo;
- un caso fallido no se repite salvo incidencia técnica permitida por el protocolo;
- no corregir la aplicación durante el run;
- no alterar datos o criterios para confirmar un hallazgo;
- utilizar la técnica controlada de modificación temporal del DOM únicamente donde este instrumento la autoriza expresamente;
- no utilizar la técnica controlada para explorar valores, rutas o hipótesis diferentes de las ya congeladas;
- registrar como incidencia cualquier caso en el que la técnica controlada no permita hacer llegar la solicitud prevista al servidor.

## 6. Registro

Para cada caso se registra como mínimo:

| Campo |
|---|
| ID del caso |
| fecha/hora |
| investigador |
| resultado observado |
| PASS/FAIL respecto al comportamiento esperado |
| evidencia |
| técnica controlada aplicada, si corresponde |
| observaciones |
| incidencia asociada, si aplica |

## 7. Control de cambios

### v0.1

Versión utilizada por `PILOT-CONV-01`.

`PILOT-CONV-01` fue invalidado debido a `INC-C03-001` e `INC-C03-002`.

### v0.2

Cambios derivados exclusivamente de las incidencias del piloto:

1. MC-04E: se define cómo superar temporalmente `maxlength` para comprobar BR-01/BR-07 en servidor.
2. MC-05D: se fija un valor determinista de 256 caracteres y se define cómo superar los controles cliente para comprobar BR-02/BR-07.
3. MC-07F: se define cambio temporal de `type` para enviar `abc` al servidor y comprobar BR-05/BR-07.
4. MC-08C: se define cómo superar temporalmente `maxlength` para comprobar BR-06/BR-07.
5. MC-12: se define un POST controlado mediante un formulario normal de U2, preservando sesión y CSRF, para comprobar BR-08 en cancelación.

Estos cambios:

- se realizan fuera de `PILOT-CONV-01`;
- no modifican retroactivamente sus resultados;
- no alteran las reglas BR-01–BR-12;
- no introducen casos nuevos;
- no consultan D01–D05;
- requieren revalidación antes de un nuevo freeze.
