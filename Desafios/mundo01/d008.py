m = float(input('\ninforme um valor em metros: '))

dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000

print('\nO valor informado em metros é: {:.2f} m'.format(m))
print('{:.2f} m em dm é igual a: {:.0f} \n{:.2f} m em cm é igual a: {:.0f} \n{:.2f} m em mm é igual a: {:.0f} \n{:.2f} m em dam é igual a: {:.1f} \n{:.2f} m em hm é igual a: {:.2f} \n{:.2f} m em km é igual a: {:.3f}\n'.format(m, dm, m, cm, m, mm, m, dam, m, hm, m, km))
