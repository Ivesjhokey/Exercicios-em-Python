'''Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''

from math import radians, sin, cos, tan
n1 = float(input('digite um angulo: '))
print(sin(radians(n1)))
print(cos(radians(n1)))
print(tan(radians(n1)))
