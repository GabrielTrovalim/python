from datetime import date
from time import sleep
at_ano = date.today().year
ano_nasc = int(input('Em que ano o atleta nasceu? '))
age = at_ano - ano_nasc # Diz a idade de acordo com o ano do s.o
print('\nVerificando...')
sleep(1)
if (age < 0):
    print('\n[ERRO] A idade de {} anos não corresponde a uma idade real.\nReinicie o programa para tentar novamente.'.format(age))
elif (ano_nasc < 0):
    print('\n[ERRO] A idade de {} anos não corresponde a uma idade real.\nReinicie o programa para tentar novamente.'.format(age))
elif (ano_nasc < (at_ano - 100)):
    print('\n[ALERTA] Provavelmente a pessoa indicada não pratica mais esportes por ter uma idade avançada ({}).\nCaso essa pessoa ainda pratique esportes pode ser considerado(a) \033[0;35mMASTER\033[m.'.format(age))
else:
    if (age < 10):
        print('\nO atleta indicado é considerado um atleta \033[0;31mMIRIM\033[m.')
        print('Por ter {} anos em {}.'.format(age, at_ano))
    elif (age < 15):
        print('\nO atleta indicado é considerado um atleta \033[0;32mINFANTIL\033[m.')
        print('Por ter {} anos em {}.'.format(age, at_ano))
    elif (age < 20):
        print('\nO atleta indicado é considerado um atleta \033[0;33mJUNIOR\033[m.')
        print('Por ter {} anos em {}.'.format(age, at_ano))
    elif (age < 25):
        print('\nO atleta indicado é considerado um atleta \033[0;34mSÊNIOR\033[m.')
        print('Por ter {} anos em {}.'.format(age, at_ano))
    else: 
        print('\nO atleta indicado já pode ser considerado um atleta \033[0;35mMASTER\033[m.')
        print('Por ter {} anos em {}.'.format(age, at_ano))
sleep(1)
print('\nFim da verificação.\nTenha um bom dia!\n')