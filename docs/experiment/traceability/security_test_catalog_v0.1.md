# Catálogo de pruebas específicas de seguridad — v0.1

**Estado:** IMPLEMENTADO Y CALIBRADO LOCALMENTE; pendiente de piloto y congelación del protocolo.

| ID | ASVS 5.0.0 | Archivo | Objetivo principal | Evidencia esperada en baseline seguro |
|---|---|---|---|---|
| SEC-V121-01 | `v5.0.0-1.2.1` | `tests/security/test_v121_output_encoding.py` | Comprobar que contenido persistido no confiable se escape en contexto HTML. | Carga de `<script>` aparece codificada y no como marcado ejecutable. |
| SEC-V124-01 | `v5.0.0-1.2.4` | `tests/security/test_v124_injection.py` | Comprobar que una carga SQL no altere la consulta de autenticación. | La carga no autentica; Semgrep/DAST aportarán evidencia complementaria del mecanismo. |
| SEC-V221-01 | `v5.0.0-2.2.1` | `tests/security/test_v221_input_validation.py` | Comprobar reglas y fronteras documentadas para entradas relevantes. | Inválidos rechazados sin persistencia; fronteras válidas aceptadas. |
| SEC-V222-01 | `v5.0.0-2.2.2` | `tests/security/test_v222_server_validation.py` | Omitir controles HTML y comprobar que el servidor sigue validando. | HTTP directo inválido es rechazado en creación y edición. |
| SEC-V351-01 | `v5.0.0-3.5.1` | `tests/security/test_v351_csrf.py` | Comprobar protección anti-forgery de una operación sensible. | Token ausente/inválido: 400 y sin cambio; token válido: operación permitida. |
| SEC-V353-01 | `v5.0.0-3.5.3` | `tests/security/test_v353_http_methods.py` | Comprobar que métodos HTTP seguros no produzcan cambios de estado. | GET/HEAD/OPTIONS conservan `ACTIVE`; POST puede cambiar a `CANCELLED`. |

## Nota metodológica

Estas pruebas pertenecen al **proceso propuesto**. Durante la evaluación definitiva no deben utilizarse como guía ni ejecutarse dentro del proceso convencional. Antes de la congelación del protocolo pueden ejecutarse sobre la instancia de calibración para comprobar que el mecanismo, el registro y la evidencia funcionan correctamente.

La evidencia de estas pruebas ya se complementa con Semgrep y OWASP ZAP según la matriz de operacionalización. Ningún mecanismo se interpreta aisladamente como demostración suficiente cuando el criterio del requisito exige evidencia combinada. La calibración local registró 22/22 pruebas específicas aprobadas; el resultado no forma parte de la comparación experimental definitiva.
