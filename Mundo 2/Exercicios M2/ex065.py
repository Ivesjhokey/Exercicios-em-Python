# alternativa 1 de jhokey

soma = cont = maior = menor = 0
parar = 1
while parar != 0:
    n1 = int(input('digite um numero: '))
    cont += 1
    soma = soma + n1
    if parar == 1:
        maior = menor = n1
        parar = 2
    elif n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1
    continuar = input('quer continuar? [S/N]: ').upper()
    if continuar == 'N':
        parar = 0
print('voce digitou {} vezes, e a soma é {}, o maior é {},'
      ' o menor é {}, e a media é {}'.format(cont, soma, maior, menor, soma/cont))

