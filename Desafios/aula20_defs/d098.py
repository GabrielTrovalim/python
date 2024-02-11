from time import sleep
def conta():

    print('Contagem de 0 a 10 com passo = 1')
    for c in range (0,11,1):
        print('{}'.format(c),end=' ')
    print('\nContagem de 10 a 0 com passo = 2')
    for ci in range (10,-1,-2):
        print('{}'.format(ci),end=' ')

def conte(ori,fim,pas):
    fimt = fim + 1
    fimtn = fim - 1
    if ori > fim:
        if pas <= -1:
            for cf in range (ori, fimtn, pas):
                print('{}'.format(cf),end=' ')
        elif pas == 0:
            for cf in range (ori, fimtn, -1):
                print('{}'.format(cf),end=' ')
        else:
            for cf in range (ori,fimtn,-pas):
                print('{}'.format(cf),end=' ')
    else:
        if pas == 0:
            for cf in range (ori, fimt, 1):
                print('{}'.format(cf),end=' ')
        else:
            for cf in range (ori, fimt, pas):
                print('{}'.format(cf),end=' ')


conta()
sleep(0.5)
print('\nAgora é a sua vez de escolher os dados.\n')
conte(ori= int(input('Digite a origem: ')),fim= int(input('Digite o fim da contagem: ')), pas= int(input('Digite o passo da contagem: ')))
