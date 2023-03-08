from random import randint
from time import sleep
print('=-' * 30)
print('{:^60}'.format('Jogo do sorteio!'))
print('-=' * 30)
jogo = 'S'
while jogo != 'N':
    num_pc = randint(0,10)
    print('\nO computador está sorteando um número...')
    sleep(2)
    print('\nPronto.\nNúmero sorteado! {}'.format(num_pc))
    sleep(1)
    num = int(input('\nTente adivinhar o número entre 1 e 10\nSua jogada: '))
    if num == num_pc:
        print('\nParabéns você ganhou!')
    else:
        while num != num_pc:
            print('\nOps, parece que você errou...')
            num = int(input('Tente novamente: '))
        print('\nParabéns você ganhou!')
    jogo = str(input('\nVocê gostaria de jogar novamente? [S/N]: ')).strip().upper()
print('\nMuito obrigado por ter jogado!\n')