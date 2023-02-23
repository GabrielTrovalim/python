print('Vamos verificar se um número é PAR ou ÍMPAR\n')
num = int(input('Digite um número inteiro: '))
cont = num % 2 # Divisão inteira por 2.
if (cont == 0):
    print('\nO número {} é PAR'.format(num))
else:
    print('\nO número {} é ÍMPAR'.format(num))
print('\nPara tentar novamente, reinicie o programa.\n')