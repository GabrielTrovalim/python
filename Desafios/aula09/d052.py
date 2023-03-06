# se o número for par (exeto o 2) ele já não é primo.
# números primos são divididos só e somente por 1 e eles mesmos.
num = int(input('\nDigite um número inteiro: '))
if (num % 2 == 0 and num != 2):
    print('Número não primo')
else:
    if(num == 3):
        print('Número primo!')
    elif(num == 2):
        print('Número primo!')
    elif(num == 5):
        print('Número primo!')
    elif(num == 7):
        print('Número primo!')
    else:
        if(num % 7 == 0):
            print('Número não primo')
        elif(num % 3 == 0):
            print('Número não primo')
        elif(num % 5 == 0):
            print('Número não primo')
        else:
            print('Número primo!')