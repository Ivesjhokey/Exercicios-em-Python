'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
   Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''

import random
n1 = input('digite o nome do primeiro aluno: ')
n2 = input('digite o nome do segundo aluno: ')
n3 = input('digite o nome do terceiro aluno: ')
n4 = input('digite o nome do quarto aluno: ')
n5 = [n1, n2, n3, n4]
random.shuffle(n5)
print(n5)
