# Conciliación documental pospiloto — 25 de octubre de 2026

**Naturaleza:** checkpoint documental nuevo y derivado, preparado a partir de una auditoría estática del ZIP `tfm_reservas_starter(20261025-210558).zip`, de la versión académica adjunta y de los registros de cierre P10. No es un cambio metodológico del piloto ni una ejecución experimental.

## 1. Autoridad académica

El equipo confirmó expresamente el 25/10/2026 que el documento académico rector vigente es **`TFM - 7B.docx`**. El adjunto técnico suministrado se denominaba `TFM - 7B(2).docx`, con SHA-256:

`0B8B1FC6ECB3DF17859B516991C64F7E3BCC79D38B9FE70245E8370956066332`

El nombre canónico comunicado no cambia los bytes del archivo recibido. El antiguo `TFM - G7.docx` se mantiene solo como antecedente documental. El nuevo DOCX desarrolla los capítulos 1 y 2, mantiene los capítulos 3–5 pendientes de desarrollo y análisis final, y contiene 35 entradas bibliográficas visibles. Esto no significa que las ejecuciones definitivas se hayan realizado.

## 2. Cadena de evidencia del piloto propuesto

El cierre de `PILOT-PROP-01` está documentado como `VALID_WITH_DOCUMENTED_LIMITATION / COMPLETED / ARCHIVED / VERIFIED / SEALED`. P10 se selló el 14/10/2026. Los valores de referencia comprobados en el ZIP auditado son:

| Referencia | Valor |
|---|---|
| Evidencias dentro del run | 250 archivos |
| Manifiesto base final | 248 entradas verificadas |
| Archivo ZIP final | 250 entradas verificadas |
| SHA-256 manifiesto | `8BF199916349628D544DFBDDC6B9E338218E91F0229F432C97C36B81B973E372` |
| SHA-256 sello | `0D4EB7D54ACBA33F3B47FF54149748A967098390BC58DB17609BB82EDA3793B9` |
| SHA-256 ZIP | `C957E841C57A5925B6AFE2B4A04B06E2E6A9A05D787922FCB16CE3C12BBCCB04` |
| SHA-256 recibo externo | `2D410A597D702E61DF7BE1BEB032EC5238CE3F9622DB8B2D4AC1054A75625ED8` |
| Esfuerzo humano propuesto | 604,22 minutos-persona, solo calibración |
| Esfuerzo humano convencional válido | 146,71 minutos-persona, solo calibración |

`INC-P01-001` fue cerrada mediante disposición P10 `CLOSED_WITH_MEASUREMENT_LIMITATION`, manteniendo el registro histórico original. Los ~44 segundos informados retrospectivamente no se imputaron al esfuerzo observado. `PILOT-CONV-01` permanece invalidado y archivado; `PILOT-CONV-02` válido y archivado.

**Alcance:** la comprobación de integridad corresponde al contenido del ZIP recibido el 25/10/2026; no constituye una nueva verificación en vivo del repositorio GitHub ni de la segunda copia OneDrive.

## 3. Discrepancia y tratamiento

Los archivos descriptivos `README.md`, `experiment/README.md` y `docs/experiment/protocol/README.md` aún reflejaban, en el commit del snapshot, estados `PILOT-PROP-01 = OPEN / IN_PROGRESS`, P03–P10 pendientes y `PREPARE_P03_SECURITY_TESTS` como paso inmediato. Se preparó una actualización de **índices vivos** que:

1. consigna el cierre real P10 y sus referencias de evidencia;
2. corrige la autoridad académica a `TFM - 7B.docx`;
3. distingue el checkpoint P02 del estado vigente y conserva su contenido histórico;
4. mantiene expresamente pendiente el freeze definitivo y los runs `DEF-CONV-01`/`DEF-PROP-01`;
5. identifica `POST_PILOT_REVIEW_AND_FREEZE_PREPARATION` como siguiente etapa de revisión, sin convertirla en autorización automática.

No se modificaron los instrumentos históricos `pilot_protocol_v0.2.md`, `pilot_results_v0.2.md`, `pilot_execution_log_v0.2.md`, `protocol_freeze_checklist_v0.2.md`, las pruebas, el código Flask ni los artefactos contenidos en `evidence/PILOT-PROP-01/`. Los instrumentos congelados continúan referenciando sus versiones históricas en el momento en que fueron fijados.

## 4. Integridad de la entrega y publicación

La auditoría local del ZIP permitió leer Git `main`, con `HEAD = origin/main = 124a45914be5db7eba86c83a751f3c367c560548` en el snapshot suministrado. **No** se consultó el remoto actual ni se registró un commit o push nuevo.

La distribución de un archivo corregido no acredita su instalación en Windows. Antes de aplicar esta conciliación se deben verificar los hashes de las tres fuentes actuales, conservar una copia anterior, revisar el diff y documentar el commit y push reales si se autoriza su publicación.

El archivo `ESTADO_ACTUAL_TFM.md` externo al repositorio requerirá un checkpoint nuevo que registre la autoridad académica y la publicación documental **solo después** de comprobar las acciones efectivamente realizadas. No deben reescribirse checkpoints previos.

## 5. Siguiente estado autorizado por los documentos

```text
ACADEMIC_CANONICAL = TFM - 7B.docx
PILOT-CONV-02 = VALID / COMPLETED / ARCHIVED
PILOT-PROP-01 = VALID_WITH_DOCUMENTED_LIMITATION / ARCHIVED / VERIFIED / SEALED
P10 = COMPLETED / ARCHIVED / SEALED
D01-D05 = NOT_INTRODUCED_IN_DEFINITIVE_VARIANT_IN_AUDITED_MATERIAL
DEFINITIVE_FREEZE = NOT_APPROVED_IN_AUDITED_MATERIAL
DEF-CONV-01 = NOT_STARTED_IN_AUDITED_MATERIAL
DEF-PROP-01 = NOT_STARTED_IN_AUDITED_MATERIAL
NEXT_FORMAL_STEP = POST_PILOT_REVIEW_AND_FREEZE_PREPARATION
THIS_DOCUMENT = DOCUMENTARY_RECONCILIATION_ONLY
GIT_PUSH = NOT_ASSERTED
```

**Regla de preservación:** no introducir defectos, ejecutar pruebas, resetear entornos, modificar registros históricos o reabrir evidencias archivadas como parte de este checkpoint.
