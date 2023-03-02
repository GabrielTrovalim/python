from time import sleep
print('-=' * 20)# faz 40 sinais.
print('{:^40}'.format('Calculadora'))
print('=-' * 20)
pt_1 = float(input('Digite o primeiro número: '))
# operações simples possíveis.
print('\nEscolha a operação a se fazer\n[+] Somar\n[-] Subtrair\n[X] Multiplicar\n[/] Dividir\n')
sinal = str(input('Sua opção: ')).upper() # Guarda a operação escolhida.
pt_2 = float(input('\nDigite o segundo número: '))
print('\nCalculando o seu resultado...')
sleep(2)
if (sinal == '+'):
    resu_soma = pt_1 + pt_2
    print('\nResultado:\n {:.1f} + {:.1f} = {:.1f}'.format(pt_1, pt_2, resu_soma))
    sleep(1)
    print('\nObrigado por testar, tenha um bom dia!\n')
elif (sinal == '-'):
    resu_sub = pt_1 - pt_2
    print('\nResultado:\n {:.1f} - {:.1f} = {:.1f}'.format(pt_1, pt_2, resu_sub))
    sleep(1)
    print('\nObrigado por testar, tenha um bom dia!\n')
elif (sinal == 'X'):
    resu_mult = pt_1 * pt_2
    print('\nResultado:\n {:.1f} X {:.1f} = {:.1f}'.format(pt_1, pt_2, resu_mult))
    sleep(2)
    print('\nObrigado por testar, tenha um bom dia!\n')
elif (sinal == '/'):
    resu_div = pt_1 / pt_2
    print('\nResultado:\n {:.1f} / {:.1f} = {:.1f}'.format(pt_1, pt_2, resu_div))
    sleep(2)
    print('\nObrigado por testar, tenha um ótimo dia!\n')
else:
    print('\n[ERRO] entrada de dados invalida. Tente novamente!\n')
    sleep(2)
    print('FIM')