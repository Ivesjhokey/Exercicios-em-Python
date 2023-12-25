n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
md = (n1 + n2) / 2
if md >= 7:
    print('aprovado')
elif md < 5:
    print('reprovado')
elif 5 < md < 6.9:
    print('recuperação')
