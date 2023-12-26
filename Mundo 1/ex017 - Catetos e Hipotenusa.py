'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
   calculo e mostre o comprimento da hipotenusa'''

from math import sqrt, hypot
n1 = float(input('digite o cateto oposto: '))
n2 = float(input('digite o cateto adjacente: '))
n3 = n1**2 + n2**2
print(sqrt(n3))

n1 = float(input('digite o cateto oposto: '))
n2 = float(input('digite o cateto adjacente: '))
n3 = hypot(n1, n2)
print(n3)
