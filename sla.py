def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(elemento == jogador for elemento in linha):
            return True

    for coluna in range(len(tabuleiro)):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(len(tabuleiro))):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(len(tabuleiro))):
        return True

    if all(tabuleiro[i][len(tabuleiro) - 1 - i] == jogador for i in range(len(tabuleiro))):
        return True

    return False

def jogar_jogo():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vencedor(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break

            jogador_atual = "X" if jogador_atual == "O" else "O"
        else:
            print("Essa posição já está ocupada. Escolha outra posição.")

jogar_jogo()