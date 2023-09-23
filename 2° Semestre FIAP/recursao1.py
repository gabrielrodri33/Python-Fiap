#Recursão

#Exemplo 1 - somar uma lista de números (sem recusão)
# (1,3,5,7,9) = ?

# "Função de soma padrão"
def somar(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

#Função de soma com recursão
def somarRecursivo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somarRecursivo(lista[1:])
    
#Programa principal
lista = [1,3,5,7,9]
print(f"Soma: {somarRecursivo(lista)}")
