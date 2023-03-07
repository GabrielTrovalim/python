pesos = [] # armazena os pesos informados.
for c in range(0,5):
    peso = float(input('Qual é o seu peso em (kg): '))
    pesos.append(peso)

pesos.sort() # Organiza os números de forma crescente.

print('\nO maior peso detectado na pesquisa foi: {}Kg\nJá o menor peso detectado foi: {}Kg'.format(pesos[-1], pesos[0]))