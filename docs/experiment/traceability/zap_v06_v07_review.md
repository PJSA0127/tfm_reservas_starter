# Revisión técnica ZAP v0.6 → v0.7

## Código fuente comprobado

Las rutas:

- `/reservations/`
- `/reservations/new`
- `/reservations/<id>`
- `/reservations/<id>/edit`

utilizan `@login_required`.

En ausencia de sesión Flask-Login redirige al login (`302`).

## Evidencia observada

En una ejecución no autenticada previa ZAP reportó:

`Expected : 200 Received : 302`

para las cuatro rutas.

En v0.6 las mismas cuatro peticiones se ejecutaron sin una diferencia de
`responseCode`, por lo que recibieron `200`.

La posterior falla ocurrió únicamente al evaluar expresiones de texto mediante
los URL Presence tests.

## Decisión

Se mantienen los `responseCode: 200` como guarda directa y se añaden las
estadísticas de autenticación recomendadas por ZAP.

No se modifica la aplicación para acomodar al escáner.
