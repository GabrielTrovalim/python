print('\nConversor de temperatura\n')
celsiu = float(input('Informe a temperatura em °C: '))
convert = (celsiu * (9 / 5) + 32) # Convertendo para °F.
kelvin = celsiu + 273.15 # Convertendo para kelvin.
print('A temperatura de {:.2f}°C corresponde a  {:.2f}°F e a {:.2f}K.'.format(celsiu, convert, kelvin)) # Adicionando as medidas internacionais mais famosas.