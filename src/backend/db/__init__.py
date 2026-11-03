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
        pass