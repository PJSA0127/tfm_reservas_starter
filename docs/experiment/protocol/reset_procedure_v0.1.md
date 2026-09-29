# Procedimiento de restauración del entorno — v0.1

## 1. Estado

**CERRADO PARA PILOTAJE / RESET PREPARADO NO EJECUTADO / FREEZE DEFINITIVO PENDIENTE.**

## 2. Objetivo

Garantizar que cada proceso parta de un estado inicial equivalente y que no herede datos técnicos, sesión o artifacts de la ejecución previa.

## 3. Roles

- I1 ejecuta las acciones técnicas.
- I2 registra el reset y sus tiempos.
- I3 verifica y autoriza el inicio del siguiente proceso.

El siguiente proceso no comienza sin aprobación de I3.

## 4. R01 — Cerrar ejecución anterior

Antes del reset:

1. detener cronometraje;
2. cerrar run record;
3. archivar evidencia;
4. registrar incidencias;
5. no crear nueva evidencia para el run cerrado.

## 5. R02 — Detener entorno

Ejecutar el equivalente congelado de:

```powershell
docker compose down -v --remove-orphans
```

para el proyecto/entorno correspondiente.

## 6. R03 — Limpiar estado efímero

Eliminar del workspace activo:

- artifacts temporales;
- reportes efímeros;
- caches permitidas;
- sesiones técnicas no necesarias.

No eliminar la copia archivada de la evidencia anterior.

## 7. R04 — Restaurar código

Restaurar el commit/tag asignado.

Para convencional, generar/restaurar el workspace sanitizado derivado del mismo origen.

Para propuesto, utilizar la instrumentación completa.

## 8. R05 — Restaurar configuración

- recrear `.env` desde `.env.example`;
- restaurar las mismas variables;
- validar Compose;
- no reutilizar secretos/sesiones de una ejecución previa salvo que estén definidos como parte del entorno congelado.

## 9. R06 — Reconstruir e inicializar

- reconstruir/levantar servicios;
- esperar estado healthy;
- comprobar init service;
- inicializar la misma BD/datos previstos;
- comprobar ausencia de errores de arranque.

## 10. R07 — Comprobación funcional mínima

Antes de autorizar el siguiente run:

- healthcheck;
- aplicación accesible;
- flujo mínimo de autenticación cuando corresponda;
- ausencia de HTTP 5xx inesperados;
- estado inicial esperado.

Esta comprobación no se utiliza para descubrir defectos ni genera resultados experimentales.

## 11. R08 — Estado del navegador

Utilizar un **perfil privado/incógnito nuevo para cada ejecución**.

No reutilizar cookies, local storage ni autenticación de la ejecución previa.

## 12. R09 — Evidencia del reset

Registrar:

- fecha/hora;
- commit/tag;
- workspace;
- comandos ejecutados;
- estado de contenedores;
- estado de volúmenes;
- inicialización de BD;
- healthcheck;
- perfil de navegador limpio;
- incidencias;
- aprobación I3.

## 13. Criterio PASS

El reset es PASS cuando I3 confirma que se recuperó el estado inicial requerido.

Si no puede garantizarse:

```text
NO INICIAR SIGUIENTE PROCESO
```

hasta resolver la incidencia.

## 14. Entre convencional y propuesto definitivo

No se permite:

- corregir código;
- modificar defectos;
- añadir/quitar controles;
- cambiar configuración experimental;
- modificar criterios.

Aunque el convencional descubra un defecto, este permanece intacto para el proceso propuesto.
