"""Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando."""


from ex111.utilidadescursoemvideo import Moeda5

n1 = float(input('Digite o preço: R$: '))
Moeda5.resumo(n1, 10, 10)
