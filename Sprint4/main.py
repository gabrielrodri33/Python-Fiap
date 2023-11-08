import db
# import neverbounce_sdk
import bcrypt
import json
import base64
import getpass
import datetime
import os
import re
import webbrowser
from api import viacep

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
                    print("Por favor escolha uma opção de 1 a 7!")

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

                if 1 <= mudanca <=7:
                    status = True
            except ValueError as e:
                print(f"Error: {e}")

    elif dado == 3:
        while not status:
            try:
                separador(30, 3)
                option = input("Deseja fazer cadastro? [S/N] ").strip().upper()
                if option in ["S", "N"]:
                    status = True
            except ValueError as e:
                print(f"Error: {e}")

    elif dado == 4:
        while not status:
            try:
                option = input("Informações corretas? [S/N]").strip().upper()
                if option in ["S", "N"]:
                    status = True
            except ValueError as e:
                print(f"Error: {e}")


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

def pwd():
    password = getpass.getpass("Senha: ").encode("utf-8")
    confirm_password = getpass.getpass("Confirmar senha: ").encode("utf-8")

    while password != confirm_password:
        separador("Senhas diferentes!", 7)
        password = getpass.getpass("Senha: ").encode("utf-8")
        confirm_password = getpass.getpass("Confirmar senha: ").encode("utf-8") 

    code = base64.b64encode(password).decode('utf-8')

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed, code

def validaEmail():
    status = False
    verifica = False
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+'

    while True:
        email = input("Email: ")
        if re.match(regex, email):
            status = True
        else:
            separador("Email inválido!", 7)
            print("Exemplo: usuario@example.com")
            status = False
            
        if db.verifica_email_existente(email):
            verifica = False
        else:
            verifica = True
        
        if status == True and verifica == True:
            break

    return email

def logarEmail():
    status = False
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+'

    while status == False:
        email = input("Email: ")
        if re.match(regex, email):
            status = True
        else:
            separador("Email inválido!", 7)
            print("Exemplo: usuario@example.com")

    return email

def centralizar(texto):
    largura = 60
    texto_formatado = texto.center(largura)

    return print(texto_formatado)

def consultaCep():
    cep = input("Informe seu CEP!\nCaso não saiba apenas tecle ENTER!\nCEP: ").replace(" ", "").replace(".", "").replace("-", "")

    while len(cep) != 8 or not cep.isdigit():
        separador("Inválido!", 7)
        cep = input("Informe seu CEP!\nCaso não saiba apenas tecle ENTER!\nCEP: ").replace(" ", "").replace(".", "").replace("-", "")
    
    if cep == "":
        link = "https://buscacepinter.correios.com.br/app/endereco/index.php"
        webbrowser.open(link)
        cep = input("CEP: ")
    
    cep, dic = viacep.cep(cep)

    return cep, dic

def menuPrincipal():
    option = validacao(1)
    clear_console()
    status = False
    login = False
    while True:
        match option:
            case 1:
                c = 0
                dados_login = carregarLista("clientes.json")
                while status == False:
                    separador(30, 3)
                    email = logarEmail()
                    senha = getpass.getpass("Senha: ").encode("utf-8")
                    senha = base64.b64encode(senha).decode("utf-8")
                    
                    if email in dados_login and dados_login[email] == senha:
                        status = True
                        login = True
                    else:
                        clear_console()
                        separador(30, 3)
                        separador("Email ou senha incorretos!", 7)
                        c += 1
                
                    if c == 3:
                        print("Limite de tentativas atingido!")
                        option = validacao(3)
                        if option == "S":
                            option = 2
                            print(option)

                email = ""
                senha = ""
                if status == True:
                    clear_console()
                    separador(30,1)
                    centralizar("Logado!")
                    option = validacao(1)
                    

            case 2:
                dados_cliente = {}
                clear_console()
                separador(30, 3)
                nome = input("Nome: ")
                email = validaEmail()
                senha, code = pwd()

                salvarCredenciais(email, code)
                cpf = formatarCpf()
                dt_nasc = formatarData()
                tel_fixo = formatarTelefone()
                tel_celular = formatarCell()
                db.insert(cpf, nome, dt_nasc, tel_fixo, tel_celular, email, senha)
                dados_cliente = addDict(dados_cliente, nome, email, dt_nasc, tel_fixo, tel_celular, cpf)

                clear_console()
                separador(30,3)
                while True:
                    cep, endereco = consultaCep()
                    logradouro = endereco['logradouro']
                    bairro = endereco['bairro']
                    localidade = endereco['localidade']
                    uf = endereco['uf']

                    print(f'Logradouro: {logradouro}')
                    print(f'Bairro: {bairro}')
                    print(f'Localidade: {localidade}')
                    print(f'uf: {uf}')
                    correto = validacao(3)
                    if correto == "S":
                        complemento = input("Complemento (opcional): ")
                        numero = input("Número (opcional): ")
                        print(cep)
                        break
                db.insertEndereco(cpf, logradouro, bairro, numero, complemento, localidade, uf, cep)
                
                break
                    

                # clear_console()
                # separador(30, 2)
                # print(f'1- Nome: {dados_cliente["nome"]}\n2- CPF: {cpf}\n3- Data de nascimento: {dados_cliente["data_nascimento"]}\n4- Telefone fixo: {dados_cliente["telefone_fixo"]}\n5- Telefone celular: {dados_cliente["telefone_celular"]}\n6- Email: {dados_cliente["email"]}')
                # mudanca = input('Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ').strip()
                # while mudanca != '0':
                #     mudanca = validacao(mudanca, 1, dados_cliente)
                #     if mudanca == '1':
                #         nome = input('Nome: ').strip().title()
                #         dados_cliente[cpf]["nome"] = nome

                #     elif mudanca == '2':
                #         cpf = input('CPF: ')
                #         cpf_formatado = formatarCpf(cpf)
                #         dados_cliente[cpf]["cpf"] = cpf_formatado

                #     elif mudanca == '3':
                #         dt_nasc = input('Data de nascimento: ')
                #         data_formatada = formatarData(dt_nasc)
                #         dados_cliente[cpf]["data_nascimento"] = data_formatada

                #     elif mudanca == '4': 
                #         telefone_fixo = input('Telefone fixo: ')
                #         dados_cliente[cpf]["telefone_fixo"] = telefone_fixo

                #     elif mudanca == '5':
                #         celular = input('Celular: ')
                #         dados_cliente[cpf]["telefone_celular"] = celular

                #     elif mudanca == '6':
                #         email = input('Email: ')
                #         dados_cliente[cpf]["email"] = email

            case 3:
                if login:
                    pass
                else:
                    separador(30,3)
                    print("É neccesário estar logado!")
                    option = 1




def principal():
    clear_console()
    menuPrincipal()

#Programa principal
principal()