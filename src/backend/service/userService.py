from uuid import uuid4

from db.controller import Database
from models.users import User
from utils.passwordUtil import *


class UserService:
    def __init__(self, db_connection: Database):
        self.db = db_connection

    def addUser(self, user: User):
        uuid = uuid4()
        name = user.name
        salt = generateNewSalt()
        password = hashPassword(salt=salt, clearPassword=user.password)
        sessionHash = generateNewSessionHash(uuid=uuid)

        user = User(uuid=uuid, name=name, salt=salt, password=password, session_hash=sessionHash)
        res = self.db.addUser(user)

    def invalidateSessionHashByUuid(self, uuid: str):
        pass