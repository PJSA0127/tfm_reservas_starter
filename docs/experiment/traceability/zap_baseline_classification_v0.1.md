# Clasificación de hallazgos ZAP — calibración baseline v0.1

**Estado:** EVIDENCIA HISTÓRICA DE CALIBRACIÓN INICIAL. Este documento registra una ejecución previa y queda supersedido como estado final por `zap_dast_calibration_v0.1.md`; se conserva para trazabilidad de los ajustes de instrumentación.

## Resultado observado

La primera ejecución DAST completó autenticación, exploración, análisis pasivo,
active scan y generación de artefactos. Se observaron los siguientes tipos de
alerta:

| Plugin ID | Riesgo | Hallazgo | Clasificación experimental |
|---:|---|---|---|
| 10038 | Medium | Content Security Policy (CSP) Header Not Set | Hallazgo adicional válido; fuera de D01–D05 y de los seis requisitos seleccionados. |
| 10020 | Medium | Missing Anti-clickjacking Header | Hallazgo adicional válido; fuera de D01–D05 y de los seis requisitos seleccionados. |
| 10036 | Low | Server Leaks Version Information via `Server` header | Hallazgo adicional válido; fuera de D01–D05. |
| 10021 | Low | `X-Content-Type-Options` Header Missing | Hallazgo adicional válido; fuera de D01–D05. |
| 10111 | Informational | Authentication Request Identified | Información de instrumentación; no es vulnerabilidad. |
| 10112 | Informational | Session Management Response Identified | Información de instrumentación; no es vulnerabilidad. |
| 10113 | Informational | Verification Request Identified | Información de instrumentación; no es vulnerabilidad. |

## Relación con los defectos controlados

En esta calibración no se observó una alerta activa correspondiente a:

- D01 / XSS (`40012` o `40014`);
- D02 / SQL Injection (`40018`);
- D04 / ausencia de anti-CSRF (`10202`).

Esto es coherente con el baseline seguro, pero no se interpreta aisladamente
como prueba suficiente de cumplimiento. La decisión de verificación se basa en
el conjunto de mecanismos definido para cada requisito.

## Acción sobre los hallazgos adicionales

Los hallazgos 10038, 10020, 10036 y 10021 **no se corrigen como consecuencia de
esta ejecución de calibración** antes de cerrar el protocolo, porque:

1. no pertenecen al catálogo D01–D05;
2. no forman parte de los seis requisitos ASVS seleccionados;
3. corregirlos como reacción al escaneo alteraría el baseline por hallazgos
   ajenos al objeto experimental.

Se conservan y documentan como hallazgos adicionales válidos.

## Mejora de instrumentación aplicada

La primera exportación de URLs demostró acceso a `/reservations/`, pero no
permitió demostrar de forma inequívoca que las páginas de creación, detalle y
edición habían sido exploradas.

Por ello la versión v0.2 del plan DAST añade solicitudes autenticadas explícitas
y tests de respuesta para:

- `/reservations/` → debe contener `Mis reservas`;
- `/reservations/new` → debe contener `Nueva reserva`;
- `/reservations/1` → debe contener `Cliente DAST`;
- `/reservations/1/edit` → debe contener `Editar reserva`.

Esta modificación corresponde a una mejora de instrumentación durante la fase
de calibración y debe quedar congelada antes de la evaluación definitiva.
