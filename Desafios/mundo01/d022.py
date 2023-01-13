nome = str(input('Digite o seu nome completo: ')).strip()

print('\nSeu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
sespaco = nome.replace(' ', '')
print('Seu nome tem ao todo {} letras'.format(len(sespaco)))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))