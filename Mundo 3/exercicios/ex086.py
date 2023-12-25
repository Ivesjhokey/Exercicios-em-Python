matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'digite o valor da posição [{linha}][{c}]: '))
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^4}]', end='')
    print()
