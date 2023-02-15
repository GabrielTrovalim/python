print('\nAluguel de carros\n')
kms = float(input('Quantos KM foram rodados com o carro? '))
dias = float(input('Por quantos dias o carro esteve alugado? '))
# R$60 por dia alugado / R$0.15 por KM rodado.
divida = (dias * 60) + (kms * 0.15)
print('\nO total a se pagar pelo aluguel do carro é de R${:.2f}'.format(divida))