from datetime import date
hoje = date.today().year
anon = int(input('Em que ano você nasceu? '))
at_age = hoje - anon
dezoito = at_age - 18
print(hoje)
print('Você tem {} anos'.format(at_age))
print(dezoito)
if (at_age > 18):
    print('Você provavelmente já se apresentou ao exercito.')
    print('fazem {} anos que você se apresentou.'.format(dezoito))
else:
    print('Você ainda tem que se apresentar ao exercito.')
    print('Você ainda terá {} anos para se apresentar ao exercito.'.format(dezoito * -1))