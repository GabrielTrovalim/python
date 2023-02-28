from time import sleep
print('\033[0;31m-=\033[m' * 20)
print('          NOTAS!')
print('\033[0;31m=-\033[m' * 20)

nota1 = float(input('\nDigite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
med = (nota1 + nota2) / 2
print('\nCalculando média...')
sleep(2)
if (nota1 > 10 or nota1 < 0):
    print('\n[ERRO] Entrada de dados invalida.\nReinicie o programa para tentar novamente.')
elif (nota2 > 10 or nota2 < 0):
    print('[ERRO] Entrada de dados invalida.\nReinicie o programa para tentar novamente.')
else:
    if (med >= 7):
        print('\nMédia do aluno: {}\nPrimeira nota: {}\nSegunda nota: {}\nSituação: Aprovado!'.format(med, nota1, nota2))
    elif (med < 5):
        print('\nMédia do aluno: {}\nPrimeira nota: {}\nSegunda nota: {}\nSituação: Reprovado, por média insuficiente.'.format(med, nota1, nota2))
    else:
        print('\nMédia do aluno: {}\nPrimeira nota: {}\nSegunda nota: {}\nSituação: Em recuperação.'.format(med, nota1, nota2))
print('\nFim da geração de boletim.\nTenha um bom dia!')