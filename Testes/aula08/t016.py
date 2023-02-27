v_casa = float(input('Qual é o valor da casa?\nR$'))
salario = float(input('Informe o seu salário:\nR$'))
t_casa = int(input('Em quantos anos você pretende pagar a divida? '))
ano = 12 # 12 meses no ano.
prest_men = v_casa / (t_casa * ano)
trin_porcent = salario * 0.3
cont = trin_porcent + salario


print('Com o valor da casa em R${:.2f} sendo pago em {} anos, você terá prestações mensais de R${:.2f}'.format(v_casa, t_casa, prest_men))
print('{:.0f} com 30% de aumento você passa a ter {:.2f}'.format(trin_porcent, cont))