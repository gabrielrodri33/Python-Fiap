#Manipulação de listas com funções

'''
1- Função para obter o tamanho da lista - tamanho_lista()
2- Função para criar a lista - criar_lista()
3- Função para imprimir a lista - imprimir_lista()
4- Função para imprimir os elementos pares da lista - lista_par()
5- Função para imprimir os elementos ímpares da lista - lista_impar()
6- Função para separar os elementos pares da lista - separar_par()
7- Função para separar os elementos ímpares da lista - separar_impar()
8- Função que verifica a ocorrência de um determinado número - ocorrencia()
9- Funçã que obtem um número - obter_numero()
'''

def tamanho_lista():
    print("*- TAMANHO da LISTA -*")
    print("-="*15)

    t = int(input("Tamanho da lista: "))
    return t

def criar_lista(t):
    print("*- CRIAR uma LISTA -*")
    print("-="*15)
    lista = [] #lista vazia
    i = 0
    while i < t:
        n = int(input("Número: "))
        lista.append(n)
        i += 1
    return lista

def imprimir(lista):
    print("*- IMPRIMIR uma LISTA -*")
    print("-="*15)

    for i in lista:
        print(f"Elemento: {i}")

def lista_par(par):
    print('-* NÚMEROS PARES -*')
    i = len(par)
    c = 0
    while c < i:
        if (par[c] % 2) == 0:
            print(par[c], end=" ")
        c += 1

#Programa principa
t = tamanho_lista()
lista = criar_lista(t)
print(lista_par(lista))
imprimir(lista)
