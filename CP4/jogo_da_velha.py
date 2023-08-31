import os

#Realizar um jogo da velha

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Função de cores
def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'},
        5: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
    }
        #separador do menu inicial
    if cor == 1:
        mensagem = print(f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n)
        #separador de vitória em cima da máquina
    elif cor == 2:
        mensagem = print(f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n)
        #separador do if de empresas
    elif cor == 3:
        mensagem = print(f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n)
        #separador derrota da máquina
    elif cor == 5:
        mensagem = print(f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n)
        #separador de empate de ambos modos de jogo
    else:
        mensagem = print(f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n)
    return mensagem

#Função para limpar o console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def validacao_dados(v, tipo):
    if tipo == 1:
        while v != "1" and v != "2":
            separador(28, 5)
            v = input("OPÇÃO INVÁLIDA!\nDigite o número de acordo com o modo do jogo desejado:\n1- Jogador Vs. Máquina\n2- Jogador Vs. Jogador\n")
            if v != "1" and v != "2":
                separador(28, 5)
        return v

#Função para escolher o modo de jogo
def escolher_modo():
    separador(28, 1)
    modoDeJogo = input(" xox JOGO DA VELHA xox\nDigite o número de acordo com o modo do jogo desejado:\n1- Jogador Vs. Máquina\n2- Jogador Vs. Jogador\n")
    modoDeJogo = validacao_dados(modoDeJogo, 1)
    return modoDeJogo

#Função do modo de jogo vs máquina
def jogador_maquina():
    print('Vs. máquina')

def jogador_jogador(m):
    matriz = m.copy()
    print(matriz)

#Função que chama todas as funções
def principal(m):
    modo = escolher_modo()
    if modo == "1":
        separador(28, 2)
        print("Modo de jogo selecionado!")
        jogador_maquina()
    else:
        jogador_jogador(m)

#Programa principal
principal(matriz)

print("OK!")