print('\nSeu número é par ou ímpar?\n')
nume = float(input('Digite um número: '))

verifi = nume % 2
if(verifi == 0): print('O número {:.0f} é par!'.format(nume))
else: print('O número {:.0f} é ímpar!'.format(nume))