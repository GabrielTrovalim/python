#teste de contador usando def

def cont(*num):
    tam = len(num)
    print('Em {} temos {} números.'.format(num,tam))


cont(1,2,3,4,5)