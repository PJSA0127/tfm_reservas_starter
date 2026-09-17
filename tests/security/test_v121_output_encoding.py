from datetime import date, timedelta

from app.extensions import db_session
from app.models import Reservation


def test_sec_v121_01_persisted_html_is_contextually_escaped(
    authenticated_client, app
):
    """SEC-V121-01 / ASVS v5.0.0-1.2.1."""
    payload = "<script>alert(1)</script>"

    response = authenticated_client.post(
        "/reservations/new",
        data={
            "guest_name": "Cliente XSS",
            "guest_email": "xss@example.com",
            "reservation_date": (date.today() + timedelta(days=5)).isoformat(),
            "party_size": "2",
            "notes": payload,
        },
        follow_redirects=False,
    )
    assert response.status_code == 302

    with app.app_context():
        reservation = db_session.query(Reservation).one()
        reservation_id = reservation.id

    response = authenticated_client.get(f"/reservations/{reservation_id}")
    assert response.status_code == 200

    # El texto no confiable debe aparecer codificado para contexto HTML.
    assert payload.encode() not in response.data
    assert b"&lt;script&gt;alert(1)&lt;/script&gt;" in response.data
