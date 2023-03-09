cho = 'S' # escolha para continuar calculando.
while cho == 'S':
    p_pa = int(input('\nDigite o primeiro termo da p.a: '))
    ra = int(input('Digite a razão da p.a: '))
    print('') # espaço improvisado.
    n = p_pa - ra
    calc = (ra * 9) + p_pa
    cont = 0 # contador.
    while n < calc:
        n += ra
        cont += 1
        print('{:3}° termo da p.a: {}'.format(cont, n))
    cho = str(input('\nVocê gostaria de tentar novamente? [S/N]: ')).upper().strip()
print('\nMuito obrigado, tenha um bom dia!\n')