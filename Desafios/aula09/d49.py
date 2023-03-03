print('-=' * 20)
print('{:^40}'.format('TABUADA'))
print('=-' * 20)
# área do exercício:
num = int(input('\nDigite um número e veja a sua tabuada: '))
print('')
for c in range(1, 11):
    print('{} X {:2} = {:2}'.format(num, c, num * c))
print('\nFim da geração de tabuadas\n')