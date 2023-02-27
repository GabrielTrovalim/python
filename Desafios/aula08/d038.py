from time import sleep
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
print('\nVerificando...')
sleep(2)
if (num1 > num2): 
    print('\nO primeiro valor ({:.1f}) é maior que o segundo valor ({:.1f}).'.format(num1, num2))
elif (num1 == num2):
    print('\nOs dois valores digitados são iguais.')
else:
    print('\nO segundo valor ({:.1f}) é maior que o primeiro valor ({:.1f})'.format(num2, num1))
sleep(1)
print('\nObrigado por testar!')