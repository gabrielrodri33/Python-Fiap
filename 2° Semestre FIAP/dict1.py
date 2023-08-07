lista1 = ['primeiro',  'segundo', 'terceiro']
lista2 = [1, 2, 3]
lista3 = list(zip(lista1, lista2)) #Comando "zip" serve para concatenar (compactar)
lista4 = dict(zip(lista1, lista2)) # Dict criado

print(f'{lista1}')
print(f'{lista2}')
print(f'{lista3}')
print(f'{lista4}')

print('\n')

pessoa = {'nome': 'Gabriel', 'altura': 1.7, 'idade': 19}
print(pessoa.get('nome')) # O comando 'get serve para buscarmos algum valor dentro de um dicionario

print('\n')

computador = {'CPU': 'Intel', 'RAM': '16gb', 'SSD': '256gb'}
print(computador.keys()) #Comando 'keys' utilizado para buscar apenas as chaves do dicionario
print(computador.values()) #Comando 'values' utilizado para buscar apeanas os valores atribuidos a chave do dict

print('\n')

for chave in computador.keys():
    print(f'Chave: {chave} e Valor: {computador[chave]}') #For realizado para percorrer um dicionario e printar suas chaves e elementos

print('\n')

notas = {'Python': 9, 'Java': 7, 'BD': 5}
for nota in notas.values():

    print(f'Nota: {nota}')