# Primeiro elemento da p.a -> de onde parte o nosso programa.
# Razão da p.a -> passo da contagem
num_pa = int(input('\nDigite o primeiro termo: '))
ra = int(input('Digite a razão da p.a: '))
calc = (ra * 10) + num_pa
for c in range(num_pa,calc,ra):
    print(c)