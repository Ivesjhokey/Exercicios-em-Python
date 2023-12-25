# alternativa 1 jhokey
n = int(input('digite um numero: '))
r = int(input('digite a razão: '))
c = 1
n1 = 11
while c < n1:
    print(n, end=' ')
    n = n + r
    c += 1
print('fim')

# alternativa guanabara

primeiro = int(input('digite um numero: '))
razao = int(input('digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('fim')

# alternativa guanabara melhorada por jhokey

primeiro = int(input('digite um numero: '))
razao = int(input('digite a razão: '))
cont = 1
while cont <= 10:
    print(primeiro, end=' -> ')
    primeiro += razao
    cont += 1
print('fim')
