# Para um número ímpar: num % 2 == 1
# Para um número divisivel por 3: num % 3 == 0
s = 0 
cont = [] # armazena a quantidade de números.
for c in range(3, 501, 6):
    s += c
    cont.append(c)
print('\nA soma dos {} valores solicitados é: {}'.format(len(cont), s))
