#calculo de área:
#versão final.
def area():
    base = float(input('Digite o valor da largura: '))
    alt = float(input('digite o valor da comprimento: '))

    calc = base * alt

    print('O valor da área do terreno de largura {}m e comprimento {}m é igual a: {}m²'.format(base,alt,calc))


area()