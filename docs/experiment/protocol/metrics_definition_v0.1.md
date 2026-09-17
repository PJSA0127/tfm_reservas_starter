# Definición operacional de métricas — v0.1

## 1. Estado

**CERRADO PARA PILOTAJE / PRE-FREEZE.**

## 2. M1 — Cobertura de requisitos

```text
Cobertura (%) =
(requisitos efectivamente verificados / 6) × 100
```

Cada requisito recibe:

- `1 = verificado`;
- `0 = no verificado`.

Un requisito se considera verificado únicamente cuando existe:

1. una actividad dirigida a comprobar el criterio;
2. un resultado observable;
3. evidencia registrada y cerrada.

No basta una afirmación general como “el código parece correcto”.

Cobertura mide **verificación**, no necesariamente conformidad.

## 3. M2 — Esfuerzo humano

Unidad: **minutos-persona activos**.

```text
Minutos-persona =
Σ minutos activos de cada investigador
```

Si I1, I2 e I3 trabajan activamente 10 minutos:

```text
10 + 10 + 10 = 30 minutos-persona
```

Si I3 permanece en espera pasiva, ese tramo no se suma a su esfuerzo.

### Categorías

- configuración inicial;
- ejecución;
- análisis;
- documentación de evidencias;
- mantenimiento/recuperación.

### Presentación obligatoria

Los resultados muestran:

1. esfuerzo operativo;
2. configuración inicial;
3. total desagregado por categoría.

No se presentará únicamente un total sin desglose.

### Exclusiones

No se suma como esfuerzo humano:

- espera pasiva;
- tiempo autónomo de herramientas;
- pausas personales;
- desarrollo general de la aplicación;
- construcción general del experimento;
- selección inicial de ASVS;
- incorporación controlada de D01–D05;
- redacción académica general.

## 4. Tiempo automático

Se registra separadamente para:

- pytest;
- Semgrep;
- ZAP;
- GitHub Actions;
- build/despliegue automatizado cuando corresponda.

No se suma a M2.

## 5. Runs invalidados

Si una ejecución es invalidada:

- su esfuerzo se conserva en el registro de incidencias;
- sus evidencias se conservan;
- el tiempo no se incorpora al comparativo definitivo.

## 6. M3 — Tasa de detección

```text
Tasa de detección (%) =
(defectos controlados correctamente detectados / 5) × 100
```

Reglas:

- D01–D05 constituyen el universo;
- D03 cuenta una sola vez;
- múltiples hallazgos del mismo defecto cuentan como una detección;
- omisiones se registran como `0`;
- hallazgos fuera del catálogo no modifican M3.

## 7. Hallazgos adicionales

Se clasifican posteriormente como:

- hallazgo adicional válido;
- falso positivo.

Se informan como contexto.

## 8. Evidencia válida para cobertura

Puede incluir:

- prueba funcional;
- prueba de seguridad;
- evidencia manual;
- revisión de código documentada;
- Semgrep;
- ZAP;
- artifact CI;
- registro trazable requisito-prueba-evidencia.

Una revisión manual documentada puede verificar un requisito si demuestra suficientemente el criterio operacional. Esto evita favorecer artificialmente al proceso propuesto.

## 9. Regla conservadora

Cuando la evidencia sea insuficiente para demostrar que un requisito fue efectivamente verificado:

```text
resultado = no verificado
```

## 10. Piloto

Los resultados de cobertura y detección obtenidos durante el piloto sirven exclusivamente para calibración y no se incorporan a M1 ni M3 definitivos.

Respecto de M2 se distinguen dos situaciones:

1. **Ejecución propiamente dicha del piloto:** los minutos-persona empleados en `PILOT-CONV-01`, reset y `PILOT-PROP-01` se registran como evidencia de calibración y no se incorporan al esfuerzo comparativo definitivo.
2. **Ajuste/configuración específica derivada del piloto:** si el piloto revela la necesidad de preparar, corregir o mantener un mecanismo específico necesario para aplicar alguno de los procesos, el trabajo humano adicional realizado fuera del run piloto puede registrarse como **configuración inicial** del proceso correspondiente, siempre que exista medición `OBSERVADO`, se documente su relación con la incidencia y no exista doble contabilización.

Las correcciones generales de la aplicación, del escenario experimental o de la metodología continúan excluidas.

## 11. Tiempos estimados

Las duraciones marcadas como `ESTIMADO` o `PLANIFICADO`:

- sirven para planificación;
- no se utilizan en M2;
- deben reemplazarse por `OBSERVADO` cuando exista medición real válida.

## 12. Interpretación

La comparación es descriptiva.

El esfuerzo se interpreta junto con cobertura y detección.

Un menor esfuerzo no constituye por sí mismo evidencia de mejor verificación.
