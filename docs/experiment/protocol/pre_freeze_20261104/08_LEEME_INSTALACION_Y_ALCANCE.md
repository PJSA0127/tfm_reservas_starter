# Paquete candidato de instrumentos pospiloto — REV-01..REV-11

**Situación:** aprobación global comunicada el 2026-11-04, paquete documental preparado para integración local de manera controlada. **NO ES FREEZE**.

## Jerarquía documental

`TFM - 7B.docx` → protocolo experimental → instrumentos → código/ejecución/evidencias. `ESTADO_ACTUAL_TFM.md` registra estado operativo y deberá recibir un checkpoint adicional; no se reescribe la sección 33.

## Instalación prevista

Carpeta nueva, sin sobrescribir originales:

`docs/experiment/protocol/pre_freeze_20261104/`

Nueve archivos exactamente: acta de decisión comunicada, cinco anexos operativos, checklist v0.3, mapa de cambios y esta guía. Los hashes se verificarán antes y después de copiar. La instalación local no equivale a revisión final ni commit ni push.

## Contenido y restricciones

- No modificar `pilot_protocol_v0.2.md`, `experimental_design_v0.1.md`, `conventional_procedure_v0.2.md`, `manual_cases_v0.2.md`, `proposed_procedure_v0.1.md`, `protocol_freeze_checklist_v0.2.md` ni instrumentos históricos.
- No tocar ninguna raíz de evidencia o directorio sellado.
- No añadir casos, modificar M1/M2/M3 ni introducir D01–D05.
- No atribuir firmas individuales; la aprobación fue comunicada por un interlocutor del equipo, sin soportes individuales aportados.
- No ejecutar pruebas, Docker, resets, CI ni actividades definitivas. El siguiente control después de instalar es revisar el diff documental y el estado actual del libro de continuidad.

## Alcance de la aprobación

La comunicación «APROBADO» respondió a la pregunta explícita sobre la revisión de los once ajustes por Paulo, Carlos y Jorge. Se registra el consenso **comunicado**, no firmas directas. Los documentos integrados son texto candidato y deben someterse a revisión final, validación y freeze antes de utilizarse para medición.
