'''Crie um programa onde o usuário possa digitar sete valores numéricos
   e cadastre-os em uma lista única que mantenha separados os valores
   pares e ímpares. No final, mostre os valores pares e ímpares
   em ordem crescente'''

# alternativa 1 jhokey
valores = []

for c in range(0, 7):
    valores.append(int(input(f'digite o {c+1} valor: ')))
print('os valores pares são: ', end='')
for c in valores:
    if c % 2 == 0:
        print(f'{c}', end=' ')
print()
print('os valores impares são: ', end='')
for c in valores:
    if c % 2 == 1:
        print(f'{c}', end=' ')

# alternativa 2 jhokey
valores = [[], []]
for c in range(0, 7):
    n1 = int(input(f'digite o {c+1} valor: '))
    if n1 % 2 == 0:
        valores[0].append(n1)
    else:
        valores[1].append(n1)
valores[0].sort()
valores[1].sort()
print(f'os valores pares são: {(valores[0])}')
print(f'os valores impares sao: {valores[1]}')
