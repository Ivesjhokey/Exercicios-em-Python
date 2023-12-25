"""Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)"""


def notas(*valores, sit=False):
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
