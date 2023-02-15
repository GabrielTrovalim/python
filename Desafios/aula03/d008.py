print('\nConversor de medidas\n')
met = float(input('Por favor informe a medida em metros: '))

cent = met * 100 # Passando para centimetros.
mili = met * 1000 # Passando para milímetros.

print('Sua medida tem {} metros.\nEm centimetros tem {} cm.\nEm milímetros tem {} mm.'.format(met, cent, mili))