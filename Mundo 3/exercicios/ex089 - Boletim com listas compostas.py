'''Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
   No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
   as notas de cada aluno individualmente'''

notas = []
temp = []
while True:
    nome = input('Digite o nome: ')
    nota1 = int(input('Digite a nota 1: '))
    nota2 = int(input('Digite a nota 2: '))
    media = (nota1 + nota2) / 2
    notas.append([nome, [nota1, nota2], media])
    temp.clear()
    n1 = input('Quer continuar S/N ?').upper()
    if n1 in 'Nn':
        break
for i, c in enumerate(notas):
    print(i, c[0], c[2])
while True:
    opc = int(input('mostrar notas de qual aluno? 999 interrompe: '))
    if opc == 999:
        break
    elif opc <= len(notas) - 1:
        print(f'as notas de {notas[opc][0]} sao: {notas[opc][1]}')
