import sqlite3
from types import FunctionType

def connect_db():
    conn = sqlite3.connect('database.db')
    return conn



"""
def db_connection(func: FunctionType):
    def wrapper(*args, **kwargs):
        conn = connect_db()
        cursor = conn.cursor()
        func(cursor, conn, *args, **kwargs)
        conn.commit()
        conn.close()

    return wrapper
"""
