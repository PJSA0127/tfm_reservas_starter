from __future__ import annotations

from datetime import UTC, date, datetime

from flask_login import UserMixin
from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from .extensions import Base


def utc_now() -> datetime:
    """
    Devuelve la fecha/hora actual en UTC como datetime naive.

    Se elimina tzinfo porque las columnas actuales utilizan
    PostgreSQL TIMESTAMP WITHOUT TIME ZONE.
    """
    return datetime.now(UTC).replace(tzinfo=None)


class User(UserMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=utc_now,
        nullable=False,
    )

    reservations: Mapped[list["Reservation"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Reservation(Base):
    __tablename__ = "reservations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True,
        nullable=False,
    )

    guest_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    guest_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    reservation_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    party_size: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    notes: Mapped[str] = mapped_column(
        Text,
        default="",
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=utc_now,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )

    owner: Mapped[User] = relationship(
        back_populates="reservations",
    )