sal = float(input('\nInforme o seu salário (em real): '))

pct = sal * 0.15
tot = sal + pct

print('\nO seu salário de R${:.2f} recebeu um aumento de 15%, agora você vai passar a receber R${:.2f}\n'.format(sal, tot))