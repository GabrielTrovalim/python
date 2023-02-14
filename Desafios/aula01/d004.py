inf = input('Digite algo: ') # Recebendo um input do usuário.

print('')
if (inf.isnumeric() == True): print('Sua informação é numérica') # isnumeric entre outros sempre retornam true ou false, por isso podemos utilizar um if else.
else: print('Sua informação não é numérica')

if (inf.isalpha() == True): print('Sua informação é alfabética')
else: print('Sua informação não é alfabética')

if (inf.isalnum() == True): print('Sua informação é alfanumérica')
else: print('Sua informação não é alfanumérica')

if (inf.isupper() == True): print('Todas as letras estão em caixa alta')
else: print('Nem todas as letras estão em caixa alta')