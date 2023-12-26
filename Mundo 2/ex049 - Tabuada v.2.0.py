'''Refaça o desafio 009, mostrando a tabuada de um número que o usuario escolher, só que agora utilizando um laço 'for'.'''

n1 = int(input('escolha um numero para tabuada: '))
for c in range(1, 11):
    print(n1 * c)
