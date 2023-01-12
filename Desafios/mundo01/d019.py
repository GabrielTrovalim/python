import random

print('\nQuem vai apagar o quadro?\n')
print('-' * 20)

n1 = str(input('\nQuem é o aluno 1? '))
n2 = str(input('Quem é o aluno 2? '))
n3 = str(input('Quem é o aluno 3? '))
n4 = str(input('Quem é o aluno 4? '))

lista = {n1: 1, n2: 2, n3: 3, n4: 4}
name, id = random.choice(list(lista.items()))

print('\nO aluno sorteado foi: {}'.format(name))