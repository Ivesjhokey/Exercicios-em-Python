'''Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usúario tentar descobrir
   qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuário venceu ou perdeu'''

from random import randint

print('acerte o numero da sorte que o computador esta pensando de 1 - 5.')
n1 = int(input('digite um numero: '))
n2 = randint(1, 5)

if n1 == n2:
    print('o numero da sorte é {}, parabéns!'.format(n2))
else:
    print('voce errou!')
