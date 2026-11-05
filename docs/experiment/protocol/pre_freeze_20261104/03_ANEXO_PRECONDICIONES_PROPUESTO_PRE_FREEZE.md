# Anexo candidato — precondiciones del proceso propuesto y tratamiento técnico

**Estado:** `CANDIDATO DOCUMENTAL PRE-FREEZE / REV-01..11 APROBADOS POR INTERLOCUTOR / TEXTO NO CONGELADO`. Referencias: `proposed_procedure_v0.1.md` (título interno v0.2), `experimental_design_v0.1.md`, `pilot_protocol_v0.2.md`; controles REV-04, REV-05, REV-06. No sustituye el procedimiento.

## P01 y P02

P01 conserva **exactamente** las actividades funcionales y técnicas comunes al convencional, su orden, datos y registro humano. P02 utiliza los seis requisitos ASVS seleccionados y la matriz congelada; **no** se redefinen criterios a partir de resultados.

## P03 — condición técnica antes del lanzamiento autorizado

Antes de iniciar el comando de seguridad definido para `proposed-definitive`, comprobar mediante el preflight aprobado: origen/contenido de `compose.yaml`, servicio de prueba aislado, imagen requerida y existencia local de la imagen si el comando congelado utiliza `--no-build`; coherencia entre comando e imagen disponible. Identificar metadatos del entorno y dejar constancia del resultado. Si la precondición falla, detener **antes** del lanzamiento experimental y resolver solo con preparación técnica expresamente autorizada, sin alterar la batería ni la base principal.

**No autoriza** ejecutar pytest de diagnóstico, construir imágenes por rutina, repetir P03 del piloto, cambiar seis archivos de `tests/security/` o variar parámetros de seguridad. No equiparar un test fallido por defecto controlado con fallo del lanzador.

## P05 — ruta de salida DAST

Antes de iniciar OWASP ZAP, comprobar que la ruta de reportes prevista por el plan congelado existe o puede prepararse por el mecanismo **preautorizado**, y que el usuario/proceso posee permisos de escritura; registrar la ruta efectiva y su correspondencia con el plan. No generar reportes anticipados, no cambiar plan, objetivos, umbrales, alertas o autenticación. Una ruta ausente sin preparación aprobada detiene el lanzamiento hasta decisión documentada.

## P05 / P06 / P07 — interpretación del resultado

| Hecho observado | Clase inicial | Reintento automático |
|---|---|---|
| Imagen/comando fallido antes de lanzar prueba | Problema técnico/instrumental, sujeto a evaluación y registro | **NO**; decisión según protocolo |
| Prueba de seguridad ejecutada que identifica incumplimiento | Hallazgo o resultado de seguridad | **NO** |
| ZAP genera alertas y código de salida condicionado por plan congelado | Resultado de escaneo/alerta; interpretar el plan y logs exactos | **NO** por el solo hecho de existir alerta |
| Falla técnica de mecanismo obligatorio sin resultado evaluable | Incidencia técnica; documentar intento, causa y alcance | Solo **si** cumple P07 y autorización correspondiente |
| Workflow CI termina `success` pero job interno emite alerta | Interpretar ambos niveles separadamente | **NO** por inferencia |

El código de salida `2` de ZAP en el piloto se documentó como señal de Medium según ese plan concreto; **no** se establece que exit code 2 siempre signifique Medium ni que un status `success` descarte alertas. Las métricas definitivas se clasifican de manera independiente tras ambos procesos.

## Invariantes

1. P03 → P04 → P05 → P06 se ejecutan solo dentro del run autorizado y en el orden del procedimiento congelado.
2. P07 admite a lo sumo **un reintento técnico condicionado en el run**, aplicado al mecanismo que haya sufrido un fallo técnico, según el procedimiento fuente; se preserva intento inicial y se registra incidencia; no se modifica regla, prueba, configuración ni criterio como reacción al resultado.
3. P08 registra hallazgos adicionales sin pruebas ad hoc; P09 consolida sin modificar; P10 cierra y conserva.
4. No iniciar `DEF-PROP-01` antes del convencional, su cierre y el reset de equivalencia autorizado.
5. Preflight preparatorio **no** equivale a ejecutar P03/P05 ni a acreditar cobertura o detección.
