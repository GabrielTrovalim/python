import random

print('\nQuem vai apagar o quadro?\n')
print('-' * 20)

n1 = str(input('\nPrimeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = {n1: 1, n2: 2, n3: 3, n4: 4}
name, id = random.choice(list(lista.items()))

print('\nO aluno sorteado foi: {}'.format(name))