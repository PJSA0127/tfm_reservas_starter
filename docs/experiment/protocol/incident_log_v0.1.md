# Registro de incidencias experimentales — v0.1

## 1. Estado

**INSTRUMENTO CERRADO PARA PILOTAJE.**

## 2. Severidades

### Bloqueante

Impide continuar manteniendo las condiciones experimentales.

Ejemplos:

- reset incompleto;
- aplicación no operativa;
- pérdida de evidencia esencial;
- herramienta obligatoria imposible de ejecutar.

### Mayor

Permite continuar parcialmente, pero afecta reproducibilidad, instrumentación o calidad de evidencia.

### Menor

No impide la ejecución ni compromete las condiciones principales.

### Documental

Problema de claridad, formato o documentación sin impacto técnico directo.

## 3. Registro

| ID | Fecha | Fase | Run ID | Proceso | Severidad | Descripción | Impacto | Acción tomada | ¿Repetición requerida? | ¿Cambio pre-freeze? | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PENDIENTE | | | | | | | | | | | |

## 4. Decisión de invalidación

I3 identifica la posible condición de invalidación.

La decisión final se toma por consenso:

```text
I1 + I2 + I3
```

## 5. Regla de invalidación

Un run puede invalidarse cuando una incidencia:

- impide completar el procedimiento;
- rompe condiciones experimentales;
- hace imposible confiar en la evidencia;
- exige modificar criterios/configuración durante la ejecución.

## 6. Repetición

Si un run es invalidado:

- no se sobrescribe;
- se conserva;
- se excluye del comparativo;
- el nuevo intento recibe un Run ID nuevo.

Ejemplo:

```text
DEF-CONV-01
INVALIDATED — EXCLUDED FROM FINAL COMPARISON

DEF-CONV-02
nuevo intento
```

## 7. Evidencia

Nunca eliminar:

- logs;
- artifacts;
- tiempos;
- causa;
- acciones de recuperación;
- decisión de invalidación.

## 8. Reintento técnico

Un único reintento técnico permitido por el procedimiento debe registrarse como incidencia aunque el run continúe siendo válido.

## 9. Piloto

Antes del freeze, una incidencia puede justificar una corrección de:

- claridad;
- instrumentación;
- reset;
- registro;
- reproducibilidad.

Debe quedar documentada la relación:

```text
incidencia -> corrección -> nueva versión del documento/configuración
```

## 10. Después del freeze

No se modifican criterios retrospectivamente como consecuencia de los resultados observados.
