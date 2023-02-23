import random
from time import sleep # Importando a função sleep que faz o computador esperar.
u_num = int(input('\nDigite um número de 0 a 5: '))
if(u_num > 5 or u_num < 0): # Valindando a entrada de dados do usuário.
    print('[ERRO] Entrada de dados invalida.')
else:
    print('\nProcessando...')
    sleep(2) # esperando dois segundos.
    num = random.randint(0 ,5) # Faz o computador sortear um número.
    if(u_num == num):
        print('\nO número sorteado foi: {}'.format(num))
        print('Você acertou o número sorteado!')
    else:
        print('\nO número sorteado foi: {}'.format(num))
        print('Você errou o número do sorteio...\nReinicie para tentar novamente.')
print('\nObrigado por jogar :)')
