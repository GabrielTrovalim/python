arm = 1 # aramzenador.
par = 0 # cont. para par.
imp = 0 # cont. para ímpar.
while arm != 0:
    arm = int(input('Digite um número: '))
    if arm % 2 == 0 and arm != 0:
        par += 1
    elif arm % 2 == 1 and arm != 0:
        imp += 1
print('\nA quantidade de números pares digitados foi: {}.\nJá a quantidade de números ímpares digitados foi: {}.'.format(par, imp))