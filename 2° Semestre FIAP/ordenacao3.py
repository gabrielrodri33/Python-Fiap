def troca(s, i, j):
    s[i], s[j] = s[j], s[i]

def empurra(s):
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)

def bubble_sort(s):
    n = len(s)
    while n > 1:
        empurra(s)
        n -= 1
    return print(s)

#Programa principal
lista = [40, 30, 20, 50 ,10]

bubble_sort(lista)
