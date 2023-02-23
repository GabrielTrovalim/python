import random
u_num = int(input('Digite um número de 0 a 5: '))
if(u_num > 5 or u_num < 0):
    print('[ERRO] Entrada de dados invalida.')
else:
    num = random.randint(0 ,5)
    if(u_num == num):
        print('\nO número sorteado foi: {}'.format(num))
        print('Você acertou o número sorteado!')
    else:
        print('\nO número sorteado foi: {}'.format(num))
        print('Você errou o número do sorteio...\nReinicie para tentar novamente.')
print('\nObrigado por jogar :)')
