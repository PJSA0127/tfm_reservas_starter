# Manifiesto del entorno experimental — v0.1

## Estado

Validación local y calibración real CAL-01 completadas; reproducibilidad técnica en cierre pre-freeze.

## Código

| Elemento | Valor |
|---|---|
| Repositorio técnico de referencia | repo corregido validado |
| Estado actual | baseline seguro; D01–D05 no introducidos |
| Commit/HEAD definitivo | PENDIENTE |
| Tag baseline/piloto | PENDIENTE |
| Tag versión experimental | PENDIENTE |

## Runtime

| Elemento | Valor |
|---|---|
| Python | 3.14.7 observado |
| Flask | 3.1.3 |
| Flask-Login | 0.6.3 |
| Flask-WTF | 1.3.0 |
| SQLAlchemy | 2.0.52 |
| psycopg[binary] | 3.3.5 |
| pytest | 9.1.1 |

## Imágenes

| Uso | Referencia | Digest conocido |
|---|---|---|
| aplicación/tests | `python:3.14-slim` | `sha256:cad9a2c871761c413caa6fdd6441c783451e740a48aaeba60ae62a8b53525ef6` |
| PostgreSQL | `postgres:18.6` | `sha256:4ef4dbc939d61acea57712655ddb4b4ab27419c913f94cca0cd57cb3ea3c2280` |
| Semgrep | `semgrep/semgrep:1.177.0-nonroot` | `sha256:012c8fe81c14da2d7691b90fcd826ce07f460a3301442b16c460575c87d3efb6` |
| ZAP | `zaproxy/zap-stable:2.17.0` | `sha256:781a2bdaea47324e7bab583e2263f21d257b0aee61ed51521a5be45f5f5081ef` |

## Host local

| Elemento | Valor |
|---|---|
| SO | Windows; edición/build PENDIENTE |
| Docker Engine | 29.5.2 |
| Docker Compose | v5.1.4 |
| Git | PENDIENTE |
| CPU/RAM | PENDIENTE si se decide incorporar |

## Seguridad

| Mecanismo | Versión/estado |
|---|---|
| Semgrep | 1.177.0 |
| Reglas Semgrep | 6 |
| ZAP | 2.17.0 |
| Active scan principal | 40012, 40014, 40018 |
| Complementario CSRF | 10202 |

## Resultados locales actuales

| Mecanismo | Resultado |
|---|---|
| Funcional | 18/18 PASS |
| Seguridad | 22/22 PASS |
| Total pytest | 40/40 PASS |
| Semgrep baseline | 0 findings / 14 targets / 0 errors |
| Semgrep fixtures | 6/6 |
| ZAP auth | 3/3 checks PASS |
| ZAP experimental gate | PASS |
| DAST 5xx | 0 |
| Simulación CI | PASS |

## Dependencias transitivas

`requirements.lock` congela las dependencias directas y transitivas observadas en CAL-01. La imagen base Python queda fijada por digest y proporciona pip 26.2.1.

## GitHub Actions — entorno adicional del proceso propuesto

El host local documentado anteriormente es el entorno común para las actividades equivalentes de ambos procesos. GitHub Actions constituye un entorno automatizado adicional del proceso propuesto, previsto expresamente en el anteproyecto. Sus características se registran por separado para no confundirlas con el host local común.

| Elemento | Valor actual |
|---|---|
| Runner | `ubuntu-24.04` |
| checkout | `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` (`v7`) |
| upload artifact | `actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` (`v7`) |
| Dependabot | `.github/dependabot.yml` limitado a `github-actions` |
| Ejecución real | CAL-01 PASS - Run ID `35247019707` - commit `7cfa55bc7bc96d67112f37d19e681007ec19d425` |

## Pendientes de freeze

- Git exacto;
- host exacto si se considera necesario;
- commit/tags;
