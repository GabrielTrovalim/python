from time import sleep
print('\nCalculador de IMC\n')
altura = float(input('Informe a sua altura em metros: '))
peso = float(input('Informe o seu peso em Kg: '))
print('\nCalculando o seu IMC...')
sleep(2)
if (altura <= 0 or peso <= 0):
    print('\033[0;31m[ERRO]\033[m Valor invalido.\nReinicie o programa para tentar novamente.')
else:
    imc = peso / (altura ** 2) # Apenas após a validação da entrada de dados é possível fazer o calculo.
    if (imc < 18.5): 
        print('\nO seu IMC é igual a: {:.1f}.\nVocê se encontra a \033[0;33mbaixo do peso\033[m ideal para a sua altura.'.format(imc))
    elif (imc < 24.99):
        print('\nO seu IMC é igual a: {:.1f}.\nVocê se encontra no \033[0;32mpeso ideal\033[m para a sua altura!'.format(imc))
    elif (imc < 29.99):
        print('\nO seu IMC é igual a: {:.1f}.\nVocê se encontra com \033[0;33msobrepeso\033[m para a sua altura.'.format(imc))
    else:
        print('\nO seu IMC é igual a: {:.1f}.\nVocê se encontra em estado de \033[0;31mobesidade\033[m para a sua altura.'.format(imc))
sleep(1)
print('\nFim do calculo de IMC.\nObrigado por participar <3.\n')