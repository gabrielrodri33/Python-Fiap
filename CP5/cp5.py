import time
import os
import criar_listas

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'},
        5: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
    }

    if cor == 1:
        mensagem = print(f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n)

    elif cor == 2:
        mensagem = print(f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n)

    elif cor == 3:
        mensagem = print(f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n)

    elif cor == 5:
        mensagem = print(f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n)

    else:
        mensagem = print(f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n)
    return mensagem

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min_index]:
                seq[j], seq[min_index] = seq[min_index], seq[j]

def insertion_sort(lista):
    for i in range (1, len(lista)):
        pivo = lista[i]
        j = i-1
        while ((j >= 0) and (pivo < lista[j])):
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = pivo

def merge_sort(lista):
    if len(lista)>1 :
        meio = len(lista) // 2

        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i]<direita [j]:
                lista[k]=esquerda[i]
                i+=1
            else:
                lista[k] = direita[j]
                j += 1
            
            k += 1

        while (i < len(esquerda)):
            lista[k] = esquerda [i]
            i += 1
            k +=1

        while (j < len(direita)):
            lista[k] = direita[j]
            j += 1
            k += 1

def validacao(var, tipo):
    if tipo == 1:
        while var not in ["1","2","3","4","5"]:
            clear_console()
            separador(21,5)
            var = input("Opção inválida\nEscolha o tamanho da lista\n1- 10 mil\n2- 100 mil\n3- 500 mil\n4- 1 milhão\n5- 5 milhões\n").strip()
        return var
    
    elif tipo == 2:
        while var not in ["1","2","3","4"]:
            clear_console()
            separador(21,5)
            var = input("Opção inválida\nEscolha o método que deseja utilizar\n1- Bubble Sort\n2- Selection Sort\n3- Insertion Sort\n4- Merge Sort\n").strip()
        return var

def get_time(arg):    
    inicio = time.time()    
    time.sleep(arg) 
    fim = time.time()
    return print(f'Tempo: {fim-inicio}')

def medir_tempo(limite):
    inicio = time.time()
    for i in range(limite):
        print(f'i: {i}')
    fim = time.time()
    print(f'Tempo: {fim-inicio}')

def carregarListas():
    return criar_listas.carregarLista("listas.json")

def menuPrincipal():
    listas = carregarListas()
    separador(21, 1)
    tamLista = input("Escolha o tamanho da lista\n1- 10 mil\n2- 100 mil\n3- 500 mil\n4- 1 milhão\n5- 5 milhões\n").strip()
    tamLista = validacao(tamLista, 1)

    if tamLista == "1":
        listaDesordenada = listas[0]

    elif tamLista == "2":
        listaDesordenada = listas[1]

    elif tamLista == "3":
        listaDesordenada = listas[2]

    elif tamLista == "4":
        listaDesordenada = listas[3]

    elif tamLista == "5":
        listaDesordenada = listas[4]
    
    clear_console()
    separador(21, 2)

    metodo = input("Escolha o método que deseja utilizar\n1- Bubble Sort\n2- Selection Sort\n3- Insertion Sort\n4- Merge Sort\n").strip()
    metodo = validacao(metodo, 2)

    print('Iniciando ordenação')
    inicio = time.time()

    if metodo == "1":
        listaOrdenada = bubble_sort(listaDesordenada)
        fim = time.time()

    elif metodo == "2":
        listaOrdenada = selection_sort(listaDesordenada)
        fim = time.time()
    
    elif metodo == "3":
        listaOrdenada = insertion_sort(listaDesordenada)
        fim = time.time()
    
    elif metodo == "4":
        listaOrdenada = merge_sort(listaDesordenada)
        fim = time.time()
        
    print(f'Tempo de ordenação: {fim-inicio:.3f} segundos')

    

def principal():
    clear_console()
    menuPrincipal()

#Programa principal
principal()



# lista = [1,2,3,4,5,6,1,3,5,6,2,4,56,1,1,3,8,9,53,4,5,7,2,1]

# merge_sort(lista)
# get_time(1)
# print(lista)

# print(get_time(1000000))