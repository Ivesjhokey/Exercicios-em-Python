from datetime import date
n1 = int(input('digite um ano qualquer ou 0 para o ano atual: '))
if n1 == 0:
    n1 = date.today().year
if n1 % 400 == 0:
    print('ele é bissexto')
else:
    print('ele nao é bissexto')
