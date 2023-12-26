'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar
   ao serviço militar, se é a hora de se alistar ou se ja passou do tempo do alistamento.
   Seu programa também devera mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('digite seu ano de nascimento: '))
if date.today().year - ano > 18:
    print('voce ja passou {} anos do tempo de alistamento'.format((date.today().year - ano) - 18))
elif date.today().year - ano == 18:
    print('ja esta na hora de voce se alistar no serviço militar')
else:
    print('voce deve se alistar no serviço militar em {} ano(s)'.format(((date.today().year - ano) - 18) * -1))
