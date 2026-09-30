# PILOT-CONV-02 — Estado READY_TO_START previo a C00

## Estado general

**PILOT-CONV-02 = READY_TO_START / NOT_STARTED**

El entorno convencional fue reconstruido, verificado y congelado después de la invalidación de `PILOT-CONV-01` y de la revalidación de los instrumentos convencionales v0.2 mediante `REV-INSTR-01`.

Este estado es previo a `C00`. No se ha iniciado cronometraje experimental ni se han ejecutado actividades experimentales de `PILOT-CONV-02`.

---

## Antecedentes

- `PILOT-CONV-01`: INVALIDATED / EXCLUDED FROM FINAL COMPARISON.
- `REV-INSTR-01`: COMPLETADA / SELLADA.
- Subcomprobaciones revalidadas: 5/5 PASS.
- Instrumentos convencionales v0.2: REVALIDADOS.
- Código de la aplicación modificado durante la corrección de instrumentos: NO.

---

## Baseline técnico

- Tag: `pre-pilot-freeze-v0.1`
- Commit: `32d27a04305617f8fea031704e24d7e68ce9c451`

---

## Workspace de ejecución

`D:\Repositorios\tfm_reservas_pilot_conv_run_02`

Proyecto Docker:

`tfm_pilot_conv_02`

Archivos fuente congelados:

`31`

Estado:

- `db = healthy`
- `db_init = exited 0`
- `web = healthy`
- `HTTP /health = 200`
- `user_count = 2`
- `reservation_count = 0`

Usuarios piloto:

- `1|pilot.user1@tfm.local`
- `2|pilot.user2@tfm.local`

---

## Siembra de usuarios

Durante el preflight de `PILOT-CONV-02`, el volumen PostgreSQL limpio fue creado correctamente pero quedó inicialmente con:

- `user_count = 0`
- `reservation_count = 0`

Se verificó que `db_init` crea el esquema pero no realiza la siembra de los usuarios piloto.

Se reprodujo el mismo procedimiento de preparación utilizado antes de `PILOT-CONV-01`, creando U1 y U2 mediante `User.set_password()`.

Registro:

`PREP-PILOT-CONV-02-001`

Resultado:

- usuarios = 2
- reservas = 0
- archivos fuente modificados = 0
- pruebas experimentales ejecutadas = 0

---

## Identificadores de integridad

Candidate manifest SHA-256:

`cfbaa735d5f0c8f4f82d3fde283212b5ce37b47719fde504dbfbb678357be839`

Candidate package SHA-256:

`f6e3335ff10ce4fe79a9410eefbb4b3dbf3e87d76f486ea5bbcc8e47a071c214`

Runtime `.env` SHA-256:

`ee6fddb929b09e0ed7410d4c8436d604b1e62962d8af5002412413a9cdb9f652`

Preflight SHA-256:

`8786a43cccd3cf88a18c1d50d8708e9fdb017a6a9ebaed01a4995a7e5545869e`

PREP-PILOT-CONV-02-001 SHA-256:

`ac7dae9d924229afc327205f25cb48e6d8ca0bd1f34cbfa4d39ddf643b2803f6`

Final freeze manifest SHA-256:

`01e88118ca8798926cb1ec4c72fde8ce35bade052c6776f1ac5e68f8697481b6`

Freeze receipt SHA-256:

`83c7ca630eb5b472c7c7f8a549389ff6b31794979b43769fd01a60769b50092e`

La copia secundaria del freeze fue verificada por hashes: PASS.

---

## Estado experimental

- `PILOT-CONV-02 = READY_TO_START / NOT_STARTED`
- `C00 = NO INICIADO`
- `C01 = NO EJECUTADO`
- Casos manuales = NO EJECUTADOS
- Revisión experimental = NO EJECUTADA
- Tiempo experimental acumulado = 0

---

## Regla de continuidad

Antes de iniciar `C00` se deben revalidar únicamente las condiciones volátiles:

- Docker disponible;
- `db` healthy;
- `web` healthy;
- `db_init` en estado válido;
- `/health = 200`;
- U1 y U2 presentes;
- `reservation_count = 0`;
- navegador/perfil privado limpio;
- evidencia disponible;
- I1, I2 e I3 disponibles.

No se deben repetir la reconstrucción del workspace, la revalidación de instrumentos, la generación del paquete, los manifiestos ni el freeze mientras no se detecte una discrepancia de integridad.

Apagar o reiniciar el equipo antes de `C00` no constituye una pausa experimental.

El siguiente paso formal es `C00`, únicamente cuando se autorice explícitamente el inicio de `PILOT-CONV-02`.