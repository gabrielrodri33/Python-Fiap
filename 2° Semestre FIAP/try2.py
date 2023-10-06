import clearconsole

def dividir(numerador, denominador1, denominador2):
    resultado = 0
    try:
        resultado = numerador/denominador1
    except ZeroDivisionError:
        try:
            resultado = numerador/denominador2
        except ZeroDivisionError as e:
            print(f'Erro: {e}')
        else:
            print('Operação realizada com o denominador 2')
    else:
        print("Operacção realizada com o denominador 1")
    return resultado

def adicionar(x,y):
    resultado = 0
    try:
        resultado = int(x) + int(y)
    except ValueError:
        print("Erro de entrada de dados!")
    else:
        return resultado

# teste
clearconsole.clear_console()
print('Divisão')
dividir(5,0,0)
dividir(5,0,1)
dividir(5,1,0)
print('\nSoma')
adicionar(5,6)
adicionar(3,'1')
adicionar(4,'r')