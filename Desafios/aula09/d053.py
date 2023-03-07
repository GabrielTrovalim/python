frase = str(input('Digite uma frase: ')).upper().strip()
final = frase.capitalize()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
if(junto == inverso):
    print('\nA frase, {} é um palindromo.'.format(final))
else:
    print('\nA frase, {} não é um palindromo.'.format(final))