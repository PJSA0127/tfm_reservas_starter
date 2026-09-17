from datetime import date, timedelta

import pytest

from app.extensions import db_session
from app.models import Reservation


def _valid_payload(**overrides):
    payload = {
        "guest_name": "Cliente Valido",
        "guest_email": "cliente@example.com",
        "reservation_date": (date.today() + timedelta(days=5)).isoformat(),
        "party_size": "2",
        "notes": "",
    }
    payload.update(overrides)
    return payload


@pytest.mark.parametrize(
    ("field", "value", "expected_message"),
    [
        ("guest_name", "A", "El nombre debe tener entre 2 y 100 caracteres."),
        ("guest_name", "A" * 101, "El nombre debe tener entre 2 y 100 caracteres."),
        ("guest_email", "correo-invalido", "Ingrese un correo electrónico válido."),
        (
            "reservation_date",
            (date.today() - timedelta(days=1)).isoformat(),
            "La fecha no puede estar en el pasado.",
        ),
        (
            "reservation_date",
            (date.today() + timedelta(days=366)).isoformat(),
            "La fecha no puede superar un año desde hoy.",
        ),
        ("party_size", "0", "La cantidad de personas debe estar entre 1 y 12."),
        ("party_size", "13", "La cantidad de personas debe estar entre 1 y 12."),
        ("party_size", "abc", "Ingrese una cantidad válida."),
        ("notes", "x" * 501, "Las notas no pueden superar 500 caracteres."),
    ],
)
def test_sec_v221_01_invalid_business_inputs_are_rejected(
    authenticated_client, app, field, value, expected_message
):
    """SEC-V221-01 / ASVS v5.0.0-2.2.1."""
    response = authenticated_client.post(
        "/reservations/new",
        data=_valid_payload(**{field: value}),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert expected_message.encode() in response.data

    with app.app_context():
        assert db_session.query(Reservation).count() == 0


@pytest.mark.parametrize(
    "payload",
    [
        {
            "guest_name": "AB",
            "reservation_date": date.today().isoformat(),
            "party_size": "1",
            "notes": "x" * 500,
        },
        {
            "guest_name": "A" * 100,
            "reservation_date": (date.today() + timedelta(days=365)).isoformat(),
            "party_size": "12",
            "notes": "",
        },
    ],
)
def test_sec_v221_01_documented_boundary_values_are_accepted(
    authenticated_client, app, payload
):
    """SEC-V221-01 / ASVS v5.0.0-2.2.1 — fronteras válidas."""
    response = authenticated_client.post(
        "/reservations/new",
        data=_valid_payload(**payload),
        follow_redirects=False,
    )

    assert response.status_code == 302

    with app.app_context():
        assert db_session.query(Reservation).count() == 1
