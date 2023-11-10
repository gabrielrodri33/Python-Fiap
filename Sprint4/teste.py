import datetime

def cadastrar_usuario(info, info2):
    date = datetime.datetime.now()
    texto = f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n{info}: {info2}\nDia e hora: {date}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
    with open('Sprint4/archive/eventos.txt', 'a') as file:
        file.write(texto)


cadastrar_usuario('Usuário cadastrado', 'email')