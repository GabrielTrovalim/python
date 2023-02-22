import random # Importando a biblioteca random.
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4] # Criando a lista com os inputs.
random.shuffle(lista) # Embaralhando os nomes na lista.
print('A ordem de apresentação é a seguinte:\n{}'.format(lista))