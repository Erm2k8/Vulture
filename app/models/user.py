from ..database import connect_db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import json


class User():
    def __init__(self, name, username, email, password) -> None:
        self.name = name 
        self.username = username
        self.email = email
        self.password = password


def create_users_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def get_user_by_email(email):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user_data = cursor.fetchone()
        if user_data:
            return User(*user_data)
    return None


def user_already_exists(email):
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user_exists = cursor.fetchone()

        if user_exists:
            return True
        else:
            return False


def get_user_by_id(id):
    with connect_db() as conn:
        cursor  = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (id,))
        user_data = cursor.fetchone()
        if user_data:
            return User(*user_data)
    return None


def insert_user(name, username, email, password):
    with connect_db() as conn:
        cursor = conn.cursor()
        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (name, username, email, password) VALUES (?, ?, ?, ?)", (name, username, email, hashed_password))
        conn.commit()


def update_user(user_info, new_data: dict):
    with connect_db() as conn:
        cursor = conn.cursor()
        if isinstance(user_info, str):
            user = get_user_by_email(email=user_info)
            if user:
                hashed_password = generate_password_hash(new_data["password"])
                cursor.execute("UPDATE users SET name = ?, username = ?, password = ? WHERE email = ?", (new_data["name"], new_data["username"], hashed_password, user_info))
                conn.commit()
            else:
                raise ValueError("User with provided email does not exist.")
        elif isinstance(user_info, int):
            user = get_user_by_id(id=user_info)
            if user:
                hashed_password = generate_password_hash(new_data["password"])
                cursor.execute("UPDATE users SET name = ?, username = ?, password = ? WHERE id = ?", (new_data["name"], new_data["username"], hashed_password, user_info))
                conn.commit()
            else:
                raise ValueError("User with provided ID does not exist.")
        else:
            raise ValueError("The User identifier is incorrect or inexistent.")


def delete_user(user_info):
    with connect_db() as conn:
        cursor = conn.cursor()
        if isinstance(user_info, str):
            user = get_user_by_email(email=user_info)
            cursor.execute("DELETE FROM users WHERE email = ?", (user_info,))
            conn.commit()
        elif isinstance(user_info, int):
            user = get_user_by_id(id=user_info)
            cursor.execute("DELETE FROM users WHERE id = ?", (user_info,))
            conn.commit()
        else:
            raise ValueError("Non-existent parameter for the search on Databank.")

    