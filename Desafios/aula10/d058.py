from random import randint
num_pc = randint(0,10)
print(num_pc)
num = int(input('Tente adivinhar o número: '))
if num == num_pc:
    print('\nParabéns você ganhou!')
else:
    while num != num_pc:
        print('\nOps, parece que você errou...')
        num = int(input('Tente novamente: '))
    print('\nParabéns você ganhou!')