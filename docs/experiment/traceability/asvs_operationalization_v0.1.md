# Operacionalización de requisitos OWASP ASVS 5.0.0 L1 — v0.1

**Estado:** IMPLEMENTADO Y CALIBRADO. Preparación pre-piloto completada; pilotos no iniciados; freeze experimental definitivo pendiente.

## Convención de identificación

Para evitar ambigüedad entre versiones, la documentación experimental utilizará el identificador completo `v5.0.0-X.Y.Z`. Se mantiene entre paréntesis el identificador corto empleado en `TFM - G7.docx`.

## Matriz de operacionalización

| ID ASVS | Condición de seguridad operacional | Criterio para considerar el requisito efectivamente verificado | Mecanismo previsto — proceso propuesto | Evidencia mínima esperada | Defecto asociado |
|---|---|---|---|---|---|
| **v5.0.0-1.2.1 (V1.2.1)** | Los datos no confiables mostrados en respuestas HTML no deben poder alterar la estructura del documento ni introducir contenido ejecutable por falta de codificación contextual. | Se ejecuta una prueba con cargas de marcado/script en campos persistentes y la respuesta renderizada contiene el contenido codificado/escapado, sin interpretarlo como HTML ejecutable. Además, no se identifican usos intencionales de mecanismos de bypass de autoescape en los puntos evaluados. | Prueba específica `pytest` + regla/revisión SAST con Semgrep; DAST de ZAP como evidencia complementaria frente a XSS. | Reporte pytest; salida Semgrep; reporte ZAP cuando aplique; referencia al archivo/endpoint evaluado. | D01 |
| **v5.0.0-1.2.4 (V1.2.4)** | Las operaciones de selección y modificación de datos no deben construir consultas SQL con datos no confiables mediante concatenación/interpolación insegura. | Los flujos evaluados emplean ORM/consultas parametrizadas y las cargas de inyección definidas no alteran la semántica de la consulta ni permiten recuperar/modificar datos fuera de lo esperado. | Semgrep + prueba específica `pytest`/HTTP con carga de inyección + ZAP SQL Injection como evidencia complementaria. | Reporte Semgrep; resultado de prueba específica; reporte ZAP; referencia a las operaciones de persistencia. | D02 |
| **v5.0.0-2.2.1 (V2.2.1)** | Las entradas que intervienen en decisiones funcionales deben ajustarse a las reglas documentadas BR-01–BR-06. | Para creación y edición, los casos inválidos y de frontera definidos son rechazados de acuerdo con las reglas y no producen persistencia de un estado inválido. | Pruebas específicas `pytest` dirigidas directamente al servidor, reutilizando el catálogo documentado de valores válidos, inválidos y frontera. | Reporte pytest con casos positivos/negativos y evidencia de no persistencia ante entradas inválidas. | D03 |
| **v5.0.0-2.2.2 (V2.2.2)** | La validación de entrada debe aplicarse en una capa confiable del servidor y no depender del HTML, JavaScript o restricciones del navegador. | Solicitudes HTTP construidas sin respetar controles de cliente siguen siendo rechazadas por el servidor cuando incumplen BR-01–BR-06, tanto en creación como en edición. | Prueba específica `pytest` usando el cliente HTTP de Flask o solicitudes directas sin validación de navegador; revisión del flujo servidor como apoyo. | Reporte pytest mostrando rechazo server-side y ausencia de persistencia inválida; referencia al validador invocado por los endpoints. | D03 |
| **v5.0.0-3.5.1 (V3.5.1)** | Las operaciones sensibles susceptibles de falsificación de solicitudes deben verificar que la solicitud se origine en el contexto permitido mediante un mecanismo anti-forgery aplicable. | Una solicitud mutante sin token CSRF o con token inválido es rechazada; una solicitud equivalente con token válido puede procesarse cuando el resto de condiciones son correctas. | Prueba específica `pytest` de CSRF + ZAP como verificación dinámica complementaria de ausencia/presencia de protección. | Resultado pytest para token ausente, inválido y válido; reporte ZAP cuando aplique; evidencia de configuración `CSRFProtect`. | D04 |
| **v5.0.0-3.5.3 (V3.5.3)** | La funcionalidad que cambia estado no debe depender de métodos HTTP definidos como seguros, como `GET` o `HEAD`. | Las solicitudes `GET`/`HEAD`/`OPTIONS` a operaciones mutantes no producen modificación de estado. La modificación solo ocurre a través del método no seguro definido (`POST` en el demostrador). | Prueba específica `pytest` + Semgrep/revisión de decoradores de rutas; ZAP puede aportar evidencia dinámica complementaria. | Reporte pytest antes/después del estado; salida Semgrep/revisión de rutas; evidencia del método permitido. | D05 |

## Identificadores propuestos para las pruebas específicas

| ID prueba | Requisito | Propósito |
|---|---|---|
| SEC-V121-01 | v5.0.0-1.2.1 | Verificar escape contextual de datos persistidos en HTML. |
| SEC-V124-01 | v5.0.0-1.2.4 | Verificar resistencia del flujo seleccionado a entrada de inyección y uso de acceso parametrizado/ORM. |
| SEC-V221-01 | v5.0.0-2.2.1 | Verificar reglas de validación mediante valores inválidos y de frontera. |
| SEC-V222-01 | v5.0.0-2.2.2 | Verificar que la validación se mantenga al omitir/burlar controles de cliente. |
| SEC-V351-01 | v5.0.0-3.5.1 | Verificar rechazo de operación sensible sin token anti-forgery válido. |
| SEC-V353-01 | v5.0.0-3.5.3 | Verificar que métodos HTTP seguros no modifiquen estado. |

## Reglas de evidencia

1. Un requisito no se marcará como **verificado** únicamente porque la implementación parezca correcta.
2. Debe existir evidencia de que el mecanismo definido se ejecutó y produjo un resultado evaluable.
3. La ausencia de alertas de Semgrep o ZAP, por sí sola, no se interpretará como demostración suficiente cuando el requisito requiera una comprobación específica.
4. Un único defecto puede afectar más de un requisito; D03 se registra una sola vez para tasa de detección, pero V2.2.1 y V2.2.2 se evalúan por separado para cobertura.
5. Las evidencias automatizadas se generan en `artifacts/` localmente y, en CI, se preservan mediante artifacts específicos por mecanismo y ejecución.
6. Los mecanismos, cargas, reglas y criterios se congelarán antes de la ejecución definitiva.

## Correspondencia inicial con el código actual

| Requisito | Punto actual del baseline que permite operacionalizarlo |
|---|---|
| v5.0.0-1.2.1 | Renderizado Jinja2 de `guest_name`, `guest_email` y `notes` en las plantillas de reservas. |
| v5.0.0-1.2.4 | Uso de SQLAlchemy ORM/`select()` y asignaciones ORM en los flujos CRUD. |
| v5.0.0-2.2.1 | `validate_reservation()` y reglas BR-01–BR-06. |
| v5.0.0-2.2.2 | Llamada a `validate_reservation()` desde los `POST` de creación y edición. |
| v5.0.0-3.5.1 | `CSRFProtect` inicializado globalmente y tokens presentes en formularios mutantes. |
| v5.0.0-3.5.3 | Cancelación declarada como `POST`; creación/edición persisten cambios únicamente durante `POST`. |

## Estado de esta versión

La operacionalización ya cuenta con implementación y calibración local de los mecanismos técnicos:

- seis pruebas específicas de seguridad `pytest`;
- seis reglas Semgrep locales y versionadas;
- plan ZAP autenticado y calibrado;
- correspondencia SAST/DAST documentada;
- rutas locales de evidencia;
- workflow CI manual del proceso propuesto preparado.

La preparación pre-piloto de esta operacionalización está cerrada. Antes del freeze experimental definitivo todavía falta:

- ejecutar `PILOT-CONV-01` sobre la instancia segura de calibración;
- cerrar, archivar y verificar la integridad de la evidencia del piloto convencional;
- ejecutar el reset formal entre los procesos y verificar condiciones equivalentes;
- ejecutar `PILOT-PROP-01` sobre la instancia segura de calibración;
- cerrar, archivar y verificar la integridad de la evidencia del piloto propuesto;
- analizar las incidencias, lecciones y registros de esfuerzo obtenidos durante ambos pilotos;
- aplicar únicamente los ajustes permitidos por claridad, instrumentación o reproducibilidad y versionar los instrumentos afectados cuando corresponda;
- fijar las versiones, digests y SHAs definitivos y congelar el protocolo experimental antes de introducir D01–D05.
