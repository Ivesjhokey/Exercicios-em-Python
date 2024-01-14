"""Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando."""


from utilidadescursoemvideo import Moeda

n1 = int(input('digite um valor: '))
n3 = int(input('digite o aumento: '))
n4 = int(input('digite a redução: '))
n2 = str(input('quer converter "." para ","? [sim],[nao]: ')).lower()
print(Moeda.resumo(n1, n2, n3, n4))
