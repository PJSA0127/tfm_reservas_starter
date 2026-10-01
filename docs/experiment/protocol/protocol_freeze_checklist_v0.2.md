# Checklist de congelación del protocolo — v0.2

## Estado

**PREPARACIÓN PRE-PILOTO COMPLETADA / FREEZE DEFINITIVO PENDIENTE**

Este checklist distingue entre:

- condiciones ya satisfechas para iniciar el piloto;
- actividades que únicamente pueden cerrarse mediante ejecución observada del piloto;
- condiciones correspondientes a la versión experimental definitiva con D01–D05;
- autorización del freeze definitivo posterior al piloto.

El estado operacional exacto de los runs se mantiene en `ESTADO_ACTUAL_TFM.md`.

## Diseño alineado al TFM

- [x] dos procesos definidos;
- [x] convencional primero;
- [x] una ejecución definitiva por proceso;
- [x] mismo estado experimental;
- [x] mismo equipo investigador para actividades equivalentes;
- [x] mismos roles en actividades equivalentes;
- [x] un único equipo experimental principal definido;
- [x] dispositivos auxiliares limitados a registro/checklist;
- [x] conocimiento general de la existencia de cinco defectos reconocido;
- [x] restricción de acceso a catálogo/ubicación durante convencional;
- [x] asociación final después de ambos procesos;
- [x] piloto previo sin D01–D05.

## Roles

- [x] roles I1/I2/I3 definidos;
- [x] responsabilidades y restricciones de cada rol documentadas;
- [x] actividades conjuntas se registran por investigador activo;
- [x] mismos roles en actividades equivalentes;
- [x] asignación nominal registrada antes de C00: I1 = Paulo, I2 = Carlos, I3 = Jorge.
- [x] registro: `investigator_role_assignment_v0.1.md`;
- [x] SHA-256 del registro: `219a8d9b925f101f6d1168a9d396a497c2a3997035e8d358f1a09ff78acfc631`.

## Convencional

- [x] pruebas funcionales incluidas;
- [x] recorrido manual incluido;
- [x] revisión técnica incluida;
- [x] ASVS explícito excluido;
- [x] SAST/DAST excluidos;
- [x] pruebas específicas de seguridad excluidas;
- [x] estrategia de workspace sanitizado mediante allowlist definida;
- [x] suite funcional exacta congelada dentro del baseline técnico `pre-pilot-freeze-v0.1`;
- [x] casos y datos manuales pre-piloto congelados y versionados;
- [x] workspace convencional real generado, sanitizado y validado;
- [x] manifiesto y paquete convencional protegidos mediante SHA-256.

## Propuesto

- [x] actividades comunes conservadas;
- [x] ASVS explícito;
- [x] matriz;
- [x] pruebas específicas;
- [x] Semgrep;
- [x] ZAP;
- [x] CI;
- [x] semántica hallazgo de seguridad vs. error técnico separada;
- [x] GitHub Actions real validado mediante CAL-01 y CAL-02;
- [x] Actions utilizadas por el workflow fijadas por SHA completo;
- [x] workflow exclusivamente manual mediante `workflow_dispatch`.

## Métricas

- [x] cobertura definida;
- [x] esfuerzo en minutos-persona;
- [x] categorías de esfuerzo definidas;
- [x] tiempo automático separado;
- [x] detección D01–D05 definida;
- [x] hallazgos adicionales separados;
- [x] criterio conservador de evidencia insuficiente definido;
- [x] criterio de mejora observable alineado al TFM.

## Esfuerzo

- [x] actividades generales del TFM excluidas;
- [x] selección inicial ASVS excluida;
- [x] configuración específica incluida cuando exista tiempo observado;
- [x] ejecución propiamente dicha del piloto excluida de la comparación;
- [x] ajustes/configuración específica derivados del piloto pueden registrarse separadamente como configuración inicial si existe medición observada;
- [x] tiempos `ESTIMADO`/`PLANIFICADO` excluidos de M2;
- [ ] registrar tiempos observados reales cuando se ejecuten piloto y fase definitiva.

## Piloto

- [x] secuencia `PILOT-CONV-01` -> cierre/archivo -> reset -> `PILOT-PROP-01` definida;
- [x] baseline seguro sin D01–D05;
- [x] familiarización del equipo incluida;
- [x] criterio de repetición definido;
- [x] Run IDs del piloto definidos;
- [x] commit/tag baseline técnico pre-piloto fijado;
- [x] asignación nominal de I1/I2/I3 registrada y protegida mediante SHA-256;
- [x] fecha/hora real de inicio de `PILOT-CONV-01` registrada;
- [x] `PILOT-CONV-01` ejecutado y cerrado;
- [x] evidencia de `PILOT-CONV-01` archivada y verificada;
- [x] reset CONV -> PROP ejecutado y verificado;
- [ ] `PILOT-PROP-01` ejecutado y cerrado;
- [ ] incidencias del piloto analizadas y resueltas conforme al protocolo;
- [ ] resultados y lecciones del piloto cerrados;
- [ ] ajustes permitidos derivados del piloto documentados y versionados;
- [ ] protocolo experimental definitivo congelado después del piloto.

## Defectos / versión experimental definitiva

- [x] D01–D05 conceptualmente definidos;
- [x] correspondencia conceptual D01–D05 ↔ requisitos ASVS definida;
- [ ] ubicaciones/manifestaciones definitivas D01–D05 congeladas;
- [ ] D01–D05 introducidos en la versión experimental;
- [ ] versión experimental definitiva creada;
- [ ] funcionalidad de la versión experimental validada;
- [ ] correspondencia defecto–requisito validada;
- [ ] commit/tag de la versión experimental definitiva fijado;
- [ ] datos de prueba definitivos congelados.

> Estas condiciones permanecen abiertas durante el piloto porque el piloto utiliza deliberadamente el baseline seguro sin D01–D05.

## Entorno técnico pre-piloto

- [x] dependencias directas y transitivas congeladas mediante `requirements.lock`;
- [x] instalación Python reproducible definida sin `pip install --upgrade pip`;
- [x] imagen Python fijada por digest;
- [x] imagen PostgreSQL fijada por digest;
- [x] imagen Semgrep fijada por digest;
- [x] imagen OWASP ZAP fijada por digest;
- [x] Git y características relevantes del host registradas;
- [x] commit/tag baseline técnico registrado;
- [x] runner GitHub real validado;
- [x] Dependabot configurado exclusivamente como apoyo de desarrollo para `github-actions`;
- [x] CAL-02 confirmó que la inmovilización técnica mantiene el comportamiento esperado del baseline seguro.

## Evidencias

- [x] estructura definida;
- [x] SHA-256 definido;
- [x] Run IDs definitivos definidos (`PILOT-CONV-01`, `PILOT-PROP-01`, `DEF-CONV-01`, `DEF-PROP-01`);
- [x] almacenamiento primario definido: disco local del proyecto;
- [x] ruta absoluta primaria definida;
- [x] almacenamiento secundario definido: OneDrive;
- [x] ruta/carpeta secundaria definida;
- [x] retención definida: aprobación del TFM + mínimo 6 meses;
- [x] custodia definida: I2 prepara / I3 verifica;
- [x] copia primaria y secundaria preparadas y verificadas antes del piloto;
- [x] mecanismos de manifiesto y SHA-256 probados durante la preparación;
- [ ] cerrar, hashear y verificar la evidencia real de cada run piloto;
- [ ] comprobar copia primaria/secundaria de la evidencia real durante el piloto.

> Las verificaciones pre-piloto anteriores no sustituyen la comprobación de integridad que debe realizarse sobre la evidencia generada por cada run real.

## GitHub / reproducibilidad

- [x] workflow solo manual mediante `workflow_dispatch`;
- [x] fases `calibration`, `pilot`, `proposed-definitive` definidas;
- [x] artifacts con nombres neutrales por fase;
- [x] primera ejecución real `calibration` completada mediante CAL-01;
- [x] segunda calibración del freeze técnico completada mediante CAL-02;
- [x] artifacts reales descargados/revisados y protegidos mediante SHA-256;
- [x] `GITHUB_SHA` y `GITHUB_RUN_ID` registrados;
- [x] Actions fijadas por SHA completo;
- [x] lock transitivo reproducible generado;
- [x] imágenes relevantes fijadas por digest;
- [ ] ejecución GitHub Actions de fase `pilot`;
- [ ] ejecución GitHub Actions de fase `proposed-definitive`.

## Autorización del freeze definitivo

| Campo | Valor |
|---|---|
| Fecha de freeze definitivo | PENDIENTE — posterior al piloto |
| Versión definitiva del protocolo | PENDIENTE — posterior al piloto |
| Equipo que aprueba | Jorge, Carlos y Paulo — aprobación formal pendiente |
| Commit/tag experimental definitivo | PENDIENTE — versión con D01–D05 |

**No iniciar la evaluación definitiva mientras existan condiciones bloqueantes abiertas en las secciones Piloto, Defectos / versión experimental definitiva o Autorización del freeze definitivo.**

La existencia de condiciones pendientes de la evaluación definitiva **no bloquea por sí misma el inicio del piloto**, siempre que las condiciones pre-piloto aplicables hayan sido satisfechas y el estado operacional autorice la apertura de C00.

## Estado post-PILOT-CONV-01

- [x] `PILOT-CONV-01` ejecutado.
- [x] `PILOT-CONV-01` invalidado por consenso I1+I2+I3.
- [x] evidencia de `PILOT-CONV-01` archivada y verificada mediante SHA-256.
- [x] `INC-C03-001` e `INC-C03-002` analizadas.
- [x] ajustes derivados documentados y versionados.
- [x] `manual_cases_v0.2.md` generado.
- [x] `conventional_procedure_v0.2.md` generado.
- [x] revalidar las cinco correcciones de instrumentación.
- [x] aprobar instrumentos v0.2 para nuevo freeze piloto.
- [x] reconstruir y validar workspace convencional para `PILOT-CONV-02`.
- [x] generar manifiesto y paquete específico de `PILOT-CONV-02`.
- [x] ejecutar y cerrar `PILOT-CONV-02`.
- [x] ejecutar reset CONV -> PROP.
- [x] revalidar workspace propuesto con los instrumentos comunes v0.2 sin alterar el baseline técnico.
- [x] autorizar `PILOT-PROP-01` en estado `READY_TO_START / NOT_STARTED`.
- [ ] ejecutar y cerrar `PILOT-PROP-01`.
- [ ] cerrar resultados globales del piloto.
- [ ] congelar protocolo experimental definitivo.

La revalidación de instrumentos, `PILOT-CONV-02` y el reset CONV -> PROP están completados. `PILOT-PROP-01` permanece `READY_TO_START / NOT_STARTED`; el freeze experimental definitivo continúa pendiente hasta cerrar el piloto completo.