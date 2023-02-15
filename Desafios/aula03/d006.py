nume = float(input('Digite um número: '))

dob = nume * 2 # Dobro do número.
trip = nume * 3 # Triplo do número.
raiz = nume ** (1/2) # Raiz quadrada do número.

print('O numero digitado é: {:.1f}\nSeu dobro é: {}\nSeu triplo é: {}\nSua raiz quadrada é: {:.1f}'.format(nume, dob, trip, raiz))