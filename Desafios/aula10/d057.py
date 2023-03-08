print('-=' * 20)
print('{:^40}'.format('CADASTRO'))
print('=-' * 20)
cad = []
for c in range(1,3):
    nome = str(input('\nDigite o seu nome: ')).strip().capitalize()
    cad.append(nome)
    sex = str(input('Seu sexo [M/F]: ')).upper().strip()
    if sex == 'F':
        #print('Fem')
        cad.append('Feminino')
    elif sex == 'M':
        #print('masc')
        cad.append('Masculino')
    else:
        while sex != 'M' and sex != 'F':
            sex = str(input('Seu sexo [M/F]: ')).upper().strip()
        if sex == 'M': # Após o final do laço while.
            #print('{}'.format(sex))
            cad.append('Masculino')
        else:
            #print('{}'.format(sex))
            cad.append('Feminino')
print('\n1ª pessoa:\nNome: {} \nSexo: {}'.format(cad[0],cad[1]))
print('\n2ª Pessoa:\nNome: {} \nSexo: {}'.format(cad[2],cad[3]))