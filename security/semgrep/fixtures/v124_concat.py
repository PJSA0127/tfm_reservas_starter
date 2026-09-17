from sqlalchemy import text

email = "test@example.com"
query = text("SELECT * FROM users WHERE email = '" + email + "'")
