print('\nVocê está andando em uma estrada, enquanto pilota o seu carro...\n')
km = float(input('\nA quantos KM/h você passou pelo radar? '))
if (km <= 0 or km >= 400):
    print('Velocidade invalida. Valor negativo, nulo, ou a cima da capacidade de um carro...')
else:    
    if(km > 80):
        multa = (km - 80) * 7
        print('\nVocê ultrapassou o limite de velocidade da estrada.\nSua velocidade: {}km/h\nValor a pagar pela multa: R${:.2f}\n'.format(km, multa))
    else: 
        print('\nVelocidade detectada: {}km/h\nVocê está dentro do limite de velocidade da estrada!\nBoa viagem!\n'.format(km))