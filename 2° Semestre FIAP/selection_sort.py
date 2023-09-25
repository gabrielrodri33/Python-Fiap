#Algoritmo selection sort
#Complexidade 0(n^2)
#Ordenação (busca) pelo menor indice

import random

def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            #seleciona o menor elemento em cada iteração
            if seq[j] < seq[min_index]:
                #troca os elementos - atribuição paralela
                seq[j], seq[min_index] = seq[min_index], seq[j]

#Programa principal
lista = []
o = 0
while o < 100000000: 
    lista.append(random.randint(0,100)) 
    o += 1
print(f"Lista original: {lista}")
selection_sort(lista)
print(f"Lista ordenada: {lista}")
                       