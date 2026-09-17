from __future__ import annotations

from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker


class Base(DeclarativeBase):
    pass


db_session = scoped_session(sessionmaker(expire_on_commit=False))
login_manager = LoginManager()
csrf = CSRFProtect()


def init_database(app):
    engine = create_engine(app.config["DATABASE_URL"], pool_pre_ping=True)
    db_session.configure(bind=engine)
    app.extensions["sqlalchemy_engine"] = engine

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
