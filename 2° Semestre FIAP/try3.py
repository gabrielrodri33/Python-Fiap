def fahrenheit_to_celsius(f):
    return (f-32) * 5/9

while True:
    try:
        fahrenheit_temp = float(input("Temperatura °F: "))
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        print(f'{fahrenheit_temp}°F é equivalente a {celsius_temp}°C')
        break
    except ValueError:
        print('Valor inválido. Digite uma temp válida!')