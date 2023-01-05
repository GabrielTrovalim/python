# conversor de temperatura, de °C para °F e K
# 1 - °C x 9 = r
# 2 - r / 5 = R
# 3 - R + 32 
# De celciu para kelvin
# °C + 273,15

print('\nConversor de temperatura\n')
print('-' * 20)

temp = float(input('\nInforme a temperatura em Celsius: °C '))

fahren = (temp * 9)/5 + 32
kelvin = temp + 273.15

print('\nA temperatura informada era de {}°C, convertendo esse valor para Fahrenheit temos: {}°F'.format(temp, fahren))
print('De acordo com essas temperaturas, tem-se {} K\n'.format(kelvin))