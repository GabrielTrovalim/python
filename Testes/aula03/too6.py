print('\nSeu número é par ou ímpar?\n')
nume = float(input('Digite um número: '))

verifi = nume % 2
if(verifi == 0): print('O número {} é par!'.format(nume))
else: print('O número {} é ímpar!'.format(nume))