# cada litro de tinta pinta 2 metros quadrados.
altura = float(input('\nQual é a altura da sua parede em metros? '))
comp = float(input('Qual é a largura da sua parede em metros? '))

area = (altura * comp) # Calculando a área da parede.
tinta = (area/2) # Dividindo a área pela capacidade em m² da tinta.
print('\nA área da sua parede é de {:.2f}m² \nCom essas medidas, você vai precisar de {:.2f} litros de tinta'.format(area, tinta))