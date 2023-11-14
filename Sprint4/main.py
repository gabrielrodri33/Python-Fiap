import db
import bcrypt
import json
import base64
import getpass
import datetime
import os
import re
import webbrowser
import random
from api import viacep
from api import cellerecpf
import time

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
    
    elif dado == 5:
        status = False
        while not status:
            try:
                separador(30, 1)
                centralizar("Menu principal!", 60)
                separador(30, 1)
                option = int(input('Verifique as informações!\nSe correto digite 0, caso contrário 1: '))

                if option == 1 or option == 0:
                    status = True

                else:
                    clear_console()
                    separador(30, 1)
                    separador("Entrada inválida!", 7)
                    print("Por favor escolha 0 ou 1!")

            except ValueError:
                clear_console()
                separador(30, 1)
                separador("Entrada inválida!", 7)
                print("Por favor insira um número")

    elif dado == 6:
        while not status:
            try:
                separador(30, 1)
                centralizar("Menu principal!", 60)
                separador(30, 1)
                option = int(input('1- Fazer seguro de bike!\n2- Saber informações do seguro\n3- Termos de segurança e privacidade\n4- Suporte\n5- Sair\n'))

                if 1 <= option <= 5:
                    status = True

                else:
                    clear_console()
                    separador(30, 1)
                    separador("Entrada inválida!", 7)
                    print("Por favor escolha uma opção de 1 a 6!")
                
                if option == 1:
                    option = 3
                elif option == 2:
                    option = 4
                elif option == 3:
                    option = 5
                elif option == 4:
                    option = 6
                elif option == 5:
                    option = 7
                    
            except ValueError:
                clear_console()
                separador(30, 1)
                separador("Entrada inválida!", 7)
                print("Por favor insira um número")
    
    elif dado == 7:
        status = False
        while not status:
            try:
                option = int(input('Verifique as informações!\nSe correto digite 0, caso contrário 1: '))

                if option == 1 or option == 0:
                    status = True

                else:
                    clear_console()
                    separador(30, 1)
                    separador("Entrada inválida!", 7)
                    print("Por favor escolha 0 ou 1!")

            except ValueError:
                clear_console()
                separador(30, 1)
                separador("Entrada inválida!", 7)
                print("Por favor insira um número")
    
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

def add_dict_endereco(dicionario, logradouro, bairro, localidade, uf, complemento, numero):
    dicionario = {
        'logradouro': logradouro,
        'bairro': bairro,
        'localidade': localidade,
        'uf': uf,
        'complemento': complemento,
        'numero': numero
    }

    print(dicionario)
    return dicionario

def formatarCpf():

    while True:
        cpf = input("CPF: ")
        while len(cpf) != 11:
            separador('CPF inválido!', 6)
            cpf = input(f'Deve conter 11 caracteres\nDigite seu CPF: ').replace('.', '').replace('-', '').replace(' ', '')

        cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        
        if db.verifica_cpf_existente(cpf):
            verifica = False
        else:
            verifica = True

        consulta = cellerecpf.consultaCpf(cpf)
        if consulta == True and verifica == True:
            break

    return cpf

def pwd():
    while True:
        password = getpass.getpass("Senha: ").encode("utf-8")
        confirm_password = getpass.getpass("Confirmar senha: ").encode("utf-8")

        if password == confirm_password and 8 <= len(password) <= 20 and any(char.isdigit() for char in password.decode("utf-8")) and any(char.islower() for char in password.decode("utf-8")) and any(char.isupper() for char in password.decode("utf-8")):
            code = base64.b64encode(password).decode('utf-8')
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            return hashed, code
        else:
            separador("Senha inválida! Certifique-se de que ela tenha entre 8 e 20 caracteres, contenha pelo menos um número e uma letra maiúscula e minúscula.", 7)

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

    email = update_cliente(dados_cliente, cpf)

    return cpf, email
    

def cadastroEndereco(cpf):
    endereco_cliente = {}
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
            endereco_cliente = add_dict_endereco(endereco_cliente, logradouro, bairro, localidade, uf, complemento, numero)
            break
        atualizacao_txt("Endereço cadastrado", cpf)


    db.insertEndereco(cpf, logradouro, bairro, numero, complemento, localidade, uf, cep)

    return endereco_cliente
    
def update_cliente(dados_cliente, cpf):
    mudanca = ""
    while mudanca != 0:
        # clear_console()
        separador(30, 2)
        centralizar("Informações de Cadastro", 60)
        separador(30, 2)
        print(f'1- Nome: {dados_cliente["nome"]}\n2- Data de nascimento: {dados_cliente["data_nascimento"]}\n3- Telefone fixo: {dados_cliente["telefone_fixo"]}\n4- Telefone celular: {dados_cliente["telefone_celular"]}\n5- Email: {dados_cliente["email"]}')
        mudanca = validacao(2)
        match mudanca:
            case 1:
                dados_cliente["nome"] = input('Nome: ').strip().title()
                db.update("cliente", "nome", dados_cliente["nome"], cpf)
                atualizacao_txt("Nome atualizado", dados_cliente["nome"])
            case 2:
                dados_cliente["data_nascimento"] = formatarData()
                db.updateDate("cliente", "dt_nasc", dados_cliente["data_nascimento"], cpf)
                atualizacao_txt("Data de nascimento atualizada", dados_cliente["data_nascimento"])

            case 3:
                dados_cliente["telefone_fixo"] = formatarTelefone()
                db.update("cliente", "tel_fixo", dados_cliente["telefone_fixo"], cpf)
                atualizacao_txt("Telefone fixo atualizado", dados_cliente["telefone_fixo"])

            case 4:
                dados_cliente["telefone_celular"] = formatarCell()
                db.update("cliente", "tel_celular", dados_cliente["telefone_celular"], cpf)
                atualizacao_txt("Telefone celular atualizado", dados_cliente["telefone_celular"])
            
            case 5:
                dados_cliente["email"] = validaEmail()
                db.update("cliente", "email", dados_cliente["email"], cpf)
                atualizacao_txt("Email atualizado", dados_cliente["email"])
    return dados_cliente["email"]

def update_endereco(endereco_cliente, cpf):
    mudanca = ""
    while mudanca != 0:
        clear_console()
        separador(30, 2)
        centralizar("Informações de Endereço", 60)
        separador(30, 2)
        print(f'Logradouro: {endereco_cliente["logradouro"]}\nBairro: {endereco_cliente["bairro"]}\nLocalidade: {endereco_cliente["localidade"]}\nUF: {endereco_cliente["uf"]}\nComplemento: {endereco_cliente["complemento"]}\nNúmero: {endereco_cliente["numero"]}')
        mudanca = validacao(7)
        match mudanca:
            case 1:
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
                    db.delete_endereco(cpf)
                    db.insertEndereco(cpf, logradouro, bairro, numero, complemento, localidade, uf, cep)
                    break
                atualizacao_txt("Endereço atualizado", cpf)
                
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
        option = validacao(6)
    senha = ""
    return  option, login, email

def formata_valor():
    while True:
        try:
            valor = int(input("Valor: R$"))
            valor = round(valor, 2)
            valor_str = '{:,}'.format(int(valor))
            if valor == int(valor):
                valor_str += '.00'
            else:
                valor_str += '.' + '{:02d}'.format(int(valor % 1 * 100))
            return 'R$' + valor_str
        except ValueError:
            separador("Insira um número válido!", 7)

def cadastro_bike(email):
    clear_console()
    separador(30, 3)
    centralizar('Cadastro de bike!', 60)
    separador(30, 3)
    nome = input("Modelo: ")
    valor_aprox = formata_valor()
    num_serie = input("Número de série: ")
    cor = input("Cor: ")
    obs = input("Observação: ")
    cpf = db.get_cpf_from_email(email)
    id_modelo = db.insert_bike_modelo(nome, valor_aprox, cor, num_serie, obs, cpf)
    dados_bike = {
        'modelo': nome,
        'valor_aprox': valor_aprox,
        'num_serie': num_serie,
        'cor': cor,
        'obs': obs
    }
    atualizacao_txt("Bike Cadastrada!", id_modelo)
    update_bike(dados_bike, id_modelo)
    simulacao_vistoria(dados_bike["num_serie"], cpf)

def simulacao_vistoria(num_serie, cpf):
    
    url = "https://prototipo-od.vercel.app"
    webbrowser.open(url)

    situacao = random.randint(1, 2)
    if situacao == 1:
        aprov = 'S'
        print("Seguro da bike aprovado!")
    else:
        aprov = 'N'
        print("Seguro da bike recusado!")

    db.insert_vistoria(aprov, num_serie, cpf)

def update_bike(dados_bike, modelo_id):
    mudanca = ""
    while mudanca != 0:
        separador(30, 2)
        centralizar("Atualização de Informações da Bicicleta", 60)
        separador(30, 2)
        print(f'1- Modelo: {dados_bike["modelo"]}\n2- Valor Aproximado: {dados_bike["valor_aprox"]}\n3- Cor: {dados_bike["cor"]}\n4- Número de Série: {dados_bike["num_serie"]}\n5- Observação: {dados_bike["obs"]}')
        mudanca = validacao(2)
        match mudanca:
            case 1:
                dados_bike["modelo"] = input('Novo modelo: ').strip().title()
                db.update_bike("bike_modelos", "nome", dados_bike["modelo"], modelo_id)
                atualizacao_txt("Modelo atualizado", dados_bike["modelo"])
            case 2:
                dados_bike["valor_aprox"] = formata_valor()
                db.update_bike("bike_modelos", "valor_aprox", dados_bike["valor_aprox"], modelo_id)
                atualizacao_txt("Valor Aproximado atualizado", dados_bike["valor_aprox"])
            case 3:
                dados_bike["cor"] = input('Nova cor: ').strip().title()
                db.update_bike("bike_modelos", "cor", dados_bike["cor"], modelo_id)
                atualizacao_txt("Cor atualizada", dados_bike["cor"])
            case 4:
                dados_bike["num_serie"] = input('Novo número de série: ').strip().upper()
                db.update_bike("bike_modelos", "num_serie", dados_bike["num_serie"], modelo_id)
                atualizacao_txt("Número de Série atualizado", dados_bike["num_serie"])
            case 5:
                dados_bike["obs"] = input('Nova observação: ')
                db.update_bike("bike_modelos", "obs", dados_bike["obs"], modelo_id)
                atualizacao_txt("Observação atualizada", dados_bike["obs"])
    return dados_bike

def menuPrincipal():
    option = validacao(1)
    clear_console()
    # status = False
    login = False
    while True:
        match option:
            case 1:
                option, login, email = login_user()
                    
            case 2:
                if login == True:
                    print("Você já está logado")
                    option = validacao(6)
                else:
                    cpf, email = cadastroCliente()
                    endereco_cliente = cadastroEndereco(cpf)
                    update_endereco(endereco_cliente, cpf)
                    print("Redirecionando para seguro de bike!")
                    time.sleep(3)
                    option = 3

            case 3:
                if login:
                    cadastro_bike(email)
                else:
                    separador(30,3)
                    centralizar("É neccesário estar logado!", 60)
                    option = 1
                
                if option == 1:
                    pass
                else:
                    break
            
            case 4:
                separador(80, 2)
                centralizar("Informações de seguro!", 160)
                separador(80, 2)
                print('Bem-vindo ao nosso Seguro de Bicicleta, uma maneira simples e segura de proteger sua bicicleta contra imprevistos. Na Porto Seguro, compreendemos o valor que sua bicicleta tem para você, seja para o lazer ou para deslocamentos diários. Com nosso seguro de bicicleta, você pode pedalar com tranquilidade, sabendo que está protegido.\n\nPor que escolher o Seguro de Bicicleta da Porto Seguro:\n\n- Cobertura Abrangente: Nosso seguro oferece cobertura contra roubo, furto qualificado e danos acidentais à sua bicicleta.\n- Ampla Rede de Oficinas Parceiras: Trabalhamos com uma ampla rede de oficinas especializadas para garantir o melhor atendimento em caso de reparos.\n- Cobertura em Todo o Brasil: Esteja você pedalando na cidade ou explorando trilhas, nosso seguro oferece cobertura em todo o território nacional.\n- Facilidade de Contratação: Você pode adquirir seu seguro de bicicleta de forma rápida e descomplicada, diretamente pelo aplicativo.')
                break

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