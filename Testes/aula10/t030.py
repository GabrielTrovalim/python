from math import floor
valor = int(input('Digite um valor entre R$1 e R$250:\nR$'))
if valor>=1 and valor <=250:
    vint = valor / 20 # verificando a quantidade de notas de 20 possíveis para o valor inserido
    if floor(vint) < 1: # caso a quantidade de notas de 20 seja menor que 1, o programa tenta com notas de 5
        fiv = valor / 5
        if fiv < 1: # se a quantidade de notas de 5 também seja menor que 1, o programa diz que não é possível devolver nenhuma nota de 5 ou de 20
            print('O valor digitado foi R${:.2f} e esse valor não pode ser preenchido por notas de R$5 e nem notas de R$20.'.format(valor))
        else:
            notas_5 = (floor(fiv) * 2) * 2.5
            resto = valor - notas_5
            print('O valor digitado foi R${:.2f}, esse valor pode ser preenchido por {} notas de R$5, com isso faltam R${:.2f} para completar o valor inserido.'.format(valor, floor(fiv), resto)) # caso o valor inserido passe dos primeiros testes o programa calcula o resto de acordo com o valor e quantidade das notas de 5 possíveis
    else: # caso o valor inserido passe de R$20 o programa começa a devolver notas de 20
        notas20 = (floor(vint) * 2) * 10
        #print(notas20)
        rest = valor - notas20
        #print(rest)
        if rest >=5: # e se o resto for maior ou igual a R$5 o programa devolve notas de 20 e notas de 5, considerando um resto além disso.
            five = rest / 5
            notas5 = (floor(five) * 2) * 2.5
            rest2 = rest - notas5
            print('O valor digitado foi R${:.2f}, esse valor pode ser preenchido por {} notas de R$20, e {} notas de R$5, com isso faltam R${:.2f} para completar o valor inserido.'.format(valor,floor(vint),floor(five), rest2))
        else:
            print('O valor digitado foi R${:.2f}, esse valor pode ser preenchido por {} notas de R$20, com isso faltam R${:.2f} para completar o valor inserido.'.format(valor, floor(vint),rest))
else: # caso um valor menor que R$1 ou maior que R$250 for digitado o programa devolve essa mensegem de erro.
    print('\nO valor inserido R${:.2f} é inválido, tente novamente.'.format(valor))