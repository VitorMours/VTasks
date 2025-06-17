from werkzeug.security import generate_password_hash
salt = 16

def encrypt_password(password: str) -> str:
    global salt
    encrypt_password = generate_password_hash(password, "scrypt", salt)
    return encrypt_password

def check_password(hashed_password: str) -> str:
    pass
