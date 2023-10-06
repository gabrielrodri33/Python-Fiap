def dividir(x,y):
    try:
        print(f'{x} / {y} = {x/y}')
    except ZeroDivisionError as e:
        print(f'Erro: {e}')

#Programa principal
dividir(10,0)
dividir(20,4)
dividir(10,5)
dividir(20,0)