print('\nQual é o maior número?\n')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número:  '))
num3 = float(input('Digite o terceiro número: '))
if(num1 > num2 and num1 > num3): 
    print('\nO primeiro número é o maior')
else:
    if(num2 > num1 and num2 > num3):
        print('\nO segundo número é o maior')
    else:
        print('\nO terceiro número é o maior')
if(num1 < num2 and num1 < num3):
    print('\nO primeiro número é o menor')
else:
    if(num2 < num1 and num2 < num3):
        print('\nO segundo número é o menor')
    else:
        print('\nO terceiro número é o menor')
