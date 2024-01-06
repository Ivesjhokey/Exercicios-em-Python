'''Faça um programa que tenha uma função chamada área(), que receba
   as dimensões de um terreno retangular(largura e comprimento) e
   mostre a área do terreno.'''

def area(a, b):
    print('controle de terrenos')
    c = a * b
    print(f'a area de um terreno de {a}m x {b}m = {c}m²')


n1 = float(input('largura: '))
n2 = float(input('altura: '))
area(n1, n2)
