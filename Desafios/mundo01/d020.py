import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista) 
#O comando shuffle embaralha todos os itens contidos na lista e não precisa estar acompanhado de uma variável.

print('\nA sequência para a apresentação é {}'.format(lista)) # Após o embaralhamento só será necessário printar a lista que foi embaralhada.