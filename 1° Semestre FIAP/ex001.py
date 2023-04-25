#inventando um joguinho de forca

jogo = ['g','a','b','g','i','e','l']
hide = ['_','_','_','_','_','_','_']
quant_char_jogo = len(jogo)
c = erros = 0

print(f'A palavra tem {quant_char_jogo} letras')

while c != quant_char_jogo:
    print(hide[c], end='')
    c += 1