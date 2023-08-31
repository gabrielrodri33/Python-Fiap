import os

#Realizar um jogo da velha

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
    
    elif tipo == 2:
        while v != "0" and v != "1" and v != "2":
            v = input("OPÇÃO INVÁLIDA\nEscolha a linha (0, 1, 2): ")
        return int(v)
    
    elif tipo == 3:
        while v != "0" and v != "1" and v != "2":
            v = input("OPÇÃO INVÁLIDA\nEscolha a coluna (0, 1, 2): ")
        return int(v)


#Função para escolher o modo de jogo
def imprimeMenuPrincipal():
    separador(28, 1)
    modoDeJogo = input(" xox JOGO DA VELHA xox\nDigite o número de acordo com o modo do jogo desejado:\n1- Jogador Vs. Máquina\n2- Jogador Vs. Jogador\n")
    modoDeJogo = validacao_dados(modoDeJogo, 1)
    return modoDeJogo

#Função do modo de jogo vs máquina
def jogador_maquina():
    print('Vs. máquina')

#Função do modo de jogo vs jogador
def modoJogador(m):
    matriz = m.copy()
    player1 = input("Digite o nome do jogador 1: ")
    player2= input("Digite o nome do jogador 2: ")
    c=0
    player = player1
    while True:
        imprimirTabuleiro(matriz)
        linha = input(f"{player} escolha a linha (0, 1, 2): ")
        linha = validacao_dados(linha, 2)
        coluna = input(f"{player}, escolha a coluna (0, 1, 2): ")
        coluna = validacao_dados(coluna, 3)

        if player == player1 and matriz[linha][coluna] == " ":
            matriz[linha][coluna] = "X"
            if verificar_vencedor(matriz, player):
                print(f"Jogador {player} venceu!")
                break
        
        elif player == player2 and matriz[linha][coluna] == " ":
            matriz[linha][coluna] = "O"
            if verificar_vencedor(matriz, player):
                print(f"Jogador {player} venceu!")
                break

        else: 
            linha = input("\033[91mPosição inválida\033[0m, escolha a linha (0, 1, 2): ")
            linha = validacao_dados(linha, 2)
            coluna = input("\033[91mPosição inválida\033[0m, escolha a coluna (0, 1, 2): ")
            coluna = validacao_dados(coluna, 3)


        if player == player1:
            player = player2
        elif player == player2:
            player = player1
    
        clear_console()





def verificarVelha():
    print()

def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(elemento == jogador for elemento in linha):
            return True
    
    # Verificar colunas
    for coluna in range(len(tabuleiro)):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(len(tabuleiro))):
            return True
    
    # Verificar diagonal principal
    if all(tabuleiro[i][i] == jogador for i in range(len(tabuleiro))):
        return True
    
    # Verificar diagonal secundária
    if all(tabuleiro[i][len(tabuleiro) - 1 - i] == jogador for i in range(len(tabuleiro))):
        return True
    
    return False
    

def inicializarTabuleiro():
    matriz = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return matriz

def imprimirTabuleiro(tabuleiro):
    separador(18, 1)
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
        

#Função que chama todas as funções
def principal(m):
    modo = imprimeMenuPrincipal()
    if modo == "1":
        separador(28, 2)
        print("Modo de jogo selecionado!")
        jogador_maquina()
    else:
        modoJogador(m)

#Programa principal
principal(inicializarTabuleiro())