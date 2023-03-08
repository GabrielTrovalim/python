print('{:^40}\n'.format('SOMAS'))
nums = 0 # inicio da contagem.
n = 'S' # confirmação.
while n == 'S':
    num = int(input('\nDigite um número: '))
    nums += num # enviando o dado para o contador.
    n = str(input('Deseja continua? [S/N]\nSua resposta: ')).upper().strip() # Confirmação.
print('\nA soma dos números inseridos é: {}.'.format(nums))