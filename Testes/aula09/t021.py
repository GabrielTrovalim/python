homes = []
maior = 0
menor = 0
nomem = ''
for c in range(1,4):
    print('{}° pessoa'.format(c))
    nome = str(input('Digite o seu nome: ')).strip().capitalize()
    idade = int(input('Digite a sua idade: '))
    sex = str(input('Diga o seu sexo [M/f]: ')).strip().upper()
    if sex == 'M':
        homes.append(nome)
        homes.append(idade)
        if c == 1:
            maior = idade
            menor = idade
            nomem = nome
        else:
            if idade > maior:
                maior = idade
                nomem = nome
            if idade < menor:
                menor = idade
print('{}'.format(homes))
print('A maior idade detectada foi {}\nJá a menor foi {}'.format(maior, menor))
print(nomem)