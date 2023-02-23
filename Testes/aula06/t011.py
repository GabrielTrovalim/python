nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
media = (nota01 + nota02)/2
if (media >= 7):
    print('\nSua média é igual a: {:.1f}'.format(media))
    print('Você foi aprovado!')
else:
    print('\nSua média é igual a: {:.1f}'.format(media))
    print('Você foi reprovado!')
print('\nBons estudos!')