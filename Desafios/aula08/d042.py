print('\nDescreva um triângulo:\n')
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if (seg1 <= 0 or seg2 <= 0 or seg3 <= 0):
    print('\n[ERRO] Entrada de dados invalida.\nReinicie para tentar novamente.')
else:
    if (seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1):
        print('\nOs segmentos descritos são capazes de formar um triângulo!')
        if (seg1 == seg2 and seg1 == seg3 and seg3 == seg2):
            print('O triângulo formado pelos segmentos é do tipo: Equilátero.')
        elif (seg1 == seg2 or seg1 == seg3 or seg2 == seg3):
            print('O triângulo formado pelos segmentos é do tipo: Isósceles.')
        else: 
            print('Todos os lados do triângulo são diferentes, sendo do tipo: Escaleno.')
    else:
        print('\nOs segmentos descritos \033[0;31mnão\033[m são capazes de formar um triângulo...')