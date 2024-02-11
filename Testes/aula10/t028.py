from math import floor
val = int(input('Digite um valor entre R$1 e R$250:\nR$'))
if val >=1 and val <=250:
    vint = val / 20
    if floor(vint) < 1:
        print('O valor digitado foi R${:.2f} e esse valor não pode ser preenchido por notas de R$20.'.format(val))
    else:
        notas20 = (floor(vint) * 2) * 10
        resto = val - notas20 
        print('O valor digitado foi R${:.2f}, a quantidade de notas de R$20 que preenchem esse valor é igual a {}, com isso faltam R${:.2f} para completar o valor inserido'.format(val,floor(vint), resto).replace('.', ','))
else:
    print('\nO valor inserido é invalido, tente novamente.')