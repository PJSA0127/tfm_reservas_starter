# Checkpoint documental posterior al sello P02 — 2026-10-10

## Naturaleza y límites

- Run activo: `PILOT-PROP-01` (`OPEN / IN_PROGRESS`).
- Estado observado: `P01 = COMPLETED`; `P02 = COMPLETED / SEALED`; `P03 = NOT_STARTED`.
- Paso siguiente: `PREPARE_P03_SECURITY_TESTS`.
- Documento de estado externo: `ESTADO_ACTUAL_TFM.md`, nueva sección 20.
- Repositorio base de esta actualización: `8fa2451c414376139ecfe331a33201a385f6c846` (último commit documental visible en el ZIP de 2026-10-10, antes de aplicar este checkpoint).
- La presente modificación es **solo documental**. No incorpora resultado experimental, tiempo humano ni prueba de seguridad.

## Integridad P02

- Sello: `evidence/PILOT-PROP-01/metadata/p02_closure_seal_20261010.md`.
- SHA-256 del sello: `AF7EEC4DA51B40D7528F92CC452F760B8FEAA5E9AD0F48D48FCDA4924146F0C0`.
- Manifiesto: `evidence/PILOT-PROP-01/hashes/p02_closure_manifest_20261010.txt`.
- SHA-256 del manifiesto: `CC5A8998D23FE89BED2C7DFD933E4C08C201598862BB14440A8F49A24D958BFB`.
- Artefactos del manifiesto: `9/9 PASS` según revisión del ZIP entregado y consola previa; copia secundaria `PASS` según salida de sincronización.
- `run_record.md` final SHA-256: `960DDB1A7BA91BF1FC3D9214F11A99A3C46D698A33212D3D4570638F5E31B094`.
- `effort_log.md` final SHA-256: `F3FDB6BAA8CC2226C124AEB2AF818F70371C97EAF2C7FCF0D1AD0232E7A4F76C`.
- `incident_log.md` final SHA-256: `A5894E7915208476C3C2C5F9387833E2083A054DC7965F1C63C3DEF15FFD5A4A`.
- No se modifica ni reemplaza ninguno de estos artefactos.

## Actualización de índices del repositorio principal

1. `README.md`: estado experimental y paso P03.
2. `experiment/README.md`: estado, esfuerzos y regla de inmutabilidad de P02.
3. `docs/experiment/protocol/README.md`: sección operacional nueva y aclaración de snapshot histórico.

Los archivos de procedimiento, operacionalización ASVS, catálogo, pruebas, reglas Semgrep, planes ZAP, Compose y CI **no se editan** durante esta actualización.

## Cinco hallazgos transversales

| Hallazgo | Decisión y estado |
|---|---|
| Estado externo anterior aún situado en P01 | Generada una nueva sección 20 para reemplazar estado vigente, conservando 1–19 como historia; instalación externa pendiente de comprobación |
| Índices README desfasados | Actualización documental generada; estado Git pendiente de instalación/commit real |
| Workspace de P03 no incluido en el ZIP principal | Preflight de solo lectura pendiente en `D:\Repositorios\tfm_reservas_pilot_prop`; no afirmar que está verificado ahora |
| Matriz P02 sellada | No alterar; generar matriz de continuación o registros nuevos en P03–P06 |
| Divergencias entre nombre `v0.1` y versión interna | Diferido hasta después del piloto; no modificar instrumentos congelados |

## Control metodológico

- `PILOT-CONV-02` continúa `VALID / COMPLETED / ARCHIVED`.
- `INC-P01-001 = OPEN / NON-BLOCKING`, `INC-P01-002 = DOCUMENTED / NON-BLOCKING`; no desaparecen por cierre de P02.
- `P02_INCIDENTS = 0`, `P02_PROCEDURAL_DEVIATIONS = 0`.
- Esfuerzo humano P01 `119.09`, P02 `127.05`, acumulado `246.14 min-persona`; automático conocido `0.21 min`.
- D01–D05 no introducidos. No repetir P01/P02. No resetear la base de datos principal ni ejecutar mecanismos P03–P06 durante este checkpoint.
- Clasificación final de cobertura `0/1`: aún no realizada.

## Condición de cierre de este checkpoint documental

La actualización se considera instalada solo cuando las rutas de destino existan, los hashes de los archivos generados coincidan, se haya actualizado el `ESTADO_ACTUAL_TFM.md` canónico sin perder historial, y el estado Git/commit se registre como realmente observado. No adjudicar commit nuevo ni sincronización adicional antes de disponer de la salida correspondiente.
