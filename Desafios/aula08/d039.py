from datetime import date
ano_atual = date.today().year # Pegando o ano atual do S.O
ano_nasc = int(input('Em que ano você nasceu? '))
age = ano_atual - ano_nasc
if (age > 18): 
    print('Você provavelmente já se apresentou ao exercíto.')
elif (age < 18):
    print('Você ainda precisa se apresentar ao exercíto.')
else:
    print('Esse ano você se apresentará ao exercíto.')