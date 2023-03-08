cont = 1 # contador inicial.
num = int(input('Digite um número inteiro: '))
cont += num # contador inicial recebe o valor inserido.
fat = 1 # contador fatorial.
while cont > 1:
    cont -= 1 # contagem regressiva.
    fat *= cont # multiplicação da contagem.
    print(cont, end=' ')
print('\nResultado fatorial de {}!: {}\n'.format(num, fat))