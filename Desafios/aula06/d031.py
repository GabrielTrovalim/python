km = float(input('\nQual a distância da sua viagem em km? '))
if(km <= 0):
    print('[erro] Valor invalido...')
else:
    if(km <= 200):
        cont = km * 0.50
        print('\nViajando {}KM você irá pagar: R${:.2f}'.format(km, cont))
    else:
        cont2 = km * 0.45
        print('\nViajando uma distância maior que 200km você recebe um desconto de 0,05 centavos!\nCom uma viagem de {}KM você irá pagar: R${:.2f}'.format(km, cont2))
print('\nObrigado por escolher a nossa companhia de viagens!\n')