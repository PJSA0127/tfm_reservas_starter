# Anexo candidato — control de inventario y copias antes del sellado definitivo

**Estado:** `CANDIDATO DOCUMENTAL PRE-FREEZE / REV-01..11 APROBADOS POR INTERLOCUTOR / TEXTO NO CONGELADO`. Complementa `evidence_archival_v0.1.md` (título interno v0.2); REV-07. No se aplica a los directorios ya sellados de los pilotos.

## Conservación original

- Primaria: `D:\Repositorios\tfm_reservas_starter\evidence`.
- Secundaria: `D:\Users\PJ\OneDrive - Universidad Internacional del Ecuador\TESIS\evidence`.
- I2 prepara/recopila/copia; I3 verifica; conservar evidencias válidas e invalidadas hasta la aprobación del TFM más un mínimo de seis meses.
- El expediente de cada run se aísla por Run ID. No crear documentos nuevos dentro de `PILOT-CONV-01`, `PILOT-CONV-02` ni `PILOT-PROP-01` sellados.

## Control para futuros runs (antes del sello)

| Etapa | Verificación/artefacto | Resultado real |
|---|---|---|
| 1 | Run ID, proceso, actividades completadas y acta/registro de cierre en preparación | PENDIENTE |
| 2 | Inventario de salidas obligatorias **según proceso**: funcional/manual/review/effort/incidents/metadata; P03/SAST/DAST/CI para propuesto | PENDIENTE |
| 3 | Inventario de archivos presentes en primaria; clasificación de faltantes | PENDIENTE |
| 4 | Preservación de originales e intentos/artefactos de incidente | PENDIENTE |
| 5 | Copia secundaria selectiva sin sobrescritura retroactiva y registro de procedimiento | PENDIENTE |
| 6 | Comparación de existencia y SHA-256 de los archivos cerrados entre ambas raíces | PENDIENTE |
| 7 | Discrepancias registradas, investigadas y tratadas conforme al protocolo, con evidencia | PENDIENTE |
| 8 | Comprobación I3 de integridad y procedencia | PENDIENTE |
| 9 | Creación del manifiesto/sello **únicamente** según algoritmo, orden y procedimiento aprobados | PENDIENTE |
| 10 | Verificación independiente del sello final y congelamiento posterior de la evidencia | PENDIENTE |

## Reglas

Una comprobación pre-sello NO tiene el mismo sentido que generar el manifiesto final. La secuencia exacta de creación de manifiesto y verificación de copias debe quedar fijada por la versión definitiva aprobada y evitar autorreferencia de hash. No declarar `PASS` hasta ver salidas reales y conservar sus rutas/recibos.

Si existen archivos no replicados como ocurrió con los cinco logs P05 de la calibración, elaborar inventario de faltantes, comprobar origen y recuperar por procedimiento autorizado **antes** de sellar; sin recrear salidas históricas ni sobrescribir sellos.

El valor de hash de un archivo vivo pertenece a esa versión y a su checkpoint. No substituirlo retroactivamente si el archivo evolucionó legítimamente. El nuevo manifiesto definitivo debe listar **solo** artefactos realmente presentes del run futuro.
