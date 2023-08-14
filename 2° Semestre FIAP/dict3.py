def teste(a,b,c):
    print(f'a: {a} - b: {b} - c: {c}')

lista = [1, 'banana', True]
teste(*lista) #desempacotamento de sequencias ou unpacked, mesma coisa que "teste(lista[0], lista[1], lista[2])"

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
def teste2(n,s):
    n = n + 2
    s[0] = s[0] + 1
    return

n1 = 1
lista = [1]

teste2(n1, lista)
print('fim')