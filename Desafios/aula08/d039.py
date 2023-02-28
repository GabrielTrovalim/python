from datetime import date
from time import sleep
ano_atual = date.today().year # Pegando o ano atual do S.O
ano_nasc = int(input('Em que ano você nasceu? '))
age = ano_atual - ano_nasc # Idade do usuário.
dezoito = age - 18
data = ano_atual - dezoito
print('\nVerificando...')
sleep(2)
if (age > 18):
    print('\nCom {} anos, você já passou pelo alistamento militar.'.format(age))
    print('Você se apresentou ao exercito a {} anos, em {}.'.format(dezoito, data))
elif (age < 18):
    print('Com {} anos, você ainda não passou pelo alistamento militar.')
    
    
print(data)