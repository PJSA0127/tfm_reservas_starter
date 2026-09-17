import re

import pytest

from app.extensions import db_session
from app.models import Reservation


@pytest.mark.parametrize("token", [None, "token-invalido"])
def test_sec_v351_01_cancel_rejects_missing_or_invalid_csrf_token(
    csrf_authenticated_client, csrf_app, csrf_reservation, token
):
    """SEC-V351-01 / ASVS v5.0.0-3.5.1."""
    data = {} if token is None else {"csrf_token": token}

    response = csrf_authenticated_client.post(
        f"/reservations/{csrf_reservation.id}/cancel",
        data=data,
        follow_redirects=False,
    )

    assert response.status_code == 400

    with csrf_app.app_context():
        stored = db_session.get(Reservation, csrf_reservation.id)
        assert stored is not None
        assert stored.status == "ACTIVE"


def test_sec_v351_01_cancel_accepts_valid_csrf_token(
    csrf_authenticated_client, csrf_app, csrf_reservation
):
    """SEC-V351-01 / ASVS v5.0.0-3.5.1."""
    detail = csrf_authenticated_client.get(
        f"/reservations/{csrf_reservation.id}"
    )
    assert detail.status_code == 200

    match = re.search(
        rb'name="csrf_token"\s+value="([^"]+)"',
        detail.data,
    )
    assert match is not None
    csrf_token = match.group(1).decode()

    response = csrf_authenticated_client.post(
        f"/reservations/{csrf_reservation.id}/cancel",
        data={"csrf_token": csrf_token},
        follow_redirects=False,
    )

    assert response.status_code == 302

    with csrf_app.app_context():
        stored = db_session.get(Reservation, csrf_reservation.id)
        assert stored is not None
        assert stored.status == "CANCELLED"
