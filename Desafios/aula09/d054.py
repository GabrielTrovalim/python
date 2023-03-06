from datetime import date
hoje = date.today().year
lista = []
for c in range(0,7):
    age = int(input('Em que ano você nasceu? '))
    lista.append(age)
age01 = hoje - lista[0] # contas das idades.
age02 = hoje - lista[1]
age03 = hoje - lista[2]
age04 = hoje - lista[3]
age05 = hoje - lista[4]
age06 = hoje - lista[5]
age07 = hoje - lista[6]
lista18 = []
lista17 = []
if age01 > 18: # Condições.
    lista18.append(age01)
else:
    lista17.append(age01)
if age02 > 18:
    lista18.append(age02)
else:
    lista17.append(age02)
if age03 > 18:
    lista18.append(age03)
else:
    lista17.append(age03)
if age04 > 18:
    lista18.append(age04)
else:
    lista17.append(age04)
if age05 > 18:
    lista18.append(age05)
else:
    lista17.append(age05)
if age06 > 18:
    lista18.append(age06)
else:
    lista17.append(age06)
if age07 > 18:
    lista18.append(age07)
else:
    lista17.append(age07)
print('\nEm relação a data atual temos {} pessoas com mais de 18 anos e {} pessoas com menos de 18 anos.'.format(len(lista18), len(lista17)))