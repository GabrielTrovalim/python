algo = input('\nDigite algo: ')

print('\nO tipo primitivo do que você escreveu é: {}'.format(type(algo)))

print('\nO que você digitou é numérico? Resposta = {}'.format(algo.isnumeric()))

print('\nO que você digitou é alfabético? Resposta = {}'.format(algo.isalpha()))

print('\nO que você digitou é alfabético e numérico? Resposta = {}'.format(algo.isalnum()))

print('\nO que você digitou está em caixa alta? Resposta = {}'.format(algo.isupper()))