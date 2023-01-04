m = float(input('informe um valor em metros: '))

cm = m * 100
mm = m * 1000

print('\nO valor informado em metros é: {:.2f} m'.format(m))
print('\nConvertendo esse valor para centímetros, temos: {:.2f} cm \nE convertendo esse valor para milímetros, temos {:.2f} mm'.format(cm, mm))
