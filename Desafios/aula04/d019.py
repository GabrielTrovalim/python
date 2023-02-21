import random # Chamando a biblioteca random.
lista = ['Gabriel', 'João', 'Zézão', 'claudin', 'julia', 'isabela', 'Joana', 'zuleide'] # Criando a lista de alunos.
escolha = random.randint(0 , 7) # Randomizando números de acordo com os valores na lista.
print('O escolhido para apagar a lousa foi: {}'.format(lista[escolha])) # Permitindo que random escolha um número da lista e mostre o resultado na tela.