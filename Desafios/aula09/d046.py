from time import sleep
from datetime import date
atual = date.today().year
# contagem regressiva:
print('\nVai começar a contagem regressiva.\n')
sleep(2) 
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\nFeliz ano novo!!\nFeliz {}!\n'.format(atual + 1))
