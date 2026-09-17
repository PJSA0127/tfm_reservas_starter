# Archivo y conservación de evidencias — v0.1

## 1. Estado

**CERRADO PARA PILOTAJE / PRE-FREEZE.**

## 2. Run IDs

Convención adoptada:

```text
PILOT-CONV-01
PILOT-PROP-01
DEF-CONV-01
DEF-PROP-01
```

Una repetición por invalidación incrementa el número y nunca sobrescribe el run anterior:

```text
DEF-CONV-01 -> invalidado
DEF-CONV-02 -> nueva ejecución
```

## 3. Estructura primaria

Dentro del almacenamiento local del proyecto:

```text
evidence/
  <run-id>/
    metadata/
    functional/
    manual/
    review/
    security/
    semgrep/
    zap/
    ci/
    effort/
    incidents/
    evaluation/
    hashes/
```

Solo se crean carpetas aplicables al proceso.

## 4. Copia primaria

**Disco local del proyecto.**

La ruta exacta absoluta se registrará en el manifiesto del entorno antes del piloto.

## 5. Copia secundaria

**OneDrive.**

La ruta/carpeta definitiva se registra antes del piloto.

GitHub no constituye la única copia de evidencia.

## 6. Responsabilidades

### I2

- prepara la estructura;
- recopila artifacts;
- copia evidencias;
- genera manifiestos;
- realiza la copia secundaria.

### I3

- verifica integridad;
- comprueba que el Run ID sea correcto;
- comprueba que la copia primaria y secundaria existan;
- verifica hashes.

## 7. Evidencia convencional

Como mínimo:

- reporte funcional;
- registros manuales;
- notas de revisión;
- hallazgos;
- run record;
- effort log;
- incident log;
- metadatos del entorno.

## 8. Evidencia propuesta

Además:

- seguridad pytest;
- Semgrep;
- ZAP;
- CI;
- matriz requisito-prueba-evidencia;
- metadata GitHub;
- artifacts descargados.

## 9. Integridad

Algoritmo obligatorio:

```text
SHA-256
```

Después de cerrar el run:

```powershell
Get-ChildItem <directorio-run> -Recurse -File |
    Get-FileHash -Algorithm SHA256
```

El manifiesto se guarda en `hashes/`.

Después del hash no se modifica la evidencia original.

## 10. GitHub Actions

Después de cada run aplicable:

1. descargar artifacts;
2. verificar contenido;
3. almacenar localmente;
4. copiar a OneDrive;
5. registrar `GITHUB_SHA`;
6. registrar `GITHUB_RUN_ID`;
7. generar hashes.

## 11. Evidencia de evaluación posterior

Conservar:

- instrumento independiente;
- clasificación D01–D05;
- cálculos finales;
- justificaciones de consenso.

## 12. Runs invalidados

Las evidencias no se eliminan.

La carpeta debe contener una marca explícita:

```text
INVALIDATED — EXCLUDED FROM FINAL COMPARISON
```

## 13. Retención

Conservar las evidencias:

```text
hasta la aprobación definitiva del TFM
+ al menos 6 meses adicionales
```

## 14. Grabación opcional

Video/pantalla:

- no es obligatorio;
- solo se usa si fue pilotado y congelado antes de la fase definitiva;
- se archiva como evidencia suplementaria;
- no sustituye registros estructurados.

## 15. Pendientes puramente operativos

Antes del piloto deben escribirse:

- ruta absoluta primaria;
- ruta/carpeta OneDrive secundaria.
