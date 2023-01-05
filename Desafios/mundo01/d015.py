# custos do aluguel: 
# R$60 por dia
# R$0.15 por Km rodado

print('\nAlugel de carros\n')
print('-' * 15)

km = float(input('\nQuantos km foram percorridos com o carro? '))
dia = int(input('\nPor quantos dias o carro foi alugado? '))

preco = (km * 0.15) + (dia * 60)

print('\nO total a pagar pelo aluguel do carro é igual a: R${:.2f}'.format(preco))
