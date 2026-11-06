import sqlite3 as sql
from typing import Any

# TODO: Should be in init.py / __init__.py is used to make internal modules accessible to above layers


#################################################
## Initialisation of new SQLite3 Database file ##
#################################################

class Init:
    conn: Any
    cursor: Any
    db_path: Any

    def __init__(self, db_path: str) -> None:
        self.conn = sql.connect(db_path)
        self.cursor = self.conn.cursor()
        self.db_path = db_path

    def close(self):
        self.conn.close()

    def initialise(self):
        self.cursor.execute("DROP TABLE IF EXISTS pet_stats")
        self.cursor.execute("DROP TABLE IF EXISTS pets")
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.cursor.execute("DROP TABLE IF EXISTS app_config")
        # TODO: Include foreign keys (FK) for UUIDs
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            uuid TEXT PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
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
            birth_date TEXT NOT NULL,

            FOREIGN KEY (owner) REFERENCES users(uuid)
            ON DELETE CASCADE
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pet_stats (
            pet_uuid TEXT PRIMARY KEY,
            hunger INTEGER NOT NULL,
            health INTEGER NOT NULL,
            sleep INTEGER NOT NULL,
            joy INTEGER NOT NULL,

            FOREIGN KEY (pet_uuid) REFERENCES pets(uuid)
            ON DELETE CASCADE
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS app_config (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """)
        self.conn.commit()