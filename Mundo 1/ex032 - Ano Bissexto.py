'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

n1 = int(input('digite um ano qualquer: '))
if n1 % 400 == 0:
    print('ele é bissexto')
else:
    print('ele nao é bissexto')
