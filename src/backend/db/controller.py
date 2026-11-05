import sqlite3 as sql
from pathlib import Path

from models.dbReply import Reply
from models.pets import Pet


class Database:
    db_path = Path

    def __init__(self, db_path):
        self.conn = sql.connect(db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def addPet(self, pet: Pet) -> Reply:
        self.cursor.execute("""
            INSERT INTO pets (uuid, owner, name, birth_date)
            VALUES (?, ?, ?, ?)
            """, (pet.uuid, pet.owner, pet.name, pet.birth_date)) # TODO: FILL ME
        self.conn.commit()
        return Reply('ok', data=pet)

    def getPetByUuid(self, uuid: str) -> Reply:
        self.cursor.execute("""
            SELECT * FROM pets WHERE uuid = ?
        """, (uuid,))
        res = self.cursor.fetchone()
        print(res)
        pet = Pet()
        return Reply('ok', data=pet)

    def removePetByUuid(self, uuid: str) -> Reply:
        self.cursor.execute() # TODO: FILL ME
        self.conn.commit()
        return Reply('ok')