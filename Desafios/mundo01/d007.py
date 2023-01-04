msg = str('\nCálculo de média\n')
bar = str('=')
print('{:^40}'.format(msg))
print('{:=^39} \n'.format(bar))

no1 = float(input('Digite a primeira nota: '))
no2 = float(input('\nDigite a segunda nota: '))

media = (no1 + no2)/2

print('\nA nota 1 do aluno foi: {:.2f} \nA nota 2 do aluno foi: {:.2f}'.format(no1, no2))
print('\nA média obitida pelo aluno foi de: {:.2f}'.format(media))
