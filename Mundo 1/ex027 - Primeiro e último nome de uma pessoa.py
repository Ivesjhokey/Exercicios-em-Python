'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
   ex: Ana Maria de Souza
   ex: priomeiro = Ana
   ex: ultimo = Souza'''

nome = input('digite um nome: ').strip().upper()
nome = nome.split()
print(nome[0])
print(nome[-1])
