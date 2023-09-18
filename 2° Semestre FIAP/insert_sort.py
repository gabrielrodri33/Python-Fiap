#Insertion sort
import clearconsole

def insertion_sort(lista):
    for i in range (1, len(lista)):
        pivo = lista[i]
        j = i-1
        while ((j >= 0) and (pivo < lista[j])):
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = pivo

#Programa principal
clearconsole.clear_console()
lista = [12, 11, 13, 5, 6, 10, -1, 9, 8, 12, -22, 0, 17]
print(f'Lista original: {lista}')
insertion_sort(lista) 
print(f'Lista ordenada: {lista}')