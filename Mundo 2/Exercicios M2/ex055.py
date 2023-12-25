maior = 0
menor = 1000000
for c in range(1, 4):
    n1 = float(input('digite o peso da {}° pessoa: '.format(c)))
    if n1 >= maior:
        maior = n1
    if n1 <= menor:
        menor = n1
print('o maior é', maior)
print('o menor é', menor)

# melhor alternativa

maior = 0
menor = 0
for c in range(1, 4):
    n1 = float(input('digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = n1
        menor = n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
print('o maior é', maior)
print('o menor é', menor)
