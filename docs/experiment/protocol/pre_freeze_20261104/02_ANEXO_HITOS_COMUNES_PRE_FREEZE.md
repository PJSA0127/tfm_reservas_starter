# Anexo candidato — confirmación de hitos de actividades comunes

**Estado:** `CANDIDATO DOCUMENTAL PRE-FREEZE / REV-01..11 APROBADOS POR INTERLOCUTOR / TEXTO NO CONGELADO`. Referencias: `conventional_procedure_v0.2.md` C02/C04, `manual_cases_v0.2.md`, `proposed_procedure_v0.1.md` P01 (encabezado interno v0.2), REV-02 y REV-03.

## Principio de equivalencia

Este control es **exclusivamente de marcación administrativa de pasos ya existentes**, no agrega comprobaciones, payloads, datos, valores límite, pruebas, nuevas rutas ni criterios. Debe utilizarse del mismo modo en C02/C04 y su equivalente P01; no revelar catálogo D01–D05, mappings ASVS, pruebas específicas, Semgrep o ZAP al convencional. No alterar C00→C06 ni el conjunto MC-01..MC-14.

## C02 / P01 walkthrough: secuencia ya congelada

| Orden del procedimiento común | Fecha/hora observada / evidencia | Ejecutado en ese orden | Observación/omisión contemporánea |
|---|---|---|---|
| 1. Autenticación | PENDIENTE | PENDIENTE | PENDIENTE |
| 2. Listado/consulta | PENDIENTE | PENDIENTE | PENDIENTE |
| 3. Creación | PENDIENTE | PENDIENTE | PENDIENTE |
| 4. Detalle | PENDIENTE | PENDIENTE | PENDIENTE |
| 5. Modificación | PENDIENTE | PENDIENTE | PENDIENTE |
| 6. Cancelación | PENDIENTE | PENDIENTE | PENDIENTE |
| 7. Control de acceso, cuando corresponda | PENDIENTE | PENDIENTE | PENDIENTE |

Una omisión se registra **en cuanto se advierte** como desviación, sin realizar pruebas ad hoc ni completar una evidencia retroactiva como si hubiese ocurrido en su posición. La decisión de continuidad sigue `incident_log_v0.1.md` y el protocolo; no se impone aquí invalidación automática ni repetición. I2 registra el orden y el tiempo humano de los responsables.

## C04 / P01 revisión técnica común: secuencia ya congelada

| Orden | Flujos/superficie de revisión existente | Evidencia de revisión | Hora/tramo observado |
|---|---|---|---|
| 1 | Autenticación y sesiones | PENDIENTE | PENDIENTE |
| 2 | Rutas/endpoints | PENDIENTE | PENDIENTE |
| 3 | Validación de entradas | PENDIENTE | PENDIENTE |
| 4 | Acceso a datos/persistencia | PENDIENTE | PENDIENTE |
| 5 | Templates y generación de respuestas | PENDIENTE | PENDIENTE |
| 6 | Operaciones que modifican estado y métodos HTTP | PENDIENTE | PENDIENTE |

**Hito de cronometría:** inicio/final con zona horaria de la **actividad completa** y personas activas conforme al anexo M2; los subhitos pueden documentarse por orden sin estimar duración individual si no fue medida. Este control no obliga a ejecutar herramientas nuevas, y no pretende convertir una revisión convencional en revisión ASVS explícita.

## Incidencias

| Run ID / actividad | Hito | Hecho observado | Inicio/fin con offset si corresponde | Registro de incidencia | Decisión |
|---|---|---|---|---|---|
| PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

El anexo solamente se utilizará si se aprueba y congela antes de los runs definitivos; no debe aplicarse para «reparar» el walkthrough histórico de `PILOT-PROP-01`.
