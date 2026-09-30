# Auditoría de referencias después de PILOT-CONV-01 — v0.2

## Corrección respecto del reporte previo

El primer script de auditoría produjo un error de compatibilidad al construir una colección de metadatos.

Además, su clasificación automática incluyó falsos positivos: autorreferencias de scripts auxiliares y menciones históricas deliberadas.

Este reporte aplica clasificación semántica.

## Estado

- `PILOT-CONV-01`: `INVALIDATED - EXCLUDED FROM FINAL COMPARISON`.
- evidencia del run: sellada; no modificar.
- `manual_cases_v0.2.md`: generado.
- `conventional_procedure_v0.2.md`: generado.
- `post_pilot_instrument_adjustments_v0.1.md`: generado.
- `PILOT-CONV-02`: NO INICIADO.

## Referencias v0.1 que se preservan deliberadamente

1. evidencia sellada de `PILOT-CONV-01`;
2. menciones históricas en controles de cambios;
3. scripts auxiliares que verifican integridad de versiones v0.1;
4. versiones documentales v0.1 preservadas como histórico.

## Documentos operacionales migrados

- `README.md`.
- `conventional_workspace_sanitization_v0.2.md`.
- `pilot_protocol_v0.2.md`.
- `protocol_freeze_checklist_v0.2.md`.
- `pilot_execution_log_v0.2.md`.
- `pilot_results_v0.2.md`.

## Pendientes

1. revalidación controlada de MC-04E;
2. revalidación controlada de MC-05D;
3. revalidación controlada de MC-07F;
4. revalidación controlada de MC-08C;
5. revalidación controlada de la cancelación de MC-12;
6. reconstrucción y sanitización del workspace para `PILOT-CONV-02`;
7. generación de nuevo manifiesto y paquete;
8. actualización de `ESTADO_ACTUAL_TFM.md`;
9. autorización del nuevo freeze piloto convencional.

La migración documental no inicia `PILOT-CONV-02` y no modifica el baseline técnico.