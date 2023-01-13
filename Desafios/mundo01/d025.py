nome = str(input('Digite o seu nome: ')).strip()
up = nome.upper().strip()
name = nome.capitalize().strip()

proc = 'SILVA' in up

print('\nO seu nome é {}'.format(name))
if proc == True: print('\nO seu nome contém Silva')
else: print('\nO seu nome não contém o sobrenome silva')