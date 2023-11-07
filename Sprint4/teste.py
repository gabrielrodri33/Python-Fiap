import bcrypt
import getpass

password = getpass.getpass("Senha: ").encode("utf-8")
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")