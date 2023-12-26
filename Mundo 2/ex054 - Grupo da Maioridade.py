'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
   ainda não atingiram a maioridade e quantas ja são maiores'''

from datetime import date

adulto = 0
nadulto = 0
for c in range(1, 4):
    print(date.today().year)
    n1 = int(input('em que ano nasceu a {}° pessoa: '.format(c)))
    if date.today().year - n1 >= 18:
        adulto += 1
    else:
        nadulto += 1
print(adulto, 'sao adultos')
print(nadulto, 'nao sao adultos')
