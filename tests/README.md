# Suite de pruebas

La suite queda separada deliberadamente en dos conjuntos.

## `tests/functional`

Contiene las pruebas funcionales comunes al escenario experimental. Son las pruebas que forman parte de la base compartida entre el proceso convencional y el proceso propuesto.

Ejecutar:

```powershell
docker compose --profile test run --rm test
```

El servicio `test` ejecuta por defecto únicamente:

```text
pytest -v tests/functional
```

## `tests/security`

Contiene las pruebas específicas de seguridad del proceso propuesto.

Ejecutar:

```powershell
docker compose --profile test run --rm test pytest -v tests/security
```

Estas pruebas no deben incorporarse al procedimiento del proceso convencional durante la evaluación definitiva.

## Suite completa durante desarrollo/calibración

Antes de congelar el protocolo puede ejecutarse todo el conjunto para comprobar el laboratorio:

```powershell
docker compose --profile test run --rm test pytest -v tests
```

La ejecución conjunta durante desarrollo o calibración no convierte las pruebas de seguridad en actividades del proceso convencional. En la evaluación definitiva los comandos y procedimientos de cada proceso deben permanecer separados.
