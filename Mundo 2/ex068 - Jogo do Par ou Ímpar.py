'''Faça um programa que jogue 'Par ou Ímpar' com o computador. O jogo só será interrompido quando o jogador perder, 
   mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''

from random import randint
venceu = 0
while True:
    pc = randint(0, 10)
    n1 = int(input('digite um valor: '))
    par = input('par ou impar?: ')
    if par == 'par':
        if (n1 + pc) % 2 == 0:
            print('parabens, voce venceu')
            venceu += 1
        else:
            print('game over')
            break
    elif par == 'impar':
        if (n1 + pc) % 2 == 1:
            print('parabens, voce venceu')
            venceu += 1
        else:
            print('game over')
            break
print(f'voce venceu {venceu} vezes seguidas')
