from time import sleep
nome = str(input('\nDigite o nome do cliente: ')).strip().title()
v_casa = float(input('Diga o valor da casa que o cliente pretende comprar: \nR$'))
salario = float(input('Por favor, informe o salário do cliente: \nR$'))
q_anos = int(input('Quantidade de anos para a divida ser quitada: '))
# contas:
v_parcela = v_casa / (q_anos * 12)
porcent = salario * 0.3 # 30% do salário do cliente.
sleep(1)
print('\nInformações guardadas')
print('Calculando...')
sleep(2)
if (v_parcela > porcent):
    print('\nInfelizmente o empréstimo foi negado...\nO valor de R${:.2f} mensais ultrapassam 30% do salário do cliente.'.format(v_parcela))
else:
    print('\nO seu pedido de empréstimo foi aceito!\nValor mensal a pagar: R${:.2f}\nQuantidade de parcelas: {}'.format(v_parcela, q_anos * 12))
print('\nTenha um ótimo dia, {}!'.format(nome))
