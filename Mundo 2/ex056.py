imedia = 0
velho = ''
idadevelho = 0
mulheres = 0
for c in range(1, 4):
    n1 = input('nome da {} pessoa'.format(c))
    i1 = int(input('idade da {} pessoa'.format(c)))
    p1 = (input('sexo da {} pessoa'.format(c)))

    if c == 1 and p1 == 'masculino':
        velho = n1
        idadevelho = i1
    elif p1 == 'masculino' and i1 > idadevelho:
        velho = n1
        idadevelho = i1
    elif p1 == 'feminino' and i1 < 20:
        mulheres = mulheres + 1
    imedia = imedia + i1

print(mulheres, 'mulheres tem menos de 20 anos')
print(imedia/3, 'é a media de peso do grupo')
print(velho, 'é o mais velho e tem ', idadevelho,'anos de idade')
