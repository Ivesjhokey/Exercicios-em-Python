'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
   O programa vai perguntar quantos jogos serão gerados e vai sortear
   6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

# alternativa 1 jhokey
from random import randint
lista = []
tempo = []
n1 = int(input('quantos jogos? '))
for n in range(0, n1):
    for j in range(0, 6):
        tempo.append(randint(1, 60))
    lista = tempo[:]
    tempo.clear()
    print(lista)

# alternativa 2 jhokey
lista = []
original = []
n1 = int(input('quantos jogos? '))
while n1 != 0:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        if len(lista) >= 6:
            n1 = n1 - 1
            break
    original.append(lista[:])
    lista.clear()
    original.sort()
for c in range(0, len(original)):
    print(original[c])
