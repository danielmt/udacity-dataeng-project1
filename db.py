from typing import Tuple

import psycopg2
from psycopg2.extensions import connection, cursor

# defaults
DB_HOST = "127.0.0.1"
DB_NAME = "sparkifydb"
DB_USER = "student"
DB_PASSWORD = "student"


def get_connection(db: str=None) -> Tuple[connection, cursor]:
    """connect to database and return a connection and cursor tuple"""
    if not db:
        db = DB_NAME
    conn = psycopg2.connect(f"host={DB_HOST} dbname={db} user={DB_USER} password={DB_PASSWORD}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    return conn, cur
