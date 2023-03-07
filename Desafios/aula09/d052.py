cont = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if (num % c == 0):
        print('\033[0;32m', end=' ')
        cont += 1
    else:
        print('\033[0;31m', end=' ')
    print('{}'.format(c),end=' ')
if cont == 2:
    print('\n\033[mO número {} é PRIMO.\n'.format(num))
else:
    print('\n\033[mO número {} não é PRIMO.\n'.format(num))
