'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
   A multa vai custar R$7,00 por cada Km acima do limite'''

n1 = int(input('digite a velocidade do carro em km/h: '))
if n1 > 80:
    print('voce foi multado!\na multa vai custar 7$ por cada km acima do limite.\nsua multa é: {}$'.format((n1-80)*7))
print('voce nao sera multado se nao passar de 80km/h')
