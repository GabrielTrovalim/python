sal = float(input('Informe o seu salário atual: R$'))
limit = sal * 0.10 # Salários superiores a R$1250,00 com aumento de 10%
resu_limit = (sal + limit) # Acrescentando o aumento salarial de 10%

infi_limit = sal * 0.15 # Iguais ou inferiores a R$1250,00
resu_infi = (sal + infi_limit)
if (sal > 1250):
    print('\nComo o seu salário de R${:.2f} é maior que R$1250,00 você reberá um aumento de 10%.\nCom o reajuste do seu salário você passará a receber R${:.2f} por mês.'.format(sal, resu_limit))
else: 
    print('\nComo o seu salário atual é igual ou inferior a R$1250,00 você receberá um aumento de 15%.\nCom o reajuste do seu salário você passrá a receber R${:.2f} por mês.'.format(resu_infi))
print('\nTenha um bom dia!\n')