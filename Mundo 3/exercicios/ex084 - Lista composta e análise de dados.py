'''Faça um programa que leia o nome e o peso de várias pessoas, guardando
   tudo em uma lista. No final, mostre:
   A- Quantas pessoas foram cadastradas
   B- Uma listagem com as pessoas mais pesadas
   C- Uma listagem com as pessoas mais leves'''

cadastradas = []
temporario = []
maior = menor = 0

while True:
    temporario.append(str(input('nome? ')))
    temporario.append(int(input('peso? ')))
    cadastradas.append(temporario[:])
    if maior == 0:
        maior = menor = temporario[1]
    elif temporario[1] > maior:
        maior = temporario[1]
    elif temporario[1] < menor:
        menor = temporario[1]
    temporario.clear()
    loop = str(input('quer continuar? [S/N]')).upper()
    if loop in 'nN':
        break

print(f'foram cadastradas {len(cadastradas)} pessoas')
print(f'o maior peso é {maior} de ', end='')
for pessoas in cadastradas:
    if pessoas[1] == maior:
        print(f'[{pessoas[0]}]', end=' ')
print()
print(f'o menor peso e {menor} de ', end='')
for pessoas in cadastradas:
    if pessoas[1] == menor:
        print(f'[{pessoas[0]}]', end=' ')
