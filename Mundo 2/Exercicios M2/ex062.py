n = int(input('digite um numero: '))
r = int(input('digite a razão: '))
c = 0
n1 = 10
contador = 0
while c < n1:
    contador += 1
    print(n, end=' ')
    n = n + r
    n1 -= 1
    if c == n1:
        n1 = int(input('\nquer mais algum termo? [0] para sair: '))
print('\nfim com {} termos mostrados'.format(contador))
