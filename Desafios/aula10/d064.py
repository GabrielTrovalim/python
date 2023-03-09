from time import sleep
cho = 'S' # escolha de reiniciar.
while cho == 'S':
    no = 0
    soma = 0
    cont = 0
    print('\n[ATENÇÃO] Digite 999 para parar o programa.\n')
    sleep(2)
    while no != 999:
        num = int(input('Digite o {}° número inteiro: '.format(cont + 1)))
        if num == 999:
            no = 999
        else:
            soma += num
            cont += 1
    if cont == 0:
        print('\nNenhum número foi digitado, fora o comando de parada.')
    elif cont == 1:
        print('\nO único número digitado foi: {}'.format(soma))
    else:
        print('\nA soma de todos os {} números digitados é: {}'.format(cont, soma))
    cho = str(input('\nVocê deseja tentar de novo? [S/N]: ')).upper().strip()
print('\nMuito obrigado por testar o programa!\nTenha um ótimo dia.\n')