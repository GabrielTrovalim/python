import random
print('=-' * 20)
print(' ' * 15 + 'Joknepô'.upper())
print('-=' * 20)
jogada = str(input('Você tem as opções: "pedra", "papel" ou "tesoura".\nDigite a sua opção aqui: ')).strip().upper()
ops = ['pedra','papel','tesoura']
esco = random.choice(ops)
# Caminho da pedra.
if (jogada == 'PEDRA' and esco == ops[0]):
    print('\nO computador escolheu {}.'.format(esco))
    print('Você empatou.\nPedra com pedra.')
    print('\nObrigado por jogar!')
elif (jogada == 'PEDRA' and esco == ops[1]):
    print('\nO computador escolheu {}.'.format(esco))
    print('Você perdeu!\nPapel ganha de pedra.')
    print('\nObrigado por jogar!')
elif (jogada == 'PEDRA' and esco == ops[2]): 
    print('\nO computador escolheu {}.'.format(esco))
    print('Você ganhou!\nPedra quebra tesoura.')
    print('\nObrigado por jogar!')
# Caminho do papel.
elif (jogada == 'PAPEL' and esco == ops[0]):
    print('\nO computador escolheu {}.'.format(esco))
    print('Você ganhou!\nPapel ganha de pedra.')
    print('\nObrigado por jogar!')
elif (jogada == 'PAPEL' and esco == ops[1]):
    print('\nO computador escolheu {}.'.format(esco))
    print('Você empatou..\nPapel com papel.')
    print('\nObrigado por jogar!')
elif (jogada == 'PAPEL' and esco == ops[2]):
    print('\nO computador escolheu {}.'.format(esco))
    print('Você perdeu.\nTesoura corta papel')
    print('\nObrigado por jogar!')
#Caminho da tesoura.
elif (jogada == 'TESOURA' and esco == ops[0]):
    print('\nO computador escolheu {}.'.format(esco))
    print('Você perdeu.\nPedra quebra tesoura.')
    print('\nObrigado por jogar!')
elif (jogada == 'TESOURA' and esco == ops[1]):
    print('\nO computador escolheu {}.'.format(esco))
    print('Você ganhou!\nTesoura corta papel.')
    print('\nObrigado por jogar!')
elif (jogada == 'TESOURA' and esco == ops[2]):
    print('\nOcomputador escolheu {}.'.format(esco))
    print('Você empatou.\nTesoura com tesoura.')
    print('\nObrigado por jogar!')
else:
    print('\n[ERRO] Entrada de dados invalida')