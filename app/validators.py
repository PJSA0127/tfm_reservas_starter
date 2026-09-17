from __future__ import annotations

from datetime import date, timedelta


def validate_reservation(data: dict[str, str]) -> dict[str, str]:
    errors: dict[str, str] = {}

    name = data.get("guest_name", "").strip()
    email = data.get("guest_email", "").strip()
    raw_date = data.get("reservation_date", "").strip()
    raw_party_size = data.get("party_size", "").strip()
    notes = data.get("notes", "").strip()

    if not (2 <= len(name) <= 100):
        errors["guest_name"] = "El nombre debe tener entre 2 y 100 caracteres."

    if len(email) > 255 or "@" not in email or email.startswith("@") or email.endswith("@"):
        errors["guest_email"] = "Ingrese un correo electrónico válido."

    try:
        parsed_date = date.fromisoformat(raw_date)
        if parsed_date < date.today():
            errors["reservation_date"] = "La fecha no puede estar en el pasado."
        elif parsed_date > date.today() + timedelta(days=365):
            errors["reservation_date"] = "La fecha no puede superar un año desde hoy."
    except ValueError:
        errors["reservation_date"] = "Ingrese una fecha válida."

    try:
        party_size = int(raw_party_size)
        if not 1 <= party_size <= 12:
            errors["party_size"] = "La cantidad de personas debe estar entre 1 y 12."
    except ValueError:
        errors["party_size"] = "Ingrese una cantidad válida."

    if len(notes) > 500:
        errors["notes"] = "Las notas no pueden superar 500 caracteres."

    return errors
