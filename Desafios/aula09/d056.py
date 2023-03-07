idade = [] # lista para idade
homem = [] # lista para homens
mulher = [] # lista para mulheres
mulher19 = [] # lista de mulheres com menos de 20
for c in range(0,5):
    nome = str(input('\nDiga o seu nome: ')).strip().capitalize()
    sex = str(input('Informe o seu sexo (M para masculino e F para feminino): ')).upper()
    age = int(input('Diga a sua idade: '))
    if sex == 'M':
        homem.append(nome)
        #homem.append(sex)
        homem.append(age)
    else:
        mulher.append(nome)
        #mulher.append(sex)
        mulher.append(age)
    idade.append(age)
    if sex == 'F' and age < 20:
        mulher19.append(nome)

# 1,4,7,10,13
media = (idade[0] + idade[1] + idade[2] + idade[3] + idade[4]) / 5
print('\nA média de idade do grupo é: {} anos.'.format(media))
print('\nO homem mais velho do grupo se chama: {}, com {} anos.'.format(homem[-2], homem[-1]))
print('\nO grupo possui {} garotas com menos de 20 anos.'.format(len(mulher19)))
