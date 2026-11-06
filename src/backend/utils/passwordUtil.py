import secrets
import hashlib


def generateNewSalt():
    return secrets.token_hex(16)

def hashPassword(salt, clearPassword):
    combinedClear = salt + clearPassword
    hashed = hashlib.sha256(combinedClear.encode()).hexdigest()
    return hashed

def generateNewSessionHash(uuid):
    sessionHash = secrets.token_hex(16)
    return sessionHash