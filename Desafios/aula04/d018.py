import math # Importando a biblioteca de matemática.
ang = int(input('Digite o valor de um angulo: '))
sen = math.sin(ang) # Calculando o seno.
cose = math.cos(ang) # Calculando o cosseno.
tg = math.tan(ang) # Calculando a tangente.
print('Para o angulo de {}° temos: \nSeno = {:.3f} \nCosseno = {:.3f} \nTangente = {:.3f}'.format(ang, sen, cose, tg))