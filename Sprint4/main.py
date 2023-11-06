# import db
# import neverbounce_sdk
# import bcrypt
import json
import getpass
import datetime
import os
import smtplib
from email.mime.text import MIMEText

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'},
        5: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
    }

    if cor == 1:
        mensagem = f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n

    elif cor == 2:
        mensagem = f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n

    elif cor == 3:
        mensagem = f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n

    elif cor == 5:
        mensagem = f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n

    elif cor == 6:
        mensagem = f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n
    
    elif cor == 7:
        mensagem = f'{cores[5]["vermelho"]}{n}{cores[5]["limpa"]}'
    return print(mensagem)

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
                    clear_console()
                    separador(30, 1)
                    separador("Entrada inválida!", 7)
                    print(" Por favor escolha uma opção de 1 a 7!")

            except ValueError:
                clear_console()
                separador(30, 1)
                separador("Entrada inválida!", 7)
                print(" Por favor insira um número")

    elif dado == 2:
        while not status:
            try:
                separador(30, 2)
                mudanca = int(input('Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: '))
    return option

def formatarData():
    data  = input("Data de nascimento dd/mm/yyyy: ").strip().replace('/', '')
    while True:
        if len(data) != 8:
            separador('Erro!', 7)
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
    cell = input("Celular (xx)xxxxx-xxxx: ").replace("(","").replace(")", "").replace("-", "").replace(" ", "")

    while len(cell) != 11:
        separador("Entrada inválida!", 7)
        cell = input("Celular (xx)xxxxx-xxxx: ").replace("(","").replace(")", "").replace("-", "").replace(" ", "")

    return f'({cell[:2]}) {cell[2:7]}-{cell[7:]}'

def formatarTelefone():
    tel = input("Telefone fixo xxxx-xxxx: ").replace("-",'').strip()

    while len(tel) != 8:
        separador("Entrada inválida!", 7)
        tel = input("\nTelefone fixo xxxx-xxxx: ").replace("-",'').strip()

    # while True:
    #     try:
    #         tel = int(tel)
    #         break
    #     except:

    return f'{tel[:4]}-{tel[4:]}'

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

def verificaçãoEmail(email):
    server_smtp = "smtp.gmail.com"
    smtp_port = 587

    sender = "gabrielkeeper2@gmail.com"
    receiver = email
    topic = "Verificação de email"
    body = "Código"

    message = MIMEText(body)
    message['Subject'] = topic
    message['From'] = sender
    message['To'] = receiver

    server = smtplib.SMTP(server_smtp, smtp_port)
    server.starttls()
    user = "bikevision083@gmail.com"
    pwd = "Fiap2023"
    server.login(user, pwd)

    server.sendmail(sender, receiver, message.as_string())

    server.quit()

def addDict(dicionario, nome, email, dt_nasc, tel_fixo, tel_celular, cpf):
    dicionario = {
        "nome": nome,
        "email": email,
        "cpf": cpf,
        "data_nascimento": dt_nasc,
        "telefone_fixo": tel_fixo,
        "telefone_celular": tel_celular
    }

    return dicionario

def formatarCpf():
    cpf = input("CPF: ")
    while len(cpf) > 11 or len(cpf) < 11:
        print(separador('CPF inválido!', 6), end='')
        cpf = input(f', deve conter 11 caracteres\nDigite seu CPF: ').replace('.', '').replace('-', '').replace(' ', '')
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def menuPrincipal():
    option = validacao(1)
    clear_console()

    match option:
        case 1:
            dados_login = carregarLista("clientes.json")
            email = input("Email: ") 
            senha = input("Senha: ")
            
            if email in dados_login:
                print("Logado")
        
        case 2:
            dados_cliente = {}
            clear_console()
            separador(30, 3)
            nome = input("Nome: ")
            email = input("Email: ")
            senha = getpass.getpass("Senha: ")
            confirma = getpass.getpass("Confirme a senha: ")

            while senha != confirma:
                separador("Senhas diferentes!", 7)
                senha = getpass.getpass("Senha: ")
                confirma = getpass.getpass("Confirme a senha: ") 

            salvarCredenciais(email, senha)
            cpf = formatarCpf()
            dt_nasc = formatarData()
            tel_fixo = formatarTelefone()
            tel_celular = formatarCell()
            dados_cliente = addDict(dados_cliente, nome, email, dt_nasc, tel_fixo, tel_celular, cpf)

            clear_console()
            separador(30, 2)
            print(f'1- Nome: {dados_cliente["nome"]}\n2- CPF: {cpf}\n3- Data de nascimento: {dados_cliente["data_nascimento"]}\n4- Telefone fixo: {dados_cliente["telefone_fixo"]}\n5- Telefone celular: {dados_cliente["telefone_celular"]}\n6- Email: {dados_cliente["email"]}')
            mudanca = input('Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ').strip()
            while mudanca != '0':
                mudanca = validacao(mudanca, 1, dados_cliente)
                if mudanca == '1':
                    nome = input('Nome: ').strip().title()
                    dados_cliente[cpf]["nome"] = nome

                elif mudanca == '2':
                    cpf = input('CPF: ')
                    cpf_formatado = formatarCpf(cpf)
                    dados_cliente[cpf]["cpf"] = cpf_formatado

                elif mudanca == '3':
                    dt_nasc = input('Data de nascimento: ')
                    data_formatada = formatarData(dt_nasc)
                    dados_cliente[cpf]["data_nascimento"] = data_formatada

                elif mudanca == '4': 
                    telefone_fixo = input('Telefone fixo: ')
                    dados_cliente[cpf]["telefone_fixo"] = telefone_fixo

                elif mudanca == '5':
                    celular = input('Celular: ')
                    dados_cliente[cpf]["telefone_celular"] = celular

                elif mudanca == '6':
                    email = input('Email: ')
                    dados_cliente[cpf]["email"] = email



def principal():
    clear_console()
    menuPrincipal()

#Programa principal
principal()