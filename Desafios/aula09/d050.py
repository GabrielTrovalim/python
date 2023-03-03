soma = 0
for c in range(0,6):
    num = int(input('Digite um valor inteiro: '))
    if (num % 2 == 0): # Verificando se o número é par.
        soma = soma + num
print('\nO somatorio dos números pares digitados é: {}'.format(soma))