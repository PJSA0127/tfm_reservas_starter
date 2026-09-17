# Procedimiento propuesto de verificación continua — v0.1

## 1. Estado

**CERRADO PARA PILOTAJE / PRE-FREEZE.**

## 2. Objetivo

Aplicar el proceso propuesto definido en el anteproyecto, conservando las actividades comunes del proceso convencional e incorporando requisitos ASVS explícitos, trazabilidad, pruebas específicas, SAST, DAST, CI y conservación estructurada de evidencias.

## 3. Roles

- **I1:** ejecutor principal.
- **I2:** registro de esfuerzo/evidencia.
- **I3:** supervisor del protocolo.

## 4. Orden obligatorio

1. actividades comunes del convencional;
2. revisión explícita de los seis requisitos ASVS;
3. pruebas específicas de seguridad;
4. Semgrep;
5. OWASP ZAP;
6. GitHub Actions;
7. consolidación de evidencias.

## 5. P01 — Actividades comunes

Ejecutar con el mismo procedimiento y datos congelados:

- pruebas funcionales;
- recorrido manual;
- casos válidos/vacíos/inválidos/frontera;
- revisión técnica del mismo alcance.

## 6. P02 — Revisión ASVS explícita

Revisar los seis requisitos mediante la operacionalización congelada.

La matriz requisito-prueba-evidencia se actualiza **durante la ejecución**, inmediatamente después de obtener una evidencia relevante.

## 7. P03 — Pruebas específicas de seguridad

Ejecutar la batería congelada de `tests/security/`.

Conservar:

- salida;
- JUnit;
- metadatos;
- clasificación posterior.

Un fallo de prueba en `proposed-definitive` puede representar evidencia de incumplimiento y no se confunde con un error técnico de pytest.

## 8. P04 — Semgrep

Ejecutar las reglas congeladas sobre la aplicación.

Conservar reporte y metadata.

Los hallazgos se registran durante la ejecución y se clasifican posteriormente.

Un hallazgo de seguridad no equivale por sí mismo a fallo técnico de Semgrep.

## 9. P05 — OWASP ZAP

Ejecutar DAST autenticado con el plan congelado.

Conservar:

- JSON;
- HTML/recursos;
- URLs;
- logs;
- clasificación;
- `web-dast.log`.

Los hallazgos adicionales fuera de D01–D05 se registran y se clasifican después para evitar desviar el procedimiento.

## 10. P06 — GitHub Actions

Ejecutar el workflow manual con la fase correspondiente:

- `pilot`;
- `proposed-definitive`.

GitHub Actions requiere conectividad y constituye un mecanismo adicional específico del proceso propuesto.

## 11. P07 — Reintento técnico

Se permite **un único reintento técnico** de un mecanismo cuando:

- el primer intento falló por causa técnica;
- no se modifica regla, prueba, criterio ni configuración experimental;
- el primer intento se conserva;
- se registra una incidencia;
- se documenta causa y resultado del reintento.

Si el reintento falla o exige cambiar criterios/configuración, la incidencia se trata según `incident_log_v0.1.md` y puede invalidar el run.

## 12. P08 — Hallazgos adicionales

Los hallazgos no pertenecientes al catálogo D01–D05:

- se registran durante la ejecución;
- no se investigan con pruebas ad hoc;
- se clasifican posteriormente como hallazgo adicional válido o falso positivo.

No modifican directamente la tasa de detección experimental.

## 13. P09 — Consolidación

I1/I2 consolidan las evidencias sin modificar resultados.

I3 comprueba que:

- las actividades previstas fueron ejecutadas;
- los artifacts pertenecen al Run ID;
- no se agregaron comprobaciones no previstas;
- las incidencias quedaron registradas.

## 14. P10 — Cierre

1. detener cronometraje;
2. cerrar registros;
3. descargar artifacts remotos aplicables;
4. archivar evidencias;
5. generar hashes según procedimiento;
6. no crear evidencia nueva después del cierre.

## 15. Internet y documentación

No se permiten búsquedas externas ad hoc durante las actividades manuales.

Se permite:

- documentación local previamente aprobada;
- conectividad necesaria para GitHub Actions y servicios que formen parte del procedimiento congelado.

## 16. Evidencia mínima

Además de la evidencia común:

- operacionalización ASVS usada;
- matriz actualizada;
- resultados de seguridad pytest;
- Semgrep;
- ZAP;
- artifacts CI;
- metadata del runner;
- run record;
- effort log;
- incident log.
