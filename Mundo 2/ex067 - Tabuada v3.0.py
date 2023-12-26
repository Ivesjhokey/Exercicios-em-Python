'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
   O programa será interrompido quando o número solicitado for negativo'''

# faça uma tabuada com 'while' # tentativa 1 jhokey

while True:
    n1 = int(input('escolha um numero para tabuada: '))
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{n1} x {c} = {n1 * c}')

# alternativa 2 jhokey

while True:
    n1 = int(input('escolha um numero para tabuada: '))
    if n1 < 0:
        break
    n2 = 0
    while True:
        if n2 == 10:
            break
        n2 += 1
        print(f'{n1} x {n2} = {n1 * n2}')
