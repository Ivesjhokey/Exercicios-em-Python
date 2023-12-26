'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
   Para salários superiores a R$1.250,00, calcule um aumento de 10%.
   Para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('digite seu salario: '))
if salario > 1250:
    salario = (salario + ((salario/100) * 10))
    print('seu novo salario é:', salario)
else:
    salario = (salario + ((salario/100) * 15))
    print('seu novo salario é:', salario)
