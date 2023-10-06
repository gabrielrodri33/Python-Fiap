import random
import json

def salvarLista(nome, listas):
    with open(nome, "w") as arquivo:
        json.dump(listas, arquivo)

def carregarLista(nome):
    with open(nome, "r") as arquivo:
        return json.load(arquivo)

def geradorLista(tamLista):
    lista = []
    l = 0
    while l < tamLista:
        lista.append(random.randint(0,10)) 
        l += 1
    return lista

nome = "listas.json"

lista1 = geradorLista(10000)
lista2 = geradorLista(100000)
lista3 = geradorLista(500000)
lista4 = geradorLista(1000000)
lista5 = geradorLista(5000000)

listas = [lista1, lista2, lista3, lista4, lista5]
salvarLista(nome, listas)

listasCarregadas = carregarLista(nome)

# print(f"Lista1 {len(listasCarregadas[0])}")
# print(f"Lista2 {len(listasCarregadas[1])}")
# print(f"Lista3 {len(listasCarregadas[2])}")
# print(f"Lista4 {len(listasCarregadas[3])}")
# print(f"Lista5 {len(listasCarregadas[4])}")