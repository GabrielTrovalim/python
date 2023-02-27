from time import sleep
nome = str(input('Qual é o seu nome? ')).strip().capitalize()
big = nome.upper()
if (big == 'GABRIEL'):
    print('Nossa, que nome lindo <3')
elif (big == 'GABRIELA'):
    print('Uaaau, amo esse nome feminino S2 !!')
else:
    print('Nossa... Que nominho mais comum em...')
sleep(2)
print('\nTenha um ótimo dia, {}!'.format(nome))