# Archivo y conservación de evidencias — v0.2

## 1. Estado

**PREPARADO Y VALIDADO PARA PILOTAJE / EVIDENCIA EXPERIMENTAL AÚN NO GENERADA**

La estructura de almacenamiento, las rutas primaria y secundaria y los mecanismos de integridad fueron preparados antes de `PILOT-CONV-01`.

Esta preparación no implica que el piloto haya comenzado ni que exista evidencia experimental observada de C00–C06.

El estado operacional exacto debe consultarse en `ESTADO_ACTUAL_TFM.md`.

## 2. Run IDs

Convención adoptada:

- `PILOT-CONV-01`
- `PILOT-PROP-01`
- `DEF-CONV-01`
- `DEF-PROP-01`

Una repetición por invalidación incrementa el número y nunca sobrescribe el run anterior.

Ejemplo:

`DEF-CONV-01` → invalidado
`DEF-CONV-02` → nueva ejecución

Los runs invalidados permanecen archivados y claramente identificados como excluidos de la comparación definitiva.

## 3. Estructura primaria

La estructura principal se mantiene dentro de:

`D:\Repositorios\tfm_reservas_starter\evidence`

Estructura por run:

- `evidence/<run-id>/metadata/`
- `evidence/<run-id>/functional/`
- `evidence/<run-id>/manual/`
- `evidence/<run-id>/review/`
- `evidence/<run-id>/security/`
- `evidence/<run-id>/semgrep/`
- `evidence/<run-id>/zap/`
- `evidence/<run-id>/ci/`
- `evidence/<run-id>/effort/`
- `evidence/<run-id>/incidents/`
- `evidence/<run-id>/evaluation/`
- `evidence/<run-id>/hashes/`

Solo se crean o utilizan las carpetas aplicables al proceso y a la fase correspondiente.

La existencia de carpetas o metadatos de preparación antes del run no constituye evidencia de ejecución experimental.

## 4. Copia primaria

**Ubicación:** disco local del proyecto.

**Ruta absoluta vigente:**

`D:\Repositorios\tfm_reservas_starter\evidence`

**Estado pre-piloto:** preparada y verificada.

Esta copia constituye la evidencia primaria de trabajo.

## 5. Copia secundaria

**Ubicación:** OneDrive institucional.

**Ruta absoluta vigente:**

`D:\Users\PJ\OneDrive - Universidad Internacional del Ecuador\TESIS\evidence`

**Estado pre-piloto:** preparada y verificada localmente.

La sincronización visual de OneDrive fue confirmada durante la preparación.

GitHub no constituye la única copia de evidencia y no sustituye a las copias primaria y secundaria.

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

La asignación nominal vigente para la ejecución experimental quedó registrada antes de C00:

- I1 — Ejecutor principal: **Paulo**;
- I2 — Registrador de evidencia y esfuerzo: **Carlos**;
- I3 — Supervisor del protocolo: **Jorge**.

Registro: `investigator_role_assignment_v0.1.md`.

SHA-256: `219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631`.

Esta asignación rige las ejecuciones experimentales posteriores a su registro. No atribuye retroactivamente a Carlos o Jorge las acciones de preparación ya realizadas antes de formalizar la correspondencia nominal.

## 7. Evidencia convencional

Para un run convencional, según corresponda, se conserva como mínimo:

- reporte funcional;
- registros manuales;
- notas de revisión técnica;
- hallazgos;
- run record;
- effort log;
- incident log;
- metadatos del entorno;
- manifiesto de integridad del run.

Durante `PILOT-CONV-01` no se generan ni consultan resultados Semgrep, OWASP ZAP, pruebas específicas de seguridad ni la matriz requisito-prueba-evidencia como guía de ejecución.

## 8. Evidencia propuesta

Además de la evidencia común, para el proceso propuesto se conservarán, cuando corresponda:

- resultados de pruebas específicas de seguridad;
- resultados Semgrep;
- resultados OWASP ZAP;
- resultados de CI;
- matriz requisito-prueba-evidencia;
- metadata GitHub;
- artifacts descargados;
- registros de verificación de los requisitos aplicables.

## 9. Integridad

Algoritmo obligatorio:

`SHA-256`

Después de cerrar un run, se genera un manifiesto de integridad.

Ejemplo de referencia:

    Get-ChildItem <directorio-run> -Recurse -File |
        Get-FileHash -Algorithm SHA256

El manifiesto se almacena en la carpeta `hashes/` correspondiente.

Después del cierre y generación de hashes:

- no se modifica la evidencia original;
- cualquier copia debe conservar exactamente los mismos archivos;
- la verificación de integridad debe realizarse tanto sobre la copia primaria como sobre la copia secundaria;
- cualquier discrepancia debe registrarse como incidencia antes de continuar.

Los hashes utilizados durante la preparación pre-piloto prueban la integridad de los artefactos de preparación, pero **no sustituyen** los hashes que deberán generarse para la evidencia experimental de cada run real.

## 10. GitHub Actions

Para los runs en los que GitHub Actions sea aplicable:

1. ejecutar únicamente la fase autorizada;
2. descargar los artifacts generados;
3. verificar su contenido;
4. almacenarlos en la evidencia primaria;
5. registrar `GITHUB_SHA`;
6. registrar `GITHUB_RUN_ID`;
7. generar o incorporar sus hashes;
8. realizar la copia secundaria;
9. verificar la integridad de ambas copias.

Los artifacts de CAL-01 y CAL-02 corresponden a calibración y validación técnica pre-piloto. No constituyen resultados de `PILOT-CONV-01`, `PILOT-PROP-01`, `DEF-CONV-01` ni `DEF-PROP-01`.

## 11. Evidencia de evaluación posterior

Después de completar las ejecuciones que correspondan se conservarán:

- instrumento independiente;
- clasificación frente a D01–D05;
- cálculos de cobertura;
- cálculos de esfuerzo;
- cálculos de tasa de detección;
- hallazgos adicionales;
- justificaciones de clasificación o consenso;
- material necesario para reproducir los cálculos finales.

La clasificación definitiva frente a D01–D05 no se realiza durante `PILOT-CONV-01`.

## 12. Runs invalidados

La evidencia de una ejecución invalidada no se elimina ni se sobrescribe.

La carpeta debe contener una marca explícita:

`INVALIDATED — EXCLUDED FROM FINAL COMPARISON`

También deberá registrarse la causa de invalidación en el `incident_log` correspondiente.

El tiempo de una ejecución definitiva invalidada se conserva como incidencia, pero no se incorpora al esfuerzo utilizado para la comparación definitiva.

## 13. Retención

Las evidencias se conservarán:

**hasta la aprobación definitiva del TFM + al menos 6 meses adicionales**

La retención aplica a:

- evidencia experimental válida;
- evidencia de runs invalidados;
- manifiestos SHA-256;
- instrumentos de registro;
- artifacts relevantes;
- metadatos necesarios para reproducibilidad.

## 14. Grabación opcional

La grabación de video o pantalla:

- no es obligatoria;
- solo se utiliza si fue pilotada y congelada antes de la fase definitiva;
- se archiva como evidencia suplementaria;
- no sustituye los registros estructurados;
- no modifica por sí misma ninguna métrica del estudio.

## 15. Estado pre-piloto verificado

Antes de `PILOT-CONV-01` se verificó:

| Control | Estado |
|---|---|
| Ruta primaria definida | `PASS` |
| Ruta secundaria definida | `PASS` |
| Estructura de evidencia preparada | `PASS` |
| Copia primaria disponible | `PASS` |
| Copia secundaria disponible | `PASS` |
| Sincronización visual OneDrive confirmada | `PASS` |
| Mecanismo SHA-256 disponible | `PASS` |
| Run ID `PILOT-CONV-01` preparado | `PASS` |
| Evidencia experimental de C00–C06 | `NO GENERADA` |
| Cronómetro experimental | `NO INICIADO` |

La evidencia primaria actualmente puede contener metadatos y sellos de preparación de `PILOT-CONV-01`.

Estos artefactos documentan que el run está preparado, no que haya comenzado.

## 16. Regla de continuidad

Antes de C00 únicamente se revalida el estado volátil necesario según `ESTADO_ACTUAL_TFM.md`.

No se deben regenerar o modificar:

- evidencia de preparación ya cerrada;
- hashes ya verificados;
- manifiestos congelados;
- sellos de preparación existentes;

salvo que exista evidencia concreta de inconsistencia.

Una vez iniciado un run, la evidencia se incorporará progresivamente siguiendo los instrumentos y actividades definidos por el protocolo.

Después del cierre del run se realizará el cierre de integridad, copia secundaria y verificación correspondiente.
