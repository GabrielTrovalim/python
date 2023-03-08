from random import randint
from time import sleep
print('=-' * 30)
print('{:^60}'.format('Jogo do sorteio!'))
print('-=' * 30)
jogo = 'S'
while jogo != 'N':
    tentativas = 1 # número de tentativas necessárias até vencer.
    num_pc = randint(0,10)
    print('\nO computador está sorteando um número... ')
    sleep(2)
    print('\nPronto.\nNúmero sorteado!')
    sleep(1)
    num = int(input('\nTente adivinhar o número entre 1 e 10\nSua jogada: '))
    if num == num_pc:
        print('\nParabéns você ganhou!')
        print('Você precisou de apenas uma tentativa.')
    else:
        while num != num_pc:
            print('\nOps, parece que você errou...')
            num = int(input('Tente novamente: '))
            tentativas += 1
        print('\nParabéns você ganhou!')
        print('Você precisou de {} tentativas para ganhar!'.format(tentativas))
    jogo = str(input('\nVocê gostaria de jogar novamente? [S/N]: ')).strip().upper()
print('\nMuito obrigado por ter jogado!\n')
sleep(1.5)