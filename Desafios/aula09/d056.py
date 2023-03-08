idade_g = 0 # idade geral
mulheres19 = 0
maior = 0 # maior idade detectada
nomem = '' # nome do homem mais velho
for c in range(1,5):
    print('\n')
    print('=' * 10, '{}° pessoa'.format(c), '=' * 10)
    nome = str(input('Qual é o seu nome? ')).strip().capitalize()
    idade = int(input('Quantos anos você tem? ')) # idade da pessoa.
    sex = str(input('Seu sexo [M/F]: ')).strip().upper()
    idade_g += idade
    if sex == 'F' and idade < 20:
        mulheres19 += 1

    if sex == 'M': 
        if c == 1:
            maior = idade
            nomem = nome
        else:
            if idade > maior:
                maior = idade
                nomem = nome

print('\n\033[0;31m','=' * 50,'\033[m')
print('\nA média da idade do grupo é igual a: {}'.format(idade_g / 4))
if mulheres19 == 1:
    print('\nO grupo possui apenas uma mulher com menos de 20 anos.')
elif mulheres19 == 0:
    print('\nO grupo não possui nenhuma mulher com menos de 20 anos.')
else:
    print('\nO grupo possui {} mulheres com menos de 20 anos.'.format(mulheres19))
print('\nO nome do homem mais velho é {} com {} anos.\n'.format(nomem, maior))