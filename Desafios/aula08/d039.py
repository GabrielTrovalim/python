from datetime import date
from time import sleep
ano_atual = date.today().year # Pegando o ano atual do S.O
sex = str(input('Informe o seu sexo.\n[m] para MASCULINO\n[f] para FEMININO\nSua resposta: ')).strip().upper()
if (sex == 'F'):
    print('\nO alistamento militar obrigatório só convoca pessoas do sexo masculino.\nVocê não precisa se preocupar com isso.\n')
elif (sex == 'M'):
    ano_nasc = int(input('Em que ano você nasceu? '))
    age = ano_atual - ano_nasc # Idade do usuário.
    dezoito = age - 18 # Descobre quantos anos se passaram ou que faltam até os 18, com base na idade atual - 18.
    data = ano_atual - dezoito # Descobre em que ano essa pessoa fez ou fará 18 anos, com base no ano de seu aniversário de 18 anos.
    print('\nVerificando...')
    sleep(2)
    if (age > 18):
        print('\nCom {} anos, você já passou pelo alistamento militar.'.format(age))
        print('Você se apresentou ao exercito a {} anos, em {}.'.format(dezoito, data))
    elif (age < 18):
        print('\nCom {} anos, você ainda não passou pelo alistamento militar.'.format(age))
        print('Você se apresentará ao exercito daqui {} anos, em {}, boa sorte!'.format(dezoito * -1, data))
    else:
        print('\nCom {} anos, você já tem idade para fazer o alistamento militar.'.format(age))
        print('Você deverá se apresentar ao exercito nesse ano ({}), boa sorte!'.format(data))
    sleep(1)
    print('\nObrigado pela verificação da data do seu alistamento.\nTenha um ótimo dia!\n')
else:
    print('\n[ERRO] entrada de dados invalida. Tente novamente.')
