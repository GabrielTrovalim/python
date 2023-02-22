import math # Chamando a biblioteca de matemática.
cata = float(input('\nDiga qual é o cateto a: '))
catb = float(input('Diga qual é o cateto b: '))
hipo = math.hypot(cata, catb) # Utilizando a função hypot para o calculo da hipotenusa.
print('\nO valor da hipotenusa é igual a: {:.2f}'.format(hipo))