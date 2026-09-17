from flask import Blueprint

bp = Blueprint("reservations", __name__, url_prefix="/reservations")

from . import routes  # noqa: E402,F401
