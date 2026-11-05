import sqlite3 as sql
from pathlib import Path

from src.backend.models.pets import Pet


class Database:
    db_path = Path

    def __init__(self, db_path):
        self.conn = sql.connect(db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def addPet(self, pet: Pet) -> None:
        self.cursor.execute("""
            INSERT INTO pets (uuid, owner, name, birth_date)
            VALUES (?, ?, ?, ?)
            """, (pet.uuid, pet.owner, pet.name, pet.birth_date)) # TODO: FILL ME
        self.conn.commit()

    def getPetByUuid(self, uuid: str) -> Pet:
        self.cursor.execute("""
            SELECT * FROM pets WHERE uuid = ?
        """, (uuid,))
        res = self.cursor.fetchone()
        print(res)
        return Pet() # TODO

    def removePetByUuid(self, uuid: str) -> None:
        self.cursor.execute() # TODO: FILL ME
        self.conn.commit()