nom1 = str(input('\nQual é o seu \033[41mnome\033[m? '))
age = int(input('Quantos anos \033[4;31mvocê\033[m tem? '))

print('\nO seu nome é \033[7;33;45m{}\033[m e você tem hoje \033[31;40m{} anos\033[m.'.format(nom1, age))
print('\033[4;34mTenha um bom dia!\033[m\n')