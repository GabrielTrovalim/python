num = int(input('Digite um número entre 0 e 9999: '))
if (num > 9999): print('Você digitou um número fora do esperado.')
else:
    uni = num // 1 % 10
    dez = num // 10 % 10
    cent = num // 100 % 10
    mili = num // 1000 % 10 
    print('O número digitado foi: {}'.format(num))
    print('\nMilhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(mili, cent, dez, uni))