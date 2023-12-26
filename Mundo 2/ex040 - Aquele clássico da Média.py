'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
   Média abaixo de 5.0 = reprovado
   Média 5.0 e 6.9 = recuperação
   Média 7.0 ou superior = aprovado'''

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
md = (n1 + n2) / 2
if md >= 7:
    print('aprovado')
elif md < 5:
    print('reprovado')
elif 5 < md < 6.9:
    print('recuperação')
