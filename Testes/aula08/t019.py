from time import sleep
print('-=' * 20)# faz 40 sinais.
print('{:^40}'.format('Calculadora'))
print('=-' * 20)
pt_1 = float(input('Digite o primeiro número: '))
# operações simples possíveis.
print('\nEscolha a operação a se fazer\n[+] Somar\n[-] Subtrair\n[X] Multiplicar\n[/] Dividir\n')
sinal = str(input('Sua opção: ')) # Guarda a operação escolhida.
pt_2 = float(input('\nDigite o segundo número: '))
print('\nCalculando o seu resultado...')
sleep(2)
if (sinal == '+'):
    resu_soma = pt_1 + pt_2
    print('\nResultado:\n {:.1f} + {:.1f} = {:.1f}\n'.format(pt_1, pt_2, resu_soma))
    sleep(1)
    print('\nObrigado por testar, tenha um bom dia!\n')
else:
    print('oi')