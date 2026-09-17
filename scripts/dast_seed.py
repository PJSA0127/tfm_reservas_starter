from datetime import date, timedelta
import os

from app import create_app
from app.extensions import Base, db_session
from app.models import Reservation, User


def main():
    app = create_app()

    email = os.environ.get("ZAP_USER_EMAIL", "zap@tfm.local").strip().lower()
    password = os.environ.get("ZAP_USER_PASSWORD", "ZapTest123!")

    with app.app_context():
        engine = app.extensions["sqlalchemy_engine"]

        # El entorno DAST es efímero y se reconstruye desde cero para que
        # cada exploración/escaneo parta del mismo estado conocido.
        db_session.remove()
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        user = User(email=email, password_hash="")
        user.set_password(password)
        db_session.add(user)
        db_session.flush()

        reservation = Reservation(
            user_id=user.id,
            guest_name="Cliente DAST",
            guest_email="cliente.dast@example.com",
            reservation_date=date.today() + timedelta(days=7),
            party_size=2,
            notes="Reserva semilla para exploración dinámica controlada.",
        )
        db_session.add(reservation)
        db_session.commit()

        print(f"Entorno DAST inicializado para {email}.")
        print(f"Reserva semilla ID={reservation.id}.")


if __name__ == "__main__":
    main()
