# Registro de ejecución piloto — v0.2

## Estado

**PARCIAL / COMPONENTE CONVENCIONAL PILOTO CERRADO / RESET PASS / PILOT-PROP-01 READY_TO_START / NOT_STARTED.**

## Identificación general

| Campo | Valor |
|---|---|
| Fecha primera ejecución convencional | 2026-09-29 |
| Equipo investigador | Jorge, Carlos y Paulo |
| I1 | Paulo — Ejecutor principal |
| I2 | Carlos — Registrador de evidencia y esfuerzo |
| I3 | Jorge — Supervisor del protocolo |
| Baseline | Baseline seguro pre-piloto sin D01–D05 |
| Commit/tag baseline | `32d27a04305617f8fea031704e24d7e68ce9c451` / `pre-pilot-freeze-v0.1` |

## Runs y etapas

| Etapa | Run ID | Estado | Evidencia |
|---|---|---|---|
| Convencional piloto — intento 1 | `PILOT-CONV-01` | `INVALIDATED - EXCLUDED FROM FINAL COMPARISON` | `evidence/PILOT-CONV-01/` |
| Revalidación de instrumentos | `REV-INSTR-01` | `5/5 PASS` | evidencia post-piloto / instrumentos v0.2 |
| Convencional piloto — intento 2 | `PILOT-CONV-02` | `VÁLIDO / COMPLETADO / ARCHIVADO` | `evidence/PILOT-CONV-02/` |
| Reset CONV -> PROP | N/A | `PASS` | `evidence/PILOT-PROP-01/metadata/` |
| Revalidación metodológica pre-PROP | N/A | `PASS` | `evidence/PILOT-PROP-01/metadata/` |
| Propuesto piloto | `PILOT-PROP-01` | `READY_TO_START / NOT_STARTED` | preparación y sellos pre-run |

## PILOT-CONV-01

`PILOT-CONV-01` permanece conservado íntegramente como evidencia de calibración.

- no se sobrescribe;
- no se utiliza para métricas definitivas;
- no se clasifica frente a D01–D05;
- su invalidación se atribuye a problemas de instrumentación;
- su manifiesto SHA-256 y copia secundaria fueron verificados.

Esfuerzo humano observado: **115.30 min-persona**.

Tiempo automático registrado: **0.19 min**.

## PILOT-CONV-02

El segundo intento convencional completó C00–C06 y fue declarado válido.

- C01: 18/18 pruebas funcionales PASS;
- C02: 7/7 recorrido manual PASS;
- C03: 14/14 casos manuales PASS;
- C04: revisión técnica completada con 5 observaciones;
- C05: 5 hallazgos consolidados;
- C06: cierre completo;
- incidencias experimentales sin resolver al cierre: 0;
- evidencia primaria/secundaria verificada y archivada.

Esfuerzo humano observado: **146.71 min-persona**.

Tiempo automático válido conocido: **0.14 min**.

## Reset CONV -> PROP

El reset R01–R09 finalizó `PASS`. Durante R06 se detectó que `db_init` crea esquema pero no usuarios; U1/U2 fueron restaurados mediante el comando documentado `create-user`. La incidencia quedó resuelta **antes** del inicio de `PILOT-PROP-01`.

Estado inicial verificado después del reset:

- `db`: healthy;
- `web`: healthy;
- `db_init`: exited / 0;
- usuarios: U1/U2 únicamente;
- reservas: 0;
- `/health`: HTTP 200;
- navegador privado limpio;
- autorización I3: PASS.

## Revalidación metodológica pre-PROP

Antes de abrir `PILOT-PROP-01` se sincronizaron como overlay activo los instrumentos comunes v0.2 ya utilizados por `PILOT-CONV-02`, preservando las versiones históricas v0.1 y sin modificar los 87 archivos técnicos del baseline.

- baseline técnico: 87/87 PASS;
- `manual_cases_v0.2.md`: ACTIVE;
- `conventional_procedure_v0.2.md`: ACTIVE;
- sello histórico pre-piloto: PRESERVED;
- revalidación metodológica: PASS;
- sello de revalidación SHA-256: `68EE5974A6F69570101C8FA3251F25F804926645819D76D4DFB9A8F54C30CB52`.

## Próximo paso

`PILOT-PROP-01` permanece **READY_TO_START / NOT_STARTED**.

El siguiente paso formal es `START_PILOT_PROP_01`. No se han iniciado P01, pytest de seguridad, Semgrep, ZAP ni GitHub Actions de fase `pilot`.
