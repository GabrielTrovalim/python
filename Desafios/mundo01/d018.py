import math

# Esse exercício relembra os conceitos matemáticos de seno cosseno e tangente do circulo trigonométrico, onde a vertical representa o sen, a horizontal o cos e a linha vertical externa ao circulo representa a tangente.

ang = float(input('Informe o ângulo: '))
sen = math.sin(math.radians(ang)) #O módulo para seno é .sin
cos = math.cos(math.radians(ang)) #O módulo para cosseno é .cos
tg = math.tan(math.radians(ang)) #O módulo para tangente é .tan

print('\nO ângulo informado foi {} \nSeu SENO é igual a {:.2f} \nSeu COSSENO é igual a {:.2f} \nSua TANGENTE é igual a {:.2f} \n'.format(ang, sen, cos, tg))