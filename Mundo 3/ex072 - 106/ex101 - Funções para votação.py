'''Crie um programa que tenha uma função chamada voto() que vai receber
   como parâmetro o ano de nascimento de uma pessoa, retornando um valor
   literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
   nas eleições.'''

from datetime import datetime
# aqui utilizamos a importaçãp global, mas poderiamos importar apenas no local


def voto(b):
    # from datetime import datetime , assim por exemplo
    a = datetime.now().year - b
    if 16 <= a < 18:
        return 'voto opcional'
    elif 18 <= a < 60:
        return 'voto obrigatorio'
    elif a >= 60:
        return 'voto opcional'
    else:
        return 'voto negado'


n1 = voto(int(input('digite seu ano de nascimento: ')))
print(n1)
