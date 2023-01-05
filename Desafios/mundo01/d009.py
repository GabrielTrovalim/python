msg = str('\nTABUADA\n')

print('{:^40}'.format(msg))
print('=' * 20)

num = int(input('\nDigite um número para ver a sua tabuada: '))

v2 = num * 2
v3 = num * 3
v4 = num * 4
v5 = num * 5
v6 = num * 6
v7 = num * 7
v8 = num * 8
v9 = num * 9
v10 = num * 10

print('\nA tabuada do {} é:\n'.format(num))
print('=' * 15)
print('\n {} x {:2} = {:2}'.format(num, 1 ,num))
print('\n {} x {:2} = {}'.format(num, 2 ,v2))
print('\n {} x {:2} = {}'.format(num, 3 ,v3))
print('\n {} x {:2} = {}'.format(num, 4 ,v4))
print('\n {} x {:2} = {}'.format(num, 5 ,v5))
print('\n {} x {:2} = {}'.format(num, 6 ,v6))
print('\n {} x {:2} = {}'.format(num, 7 ,v7))
print('\n {} x {:2} = {}'.format(num, 8 ,v8))
print('\n {} x {:2} = {}'.format(num, 9 ,v9))
print('\n {} x {:2} = {} \n'.format(num, 10 ,v10))
print('=' * 15)
