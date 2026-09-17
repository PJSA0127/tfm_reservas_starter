from datetime import date, timedelta

from app.extensions import db_session
from app.models import Reservation


def _valid_payload(**overrides):
    payload = {
        "guest_name": "Ana Torres",
        "guest_email": "ANA@example.com",
        "reservation_date": (date.today() + timedelta(days=10)).isoformat(),
        "party_size": "3",
        "notes": "Mesa cerca de la ventana",
    }
    payload.update(overrides)
    return payload


def test_create_reservation(authenticated_client, app, user):
    response = authenticated_client.post(
        "/reservations/new",
        data=_valid_payload(),
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/reservations/")

    with app.app_context():
        reservation = db_session.query(Reservation).one()
        assert reservation.user_id == user.id
        assert reservation.guest_name == "Ana Torres"
        assert reservation.guest_email == "ana@example.com"
        assert reservation.party_size == 3
        assert reservation.status == "ACTIVE"


def test_create_rejects_invalid_server_side_data(authenticated_client, app):
    response = authenticated_client.post(
        "/reservations/new",
        data=_valid_payload(party_size="99"),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert "La cantidad de personas debe estar entre 1 y 12.".encode() in response.data

    with app.app_context():
        assert db_session.query(Reservation).count() == 0


def test_edit_reservation(authenticated_client, app, reservation):
    response = authenticated_client.post(
        f"/reservations/{reservation.id}/edit",
        data=_valid_payload(guest_name="Nombre Actualizado", party_size="5"),
        follow_redirects=False,
    )

    assert response.status_code == 302

    with app.app_context():
        updated = db_session.get(Reservation, reservation.id)
        assert updated is not None
        assert updated.guest_name == "Nombre Actualizado"
        assert updated.party_size == 5


def test_cancel_reservation_requires_post(authenticated_client, reservation):
    response = authenticated_client.get(
        f"/reservations/{reservation.id}/cancel",
        follow_redirects=False,
    )

    assert response.status_code == 405


def test_cancel_reservation(authenticated_client, app, reservation):
    response = authenticated_client.post(
        f"/reservations/{reservation.id}/cancel",
        follow_redirects=False,
    )

    assert response.status_code == 302

    with app.app_context():
        cancelled = db_session.get(Reservation, reservation.id)
        assert cancelled is not None
        assert cancelled.status == "CANCELLED"


def test_user_cannot_access_another_users_reservation(
    client, app, second_user, reservation
):
    response = client.post(
        "/auth/login",
        data={"email": second_user.email, "password": "Segura123!"},
        follow_redirects=False,
    )
    assert response.status_code == 302

    response = client.get(f"/reservations/{reservation.id}")

    assert response.status_code == 404

def test_oversized_reservation_id_returns_404(authenticated_client):
    response = authenticated_client.get(
        "/reservations/5349674779157766503",
        follow_redirects=False,
    )

    assert response.status_code == 404
