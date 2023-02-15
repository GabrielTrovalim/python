print('\nConversor de medidas\n')
met = float(input('Por favor informe a medida em metros: '))

cent = met * 100 # Passando para centimetros.
mili = met * 1000 # Passando para milímetros.
dm = met * 10
dam = met / 10
hm = met / 100
km = met / 1000
# Escala = km hm dam m dm cm mm.
print('\nA medida de {:.1f}m corresponde a\n{} Km \n{} hm \n{} dam \n{:.0f} dm \n{:.0f} cm \n{:.0f} mm'.format(met,km, hm, dam, dm, cent, mili))