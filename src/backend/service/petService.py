from db.controller import Database
from models.pets import Pet
from uuid import uuid4
import utils.timeUtil as timeUtil


class PetService:
    def __init__(self, db_connection: Database):
        self.db = db_connection

    def createPet(self, pet: Pet):
        uuid = uuid4()
        name = pet.name
        owner = pet.owner
        birth_date = timeUtil.getCurrentTimestamp()
        pet = Pet(uuid=uuid, name=name, owner=owner, birth_date=birth_date)
        self.db.addPet(pet)