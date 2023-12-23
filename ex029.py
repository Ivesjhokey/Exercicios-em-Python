n1 = int(input('digite a velocidade do carro em km/h: '))
if n1 > 80:
    print('voce foi multado!\na multa vai custar 7$ por cada km acima do limite.\nsua multa é: {}$'.format((n1-80)*7))
print('voce nao sera multado se nao passar de 80km/h')
