'''Faça um programa que leia um frase pelo teclado e mostre:
   1: quantas vezes aparece a letra 'a'.
   2: em que posição ela aparece a primeira vez.
   3: em que posição ela aparece a ultima vez.'''

frase = input('digite uma frase: ').strip().upper()
print('a letra A aparece {} vezes'.format(frase.count('A')))
print('a letra A aparece pela primeira vez na posição {}'.format(frase.find('A')))
print('a letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A')))
