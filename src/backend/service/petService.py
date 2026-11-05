from db.controller import Database
from models.pets import Pet
import uuid

class PetService:
    def __init__(self, db_connection: Database):
        self.db = db_connection

    def createPet(self, pet: Pet):
        uuid = uuid.uuid4()
        name = pet.name
        owner = pet.owner
        birth_date = getCurrentTimestamp()
        pet = Pet(uuid=uuid, name=name, owner=owner, birth_date=birth_date)
        self.db.addPet(pet)