import random
import string
import time

#Função para printar um separador decorativo
def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'},
        5: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
    }
    #separador do menu
    if cor == 1:
        mensagem = print(f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n)
    #separador do if de ONG
    elif cor == 2:
        mensagem = print(f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n)
    #separador do if de empresas
    elif cor == 3:
        mensagem = print(f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n)
    #separador do if de doação
    elif cor == 5:
        mensagem = print(f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n)
    else:
        mensagem = print(f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n)
    return mensagem

#cada opção selecionada no menu há uma cor para indicar em qual "seção" está. Essa função serve para escolher a cor do separador 
def cor_separador(cor):
    if cor == '1':
        separador(35, 2)
    elif cor == '2':
        separador(35, 3)
    elif cor == '3':
        separador(35, 4)

#Função de validação para respostas de "s" ou "n"
def validacao_s_n(val, mensagem):
    while val != "s" and val != "n":
        separador(35, 5)
        print(f'{cor["vermelho"]}Opção inválida!{cor["limpa"]}')
        val = input(mensagem).lower().strip()
        separador(35, 5)
    return val

#Função utilizada para escolher a opção de cadastro
def validacao_oe():
    separador(50, 1)
    val = input("Bem vindo à nossa plataforma!\nAqui efetuamos um cadastro no qual encontraremos a melhor opção para sua empresa ou ONG!\nNossos serviços também possibilitam a doação de dinheiro através de pix!\nDigite a opção correspondente para seu cadastro ↓\n1- ONG\n2- Empresa\n3- Doação\n")
    while val != '1' and val != '2' and val != '3':
        separador(50, 1)
        val = input('Opção inválida\n1- ONG\n2- Empresa\n3- Doação\n').strip()
        separador(50, 1)
    return val

#Função para imprimir os dados de acordo com a opção de cadastro selecionada
def cpf_or_cnpj(m, nome, email, senha, celular, proposta, cpf_cnpj):
    if m == '1':
        cor_separador(m)
        print(f'1- ONG: {nome}')
    elif m == '2':
        cor_separador(m)
        print(f'1- Nome da empresa: {nome}')
    else:
        cor_separador(m)
        print(f'1- Nome:{nome}')
    
    if m == '1' or m == '2':
        print(f"2- Email: {email}\n3- Senha: {senha}\n4- Celular: {celular}\n5- CNPJ: {cpf_cnpj}\n6- Proposta: {proposta}")
        cor_separador(m)
    else:
        print(f"2- Email: {email}\n3- Senha: {senha}\n4- Celular: {celular}\n5- CPF: {cpf_cnpj}")
        cor_separador(m)
    return m

#Função para troca de informações de cadastro
def troca(m):
    m = validacao_s_n(input("Deseja trocar alguma informação? [S/N] ").strip().lower(), "Deseja trocar alguma informação? [S/N] ").lower().strip()
    return m

#Função para validar a escolha do usuario para trocar algum item
def validacao_escolha(m, nome, email, senha, celular, proposta, cpf_cnpj, c):
    if c == 0:
        cpf_or_cnpj(m, nome, email, senha, celular, proposta, cpf_cnpj)
        esc = input('Qual item a cima deseja trocar? ').strip().lower()
        while esc != '1' and esc !='2' and esc != '3' and esc != '4' and esc != '5' and esc != '6':
            separador(35, 5)
            print(f'{cor["vermelho"]}Opção inválida!{cor["limpa"]}')
            cpf_or_cnpj(m, nome, email, senha, celular, proposta, cpf_cnpj)
            esc = input('Qual item a cima deseja trocar? ').strip().lower()
            separador(35, 5)
        return esc
    
    elif c == 1:
        cpf_or_cnpj(m, nome, email, senha, celular, proposta, cpf_cnpj)
        esc = input('Deseja trocar mais algum item? [S/N] ').strip().lower()
        if esc != 's' and esc != 'n':
            esc = validacao_s_n(esc, 'Deseja trocar mais algum item? [S/N] ')

        if esc == 's':
            cor_separador(m)
            cpf_or_cnpj(m, nome, email, senha, celular, proposta, cpf_cnpj)
            esc = input('Qual item a cima deseja trocar? ').strip().lower()
            while esc != '1' and esc !='2' and esc != '3' and esc != '4' and esc != '5' and esc != '6':
                separador(35, 5)
                print(f'{cor["vermelho"]}Opção inválida!{cor["limpa"]}')
                esc = input('Qual item a cima deseja trocar? ').strip().lower()
                separador(35, 5)
            return esc
        
        elif esc == 'n':
            return esc

#funcao para caso seja a opção 3, ir para parte de pagamento
def forma_pagamento(pagamento, rs):
    if pagamento == '1' or pagamento == '2':
        nome = input('Nome do titular: ')
        numero = input('Número do cartão: ')
        val = input('Validade: ')
        cvv = input('CVV: ')
        print(f'Pagamento de R${rs:.2f} confirmado! Muito obrigado pela sua doação!')
    elif pagamento == '3':
        for c in range (32):
            caractere_aleatorio = random.choice(string.ascii_letters + string.digits)
            print(caractere_aleatorio, end='', flush= True)
            time.sleep(0.05)
        print('\nConfirmando o pagamento...')
        time.sleep(4)
        print(f'Pagamento de R${rs:.2f} confirmado! Muito obrigado pela sua doação!')

#Função para definir o fim do programa, para qual rumo ele toma
def propostas(n):
    if n == 1:
        separador(35, ong_or_empresa)
        empresa_aleatoria = random.choice(empresas)
        print('Analisamos todas as empresas cadastradas em nossa plataforma e essa foi a melhor opção para sua ONG!')
        print(f"================= {empresa_aleatoria['titulo']} =================")
        print("Empresa:", empresa_aleatoria['empresa'])
        print("ONG:", empresa_aleatoria['ong'])
        print("Título:", empresa_aleatoria['titulo'])
        print("Descrição:", empresa_aleatoria['descricao'])
        print("Objetivos:")
        for objetivo in empresa_aleatoria['objetivos']:
            print("- ", objetivo)
        print("Benefícios:")
        for beneficio in empresa_aleatoria['beneficios']:
            print("- ", beneficio)
        separador(35, ong_or_empresa)

    elif n == 2:
        separador(35, ong_or_empresa)
        proposta_aleatoria = random.choice(ong)
        print('Analizamos todas as ONGs cadastradas em nossa plataforma e essa foi a melhor opção para sua empresa!')
        print(f"================= {proposta_aleatoria['titulo']} =================")
        print("ONG:", proposta_aleatoria['ong'])
        print("Título:", proposta_aleatoria['titulo'])
        print("Descrição:", proposta_aleatoria['descricao'])
        print("Objetivos:")
        for objetivo in proposta_aleatoria['objetivos']:
            print("- ", objetivo)
        print("Benefícios:")
        for beneficio in proposta_aleatoria['beneficios']:
            print("- ", beneficio)
        separador(35, ong_or_empresa)
    elif n == 3:
        separador(35, ong_or_empresa)
        valor = float(input('Qual valor deseja doar? R$'))
        pagamento = input('Forma de pagamento:\n1- Débito\n2- Crédito\n3- Pix\n')
        while pagamento != '1' and pagamento != '2' and pagamento != '3':
            separador(35, 5)
            pagamento = input(f'{cor["vermelho"]}Opção inválida!{cor["limpa"]}\n1- Débito\n2- Crédito\n3- Pix\n')
            separador(35, 5)
        forma_pagamento(pagamento, valor)

#Listas utilizadas no programa
cor = {'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul':'\033[36m', 'roxo' : '\033[35', 'limpa' : '\033[0m'}
cadastro = []
empresas = [
    {
        'empresa': 'Innovia',
        'ong': 'FomeZero',
        'titulo': 'Programa de combate à fome',
        'descricao': 'A Innovia, uma empresa inovadora e comprometida com o impacto social, apresenta uma proposta de parceria para apoiar o programa de combate à fome desenvolvido pela ONG FomeZero.',
        'objetivos': [
            'Distribuir cestas básicas para 500 famílias',
            'Criar hortas comunitárias',
            'Promover educação nutricional'
        ],
        'beneficios': [
            'Reconhecimento como parceira de um programa de impacto social',
            'Possibilidade de colaboração em ações de combate à fome',
            'Melhoria da imagem corporativa'
        ]
    },
    {
        'empresa': 'Elixir Industries',
        'ong': 'FomeZero',
        'titulo': 'Projeto de Sustentabilidade Alimentar',
        'descricao': 'A Elixir Industries, uma empresa comprometida com a sustentabilidade e a responsabilidade social, tem o prazer de apresentar uma proposta de parceria para apoiar o programa de combate à fome desenvolvido pela ONG FomeZero.',
        'objetivos': [
            'Implementar sistemas de reciclagem de alimentos para reduzir o desperdício e aproveitar recursos',
            'Criar programas de capacitação e geração de renda para comunidades carentes envolvendo a produção e comercialização de alimentos',
            'Promover ações de conscientização sobre a importância da alimentação sustentável'
        ],
        'beneficios': [
            'Reconhecimento como parceira de um projeto inovador e sustentável',
            'Fortalecimento da imagem corporativa como empresa comprometida com a responsabilidade social',
            'Oportunidade de envolvimento de colaboradores em ações voluntárias com impacto significativo'
        ]
    },
    {
        'empresa': 'Zephyr Enterprises',
        'ong': 'FomeZero',
        'titulo': 'Projeto de Erradicação da Fome',
        'descricao': 'A Zephyr Enterprises, uma empresa comprometida com a responsabilidade social e o combate à fome, tem o prazer de apresentar uma proposta de parceria para apoiar o projeto de erradicação da fome desenvolvido pela ONG FomeZero.',
        'objetivos': [
            'Implementar programas de distribuição de alimentos em larga escala',
            'Desenvolver iniciativas de capacitação e geração de renda para comunidades carentes',
            'Promover a conscientização sobre a importância da segurança alimentar'
        ],
        'beneficios': [
            'Reconhecimento como parceira em um projeto de grande impacto social',
            'Fortalecimento da imagem corporativa como empresa comprometida com a responsabilidade social',
            'Possibilidade de desenvolver soluções inovadoras e sustentáveis para o combate à fome'
        ]   
    },
    {
        'empresa': 'Pulse Tech',
        'ong': 'FomeZero',
        'titulo': 'Projeto de Tecnologia para o Combate à Fome',
        'descricao': 'A Pulse Tech, uma empresa inovadora no ramo da tecnologia, está interessada em estabelecer uma parceria com a ONG FomeZero para desenvolver um projeto de tecnologia voltado para o combate à fome. Com o uso de soluções tecnológicas avançadas, pretendemos otimizar a distribuição de alimentos e facilitar o acesso das comunidades carentes a recursos alimentares essenciais.',
        'objetivos': [
            'Desenvolver um aplicativo de doações e distribuição de alimentos',
            'Implementar sistemas de logística inteligente para agilizar o transporte de alimentos',
            'Utilizar a análise de dados para identificar áreas de maior necessidade e direcionar os esforços de combate à fome'
        ],
        'beneficios': [
            'Reconhecimento como parceira em um projeto inovador e de impacto social',
            'Oportunidade de contribuir com soluções tecnológicas para um problema global',
            'Fortalecimento da imagem corporativa como empresa engajada com a responsabilidade social e a inovação'
        ]
    }
]

ong = {
    'ong': 'FomeZero',
    'titulo': 'Programa de combate à fome',
    'descricao': 'A ONG FomeZero está desenvolvendo um programa para combater a fome e a insegurança alimentar em comunidades carentes. A empresa patrocinadora terá a oportunidade de fazer a diferença na vida das pessoas, garantindo que tenham acesso a alimentos adequados e nutritivos.',
    'objetivos': [
        'Distribuir cestas básicas para 500 famílias',
        'Criar hortas comunitárias',
        'Promover educação nutricional'
    ],
    'beneficios': [
        'Reconhecimento como parceira de um programa de impacto social',
        'Possibilidade de colaboração em ações de combate à fome',
        'Melhoria da imagem corporativa'
    ]
},
{
    'ong': 'SaciarVidas',
    'titulo': 'Projeto de alimentação saudável',
    'descricao': 'A ONG SaciarVidas está empenhada em promover uma alimentação saudável e consciente para crianças e jovens de comunidades carentes. A empresa patrocinadora terá a oportunidade de apoiar um projeto que visa combater a desnutrição e proporcionar uma vida mais saudável para essas crianças.',
    'objetivos': [
        'Implementar programas de educação alimentar em escolas',
        'Oferecer refeições balanceadas e nutritivas para 200 crianças diariamente',
        'Realizar oficinas de culinária saudável'
    ],
    'beneficios': [
        'Participação ativa em um projeto social de impacto',
        'Visibilidade como empresa comprometida com a promoção da saúde',
        'Fortalecimento da responsabilidade social corporativa'
    ]
},
{
    'ong': 'PratoCheio',
    'titulo': 'Campanha de combate à fome',
    'descricao': 'A ONG PratoCheio tem como missão principal combater a fome e a desnutrição em comunidades carentes. Com a parceria da sua empresa, poderemos expandir nossos programas de distribuição de alimentos e ampliar nosso alcance, levando refeições nutritivas para um número maior de pessoas em situação de vulnerabilidade.',
    'objetivos': [
        'Aumentar a quantidade de refeições distribuídas mensalmente',
        'Criar redes de coleta de alimentos não utilizados',
        'Promover a conscientização sobre a importância da alimentação adequada'
    ],
    'beneficios': [
        'Contribuição direta no combate à fome e desnutrição',
        'Visibilidade como empresa engajada socialmente',
        'Oportunidade de envolver colaboradores em ações voluntárias'
    ]
},
{
    'ong': 'Pão e Compaixão',
    'titulo': 'Programa de Alimentação Solidária',
    'descricao': 'A ONG Pão e Compaixão trabalha incansavelmente para levar alimentos nutritivos e dignidade às pessoas em situação de vulnerabilidade social. Com o apoio da sua empresa, poderemos fortalecer nosso programa de Alimentação Solidária, ampliando o número de refeições oferecidas diariamente e expandindo nossas atividades para outras regiões carentes.',
    'objetivos': [
        'Ampliar o número de refeições oferecidas diariamente',
        'Implementar hortas comunitárias para promoção da segurança alimentar',
        'Capacitar e empoderar indivíduos em situação de vulnerabilidade'
    ],
    'beneficios': [
        'Contribuição direta para a redução da fome e da desigualdade social',
        'Fortalecimento da responsabilidade social da empresa',
        'Possibilidade de engajamento dos colaboradores em ações voluntárias'
    ]
},
{
    'ong': 'Alimentando Sonhos',
    'titulo': 'Projeto Educação Alimentar',
    'descricao': 'A ONG Alimentando Sonhos tem como missão promover a educação alimentar e o acesso a alimentos saudáveis para crianças em comunidades carentes. Com o apoio da sua empresa, poderemos expandir nossas atividades e alcançar um número maior de crianças, proporcionando-lhes uma base sólida de conhecimento sobre alimentação saudável e nutrição.',
    'objetivos': [
        'Realizar oficinas de educação alimentar em escolas e centros comunitários',
        'Distribuir kits de alimentos saudáveis para as famílias',
        'Promover a criação de hortas escolares'
    ],
    'beneficios': [
        'Contribuição para a melhoria da qualidade de vida das crianças e suas famílias',
        'Fortalecimento da imagem da empresa como agente de transformação social',
        'Possibilidade de envolvimento dos colaboradores em atividades voluntárias'
    ]
}

#Programa principal

#Menu pra selecionar o tipo de cadastro desejado
ong_or_empresa = validacao_oe()

cor_separador(ong_or_empresa)

email = input('Email: ').strip()
senha = input('Senha: ')
cell = input('Celular: ').strip()
cadastro.append([email, senha, cell])

match ong_or_empresa:
    case '1':
        nome = input('Nome da ONG: ').strip()
        cnpj_cpf = input('CNPJ: ').strip()
        proposta = input('Escreva um pouco sobre a sua proposta para seus futuros patrocinadores↓\n').strip()
        cadastro.append([nome, proposta, cnpj_cpf])
    case '2':
        nome = input('Nome da empresa: ').strip()
        cnpj_cpf = input('CNPJ: ').strip()
        proposta = input('Descreva sua empresa e seus objetivos em poucas palavras↓\n').strip()
        cadastro.append([nome, proposta, cnpj_cpf])
    case '3':
        nome = input('Nome: ').strip()
        cnpj_cpf = input('CPF: ').strip()
        proposta = ''
        cadastro.append([nome, proposta, cnpj_cpf,])
    case _:
        print('Opção inválida')
    
cor_separador(ong_or_empresa)

escolha = troca(ong_or_empresa)

c = 0

#Laço para trocar as informações que ele selecionar e quantas vezes o usuário quiser, caso o usuário queira
while escolha != 'n':
    escolha = validacao_escolha(ong_or_empresa, nome, email, senha, cell, proposta, cnpj_cpf, c)

    if escolha == '1':
        match ong_or_empresa:
            case '1':
                nome = input('Nome da ONG: ').strip()
                cadastro[1][0] = nome
                c = 1
            case '2':
                nome = input('Nome da empresa: ').strip()
                cadastro[1][0] = nome
                c = 1
            case '3':
                nome = input('Nome: ').strip()
                cadastro[1][0] = nome
                c = 1
            case _:
                print('Opção inválida!')

    elif escolha == '2':
        email = input("Email: ").strip()
        cadastro[0][0] = email
        c = 1

    elif escolha == '3':
        senha = input('Senha: ')
        cadastro[0][1] = senha
        c = 1

    elif escolha == '4':
        cell = input('Celular: ').strip()
        cadastro[0][2] = cell
        c = 1

    elif escolha == '5' and (ong_or_empresa == '1' or ong_or_empresa == '2'):
        cnpj_cpf = input('CNPJ: ').strip()
        cadastro[1][2] = cnpj_cpf
        c = 1

    elif escolha == '5' and ong_or_empresa == '3':
        cnpj_cpf = input("CPF: ").strip()
        cadastro[1][2] = cnpj_cpf
        c = 1
    
    elif escolha == '6':
        proposta = input('Proposta: ').strip()
        cadastro [1][1] = cnpj_cpf
        c = 1

if ong_or_empresa == '1':
    propostas(1)
elif ong_or_empresa == '2':
    propostas(2)
elif ong_or_empresa == '3':
    propostas(3)
