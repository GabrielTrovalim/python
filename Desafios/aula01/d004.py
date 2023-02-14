inf = input('Digite algo: ') # Recebendo um input do usuário.

print('')
print(type(inf))
if (inf.isnumeric() == True): print('Sua informação é numérica') # isnumeric entre outros sempre retornam true ou false, por isso podemos utilizar um if else.
else: print('Sua informação não é numérica')

if (inf.isalpha() == True): print('Sua informação é alfabética')
else: print('Sua informação não é alfabética')

if (inf.isalnum() == True): print('Sua informação é alfanumérica')
else: print('Sua informação não é alfanumérica')

if (inf.isupper() == True): print('Todas as letras estão em caixa alta')
else: print('As letras não estão totalmente em caixa alta')

if (inf.isspace() == True): print('Só há espaços nessa informação')
else: print('Há mais do que apenas espaços na sua informação')

if (inf.istitle() == True): print('Sua informação está capitalizada')
else: print('Sua informação não está capitalizada') # .istitle diz se a string condiz com um título (capitalizada) -> com a primeira letra maiúscula.