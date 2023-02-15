origip = float(input('\nQual o preço do produto? \nR$'))
desc = origip * (5/100) # Calculando os 5% de desconto no produto.
newprec = origip - desc

print('\nDetectamos um desconto de 5% para o seu produto.\nPreço original de R${:.2f}\nDesconto de R${:.2f} \nNovo preço a pagar: R${:.2f}'.format(origip, desc, newprec))