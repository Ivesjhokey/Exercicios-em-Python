'''Faça um programa que leia o nome de uma pessoa
    e mostre na tela uma mensagem de boas vindas'''

nome = input('qual seu nome: ')
print('ola', nome + '! prazer em te conhecer!')

nome = input('qual seu nome: ')
print('ola {}! prazer em te conhecer!'.format(nome))

nome = input('qual seu nome: ')
print(f'ola {nome} prazer em te conhecer!')
