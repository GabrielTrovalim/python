print('\nVerifique se um ano qualquer é bissexto\n')
ano = int(input('Digite um ano de sua preferência: '))
verifi = ano % 4
if (ano < 0): 
    print('Ano invalido, por favor tente novamente...')
else:
    if(ano > 2023):
        if(verifi == 0):
            print('O ano de {} será bissexto!'.format(ano))
        else: 
            print('O ano de {} não será bissexto...'.format(ano))
    else:
        if(verifi == 0):
            print('O ano de {} foi bissexto!'.format(ano))
        else:
            print('O ano de {} não foi bissexto...'.format(ano))
print('Fim da verificação.')