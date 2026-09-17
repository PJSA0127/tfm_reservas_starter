from datetime import date, timedelta

from app.extensions import db_session
from app.models import Reservation


def _valid_payload(**overrides):
    payload = {
        "guest_name": "Cliente Servidor",
        "guest_email": "servidor@example.com",
        "reservation_date": (date.today() + timedelta(days=5)).isoformat(),
        "party_size": "2",
        "notes": "",
    }
    payload.update(overrides)
    return payload


def test_sec_v222_01_direct_create_request_cannot_bypass_client_constraints(
    authenticated_client, app
):
    """SEC-V222-01 / ASVS v5.0.0-2.2.2."""
    # El cliente de pruebas envía HTTP directamente: no ejecuta minlength,
    # max, required ni otras restricciones del navegador.
    response = authenticated_client.post(
        "/reservations/new",
        data=_valid_payload(guest_name="A", party_size="999"),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"El nombre debe tener entre 2 y 100 caracteres." in response.data
    assert b"La cantidad de personas debe estar entre 1 y 12." in response.data

    with app.app_context():
        assert db_session.query(Reservation).count() == 0


def test_sec_v222_01_direct_edit_request_cannot_persist_invalid_state(
    authenticated_client, app, reservation
):
    """SEC-V222-01 / ASVS v5.0.0-2.2.2."""
    original_name = reservation.guest_name
    original_notes = reservation.notes

    response = authenticated_client.post(
        f"/reservations/{reservation.id}/edit",
        data=_valid_payload(
            guest_name="A",
            notes="x" * 501,
        ),
        follow_redirects=True,
    )

    assert response.status_code == 200

    with app.app_context():
        stored = db_session.get(Reservation, reservation.id)
        assert stored is not None
        assert stored.guest_name == original_name
        assert stored.notes == original_notes
