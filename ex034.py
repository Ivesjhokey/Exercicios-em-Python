salario = float(input('digite seu salario: '))
if salario > 1250:
    salario = (salario + ((salario/100) * 10))
    print('seu novo salario é:', salario)
else:
    salario = (salario + ((salario/100) * 15))
    print('seu novo salario é:', salario)
