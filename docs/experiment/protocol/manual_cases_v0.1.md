# Casos manuales funcionales — v0.1

## 1. Estado

**CERRADO PARA PILOTAJE.**

Este instrumento fija los casos manuales utilizados durante el proceso convencional y las actividades funcionales comunes del piloto.

No se agregan, eliminan ni modifican casos durante una ejecución abierta.

## 2. Referencia

Los casos se derivan exclusivamente de las reglas BR-01 a BR-12 de `business_rules_v0.1.md`.

## 3. Datos comunes congelados

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
| MC-04E | `A` repetida 101 veces | rechazado |

Cada variante se ejecuta con los demás campos válidos.

### MC-05 — Correo

Comprobar:

| Variante | Valor | Esperado |
|---|---|---|
| MC-05A | vacío | rechazado |
| MC-05B | `correo-invalido` | rechazado |
| MC-05C | `cliente@example.com` | aceptado |
| MC-05D | correo válido de longitud superior a 255 caracteres | rechazado |

Cada variante se ejecuta con los demás campos válidos.

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
| MC-07F | `abc` | rechazado |

Cada variante se ejecuta con los demás campos válidos.

### MC-08 — Notas

Comprobar:

| Variante | Valor | Esperado |
|---|---|---|
| MC-08A | vacío | aceptado |
| MC-08B | `N` repetida 500 veces | aceptado |
| MC-08C | `N` repetida 501 veces | rechazado |

Cada variante se ejecuta con los demás campos válidos.

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

### MC-11 — Normalización de correo

Crear una reserva utilizando:

`ANA@example.com`

Resultado esperado:

el correo persistido queda normalizado como:

`ana@example.com`

### MC-12 — Acceso entre usuarios

1. U1 crea una reserva.
2. Cerrar la sesión de U1.
3. Iniciar sesión como U2.
4. Intentar consultar la reserva creada por U1.
5. Intentar editarla.
6. Intentar cancelarla.

Resultado esperado:

U2 no puede consultar, modificar ni cancelar la reserva perteneciente a U1.

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
- no alterar datos o criterios para confirmar un hallazgo.

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
| observaciones |
| incidencia asociada, si aplica |

## 7. Control de cambios

Este instrumento queda congelado para la ejecución piloto.

Cualquier ajuste posterior derivado de una incidencia del piloto:

1. se realiza fuera del Run ID;
2. se documenta;
3. requiere nueva versión antes de una ejecución posterior;
4. no modifica retroactivamente los resultados del run ya cerrado.