from datetime import date, timedelta

import pytest

from app import create_app
from app.config import TestConfig
from app.extensions import Base, db_session
from app.models import Reservation, User


class SecurityTestConfig(TestConfig):
    """Configuración específica para pruebas de controles de seguridad."""
    WTF_CSRF_ENABLED = True


def _reset_database(app):
    engine = app.extensions["sqlalchemy_engine"]
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return engine


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    engine = _reset_database(app)

    yield app

    db_session.remove()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def user(app):
    with app.app_context():
        user = User(email="usuario@tfm.local", password_hash="")
        user.set_password("Segura123!")
        db_session.add(user)
        db_session.commit()
        return user


@pytest.fixture()
def second_user(app):
    with app.app_context():
        user = User(email="otro@tfm.local", password_hash="")
        user.set_password("Segura123!")
        db_session.add(user)
        db_session.commit()
        return user


@pytest.fixture()
def authenticated_client(client, user):
    response = client.post(
        "/auth/login",
        data={"email": user.email, "password": "Segura123!"},
        follow_redirects=False,
    )
    assert response.status_code == 302
    return client


@pytest.fixture()
def reservation(app, user):
    with app.app_context():
        reservation = Reservation(
            user_id=user.id,
            guest_name="Cliente Prueba",
            guest_email="cliente@example.com",
            reservation_date=date.today() + timedelta(days=7),
            party_size=4,
            notes="Reserva de prueba",
        )
        db_session.add(reservation)
        db_session.commit()
        return reservation


@pytest.fixture()
def csrf_app():
    app = create_app(SecurityTestConfig)
    engine = _reset_database(app)

    yield app

    db_session.remove()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture()
def csrf_client(csrf_app):
    return csrf_app.test_client()


@pytest.fixture()
def csrf_user(csrf_app):
    with csrf_app.app_context():
        user = User(email="csrf@tfm.local", password_hash="")
        user.set_password("Segura123!")
        db_session.add(user)
        db_session.commit()
        return user


@pytest.fixture()
def csrf_reservation(csrf_app, csrf_user):
    with csrf_app.app_context():
        reservation = Reservation(
            user_id=csrf_user.id,
            guest_name="Reserva CSRF",
            guest_email="csrf@example.com",
            reservation_date=date.today() + timedelta(days=7),
            party_size=2,
            notes="Prueba de protección CSRF",
        )
        db_session.add(reservation)
        db_session.commit()
        return reservation


@pytest.fixture()
def csrf_authenticated_client(csrf_client, csrf_user):
    # Flask-Login almacena el identificador autenticado en la sesión.
    # Se establece directamente para poder probar CSRF en los endpoints
    # sensibles sin depender del formulario de login, que también está
    # protegido por CSRF.
    with csrf_client.session_transaction() as session:
        session["_user_id"] = str(csrf_user.id)
        session["_fresh"] = True

    return csrf_client
