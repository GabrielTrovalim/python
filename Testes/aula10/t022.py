nomes = []
n = 2
while n != 0:
    name = str(input('Digite um nome: ')).strip().capitalize()
    nomes.append(name)
    n = int(input('Deseja continuar? (1 = S / 0 = N)\nSua resposta: '))
print('\nOs nomes digitados foram: {}'.format(nomes))