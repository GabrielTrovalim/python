from datetime import date
ataul = date.today().year
cont18 = 0 # contador de pessoas maiores de idade
cont17 = 0 # contador de pessoas menores de idade
for c in range(1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if ataul - ano >= 18:
        cont18 += 1
    else:
        cont17 += 1
print('\nEm relação a data atual ({}) temos {} pessoas maiores de idade e {} pessoas menores de idade.'.format(ataul, cont18, cont17))