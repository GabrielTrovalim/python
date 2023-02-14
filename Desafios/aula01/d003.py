n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número para ser somado ao primeiro: '))
# Utilizando o tipo float, para aceitar números de ponto flutuante.
soma = n1 + n2
#print('\nA soma entre o número',n1,'e o número',n2,'é igual a:',soma)

# Nova versão de print:
print('\nA soma entre o número {} e o número {} é igual a: {}'.format(n1, n2, soma))