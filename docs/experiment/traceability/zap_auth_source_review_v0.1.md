# Revisión del flujo de autenticación del código fuente

## Hallazgos

1. `app/auth/routes.py`
   - Login por `GET` y `POST`.
   - Normaliza el correo a minúsculas.
   - Busca el usuario mediante SQLAlchemy.
   - Verifica el hash de contraseña.
   - Ejecuta `login_user(user)` y redirige a `reservations.index`.

2. `app/templates/auth/login.html`
   - Campo de usuario: `email`.
   - Campo de contraseña: `password`.
   - Campo oculto CSRF: `csrf_token`.
   - Submit estándar HTML.

3. `app/config.py`
   - Sesión `HttpOnly`.
   - `SameSite=Lax`.
   - En DAST `SESSION_COOKIE_SECURE=false`, apropiado para el laboratorio HTTP local.

4. `app/__init__.py`
   - `LoginManager` configurado correctamente.
   - `login_view = auth.login`.
   - `user_loader` recupera el usuario por ID.

5. `app/reservations/routes.py`
   - Todas las rutas funcionales están protegidas con `@login_required`.

## Conclusión

La aplicación no presenta un defecto aparente que explique los redirects de ZAP.
Los redirects son coherentes con una petición que no lleva una sesión autenticada.
El problema está en la instrumentación de autenticación de ZAP.

La estrategia recomendada es aislar y diagnosticar autenticación antes de volver
a ejecutar spider y active scan.
