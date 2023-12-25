n1 = float(input('digite um numero: '))
n2 = float(input('digite um outro numero: '))
if n1 > n2:
    print('{} é o maior, {} é o menor'.format(n1, n2))
elif n1 == n2:
    print('ambos tem o mesmo valor')
else:
    print('{} é o maior, {} é o menor'.format(n2, n1))
