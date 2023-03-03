p_pa = int(input('\nDigite o primeiro termo da p.a: ')) # Primeiro termo da p.a
r_pa = int(input('Digite a razão da p.a: ')) # Razão da p.a
rd = r_pa * 10
pd = (p_pa + 10) # quando a razão é igual a 1
dr = (r_pa * 10) + 16
if (r_pa > p_pa):
    for c in range (p_pa,rd,r_pa): # se r_pa for maior que p_pa
        print(c)
elif (r_pa == 1):
    for c in range (p_pa,pd,r_pa): # se a razão for igual a um
        print(c)
elif (r_pa < p_pa):
    for c in range (p_pa, dr, r_pa):
        print(c)