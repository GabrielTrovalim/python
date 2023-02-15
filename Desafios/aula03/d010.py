real = float(input('Quantos reais você tem?\nR$'))
# US$ 1.00 = R$3.27
convert = real / 3.27
print('Com R${:.2f} você consiguirá comprar US${:.2f} para a sua viagem.'.format(real, convert))