print('\nQual é o maior e o menor número?\n')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número:  '))
num3 = float(input('Digite o terceiro número: '))
if(num1 > num2 and num1 > num3): # testando o num1.
    print('\nO maior valor digitado foi: {}'.format(num1))
else:
    if(num2 > num1 and num2 > num3): 
        print('\nO maior valor digitado foi: {}'.format(num2))
    else:
        print('\nO maior valor digitado foi: {}'.format(num3))
if(num1 < num2 and num1 < num3):
    print('O menor valor digitado foi: {}'.format(num1))
else:
    if(num2 < num1 and num2 < num3):
        print('O menor valor digitado foi: {}'.format(num2))
    else:
        print('O menor valor digitado foi: {}'.format(num3))
