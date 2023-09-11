#ordenando a lista com valores estáticos
print('-='*20)
lista = [10, 40, 30, 20, 50]

temp = lista[1]
lista[1]=lista[3]
lista [3] = temp

print(lista)

#atribuição paralela
print('-='*20)
lista = [10, 40, 30, 20, 50]

lista[1], lista[3] = lista[3], lista[1]
print(lista)