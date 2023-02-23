from datetime import date
from time import sleep
print('\nVerifique se um ano qualquer é bissexto')
ano = int(input('\nDigite o ano que deseja analisar\nCaso zero seja digitado, o ano atual será levado em consideração.\nAno: '))
hoje = date.today().year
if (ano == 0): # Caso o ano atual seja analisado:
    ano = date.today().year
    print('\nVocê escolheu analisar o ano atual')
    print('Processando...')
    sleep(2)
    if (ano % 4 == 0 and ano % 10 != 0 or ano % 400 == 0):
        print('O ano atual ({}) é bissexto.'.format(ano))
    else:
        print('O ano atual ({}) não é bissexto.'.format(ano))
else: # Caso outro ano seja analisado, no futuro ou passado:
    if (ano < hoje):
        print('Processando...')
        sleep(2)
        if (ano % 4 == 0 and ano % 10 != 0 or ano % 400 == 0):
            print('O ano de {} foi bissexto.'.format(ano))
        else:
            print('O ano de {} não foi bissexto.'.format(ano))
    else:
        print('processando...')
        sleep(2)
        if (ano % 4 == 0 and ano % 10 != 0 or ano % 400 == 0):
            print('O ano de {} será bissexto.'.format(ano))
        else:
            print('O ano de {} não será bissexto.'.format(ano))
