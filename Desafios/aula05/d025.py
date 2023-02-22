frase = str(input('Escreva uma frase: ')).strip().capitalize().upper()
most = frase.title()
proc = frase.find('A') + 1
procf = frase.rfind('A') + 1
con = frase.count('A')
print('\nA frase: {}\nTem {} aparições da letra "A"\nA primeira aparição da letra "A" é na posição {}\nA última aparição da letra "A" foi na posição {}'.format(most, con, proc, procf))