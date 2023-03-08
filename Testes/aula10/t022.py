nomes = []
n = 'S'
while n == 'S':
    name = str(input('\nDigite um nome: ')).strip().capitalize()
    nomes.append(name)
    n = str(input('Deseja continuar? [S/N]\nSua resposta: ')).upper().strip()
print('\nOs nomes digitados foram: {}'.format(nomes))