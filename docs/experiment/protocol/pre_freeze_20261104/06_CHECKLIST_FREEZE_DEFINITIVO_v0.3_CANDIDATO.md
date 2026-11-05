# Checklist de freeze experimental definitivo — propuesta derivada v0.3

> **Estado de este documento:** CANDIDATO PRE-FREEZE / AJUSTES REV-01..11 APROBADOS POR CONSENSO COMUNICADO / TEXTO TODAVÍA NO CONGELADO.  
> Documento derivado preparado fuera del repositorio original. No altera los pilotos ni autoriza D01–D05, pruebas, freeze o ejecuciones definitivas.


**Derivado de:** `protocol_freeze_checklist_v0.2.md`. No reescribir su estado histórico. El sufijo `v0.3` es **identificador propuesto**, no aprobación de versión. Cada compuerta no acreditada se deja vacía. Las referencias a pilotos son antecedentes observados, no casillas experimentales por repetir.

## A. Premisas metodológicas a preservar

- [ ] A-01: ratificar `TFM - 7B.docx` como rector y confirmar copia/hash y coherencia con el protocolo vigente.
- [ ] A-02: congelar seis requisitos ASVS 5.0.0 L1: V1.2.1, V1.2.4, V2.2.1, V2.2.2, V3.5.1, V3.5.3.
- [ ] A-03: congelar catálogo cinco defectos; D03 relacionado con dos requisitos y contado una vez para M3.
- [ ] A-04: confirmar método convencional primero, propuesto después, misma revisión defectuosa y condiciones equivalentes, instrumentación exclusiva retirada del workspace convencional.
- [ ] A-05: confirmar segregación de conocimiento del catálogo D01–D05 durante el convencional y evaluación independiente al final.

## B. Cierre de calibración — comprobar documentación, no reejecutar

**Antecedentes históricos consignados:** `PILOT-CONV-01 = INVALIDATED / ARCHIVED`, `REV-INSTR-01 = 5/5 PASS`, `PILOT-CONV-02 = VALID / ARCHIVED`, `PILOT-PROP-01 = VALID_WITH_DOCUMENTED_LIMITATION / ARCHIVED / VERIFIED / SEALED`. Sus evidencias no se reabren.

- [ ] B-01: referenciar dictamen pospiloto firmado o aprobado por medio verificable I1/I2/I3.
- [ ] B-02: vincular de forma auditable cada ajuste de instrumentos con REV-01..REV-11 y resolución real.
- [ ] B-03: preservar archivo y hashes históricos sin añadir documentos a los directorios sellados.

## C. Instrumentos y medición

- [ ] C-01: aprobar versiones nuevas solo de procedimientos/registros que lo requieran, con diff semántico y justificación.
- [ ] C-02: conservar reglas de casos manuales y revisión técnica comunes sin añadir tests al convencional.
- [ ] C-03: congelar instrumento M1/M3 y clasificación independiente de evidencia suficiente (0/1) posterior a ambos runs.
- [ ] C-04: congelar instrumento M2 con tiempo humano observado por rol y categoría, inicio/fin/offset, pausas, documentación y automatización separada.
- [ ] C-05: fijar incidencia, invalidez, conservación y único reintento técnico condicionado del propuesto sin promover hallazgos a fallos técnicos.
- [ ] C-06: registrar identificación, versión, origen y hashes verificados de todos los instrumentos efectivos; resolver deuda documental de nombres sin renombrar históricos.

## D. Variante experimental D01–D05 — NO PREPARADA SEGÚN ÚLTIMO CHECKPOINT DISPONIBLE

- [ ] D-01: autorización expresa para construir variante en entorno/branch/workspace nuevos, aislados del baseline piloto.
- [ ] D-02: establecer ubicación, manifestación, correspondencia y criterios cerrados de D01–D05.
- [ ] D-03: construir variante **única** con D01–D05 conforme a catálogo aprobado.
- [ ] D-04: validar funcionalidad necesaria y manifestación técnica de cada defecto en fase preparatoria autorizada, separada de runs definitivos.
- [ ] D-05: establecer commit/tag real e integridad de la variante.
- [ ] D-06: verificar que los workspaces convencional/propuesto derivan del mismo commit experimental, y sanitización del convencional.

## E. Entorno y datos equivalentes

- [ ] E-01: congelar lock, digests y herramientas; identificar imágenes exactas y runner CI.
- [ ] E-02: fijar datasets, usuarios, reservas y estado inicial observable equivalente.
- [ ] E-03: fijar procedimiento de restauración entre DEF-CONV y DEF-PROP, sin modificar código.
- [ ] E-04: fijar precondiciones técnicas de P03/P05, resultados y rutas/artefactos, sin alterar las baterías.
- [ ] E-05: confirmar que no se utilizará prueba ad hoc ni revisión guiada por catálogo en convencional.
- [ ] E-06: documentar controles de servicios/volúmenes y contingencias; no hacer reset hasta que exista autorización de ejecución.

## F. Evidencia, integridad y cronometraje

- [ ] F-01: fijar raíces primaria/secundaria separadas para futuros runs, retención y responsables.
- [ ] F-02: incluir inventario de outputs obligatorios, mecanismos SHA-256 y verificación de dos copias **antes de sellar**.
- [ ] F-03: fijar registro de inicio/fin local con offset, pausas, esfuerzo humano por persona y tiempo automático por herramienta.
- [ ] F-04: establecer frontera de configuración inicial elegible frente a construcción general de la variante/TFM y calibración.
- [ ] F-05: fijar Run IDs `DEF-CONV-01` y `DEF-PROP-01`; preservar intentos invalidados con ID distinto.
- [ ] F-06: fijar forma de registrar aprobación I3 y consenso I1/I2/I3 sin atribuir firmas inexistentes.

## G. Verificación integral previa al freeze

- [ ] G-01: revisar únicamente controles estáticos/dinámicos preparatorios autorizados y evidencias reales (no repetir CAL-01/CAL-02 ni pilotos).
- [ ] G-02: resolver discrepancias entre código, variantes, instrumentos, protocolo, DOCX y evidencia de preparación.
- [ ] G-03: fijar manifiesto SHA-256 de la versión experimental final y paquete de procedimientos.
- [ ] G-04: confirmar inexistencia de incidencias bloqueantes y existencia de decisiones formales trazables.
- [ ] G-05: revisar que el cierre y la recopilación no expongan secretos (`.env`), ni modifiquen evidencia histórica.

## H. Acta de autorización del freeze — NO CUMPLIMENTADA

| Campo | Valor requerido |
|---|---|
| Fecha/hora local con offset | PENDIENTE |
| Commit/tag definitivo | PENDIENTE |
| Manifiesto de instrumentos y código | PENDIENTE |
| Procedimiento/reset/datos/versiones aprobados | PENDIENTE |
| Autorización I1 | PENDIENTE |
| Autorización I2 | PENDIENTE |
| Autoridad/consenso I3 | PENDIENTE |
| Fuente verificable de decisión | PENDIENTE |
| Estado freeze definitivo | `NOT_APPROVED` |
| Habilitación DEF-CONV-01 | `NOT_AUTHORIZED` |

**Condición de salida:** cuando los controles aplicables A–G estén sustentados por evidencias verificadas y el acta H esté aprobada, podrá considerarse el freeze definitivo. **No** ejecutar `DEF-CONV-01` automáticamente: apertura y medición del run requieren una autorización posterior específica.
