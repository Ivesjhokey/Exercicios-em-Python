from datetime import date

ano = int(input('digite seu ano de nascimento\n'
                'para saber sua categoria: '))
at1 = date.today().year - ano
if at1 <= 9:
    print('mirim')
elif at1 <= 14:
    print('infaltil')
elif at1 <= 19:
    print('junior')
elif at1 <= 20:
    print('senior')
else:
    print('master')
print(at1)
