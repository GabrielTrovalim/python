print('-=' * 20)
print('Analisador de triângulos')
print('=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:  '))
r3 = float(input('Terceiro segmento: '))
if (r1 > (r2 + r3) or r2 > (r1 + r3) or r3 > (r1 + r2)):
    print('\nOs segmentos apresentados não são capazes de formar um triângulo...')
else:
    print('\nOs segmentos apresentados conseguem formar um triângulo!')