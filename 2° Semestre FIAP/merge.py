#merge sort - Ordenação por intercalação (mistura)
#complexidade: 0(n*log(n))

import random

def merge_sort(lista):
    if len(lista)>1 :

        #Encontrando o meio da lista
        meio = len(lista) // 2 #Parte inteira da lista

        #dividindo a lista em duas
        esquerda = lista[:meio] #esquerdo do meio até a metade
        direita = lista[meio:] #Direito do meio pra frente

        #chamada recursiva
        merge_sort(esquerda) #ordenar as sub-listas
        merge_sort(direita) #ordenar as sub-listas

        #Variáveis de controle
        #i - fará o controle da lista esquerda
        #j - fará o controle da lista direita
        #k - fará o controle da lista anterior à recursão
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i]<direita [j]:
                lista[k]=esquerda[i]
                i+=1
            else:
                lista[k] = direita[j]
                j += 1
            
            k += 1

        #Verificação dos elementos da lista da esquerda
        while (i < len(esquerda)):
            lista[k] = esquerda [i]
            i += 1
            k +=1

        #Verificação dos elementos da lista da direita
        while (j < len(direita)):
            lista[k] = direita[j]
            j += 1
            k += 1

#Programa principal
lista = []
o = 0
while o < 100000000: 
    lista.append(random.randint(0,100)) 
    o += 1
print(f"Lista original: {lista}")
merge_sort(lista)
print(f"Lista ordenada: {lista}")