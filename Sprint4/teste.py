import db

def cadastro_bike():
    nome = input("Modelo: ")
    valor_aprox = formata_valor()
    print(valor_aprox)
    num_serie = input("Número de série: ")
    cor = input("Cor: ")
    obs = input("Observação: ")
    db.insert_bike_modelo(nome, valor_aprox)

def formata_valor():
    status = False
    while not status:
        try:
            valor = int(input("Valor: R$"))
            break
        except:
            print("Insira um número!")

    if isinstance(valor, (int, float)):
        valor = round(valor, 2)
        valor_str = '{:,}'.format(int(valor))
        if valor == int(valor):
            valor_str += '.00'
        else:
            valor_str += '.' + '{:02d}'.format(int(valor % 1 * 100))
        return 'R$' + valor_str
    else:
        raise ValueError('Invalid valor format')
    
cadastro_bike()