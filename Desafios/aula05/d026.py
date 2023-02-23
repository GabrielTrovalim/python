nome = str(input('Digite o seu nome completo: ')).strip().title()
sepa = nome.split()
print('\nÉ um prazer te conhecer, {}.\nSeu primeiro nome é: {}\nSeu último nome é: {}'.format(nome, sepa[0], sepa[len(sepa) - 1]))
