import pytest

from app.extensions import db_session
from app.models import Reservation


@pytest.mark.parametrize("method", ["GET", "HEAD", "OPTIONS"])
def test_sec_v353_01_safe_http_methods_do_not_modify_state(
    authenticated_client, app, reservation, method
):
    """SEC-V353-01 / ASVS v5.0.0-3.5.3."""
    response = authenticated_client.open(
        f"/reservations/{reservation.id}/cancel",
        method=method,
        follow_redirects=False,
    )

    # El código concreto puede ser 405 para GET/HEAD y 200 para OPTIONS.
    # La propiedad que se verifica es que el estado NO cambie.
    assert response.status_code in {200, 405}

    with app.app_context():
        stored = db_session.get(Reservation, reservation.id)
        assert stored is not None
        assert stored.status == "ACTIVE"


def test_sec_v353_01_post_can_modify_state(
    authenticated_client, app, reservation
):
    """SEC-V353-01 / ASVS v5.0.0-3.5.3."""
    response = authenticated_client.post(
        f"/reservations/{reservation.id}/cancel",
        follow_redirects=False,
    )

    assert response.status_code == 302

    with app.app_context():
        stored = db_session.get(Reservation, reservation.id)
        assert stored is not None
        assert stored.status == "CANCELLED"
