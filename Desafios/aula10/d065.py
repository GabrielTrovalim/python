from time import sleep
n = 1 # controle.
soma = 0
cont = 0 # contador de laços.
print('\n[ATENÇÃO] Para encerrar digite 0\n')
sleep(2)
while n != 0:
    num = int(input('Digite o {}° número inteiro: '.format(cont + 1)))
    if num == 0:
        n -= 1
        
    else:
        soma += num
        cont += 1
if cont == 0:
    print('\nNenhum número foi inserido, fora o comando de parada.')
elif cont == 1:
    media = soma / cont # media de todos os números digitados.
    print('\nO único número digitado foi: {:.0f}'.format(media))
else:
    media = soma / cont
    print('\nA média de todos os {} números digitados é: {:.2f}'.format(cont, media))