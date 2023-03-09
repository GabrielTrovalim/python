cho = 'S' # controlador de inicio.
while cho == 'S':
    p_pa = int(input('\nDigite o primeiro termo da p.a: '))
    ra = int(input('Digite a razão da p.a: '))
    print('') 
    n = p_pa - ra
    calc = (ra * 9) + p_pa
    cont = 0 # contador.
    while n < calc:
        n += ra
        cont += 1
        print('{:3}° termo da p.a: {}'.format(cont, n))
    qst = str(input('\nVocê gostaria de ver termos mais a frente? [S/N]: ')).strip().upper()
    if qst == 'N':
        cho = 'N' # fechamento do programa.
    else:
        quantidade = int(input('Quantos termos você gostaria de acrescentar? '))
        #print(n)
        cont2 = cont # continuação do contador.
        n2 = n 
        calc2 = (ra * quantidade) + n
        while n2 < calc2:
            n2 += ra
            cont2 += 1
            print('{:3}° termo da p.a: {}'.format(cont2, n2))
        cho = str(input('\nVocê gostaria de reiniciar o programa? [S/N]: ')).strip().upper()    
print('\nObrigado por experimentar o programa. Tenha um bom dia!\n')
