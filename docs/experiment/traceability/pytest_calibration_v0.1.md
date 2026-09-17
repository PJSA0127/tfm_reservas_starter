# Calibración pytest — baseline seguro v0.1

**Clasificación:** desarrollo/calibración; no corresponde a la evaluación experimental definitiva.

## Implementación asociada

La separación `tests/functional` / `tests/security` quedó establecida originalmente en el **repositorio de desarrollo anterior** mediante la referencia histórica `d88d9d3` (`test: add ASVS security test suite and separate functional tests`). Esta referencia se conserva únicamente como trazabilidad histórica y **no corresponde al historial Git del repositorio experimental corregido actual**. Durante la validación pre-GitHub se añadió una regresión funcional para IDs de reserva fuera del rango `INTEGER` de PostgreSQL. El commit definitivo del repositorio experimental se registrará después de inicializar y congelar su nuevo historial.

## Ejecuciones observadas

### Suite funcional

```powershell
docker compose --profile test run --rm test
```

Resultado observado:

- 18 pruebas funcionales;
- 18 PASS;
- 0 fallos;
- sin warnings después de ajustar el uso de UTC en los modelos.

### Suite específica de seguridad

```powershell
docker compose --profile test run --rm test pytest -v tests/security
```

Resultado observado:

- 22 pruebas específicas de seguridad;
- 22 PASS;
- 0 fallos.

### Suite completa de calibración

```powershell
docker compose --profile test run --rm test pytest -v tests
```

Resultado observado:

- 40 pruebas totales;
- 40 PASS;
- 0 fallos;
- tiempo automático observado en la regresión integrada: aproximadamente 12 s (variable según host).

El tiempo automático no se suma a minutos-persona.

## Interpretación

La ejecución satisfactoria demuestra que el baseline seguro y los mecanismos de prueba definidos funcionan en el entorno de calibración. La nueva prueba `test_oversized_reservation_id_returns_404` confirma que un identificador fuera del dominio persistible se rechaza con 404 y no provoca HTTP 500. No se interpreta como resultado de cobertura/detección del experimento definitivo.
