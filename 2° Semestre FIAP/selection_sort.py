#Algoritmo selection sort
#Complexidade 0(n^2)
#Ordenação (busca) pelo menor indice

def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            #seleciona o menor elemento em cada iteração
            if seq[j] < seq[min_index]:
                #troca os elementos - atribuição paralela
                seq[j], seq[min_index] = seq[min_index], seq[j]

#Programa principal
lista = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print(f'Lista Original {lista}')
selection_sort(lista)
print(f'Lista ordenada: {lista}')
                       