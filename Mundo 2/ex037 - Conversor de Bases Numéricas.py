'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
   1 para binário
   2 para octal
   3 para hexadecimal'''

import math
n1 = int(input('digite um numero: '))
c1 = input('selecione a conversão do numero: binario, octal, hexadecimal: ').lower()
if c1 == 'binario':
    print(bin(n1))
elif c1 == 'octal':
    print(oct(n1))
elif c1 == 'hexadecimal':
    print(hex(n1))
else:
    print('tente novamente')
print('fim de programa')
