#Operadores.

nome = input('Qual é o seu nome? ')

print('\nPrazer em te conhecer {:^20}! - Centralizado'.format(nome))
print('\nPrazer em te conhecer {:>20}! - Na direita'.format(nome))
print('\nPrazer em te conhecer {:<20}! - Na esquerda'.format(nome))
print('\nPrazer em te conhecer {:=^20}! - Com iguais em volta'.format(nome))

