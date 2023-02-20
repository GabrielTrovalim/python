import math #Importando a biblioteca de matemática para o python.
num = int(input('Digite um número: '))
raiz = math.sqrt(num) # Utilizando a função sqrt da biblioteca math.
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # Formatando raiz com .ceil para arredondar o resultado de uma raiz para cima.