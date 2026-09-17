from datetime import date

from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import select

from . import bp
from ..extensions import db_session
from ..models import Reservation
from ..validators import validate_reservation


POSTGRES_INTEGER_MAX = 2_147_483_647


def _owned_reservation_or_404(reservation_id: int) -> Reservation:
    # Reservation.id is backed by PostgreSQL INTEGER (signed 32-bit).
    # Werkzeug can parse arbitrarily large Python integers from the URL,
    # so reject out-of-range values before binding them to the SQL query.
    if reservation_id < 1 or reservation_id > POSTGRES_INTEGER_MAX:
        abort(404)

    reservation = db_session.scalar(
        select(Reservation).where(
            Reservation.id == reservation_id,
            Reservation.user_id == current_user.id,
        )
    )
    if reservation is None:
        abort(404)
    return reservation


@bp.get("/")
@login_required
def index():
    reservations = db_session.scalars(
        select(Reservation)
        .where(Reservation.user_id == current_user.id)
        .order_by(Reservation.reservation_date.asc(), Reservation.id.asc())
    ).all()
    return render_template("reservations/index.html", reservations=reservations)


@bp.route("/new", methods=["GET", "POST"])
@login_required
def create():
    errors: dict[str, str] = {}
    if request.method == "POST":
        errors = validate_reservation(request.form)
        if not errors:
            reservation = Reservation(
                user_id=current_user.id,
                guest_name=request.form["guest_name"].strip(),
                guest_email=request.form["guest_email"].strip().lower(),
                reservation_date=date.fromisoformat(request.form["reservation_date"]),
                party_size=int(request.form["party_size"]),
                notes=request.form.get("notes", "").strip(),
            )
            db_session.add(reservation)
            db_session.commit()
            flash("Reserva creada correctamente.", "success")
            return redirect(url_for("reservations.index"))

    return render_template("reservations/form.html", errors=errors, reservation=None)


@bp.get("/<int:reservation_id>")
@login_required
def detail(reservation_id: int):
    reservation = _owned_reservation_or_404(reservation_id)
    return render_template("reservations/detail.html", reservation=reservation)


@bp.route("/<int:reservation_id>/edit", methods=["GET", "POST"])
@login_required
def edit(reservation_id: int):
    reservation = _owned_reservation_or_404(reservation_id)
    errors: dict[str, str] = {}

    if request.method == "POST":
        errors = validate_reservation(request.form)
        if not errors:
            reservation.guest_name = request.form["guest_name"].strip()
            reservation.guest_email = request.form["guest_email"].strip().lower()
            reservation.reservation_date = date.fromisoformat(request.form["reservation_date"])
            reservation.party_size = int(request.form["party_size"])
            reservation.notes = request.form.get("notes", "").strip()
            db_session.commit()
            flash("Reserva actualizada correctamente.", "success")
            return redirect(url_for("reservations.detail", reservation_id=reservation.id))

    return render_template("reservations/form.html", errors=errors, reservation=reservation)


@bp.post("/<int:reservation_id>/cancel")
@login_required
def cancel(reservation_id: int):
    reservation = _owned_reservation_or_404(reservation_id)
    reservation.status = "CANCELLED"
    db_session.commit()
    flash("Reserva cancelada correctamente.", "success")
    return redirect(url_for("reservations.index"))
