soma = 0
for c in range(1,7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if (num % 2 == 0): # Verificando se o número é par.
        soma = soma + num
print('\nO somatório dos números pares digitados é: {}'.format(soma))
