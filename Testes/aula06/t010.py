nome = str(input('Qual é o seu nome? ')).strip().title()
big = nome.upper()
if (big == 'GABRIEL'): 
    print('\nNossa, que nome lindo!')
else:
    print('\nAcho o seu nome meio comum demais...')

print('\nBom dia, {}, foi um prazer te conhecer!'.format(nome))