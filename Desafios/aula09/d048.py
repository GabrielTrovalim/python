# Para um número ímpar: num % 2 == 1
# Para um número divisivel por 3: num % 3 == 0
for c in range(1, 501):
    if (c % 2 == 1 and c % 3 == 0):
        print(c)
print('\nFIM')