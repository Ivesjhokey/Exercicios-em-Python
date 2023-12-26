'''Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor'''

n1 = int(input('digite um numero: '))
n2 = int(input('digite um outro numero: '))
n3 = int(input('digite um outro numero: '))

if n3 < n1 > n2:
    print(n1, 'é o maior')
elif n3 < n2 > n1:
    print(n2, 'é o maior')
elif n1 < n3 > n2:
    print(n3, 'é o maior')

if n3 > n1 < n2:
    print(n1, 'é o menor')
if n3 > n2 < n1:
    print(n2, 'é o menor')
if n1 > n3 < n2:
    print(n3, 'é o menor')

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(maior)

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(menor)
