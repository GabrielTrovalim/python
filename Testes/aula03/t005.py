print('Indique valores para operações matemáticas: \n')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
divs = n1 / n2
pot = n1 ** n2 # Potência
divint = n1 // n2 # Divisão inteira
restd = n1 % n2 # Resto da divisão

print('\nSoma = {} \nSubtração = {} \nMultiplicação = {} \nDivisão = {} \nPotência = {} \nDivisão inteira = {} \nResto da divisão = {}'.format(soma, subt, mult, divs, pot, divint, restd))