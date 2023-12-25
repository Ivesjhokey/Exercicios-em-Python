n1 = float(input('digite um segmento: '))
n2 = float(input('digite um segmento: '))
n3 = float(input('digite um segmento: '))

if (n1 - n2) < n1 < (n2 + n3) and (n1 - n3) < n2 < (n1 + n3) and (n1 - n2) < n3 < (n1 + n2):
    print('podem formar um triangulo')
else:
    print('não podem formar um triangulo')
