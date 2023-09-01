import os
import copy
import time

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

def imprimirTabuleiro(tabuleiro):
    separador(18, 1)
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def imprimeMenuPrincipal():
    separador(28, 1)
    modoDeJogo = input(" xox JOGO DA VELHA xox\nDigite o número de acordo com o modo do jogo desejado:\n1- Jogador Vs. Máquina\n2- Jogador Vs. Jogador\n")
    modoDeJogo = validacao_dados(modoDeJogo, 1)
    return modoDeJogo

def modoJogador():
    m = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    win_player1 = win_player2 = 0
    matriz = copy.deepcopy(m)
    player1 = input("Digite o nome do jogador 1: ")
    player2 = input("Digite o nome do jogador 2: ")
    current_player = player1
    clear_console()

    while True:
        separador(18, 1)
        imprimePontuacao(player1, player2, win_player1, win_player2)
        imprimirTabuleiro(matriz)
        linha = leiaCoordenadaLinha(current_player)
        coluna = leiaCoordenadaColuna(current_player)
        if posicaoValida(linha, coluna, matriz) == True:
            if current_player == player1:
                jogar(matriz, linha, coluna, "X")
                if verificar_vencedor(matriz, "X"):
                    imprimePontuacao(player1, player2, win_player1, win_player2)
                    imprimirTabuleiro(matriz)
                    print(f"Jogador {player1} venceu!")
                    win_player1 += 1
                    matriz = copy.deepcopy(m)
                else:
                    current_player = player2

            else:
                jogar(matriz, linha, coluna, "O")
                if verificar_vencedor(matriz, "O"):
                    imprimePontuacao(player1, player2, win_player1, win_player2)
                    imprimirTabuleiro(matriz)
                    print(f"Jogador {player2} venceu!")
                    win_player2 += 1
                    matriz = copy.deepcopy(m)
                else:
                    current_player = player1
                
            if verificarVelha(matriz) == True:
                imprimePontuacao(player1, player2, win_player1, win_player2)
                imprimirTabuleiro(matriz)
                print("Velha! Reiniciando o jogo...")
                matriz = copy.deepcopy(m)
                time.sleep(2)
                clear_console()

        else:
            while matriz[linha][coluna] != " ":
                print("\033[91mPosição inválida!\033[0m")
                linha = leiaCoordenadaLinha(current_player)
                coluna = leiaCoordenadaColuna(current_player)
            if current_player == player1:
                jogar(matriz, linha, coluna, "X")
                if verificar_vencedor(matriz, "X") == True:
                    imprimePontuacao(player1, player2, win_player1, win_player2)
                    imprimirTabuleiro(matriz)
                    print(f"Jogador {player2} venceu!")
                    win_player1 += 1
                    matriz = copy.deepcopy(m)
                else:
                    current_player = player2
            else:
                jogar(matriz, linha, coluna, "O")
                if verificar_vencedor(matriz, "O") == True:
                    imprimePontuacao(player1, player2, win_player1, win_player2)
                    imprimirTabuleiro(matriz)
                    print(f"Jogador {player2} venceu!")
                    win_player2 += 1
                    matriz = copy.deepcopy(m)
                else:
                    current_player = player1
            
            if verificarVelha(matriz) == True:
                imprimePontuacao(player1, player2, win_player1, win_player2)
                imprimirTabuleiro(matriz)
                print("\033[93mVelha! Reiniciando o jogo...\033[0m")
                matriz = copy.deepcopy(m)
                time.sleep(2)
                clear_console()
        
        if win_player1 == 3 or win_player2 == 3:
            break
        
        clear_console()

def jogar(matriz, linha, coluna, x):
    matriz[linha][coluna] = x

def leiaCoordenadaLinha(player):
    coordenada_linha = input(f"{player} escolha uma linha (0, 1, 2): ")
    coordenada_linha = validacao_dados(coordenada_linha, 2)
    return int(coordenada_linha)

def leiaCoordenadaColuna(player):
    coordenada_coluna = input(f"{player} escolha uma coluna (0, 1, 2): ")
    coordenada_coluna = validacao_dados(coordenada_coluna, 2)
    return int(coordenada_coluna)

def posicaoValida(linha, coluna, m):
    if m[linha][coluna] == " ":
        return True
    else:
        return False

#Função para verificar se 
def verificar_vencedor(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True

        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def verificarVelha(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            if elemento == " ":
                return False
    return True

#Função para imprimir a pontuação do jogador
def imprimePontuacao(player1, player2, win_player1, win_player2):
    print(f"{player1}: {win_player1}       {player2}: {win_player2}")

def modoFacil():
    print()

def principal():
    modo = imprimeMenuPrincipal()
    if modo == "1":
        clear_console()
        separador(28, 2)
        print("Jogador vs. Máquina")
        modoFacil()
    else:
        clear_console()
        separador(28, 2)
        print("Jogador vs. jogador")
        modoJogador()

# Programa principal
principal()