import datetime

class Pet:
    uuid: str
    name: str
    owners: list[str]
    birth_date: str

    def __init__(self, uuid: str, name: str, owner: list[str], birth_date: str):
        self.uuid = uuid
        self.name = name
        self.owner = owner
        self.birth_date = birth_date


class PetStats:
    pet: str # UUID from Pet Class
    health: int
    hunger: int
    sleep: int
    joy: int

    def __init__(self, health: int, hunger: int, sleep: int, joy: int):
        self.health = health
        self.hunger = hunger
        self.sleep = sleep
        self.joy = joy
