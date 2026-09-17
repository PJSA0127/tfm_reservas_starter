# Calibración de autenticación OWASP ZAP — v0.1

## Resultado

La ejecución aislada del Authentication Helper de ZAP 2.17.0 finalizó
satisfactoriamente.

| Control diagnóstico | Resultado |
|---|---|
| Authentication appeared to work | PASS |
| Username field identified | PASS |
| Password field identified | PASS |
| Session Handling identified | PASS |
| Verification URL identified | PASS |

## Configuración detectada

ZAP determinó automáticamente:

- autenticación: Browser Authentication;
- navegador: `firefox-headless`;
- pasos: `AUTO_STEPS`;
- URL de login: `/auth/login`;
- verificación: polling de `/reservations/`;
- indicador autenticado: `200 OK`;
- indicador no autenticado: `302 FOUND`;
- gestión de sesión: Header-Based Session Management.

Esta configuración detectada se utilizará como base para el plan DAST de
calibración v0.6.

## Tratamiento del reporte

El Authentication Report contiene las credenciales del usuario de laboratorio
dentro de la representación `afEnv`. Por este motivo el archivo original se
mantendrá fuera de Git. Si se requiere conservar evidencia documental, se
generará una copia sanitizada en la que la contraseña sea sustituida por
`[REDACTED]`.

## Clasificación metodológica

Este resultado corresponde a configuración/calibración del mecanismo DAST,
no a la ejecución experimental definitiva.
