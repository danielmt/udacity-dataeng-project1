#!/usr/bin/env python3

from psycopg2.extensions import connection, cursor

from db import get_connection
from sql_queries import create_table_queries, drop_table_queries


def create_database() -> None:
    # connect to default database
    conn, cur = get_connection(db="template1")

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    cur.close()
    conn.close()


def drop_tables(cur: cursor, conn: connection) -> None:
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur: cursor, conn: connection) -> None:
    conn, cur = get_connection()
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    create_database()

    conn, cur = get_connection()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    # close connection to database
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
