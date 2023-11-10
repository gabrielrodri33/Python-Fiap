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
from api import cellerecpf

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
                centralizar("Menu principal!", 60)
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
                print("Por favor insira um número")

    elif dado == 2:
        while not status:
            try:
                separador(30, 2)
                option = int(input('Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: '))

                if 0 <= option <=6:
                    status = True
                else:
                    clear_console()
                    separador(30, 1)
                    separador("Entrada inválida!", 7)
                    print("Por favor escolha uma opção de 1 a 6!")

            except ValueError:
                separador(30, 1)
                separador("Entrada inválida!", 7)
                print("Por favor insira um número")

    elif dado == 3:
        while not status:
            try:
                option = int(input("1- Fazer Cadastro\n2- Redefinir senha\n"))
                if option == 1 or option == 2:
                    status = True

            except ValueError as e:
                separador(30, 1)
                separador("Entrada inválida!", 7)
                print("Por favor insira um número")

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

    return f'{tel[:4]}-{tel[4:]}'

def salvarCredenciais(email, senha):
    try:
        dados_login = carregarLista("Sprint4/json/clientes.json")
    except FileNotFoundError:
        dados_login = {}

    dados_login[email] = senha

    with open("Sprint4/json/clientes.json", "w") as arquivo:
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
    while True:
        cpf = input("CPF: ")
        while len(cpf) != 11:
            separador('CPF inválido!', 6)
            cpf = input(f'Deve conter 11 caracteres\nDigite seu CPF: ').replace('.', '').replace('-', '').replace(' ', '')

        if len(cpf) == 11:
            break

        # consulta = cellerecpf.consultaCpf(cpf)
        # if consulta:
        #     break

    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def verifica_pwd(password):
    while len(password) < 8 or len(password) > 20 or not any(char.isdigit() for char in password) or not any(char.islower() for char in password) or not any(char.isupper() for char in password):
        separador("Erro!", 7)
        print("Senha deve conter:\n•Entre 8 e 20 caracteres.\n•Pelo menos um número.\n•Uma letra maiúscula e minúscula.")
        password = getpass.getpass("Digite uma senha entre 8 e 20 caracteres, que contenha pelo menos um número: ")
    return password

def pwd():
    password = getpass.getpass("Senha: ").encode("utf-8")        
    password = verifica_pwd(password)
    confirm_password = getpass.getpass("Confirmar senha: ").encode("utf-8")
    confirm_password = verifica_pwd(confirm_password)

    while password != confirm_password:
        separador("Senhas diferentes!", 7)
        password = getpass.getpass("Senha: ").encode("utf-8")
        password = verifica_pwd(password)
        confirm_password = getpass.getpass("Confirmar senha: ").encode("utf-8") 
        confirm_password = verifica_pwd(confirm_password)

    code = base64.b64encode(password).decode('utf-8')

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed, code

def validaEmail():
    status = False
    verifica = False
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+'

    while True:
        email = input("Email: ").lower().strip()
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
        email = input("Email: ").lower().strip()
        if re.match(regex, email):
            status = True
        else:
            separador("Email inválido!", 7)
            print("Exemplo: usuario@example.com")

    return email

def centralizar(texto, n):
    largura = n
    texto_formatado = texto.center(largura)

    return print(texto_formatado)

def consultaCep():
    cep = input("Informe seu CEP!\nCaso não saiba apenas tecle ENTER!\nCEP: ").replace(" ", "").replace(".", "").replace("-", "")

    if cep == "":
        link = "https://buscacepinter.correios.com.br/app/endereco/index.php"
        webbrowser.open(link)
        cep = input("CEP: ")
    
    while len(cep) != 8 or not cep.isdigit():
        separador("Inválido!", 7)
        cep = input("Informe seu CEP!\nCaso não saiba apenas tecle ENTER!\nCEP: ").replace(" ", "").replace(".", "").replace("-", "")
    
    cep, dic = viacep.cep(cep)

    return cep, dic

def cadastroCliente():
    dados_cliente = {}
    clear_console()
    separador(30, 3)
    centralizar("Cadastro", 60)
    separador(30, 3)
    nome = input("Nome: ").strip().title()
    email = validaEmail()
    senha, code = pwd()

    salvarCredenciais(email, code)
    cpf = formatarCpf()
    dt_nasc = formatarData()
    tel_fixo = formatarTelefone()
    tel_celular = formatarCell()
    db.insert(cpf, nome, dt_nasc, tel_fixo, tel_celular, email, senha)
    dados_cliente = addDict(dados_cliente, nome, email, dt_nasc, tel_fixo, tel_celular, cpf)
    atualizacao_txt("Cliente cadastrado", cpf)

    clear_console()

    return dados_cliente, cpf

def cadastroEndereco(cpf):
    while True:
        separador(30,3)
        centralizar("Endereço", 60)
        separador(30,3)
        cep, endereco = consultaCep()
        logradouro = endereco['logradouro']
        bairro = endereco['bairro']
        localidade = endereco['localidade']
        uf = endereco['uf']

        print(f'Logradouro: {logradouro}')
        print(f'Bairro: {bairro}')
        print(f'Localidade: {localidade}')
        print(f'uf: {uf}')
        correto = validacao(4)
        if correto == "S":
            complemento = input("Complemento (opcional): ")
            numero = input("Número (opcional): ")
            break
        atualizacao_txt("Endereço cadastrado", cpf)

    db.insertEndereco(cpf, logradouro, bairro, numero, complemento, localidade, uf, cep)
    
def updateCliente(dados_cliente, cpf):
    mudanca = ""
    while mudanca != 0:
        clear_console()
        separador(30, 2)
        centralizar("Informações de Cadastro", 60)
        separador(30, 2)
        print(f'1- Nome: {dados_cliente["nome"]}\n2- CPF: {cpf}\n3- Data de nascimento: {dados_cliente["data_nascimento"]}\n4- Telefone fixo: {dados_cliente["telefone_fixo"]}\n5- Telefone celular: {dados_cliente["telefone_celular"]}\n6- Email: {dados_cliente["email"]}')
        mudanca = validacao(2)
        match mudanca:
            case 1:
                dados_cliente["nome"] = input('Nome: ').strip().title()
                db.update("cliente", "nome", dados_cliente["nome"], cpf)
                atualizacao_txt("Nome atualizado", dados_cliente["nome"])
            case 2:
                dados_cliente["cpf"] = formatarCpf()
                db.update("cliente", "cpf", dados_cliente["cpf"], dados_cliente["cpf"])
                atualizacao_txt("CPF atualizado", dados_cliente["cpf"])
            case 3:
                dados_cliente["data_nascimento"] = formatarData()
                db.updateDate("cliente", "dt_nasc", dados_cliente["data_nascimento"], dados_cliente["cpf"])
                atualizacao_txt("Data de nascimento atualizada", dados_cliente["data_nascimento"])

            case 4:
                dados_cliente["telefone_fixo"] = formatarTelefone()
                db.update("cliente", "tel_fixo", dados_cliente["telefone_fixo"], dados_cliente["cpf"])
                atualizacao_txt("Telefone fixo atualizado", dados_cliente["telefone_fixo"])

            case 5:
                dados_cliente["telefone_celular"] = formatarCell()
                db.update("cliente", "tel_celular", dados_cliente["telefone_celular"], dados_cliente["cpf"])
                atualizacao_txt("Telefone celular atualizado", dados_cliente["telefone_celular"])
            
            case 6:
                dados_cliente["email"] = validaEmail()
                db.update("cliente", "email", dados_cliente["email"], dados_cliente["cpf"])
                atualizacao_txt("Email atualizado", dados_cliente["email"])
        break

def atualizacao_txt(info, info2):
    date = datetime.datetime.now()
    texto = f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n{info}: {info2}\nDia e hora: {date}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
    with open('Sprint4/archive/eventos.txt', 'a') as file:
        file.write(texto)

def login_user():
    status = False
    c = 0
    dados_login = carregarLista("Sprint4/json/clientes.json")
    while status == False:
        separador(30, 3)
        centralizar("Login", 60)
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
            clear_console()
            separador(30, 5)
            centralizar("Limite de tentativas atingido!", 60)
            separador(30, 5)
            option = validacao(3)
            if option == 1:
                option = 2

            else:
                email = logarEmail()
                senha, code = pwd()
                db.updatePwd("cliente", "senha", senha, email)
                
                with open("Sprint4/json/clientes.json", 'r') as arquivo:
                    dados_login = json.load(arquivo)

                dados_login[email] = code

                with open("Sprint4/json/clientes.json", 'w') as arquivo:
                    json.dump(dados_login, arquivo, indent=2)

                print(f'Valor da chave {email} alterado para {code}.')

                c = 0

    if status == True:
        clear_console()
        separador(30,1)
        centralizar("Logado!", 60)
        atualizacao_txt("Usuário logado", email)
        option = validacao(1)
    email = ""
    senha = ""
    return  option, login

def menuPrincipal():
    option = validacao(1)
    clear_console()
    # status = False
    login = False
    while True:
        match option:
            case 1:
                option, login = login_user()
                    
            case 2:
                if login == True:
                    pass
                else:
                    dados_cliente, cpf = cadastroCliente()
                    cadastroEndereco(cpf)
                    updateCliente(dados_cliente, cpf)
                    option = validacao(5)

            case 3:
                if login:
                    pass
                else:
                    separador(30,3)
                    print("É neccesário estar logado!")
                    option = 1
            
            case 5:
                url = 'https://www.portoseguro.com.br/conteudo/mobile/portoseguro/politica-de-privacidade.html'
                webbrowser.open(url)
                option = validacao(1)

            case 6:
                clear_console()
                separador(60, 6)
                centralizar("Suporte", 120)
                separador(60, 6)
                print('Bem vindo ao atendimento da Porto Seguro!')
                print("Atendente Virtual: Olá! Como posso ajudar você? Digite '1' para sair.")
                atendente()
                separador(60, 6)
                break
            case 7:
                break


def atendente():
    while True:
        pergunta = input('Você: ').lower()
        if 'cobertura' in pergunta:
            print('Atendente Virtual: Nossas coberturas incluem proteção contra roubo, danos acidentais e assistência 24 horas.')
        
        elif 'preco' in pergunta or 'custo' in pergunta or 'valor' in pergunta or 'preço' in pergunta:
            print('Atendente Virtual: O preço do seguro varia dependendo de vários fatores, como o valor da bicicleta e sua localização.')
        
        elif 'como contratar' in pergunta or 'como contrato' in pergunta or 'contrato' in pergunta:
            print('Atendente Virtual: Para contratar nosso seguro de bicicleta, você precisa realizar cadastro no nosso site ou aplicativo.')
        
        elif 'forma de pagamento' in pergunta or 'pagamento' in pergunta:
            print('Atendente Virtual: Formas de pagamento disóníveis: Débito, crédito, pix ou boleto')
        
        elif 'cancelar seguro' in pergunta or 'cancelar' in pergunta:
            print('Atendente Virtual: Para cancelar seu seguro de bicicleta, você pode seguir estas etapas:\n' \
                '1. Entre em contato com nosso serviço de atendimento ao cliente pelo telefone XXXX-XXXX.\n' \
                '2. Forneça as informações necessárias para identificar sua apólice, como número da apólice e dados pessoais.\n' \
                '3. Siga as instruções fornecidas pelo atendente para concluir o processo de cancelamento.\n' \
                'Lembre-se de que podem ser aplicadas políticas de cancelamento e taxas, dependendo dos termos de sua apólice.')

        elif pergunta == "1":
            break

        else:
            print('Atendente Virtual: Desculpe, não entendi a pergunta. Por favor, faça uma pergunta mais específica.')

        print("Atendente Virtual: Posso ajudar em mais alguma coisa?")


def principal():
    clear_console()
    menuPrincipal()

#Programa principal
principal()