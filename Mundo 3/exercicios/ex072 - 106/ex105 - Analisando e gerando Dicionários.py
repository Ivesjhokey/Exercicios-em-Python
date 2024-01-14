"""Faça um programa que tenha uma função notas() que pode receber várias
   notas de alunos e vai retornar um dicionário com as seguintes informações:
   – Quantidade de notas
   – A maior nota
   – A menor nota
   – A média da turma
   – A situação (opcional)
   - Adicione também as docstring"""

#Alternativa guanabara
def notas(*n, sit=False):
    '''Função Para analisar notas e situações de varios alunos.
       :parametro n: uma ou mais notas dos alunos(aceita várias).
       :parametro sit: valor opcional, indicando se deve ou não adicionar a situação.
       :return: dicionário com várias informações sobre a situação da turma.'''

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(9.5, 6.5, 4.5, sit=True)
print(resp)

#Alternativa Jhokey
'''Faça um programa que tenha uma função notas() que pode receber várias
   notas de alunos e vai retornar um dicionário com as seguintes informações:
   – Quantidade de notas
   – A maior nota
   – A menor nota
   – A média da turma
   – A situação (opcional)
   - Adicione também as docstring'''

def notas(*valores, sit=False):
    '''Função Para analisar notas e situações de varios alunos.
    :parametro valores: uma ou mais notas dos alunos(aceita várias).
    :parametro sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.'''

    final = {}
    total = len(valores)
    final['total'] = total
    contador = 0
    maior = max(*valores)
    final['maiornota'] = maior
    menor = min(*valores)
    final['menornota'] = menor
    for c in range(0, len(valores)):
        contador = contador + valores[c]
    media = contador / len(valores)
    final['media'] = media
    if sit:
        if media > 7:
            final['situação'] = 'ivesjhokey'
        elif media > 4:
            final['situação'] = 'razoavel'
        else:
            final['situação'] = 'ruim'
    return final

resp = notas(5.5, 2.5, 10, sit=True)
print(resp)
