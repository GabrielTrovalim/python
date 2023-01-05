# obj: mostrar o preço original de um produto e depois o seu desconto de 5%
# Se o preço original é 100 precisamos multiplicalo por 0.05

msg = str('\nCAIXA\n')
bar = str('=')

print('{:^40}'.format(msg))
print('{:=^39}\n'.format(bar))

pre = float(input('Informe o preço do produto: R$'))

dec = pre * 0.05
totn = pre - dec

print('\nO sub total é igual a R${:.2f} \nCom desconto de 5%, O total é de R${:.2f}\n'.format(pre, totn))