fra = str(input('Digite uma frase: ')).strip()
up = fra.upper()

print(fra)
print('A letra A apareceu {} vezes na frase'.format(up.count('A')))
print('A primeira letra A apareceu na posição {}'.format(up.find('A')+1))
print('A última letra A apareceu na posição {}'.format(up.rfind('A')+1))