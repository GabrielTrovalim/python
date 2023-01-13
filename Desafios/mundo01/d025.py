nome = str(input('Digite o seu nome: '))
proc = 'Silva' in nome
proc1 = 'silva' in nome

if proc == True: print('O seu nome contém Silva')
elif proc1 == True: print('O seu nome contém silva')
else: print('O seu nome é {} e não contém o sobrenome silva'.format(nome))