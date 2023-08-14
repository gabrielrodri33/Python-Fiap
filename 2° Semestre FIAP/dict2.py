carro = {'marca': 'Ferrari', 'motor': 'v8', 'ano': 2020}

copia_carro = carro.copy() #Obviamente ele copia o dicionario "carro"

#metodo fromkeys()

lista_chaves = ['chave1', 'chave2', 'chave3']
valor = 0

dicio = dict.fromkeys(lista_chaves, valor) #monta um dicionario com base nas infos que recebe por parametro, a cada valor da lista ele atribuiu o valor as chaves

print(dicio)