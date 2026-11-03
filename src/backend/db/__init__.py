import sqlite3 as sql
from typing import Any


#################################################
## Initialisation of new SQLite3 Database file ##
#################################################

class Init:
    conn: Any
    cursor: Any

    def __init__(self):
        self.conn = sql.connect("database.db")
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def initialise(self):
        pass