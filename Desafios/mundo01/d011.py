# área = altura x largura
# cada litro de tinta pinta 2m^2
# obj: dizer a quantidade de tinta necessária.

msg = str('\nQuantos litros de tinta a sua parede precisa para ser pintada?\n')
bar = str('=')

print('{:^60} \n {:=^69} \n'.format(msg, bar))
alt = float(input('Qual é a altura da sua parede? '))
larg = float(input('Qual é a largura da sua parede? '))

print('\n {:=^59} \n'.format(bar))

ar = alt * larg # Essa é a área da parede.
l = ar/2

print('A área da sua parede corresponde a {:.2f} metros quadrados'.format(ar))
print('\nCom essas medidas você vai precisar de {:.2f} litros de tinta'.format(l))