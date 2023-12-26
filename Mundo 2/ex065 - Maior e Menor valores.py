'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
   e qual foi o maior e o menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''

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
