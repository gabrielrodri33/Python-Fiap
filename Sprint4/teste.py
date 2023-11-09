import bcrypt
import base64
import getpass

def pwd():
    password = getpass.getpass("Senha: ").encode("utf-8")

    code = base64.b64encode(password).decode('utf-8')

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    print(f'senha: {hashed}')
    print(f'code: {code}')
    return hashed, code

pwd()