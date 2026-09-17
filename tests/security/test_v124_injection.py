def test_sec_v124_01_sql_injection_cannot_bypass_login(client, user):
    """SEC-V124-01 / ASVS v5.0.0-1.2.4."""
    injected_email = f"{user.email}' OR '1'='1' --"

    response = client.post(
        "/auth/login",
        data={
            "email": injected_email,
            "password": "Segura123!",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Credenciales inv\xc3\xa1lidas" in response.data

    # La carga no debe transformar la consulta ni autenticar al solicitante.
    protected = client.get("/reservations/", follow_redirects=False)
    assert protected.status_code == 302
    assert "/auth/login" in protected.headers["Location"]
