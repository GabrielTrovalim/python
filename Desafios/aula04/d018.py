import math # Importando a biblioteca de matemática.
ang = float(input('Digite o valor de um angulo: '))
sen = math.sin(math.radians(ang)) # Calculando o seno.
cose = math.cos(math.radians(ang)) # Calculando o cosseno.
tg = math.tan(math.radians(ang)) # Calculando a tangente.
print('Para o ângulo de {}° temos: \nSeno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}'.format(ang, sen, cose, tg))