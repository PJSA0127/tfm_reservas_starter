# Ajustes de instrumentación derivados de PILOT-CONV-01 — v0.1

## 1. Estado

**DOCUMENTADO / PENDIENTE DE REVALIDACIÓN.**

Este documento registra exclusivamente los ajustes de instrumentación derivados de las incidencias observadas durante `PILOT-CONV-01`.

No modifica evidencia cerrada del run invalidado.

## 2. Run de origen

- Run ID: `PILOT-CONV-01`
- Estado: `INVALIDATED - EXCLUDED FROM FINAL COMPARISON`
- Incidencias causales:
  - `INC-C03-001`
  - `INC-C03-002`
- Próximo Run ID reservado: `PILOT-CONV-02`

## 3. Principios del ajuste

Los cambios cumplen las reglas post-piloto:

- se realizan fuera del run cerrado;
- responden a errores de instrumentación realmente observados;
- no se orientan a favorecer un resultado;
- no modifican BR-01–BR-12;
- no modifican el código de la aplicación;
- no consultan ni utilizan D01–D05;
- requieren nueva versión y revalidación antes del siguiente freeze.

## 4. Trazabilidad incidencia → ajuste

| Incidencia | Caso afectado | Problema observado | Ajuste |
|---|---|---|---|
| INC-C03-001 | MC-04E | `maxlength=100` impidió introducir 101 caracteres | permitir eliminación temporal de `maxlength` únicamente para MC-04E |
| INC-C03-001 | MC-05D | `maxlength=255` impidió introducir el valor >255 | fijar valor determinista de 256 caracteres y permitir bypass cliente controlado |
| INC-C03-001 | MC-07F | `type=number` impidió introducir `abc` | permitir cambio temporal `number` → `text` únicamente para MC-07F |
| INC-C03-001 | MC-08C | `maxlength=500` impidió introducir 501 caracteres | permitir eliminación temporal de `maxlength` únicamente para MC-08C |
| INC-C03-002 | MC-12 | U2 no podía alcanzar el formulario de cancelación de una reserva de U1 | utilizar formulario POST legítimo de U2 y cambiar únicamente su `action` hacia la reserva de U1 |

## 5. Justificación respecto a BR-07

`BR-07` establece que BR-01 a BR-06 deben aplicarse en servidor y que la validación del navegador no constituye por sí sola un control suficiente.

Por este motivo, los casos MC-04E, MC-05D, MC-07F y MC-08C no pueden considerarse satisfechos únicamente porque HTML bloquee la entrada.

La técnica controlada permite que el valor ya congelado alcance el servidor sin introducir una herramienta de seguridad, una ruta nueva o un valor exploratorio.

## 6. Justificación respecto a BR-08

`BR-08` exige que un usuario autenticado solo pueda consultar, editar o cancelar reservas asociadas a su propio `user_id`.

La consulta y edición pudieron observarse normalmente durante `PILOT-CONV-01`, pero la cancelación no era alcanzable mediante la interfaz de U2.

El ajuste de MC-12 reutiliza:

- sesión real de U2;
- token CSRF real;
- formulario POST real de U2;
- endpoint de cancelación ya existente.

Solo cambia temporalmente el ID de destino del `action` para hacer llegar al servidor la operación exacta que BR-08 exige comprobar.

## 7. Artefactos nuevos

- `manual_cases_v0.2.md`
- `conventional_procedure_v0.2.md`
- `post_pilot_instrument_adjustments_v0.1.md`

Las versiones anteriores no se sobrescriben.

## 8. Pendientes antes de PILOT-CONV-02

1. revisar técnicamente los tres documentos;
2. comprobar que las cinco variantes pueden ejecutarse sobre el baseline seguro;
3. actualizar referencias documentales que todavía apunten a `manual_cases_v0.1.md` o `conventional_procedure_v0.1.md`;
4. reconstruir el workspace convencional sanitizado con las versiones aprobadas;
5. generar nuevos hashes/manifiestos;
6. actualizar el checklist de freeze;
7. autorizar un nuevo freeze;
8. preparar `PILOT-CONV-02`;
9. no iniciar C00 hasta completar todos los puntos anteriores.
