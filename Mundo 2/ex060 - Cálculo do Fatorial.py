'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
   Ex: 5! = 5x4x3x2x1 = 120'''

# alternativa 1 jhokey

from math import factorial
n1 = 1
while n1 != 0:
    f1 = int(input('digite um numero: '))
    print(factorial(f1))
    n1 = int(input('sair[0] continuar[1]'))
print('fim')

# alternativa 2 jhokey

n1 = int(input('digite um valor: '))
mult = n1 - 1
pare = False
print('{}X'.format(n1), end='')
while not pare:
    n1 = n1 * mult
    print(mult, end='')
    mult = mult - 1
    if mult != 0:
        print(end='X')
    else:
        pare = True
print(' = {}'.format(n1))

# alternativa 3 jhokey

n1 = int(input('digite um valor: '))
mult = n1
pare = False
while not pare:
    print(mult, end=' ')
    if mult != 1:
        print(end='X ')
        mult -= 1
    else:
        pare = True
    n1 = n1 * mult
print('= {}'.format(n1))

# alternativa 1 guanabara

n = int(input('digite um valor para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c  #f = f * c
    c -= 1  #c = c - 1
print('{}'.format(f))

# alternativa 2 guanabara

n = int(input('digite um valor para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print(c, end=' ')
    if c > 1:
        print(end='X ')
    else:
        print('=', end=' ')
    f *= c  #f = f * c
    c -= 1  #c = c - 1
print('{}'.format(f))
