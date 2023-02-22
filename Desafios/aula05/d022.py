num = int(input('Digite um número entre 0 e 9999: '))
if (num > 9999): print('Você digitou um número fora do esperado.')
else: 
    snum = str(num)
    print('\nO número digitado foi {}'.format(num))
    print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(snum[3], snum[2], snum[1], snum[0]))