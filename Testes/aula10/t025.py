sex = str(input('Seu sexo [M/F]: ')).upper().strip()
if sex != 'M' and sex == 'F':
    print('Fem')
elif sex != 'F' and sex == 'M':
    print('Masc')
else:
    while sex != 'M' and sex != 'F':
        sex = str(input('Seu sexo [M/F]: ')).upper().strip()
    print('{}'.format(sex))