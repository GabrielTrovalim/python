import emoji
import math

print(emoji.emojize("Usando pit :cérebro:", language='pt'))

catop = float(input('\nDigite o valor do cateto maior: '))
catad = float(input('\nDigite o valor do cateto melhor: '))

#A hipotenusa é calculada a partir do teorema de pitagoras, que leva a raiz da soma dos dos quadrados dos catetos.

hip = math.sqrt((catop**2) + (catad**2))

print(emoji.emojize('\nA hipotenusa é igual a: {:.2f} :astonished:'.format(hip), language='alias'))
