nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

med = (nota1 + nota2)/2 # Média simples.
print('A sua média é igual a: {:.1f}'.format(med)) # A nota só mostrará duas casas após a virgula.
if (med > 7.0): print('Você está aprovado!')
else: print('Você está reprovado!')