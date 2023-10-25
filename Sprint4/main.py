import db
import clearconsole
import json
import getpass
import datetime

def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'},
        5: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
    }

    if cor == 1:
        mensagem = print(f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n)

    elif cor == 2:
        mensagem = print(f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n)

    elif cor == 3:
        mensagem = print(f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n)

    elif cor == 5:
        mensagem = print(f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n)

    elif cor == 6:
        mensagem = print(f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n)
    
    elif cor == 7:
        mensagem = print(f'{cores[5]["vermelho"]}{n}{cores[5]["limpa"]}', end="")
    return mensagem

def validacao(dado):
    status = False
    if dado == 1:
        while not status:
            try:
                separador(30, 1)
                option = int(input('1- Fazer login\n2- Fazer cadastro\n3- Fazer seguro de bike!\n4- Saber informações do seguro\n5- Termos de segurança e privacidade\n6- Suporte\n7- Sair\n'))

                if 1 <= option <= 7:
                    status = True

                else:
                    clearconsole.clear_console()
                    separador(30, 1)
                    separador("Entrada inválida!", 7)
                    print(" Por favor escolha uma opção de 1 a 7!")

            except ValueError:
                clearconsole.clear_console()
                separador(30, 1)
                separador("Entrada inválida!", 7)
                print(" Por favor insira um número")

    return option

def formatarData(data):

    while True:
        if len(data) != 8:
            print(separador('Erro!', 6), end='')
            data = input(' Quantidades de caracteres diferente de 8!\nData de nascimento dd/mm/aaaa: ').replace('/', '').replace(' ', '')
            continue 

        data_atual = datetime.date.today()
        data_nascimento = datetime.date(int(data[4:]), int(data[2:4]), int(data[:2]))
        mes_nascimento = int(data[2:4])
        dia_nascimento = int(data[:2])
        idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento))

        if 18 <= idade <= 100:
            break 

        if idade < 18:
            print(separador('Você é menor de idade!', 6))
        elif idade > 100:
            print(separador('Você tem mais de 100 anos!', 6))

        data = input('Data de nascimento: ')

    return f'{data[:2]}/{data[2:4]}/{data[4:]}'

def formatarCell():
    pass

def formatarTelefone():
    pass
    
def salvarCredenciais(email, senha):
    try:
        dados_login = carregarLista("clientes.json")

    except FileNotFoundError:
        dados_login = {}

    dados_login[email] = senha

    with open("clientes.json", "w") as arquivo:
        json.dump(dados_login, arquivo)

def carregarLista(nome):
    with open(nome, "r") as arquivo:
        return json.load(arquivo)

def menuPrincipal():
    option = validacao(1)
    clearconsole.clear_console()

    match option:
        case 1:
            dados_login = carregarLista("clientes.json")
            email = input("Email: ") 
            senha = input("Senha: ")
            
            if email in dados_login:
                print("Logado")
        
        case 2:
            clearconsole.clear_console()
            separador(30, 3)
            nome = input("Nome: ")
            email = input("Email: ")
            senha = getpass.getpass("Senha: ")
            confirma = getpass.getpass("Confirme a senha: ")

            while senha != confirma:
                separador("Senhas diferentes!", 7)
                senha = getpass.getpass("\nSenha: ")
                confirma = getpass.getpass("Confirme a senha: ") 
            salvarCredenciais(email, senha)
            dt_nasc = formatarData()
            tel_fixo = formatarTelefone()
            tel_celular = formatarCell()

def principal():
    clearconsole.clear_console()
    menuPrincipal()

#Programa principal
principal()