real = float(input('Quantos reais (R$) você na sua carteira? R$'))

dol = float(3.27) #para real o dolar valer 3,27

# Regra a ser seguida no desafio:
# 1 dolar -> 3,27 real (valor que está no curso na época)
# x dólares - > 1 real #

calc = real/dol

print('\nVocê conseguiria comprar US${:.2f} dólares com o seu saldo atual de R${:.2f}'.format(calc, real))
print('\nINFO: O valor considerado para o dólar é de R${:.2f} \n'.format(dol))