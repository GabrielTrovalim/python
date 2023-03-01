from time import sleep
print('\033[0;31m-=\033[m' * 20)
print(' ' * 15 + 'Caixa')
print('\033[0;31m-=\033[m' * 20)
preco = float(input('\nInforme o valor do produto:\nR$'))
f_pag = str(input('\nInforme a forma de pagamento:\nAperte [d] para dinheiro à vista.\nAperte [c] para pagamento no cartão à vista.\nAperte [c2] para pagamento no cartão 2x.\nAperte [c3] para pagamento no cartão 3x.\nDigite aqui: ')).strip().upper()
print('\nVerificando...')
sleep(2)
if (f_pag == 'D'): # Opção no dinheiro à vista.
    desc = preco * 0.1
    descd = preco - desc
    print('\nVocê escolheu, dinheiro à vista!\nCom essa opção de pagamento você tem 10% de desconto.\nPreço original: R${:.2f}\nPreço c/ desconto: R${:.2f}'.format(preco, descd))
    sleep(2)
    print('\nObrigado pela preferência. Tenha um bom dia!\n')

elif (f_pag == 'C'): # Opção no cartão à vista.
    desco = preco * 0.05
    descc = preco - desco
    print('\nVocê escolheu, cartão à vista!\nCom essa opção de pagamento você tem 5% de desconto.\nPreço original: R${:.2f}\nPreço c/ desconto: R${:.2f}'.format(preco, descc))
    sleep(2)
    print('\nObrigado pela preferência. Tenha um bom dia!\n')

elif (f_pag == 'C2'): # Opção no crédito até 2x.
    parcela1 = preco / 2
    print('\nVocê escolheu, cartão em até 2x!\nValor das parcelas: R${:.2f} x2\nValor total: R${:.2f}'.format(parcela1, preco))
    sleep(2)
    print('\nObrigado pela preferência. tenha um bom dia!\n')

elif (f_pag == 'C3'): # Opção no crédito até 3x.
    juro = preco * 0.2
    juroc = preco + juro
    parcela2 = juroc / 3
    print('\nVocê escolheu, cartão em até 3x!\nCom essa opção de pagamento você tem 20% de juros.\nValor das parcelas: R${:.2f} x3\nValor total: R${:.2f}.'.format(parcela2, juroc))
    sleep(2)
    print('\nObrigado pela preferência. tenha um bom dia!\n')

else:
    print('\033[0;31m[ERRO]\033[m Opção invalida.\nReinicie o processo!\n')