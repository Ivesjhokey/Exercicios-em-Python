'''Aprimore o desafio anterior, mostrando no final:
   A- A soma de todos os valores pares digitados.
   B- A soma dos valores da terceira coluna.
   C- O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'digite o valor da posição [{linha}][{c}]: '))
for linha in range(0, 3):
    for c in range(0, 3):
        if matriz[linha][c] % 2 == 0:
            somapar = somapar + matriz[linha][c]
        print(f'[{matriz[linha][c]:^4}]', end='')
    print()

print(f'a soma dos numeros pares é {somapar}')
print(f'o maior valor da segunda linha é {max(matriz[1])}')
print(f'a soma dos valores da terceira coluna é '
      f'{matriz[0][2]+matriz[1][2]+matriz[2][2]}')
