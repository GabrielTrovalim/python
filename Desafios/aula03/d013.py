print('\nReajuste salarial\n')

atsal = float(input('Qual é o seu salário atual? \nR$')) # Recebendo o valor do salário atual do funcionário.
reajuste = atsal * (15/100) # Aplicando 15% ao salário.
newsal = atsal + reajuste

print('Com o reajuste salarial da empresa, você recebeu um aumento de 15%. \nValor do aumento: R${:.2f} \nNovo saláro: R${:.2f}'.format(reajuste, newsal))