cho = 0 # Contador da escolha
n1 = 0 # contador do primeiro valor
n2 = 0 # contador do segundo valor

num1 = float(input('\nDigite o primeiro valor: '))
n1 += num1
num2 = float(input('Digite o segundo valor: '))
n2 += num2
    # menu:
while cho != 5:
    print('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa.')
    cho = int(input('Sua escolha: '))
    if cho == 1:
        print('\nO resultado da soma entre {} e {} é igual a: {}'.format(num1, num2, (n1 + n2)))
    elif cho == 2:
        print('\nO resultado da multiplicação entre {} e {} é igual a: {}'.format(num1, num2, (n1 * n2)))
    elif cho == 3:
        if n1 > n2:
            print('\nO maior valor digitado foi: {}'.format(n1))
        elif n1 == n2:
            print('\nOs dois valores são iguais.')
        else:
            print('\nO maior valor digitado foi: {}'.format(n2))
    elif cho == 4:
        n1 -= num1
        n2 -= num2
        num1 = float(input('\nDigite o primeiro valor: '))
        n1 += num1
        num2 = float(input('\nDigite o segundo valor: '))
        n2 += num2
        print('\nOs valores foram alterados para {} e {}, respectivamente.'.format(n1, n2))
print('\nVocê saiu do programa!')