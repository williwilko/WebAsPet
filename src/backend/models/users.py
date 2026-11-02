class User:
    uuid: str
    name: str
    salt: str
    password: str
    session_hash: str

    def __init__(self, uuid: str, name: str, salt: str, password: str, session_hash: str):
        self.uuid = uuid
        self.name = name
        self.salt = salt
        self.password = password
        self.session_hash = session_hash

