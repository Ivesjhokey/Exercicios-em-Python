'''Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento'''

salario = float(input('digite seu salario: '))
aumento = ((salario/100) * 15)
final = salario + aumento
print('seu salario e {}$, com o aumento de 15% passara a ser {}$'.format(salario, final))
