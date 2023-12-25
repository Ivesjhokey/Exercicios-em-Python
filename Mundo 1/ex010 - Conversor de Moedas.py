'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar'''

real = float(input('quantos reais voce tem?: '))
dolar = real / 3.27
ivesreal = real / 1000000
print('com {} reais voce pode comprar {} dolares'.format(real, dolar))
print('com {} reais voce pode comprar {} ivesreal'.format(real, ivesreal))
