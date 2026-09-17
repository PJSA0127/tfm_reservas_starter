from datetime import date, timedelta

from app.validators import validate_reservation


def _valid_data(**overrides):
    data = {
        "guest_name": "Cliente Valido",
        "guest_email": "cliente@example.com",
        "reservation_date": (date.today() + timedelta(days=1)).isoformat(),
        "party_size": "2",
        "notes": "",
    }
    data.update(overrides)
    return data


def test_valid_reservation_has_no_errors():
    assert validate_reservation(_valid_data()) == {}


def test_name_must_have_minimum_length():
    errors = validate_reservation(_valid_data(guest_name="A"))
    assert "guest_name" in errors


def test_date_cannot_be_in_the_past():
    errors = validate_reservation(
        _valid_data(reservation_date=(date.today() - timedelta(days=1)).isoformat())
    )
    assert "reservation_date" in errors


def test_date_cannot_exceed_one_year():
    errors = validate_reservation(
        _valid_data(reservation_date=(date.today() + timedelta(days=366)).isoformat())
    )
    assert "reservation_date" in errors


def test_party_size_must_be_between_1_and_12():
    assert "party_size" in validate_reservation(_valid_data(party_size="0"))
    assert "party_size" in validate_reservation(_valid_data(party_size="13"))


def test_notes_maximum_length_is_500():
    errors = validate_reservation(_valid_data(notes="x" * 501))
    assert "notes" in errors
