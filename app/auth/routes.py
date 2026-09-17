from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from sqlalchemy import select

from . import bp
from ..extensions import db_session
from ..models import User


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("reservations.index"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = db_session.scalar(select(User).where(User.email == email))

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("reservations.index"))

        flash("Credenciales inválidas.", "danger")

    return render_template("auth/login.html")


@bp.post("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
