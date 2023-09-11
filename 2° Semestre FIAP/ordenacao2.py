#função para realizar a mesma coisa do arquivo anterior
def troca(s, i, j):
    s[i], s[j] = s[j], s[i]
    return print(s)

lista = [10, 40, 30, 20, 50]
troca(lista, 1, 3)
