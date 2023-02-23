km = float(input('Diga o km: '))
multa = (km - 80)
mult = multa * 7
if (km > 80):
    print('Você está sendo multado!\nValor da multa: {:.2f}'.format(mult))
else:
    print('Tudo de boa!')