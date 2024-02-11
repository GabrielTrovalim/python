from time import sleep
def contagem():
    co = 0
    while co < 2:
        if co == 0:
            print('Contagem de 0 a 10 com intervalo = 1')
            for c in range (0,11,1):
                sleep(0.5)
                print('{}'.format(c),end=' ')
            co += 1
        else:
            print('\ncontagem de 10 a 0 com intervalo = 2')
            for ci in range (10,-1,-2):
                sleep(0.5)
                print('{}'.format(ci),end=' ')
                co += 1
    sleep(0.4)
    print('\nAgora é a sua vez de decidir a origem, o final e o intervalo.')
    ori = int(input('Digite a origem: '))
    fim = int(input('Digite o fim da contagem: '))
    pas = int(input('Digite o intervalo: '))
    fimt =  fim + 1 #fim verdadeiro.

    for cf in range (ori,fimt,pas):
        print('{}'.format(cf),end=' ')     


contagem()