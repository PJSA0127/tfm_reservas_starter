from __future__ import annotations

import click
from flask import Flask, redirect, url_for
from sqlalchemy import select

from .config import Config
from .extensions import Base, csrf, db_session, init_database, login_manager
from .models import User


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    init_database(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from .auth import bp as auth_bp
    from .reservations import bp as reservations_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(reservations_bp)

    @app.get("/")
    def home():
        return redirect(url_for("reservations.index"))

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @login_manager.user_loader
    def load_user(user_id: str):
        if not user_id.isdigit():
            return None
        return db_session.get(User, int(user_id))

    @app.cli.command("init-db")
    def init_db_command():
        engine = app.extensions["sqlalchemy_engine"]
        Base.metadata.create_all(bind=engine)
        click.echo("Base de datos inicializada.")

    @app.cli.command("create-user")
    @click.option("--email", prompt=True)
    @click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
    def create_user_command(email: str, password: str):
        normalized_email = email.strip().lower()
        existing = db_session.scalar(select(User).where(User.email == normalized_email))
        if existing:
            raise click.ClickException("El usuario ya existe.")
        user = User(email=normalized_email, password_hash="")
        user.set_password(password)
        db_session.add(user)
        db_session.commit()
        click.echo(f"Usuario creado: {normalized_email}")

    return app
