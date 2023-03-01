from time import sleep
num = int(input('Digite um número inteiro: '))
print('[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if (opcao == 1):
    print('\nO número {} convertido em binário é: {}.'.format(num, bin(num)[2:]))
elif (opcao == 2):
    print('\nO número {} convertido em octal é: {}.'.format(num, oct(num)[2:]))
elif (opcao == 3):
    print('\nO número {} convertido em hexadecimal é: {}.'.format(num, hex(num)[2:]))
else:
    print('\n[ERRO] entrada de dados invalida.\n')
    sleep(2)
    print('Reinicie o programa!')
