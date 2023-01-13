n = str(input('\nDigite o seu nome completo: ')).strip()
nome = n.split()
print(nome)

print('\nÉ um prazer te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Seu último nome é {}'.format(nome[len(nome)-1].capitalize()))