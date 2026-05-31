import bcrypt
from database.db import get_connection


def register_user(name, email, password):

    conn = get_connection()
    cur = conn.cursor()

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:
        cur.execute(
            """
            INSERT INTO users
            (name,email,password)
            VALUES(?,?,?)
            """,
            (
                name,
                email,
                hashed
            )
        )

        conn.commit()
        return True

    except:
        return False


def login_user(email, password):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cur.fetchone()

    if user:

        if bcrypt.checkpw(
                password.encode(),
                user["password"]):

            return dict(user)

    return None