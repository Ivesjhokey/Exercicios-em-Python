'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha
   com valores lidos pelo teclado. No final, mostre a matriz na
   tela, com a formatação correta'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'digite o valor da posição [{linha}][{c}]: '))
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^4}]', end='')
    print()
