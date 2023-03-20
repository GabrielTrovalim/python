cont = 1 # contador inicial.
num = int(input('Digite um número inteiro: '))
cont += num # contador inicial recebe o valor inserido.
fat = 1 # contador fatorial.
while cont > 1:
    cont -= 1 # contagem regressiva.
    fat *= cont # multiplicação da contagem.
    print('{}'.format(cont),end=' ')
    print('x ' if cont > 1 else '= ',end='')
print('{}'.format(fat))
print('\nO resultado de {}! é igual a: {}\n'.format(num, fat))