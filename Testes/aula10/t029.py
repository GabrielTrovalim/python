from math import floor
valor = int(input('Digite um valor entre R$1 e R$250:\nR$'))
if valor >= 1 and valor <=250:
    vint = valor / 20
    if floor(vint) < 1:
        print('O valor digitado foi R${:.2f} e esse valor não pode ser preenchido com notas de R$20.'.format(valor))
    else:
        print('O valor digitado foi R${:.2f}, podendo ser preenchido por {} notas de R$20.'.format(valor,floor(vint)))
else:
    print('\nO valor digitado é invalido, tente novamente.')