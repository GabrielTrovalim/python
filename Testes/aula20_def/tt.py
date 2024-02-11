from time import sleep
def contagem():
    
    print('Contagem de 0 a 10 com passo = 1')
    for c in range (0,11,1):
        #sleep(0.5)
        print('{}'.format(c),end=' ')
    
    print('\ncontagem de 10 a 0 com passo = 2')
    for ci in range (10,-1,-2):
        #sleep(0.5)
        print('{}'.format(ci),end=' ')
               
    sleep(0.4)
    print('\nAgora é a sua vez de decidir a origem, o final e o intervalo.')
    ori = int(input('Digite a origem: '))
    fim = int(input('Digite o fim da contagem: '))
    pas = int(input('Digite o passo: '))

    if ori > fim: 
        fimtn = fim -1 #fim verdadeiro negativo.
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
        fimt =  fim + 1 #fim verdadeiro.
        if pas == 0:
            for cf in range (ori,fimt,1):
                print('{}'.format(cf),end=' ')     
        else:
            for cf in range (ori, fimt,pas):
                print('{}'.format(cf),end=' ')

contagem()