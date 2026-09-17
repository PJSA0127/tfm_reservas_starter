# Reglas de negocio del demostrador de reservas — v0.1

**Estado:** DEFINIDO para pilotaje; sujeto a freeze final.

Estas reglas documentan el comportamiento funcional actualmente implementado en el demostrador y constituyen la referencia funcional para los procedimientos.

## Reglas

| ID | Regla |
|---|---|
| BR-01 | `guest_name` es obligatorio y, tras eliminar espacios externos, debe contener entre 2 y 100 caracteres. |
| BR-02 | `guest_email` es obligatorio, debe contener una estructura mínima de correo aceptada por la aplicación y no superar 255 caracteres. |
| BR-03 | `reservation_date` debe ser una fecha ISO válida y no puede estar en el pasado. |
| BR-04 | `reservation_date` no puede superar 365 días desde la fecha actual del servidor. |
| BR-05 | `party_size` debe ser convertible a entero y estar en el rango inclusivo 1–12. |
| BR-06 | `notes` es opcional y no puede superar 500 caracteres tras eliminar espacios externos. |
| BR-07 | BR-01 a BR-06 deben aplicarse en servidor al crear y editar; la validación del navegador no constituye por sí sola un control suficiente. |
| BR-08 | Un usuario autenticado solo puede consultar, editar o cancelar reservas asociadas a su propio `user_id`. |
| BR-09 | Cancelar una reserva cambia su estado a `CANCELLED`; la fila no se elimina físicamente. |
| BR-10 | Las operaciones que modifican estado deben usar métodos HTTP no seguros en el sentido de HTTP; creación, edición y cancelación persisten mediante `POST`. |
| BR-11 | Creación y edición solo persisten cuando la validación de servidor concluye sin errores. |
| BR-12 | El correo de la reserva se normaliza a minúsculas después de superar la validación. |

## Casos de frontera mínimos

- Nombre: 1, 2, 100 y 101 caracteres.
- Correo: inválido, aceptado y >255 caracteres.
- Fecha: ayer, hoy, hoy +365 y hoy +366 días.
- Personas: 0, 1, 12, 13 y no numérico.
- Notas: 0, 500 y 501 caracteres.

## Control

- No modificar las reglas como respuesta a resultados observados.
- Cualquier cambio funcional anterior al freeze debe documentarse.
- Durante la fase definitiva ambos procesos deben evaluar la misma versión funcional.
