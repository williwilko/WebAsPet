import sqlite3 as sql
from typing import Any


#################################################
## Initialisation of new SQLite3 Database file ##
#################################################

class Init:
    conn: Any
    cursor: Any

    def __init__(self, db_path: str) -> None:
        self.conn = sql.connect(db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def initialise(self):
        # TODO: Include foreign keys (FK) for UUIDs
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            uuid TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            salt TEXT NOT NULL,
            password TEXT NOT NULL,
            session_hash TEXT NOT NULL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            uuid TEXT PRIMARY KEY,
            owner TEXT NOT NULL,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pet_stats (
            pet_uuid TEXT PRIMARY KEY,
            hunger INTEGER NOT NULL,
            sleep INTEGER NOT NULL,
            joy INTEGER NOT NULL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS app_config (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """)
        self.conn.commit()