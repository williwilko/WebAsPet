class Pet:
    uuid: str
    name: str
    owners: list[str]
    birth_date: str

    def __init__(self, uuid: str = None, name: str = None, owner: list[str] = None, birth_date: str = None):
        self.uuid = uuid
        self.name = name
        self.owner = owner
        self.birth_date = birth_date


class PetStats:
    pet: Pet # Used to get pet's UUID (pet.uuid)
    uuid: str
    health: int
    hunger: int
    sleep: int
    joy: int

    def __init__(self, pet: Pet, health: int, hunger: int, sleep: int, joy: int):
        self.uuid = pet.uuid
        self.health = health
        self.hunger = hunger
        self.sleep = sleep
        self.joy = joy
