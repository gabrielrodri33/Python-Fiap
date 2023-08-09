def tamanho_lista():
    print("*- TAMANHO da LISTA -*")
    print("----------------------")
    t = int(input("Tamanho: "))
    return t

def criar_lista(tamanho):
    print("*- CRIAR uma LISTA -*")
    print("---------------------")
    lista = []
    i = 0
    while i < tamanho:
        n = int(input("Número: "))
        lista.append(n)
        i += 1
    return lista

def imprimir_lista(lista):
    print("*- IMPRIMIR a LISTA -*")
    print("----------------------")
    for i in lista:
        print(f"Elemento: {i}")

def principal():
    print("*- PROGRAMA PRINCIPAL -*")
    print("------------------------")
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir_lista(lista)

principal()