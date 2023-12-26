'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
   Até 9 anos = mirim
   Até 14 anos = infantil
   Até 19 anos = junior
   Até 25 anos = sênior
   Acima = master'''

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
