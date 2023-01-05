num = int(input('Digite um número inteiro: '))

dob = (num * 2)
tri = (num * 3)
rq = num**(1/2)

print('\nO número que você digitou foi: {} \nO dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.2f}.'.format(num, num, dob, num, tri, num, rq))