real = float(input('Quantos reais (R$) você na sua carteira? '))

dol = float(5.48) #para real o dolar valer 3,27

# Regra a ser seguida no desafio:
# 1 dolar -> 3,27 real (valor que está no curso na época)
# x dólares - > 1 real #

calc = real/dol

print('\nVocê conseguiria comprar {:.2f} dólares com o seu saldo atual de R${:.2f}'.format(calc, real))
print('\nINFO: O valor considerado para o dólar é de {:.2f} \n'.format(dol))