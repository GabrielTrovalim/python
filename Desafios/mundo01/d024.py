city = str(input('Digite o nome da sua cidade: ')).strip()
up = city.upper()
proc = up.find('SANTO')

if proc == 0: print('\nO nome da sua cidade começa com a palavra "Santo" ')
else: print('\nO nome da sua cidade não começa com a palavra "Santo" ')
