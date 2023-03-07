soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if (num % 2 == 0): # Verificando se o número é par.
        soma += num
        cont += 1
print('\nO somatório dos {} números PARES é: {}'.format(cont, soma))
