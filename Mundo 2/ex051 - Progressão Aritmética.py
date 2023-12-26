'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
   No final, mostre os 10 primeiros termos dessa progreção'''

n = int(input('digite um numero: '))
r = int(input('digite a razão: '))
for c in range(1, 11):
    print(n, end=' ')
    n = n + r

# melhor alternativa



