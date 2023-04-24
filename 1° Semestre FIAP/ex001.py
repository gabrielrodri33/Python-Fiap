#inventando um joguinho de forca

jogo = ['g','a','b','g','i','e','l']
hide = ['_','_','_','_','_','_','_']
quant_char_jogo = len(jogo)
c = erros = 0

print(f'A palavra tem {quant_char_jogo} letras')

while c != quant_char_jogo:
    print(hide[0+c], end='')
    c += 1

while hide != jogo:
    c = 0
    chute = input('\nChute uma letra: ')
    while c == quant_char_jogo:
        hide[0+c] = chute
        print(hide)
        c += 1
