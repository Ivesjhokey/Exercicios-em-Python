'''Crie um programa que leia o nome completo de uma pessoa e mostre:
   1: o nome com todas as letras meiusculas e minusculas.
   2: quantas letras ao todo(sem considerar espeços).
   3: quantas letras tem o primeiro nome).'''

nome = input('digite seu nome: ')
print(nome.upper())
print(nome.lower())
print('seu nome tem ao todo sem considerar espaços {} letras'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('seu primeiro nome tem ao todo sem considerar espaços {} letras'.format(len(nome[0]) - nome[0].count(' ')))
