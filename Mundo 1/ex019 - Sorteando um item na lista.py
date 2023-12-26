'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
   Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''

import random
n1 = input('digite o nome do primeiro aluno: ')
n2 = input('digite o nome do segundo aluno: ')
n3 = input('digite o nome do terceiro aluno: ')
n4 = input('digite o nome do quarto aluno: ')
n5 = [n1, n2, n3, n4]
print(random.choice(n5))
