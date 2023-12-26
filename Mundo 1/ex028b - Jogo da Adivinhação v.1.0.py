'''Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usúario tentar descobrir
   qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep
import emote

jogo = str(input('quer jogar um jogo de adivinhação? |yes| or |no|''\n' + emote.lookup(':joystick:')*2)).lower()

if jogo.count('yes'):
    print(emote.lookup(':fog:') * 50)
    print('acerte o numero da sorte que o computador esta pensando de 1 - 5.')
    print(emote.lookup(':fog:') * 50)

    n1 = int(input('digite um numero: '))
    n2 = randint(1, 5)
    print('loading...')
    sleep(0.5)

    while n1 != n2:
        print('o numero da sorte é {}, tente novamente'.format(n2))
        n1 = int(input('digite um numero: '))
        n2 = randint(1, 5)

    print('o numero da sorte é {}, parabens!'.format(n2))
else:
    print('tudo bem, até logo')
print('fim de jogo!')
