'''faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta nescessária para pintá-la, sabendo que cada
    sabendo que cada litro de tinta, pinta uma área de 2m²'''

largura = float(input('digite quanto tem de largura em metros: '))
altura = float(input('digite quanto tem de altura em metros: '))
area = largura * altura
tinta = area / 2
print('para pintar uma parede {} metros quadrados, seram nescessarios {} litros de tinta'.format(area, tinta))
print('se cada litro pintar 2 metros quadrados')
