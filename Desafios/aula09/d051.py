# Primeiro elemento da p.a -> de onde parte o nosso programa.
# Razão da p.a -> passo da contagem
num_pa = int(input('\nDigite o primeiro termo: '))
ra = int(input('Digite a razão da p.a: '))
calc = (ra * 10) + num_pa
cont = 0 # contador.
print('')
for c in range(num_pa,calc,ra):
    cont += 1
    #print(c)
    print('O {:2}° da P.A é: {}'.format(cont, c))