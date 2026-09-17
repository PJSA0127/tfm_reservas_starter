from sqlalchemy import text

email = "test@example.com"
query = text(f"SELECT * FROM users WHERE email = '{email}'")
