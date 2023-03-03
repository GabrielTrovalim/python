from time import sleep
print('\nOs números pares de 1 a 50 são:\n')
sleep(1)
for c in range(1, 51):
    if (c % 2 == 0): # Se o número for par, mostre o contador.
        print(c)
# se o resto da divisão por 2 for zero, o número é par
# Resto de divisão -> % Igual -> ==