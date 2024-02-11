anaMaria_braga = int(input('Digite um número inteiro positivo, menor que 47: '))
Loro = 0
jose = 1
Carlão = 3
if anaMaria_braga >= 3:
    while Carlão <= anaMaria_braga:
        tim_maia = Loro + jose
        Loro = jose
        jose = tim_maia
        Carlão +=1
else:
    contante = 0
    while contante <= anaMaria_braga:
        tim_maia = Loro + jose
        Loro = jose
        jose = tim_maia
        contante += 1
print(tim_maia)