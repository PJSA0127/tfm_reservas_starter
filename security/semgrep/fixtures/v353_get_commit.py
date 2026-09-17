@bp.get("/danger")
def dangerous_get():
    db_session.commit()
    return "ok"
