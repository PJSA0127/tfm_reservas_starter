# Checklist de congelación del protocolo — v0.1

## Diseño alineado al anteproyecto

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
- [ ] asignar nombres concretos de los investigadores a I1/I2/I3 antes del piloto.

## Convencional

- [x] pruebas funcionales incluidas;
- [x] recorrido manual incluido;
- [x] revisión técnica incluida;
- [x] ASVS explícito excluido;
- [x] SAST/DAST excluidos;
- [x] pruebas específicas de seguridad excluidas;
- [x] estrategia de workspace sanitizado mediante allowlist definida;
- [ ] congelar suite funcional exacta mediante commit/tag;
- [ ] congelar datos manuales definitivos;
- [ ] generar/validar workspace convencional real y hashes.

## Propuesto

- [x] actividades comunes conservadas;
- [x] ASVS explícito;
- [x] matriz;
- [x] pruebas específicas;
- [x] Semgrep;
- [x] ZAP;
- [x] CI;
- [x] semántica hallazgo de seguridad vs. error técnico separada;
- [ ] validar GitHub Actions real;
- [ ] fijar Actions por SHA antes del piloto/freeze.

## Métricas

- [x] cobertura definida;
- [x] esfuerzo en minutos-persona;
- [x] categorías de esfuerzo definidas;
- [x] tiempo automático separado;
- [x] detección D01–D05 definida;
- [x] hallazgos adicionales separados;
- [x] criterio conservador de evidencia insuficiente definido;
- [x] criterio de mejora observable alineado al anteproyecto.

## Esfuerzo

- [x] actividades generales del TFM excluidas;
- [x] selección inicial ASVS excluida;
- [x] configuración específica incluida cuando exista tiempo observado;
- [x] ejecución propiamente dicha del piloto excluida de la comparación;
- [x] ajustes/configuración específica derivados del piloto pueden registrarse separadamente como configuración inicial si existe medición observada;
- [x] tiempos `ESTIMADO`/`PLANIFICADO` excluidos de M2;
- [ ] registrar tiempos observados reales cuando se ejecuten piloto y fase definitiva.

## Piloto

- [x] secuencia `PILOT-CONV-01` -> reset -> `PILOT-PROP-01` definida;
- [x] baseline sin D01–D05;
- [x] familiarización del equipo incluida;
- [x] criterio de repetición definido;
- [x] Run IDs del piloto definidos;
- [ ] fecha;
- [ ] nombres concretos de I1/I2/I3;
- [ ] commit/tag baseline;
- [ ] ejecución real;
- [ ] incidencias resueltas;
- [ ] resultados piloto cerrados.

## Defectos/versión experimental

- [x] D01–D05 conceptualmente definidos;
- [ ] ubicaciones congeladas;
- [ ] versión experimental creada;
- [ ] commit/tag experimental;
- [ ] datos de prueba definitivos congelados.

## Entorno

- [ ] dependencias transitivas congeladas;
- [ ] eliminar/evitar `pip install --upgrade pip` o fijar explícitamente el mecanismo de instalación antes del piloto;
- [ ] digest PostgreSQL;
- [ ] Git/host registrados según necesidad;
- [ ] commit/tag baseline;
- [ ] runner GitHub real validado;
- [ ] Dependabot para GitHub Actions validado como apoyo de desarrollo.

## Evidencias

- [x] estructura definida;
- [x] SHA-256 definido;
- [x] Run IDs definitivos definidos (`PILOT-CONV-01`, `PILOT-PROP-01`, `DEF-CONV-01`, `DEF-PROP-01`);
- [x] almacenamiento primario conceptual definido: disco local del proyecto;
- [x] almacenamiento secundario conceptual definido: OneDrive;
- [x] retención definida: aprobación del TFM + mínimo 6 meses;
- [x] custodia definida: I2 prepara / I3 verifica;
- [ ] registrar ruta absoluta del almacenamiento primario;
- [ ] registrar carpeta/ruta secundaria OneDrive;
- [ ] probar copia y verificación de hashes durante el piloto.

## GitHub / reproducibilidad

- [x] workflow solo manual mediante `workflow_dispatch`;
- [x] fases `calibration`, `pilot`, `proposed-definitive` definidas;
- [x] artifacts con nombres neutrales por fase;
- [ ] primera ejecución real `calibration`;
- [ ] descargar y verificar artifacts reales;
- [ ] registrar `GITHUB_SHA` y `GITHUB_RUN_ID`;
- [ ] fijar Actions por SHA completo;
- [ ] lock transitivo reproducible antes del piloto/freeze.

## Autorización

| Campo | Valor |
|---|---|
| Fecha de freeze | PENDIENTE |
| Versión protocolo | PENDIENTE |
| Equipo que aprueba | PENDIENTE |
| Commit/tag | PENDIENTE |

**No iniciar la evaluación definitiva mientras existan condiciones bloqueantes abiertas.**
