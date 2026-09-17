from app.extensions import db_session
from app.models import User


def test_reservations_require_authentication(client):
    response = client.get("/reservations/", follow_redirects=False)

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_login_with_valid_credentials(client, user):
    response = client.post(
        "/auth/login",
        data={"email": user.email, "password": "Segura123!"},
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/reservations/")


def test_login_with_invalid_credentials(client, user):
    response = client.post(
        "/auth/login",
        data={"email": user.email, "password": "incorrecta"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Credenciales inv\xc3\xa1lidas" in response.data


def test_password_is_not_stored_in_plaintext(app, user):
    with app.app_context():
        stored = db_session.get(User, user.id)
        assert stored is not None
        assert stored.password_hash != "Segura123!"
        assert stored.check_password("Segura123!")
