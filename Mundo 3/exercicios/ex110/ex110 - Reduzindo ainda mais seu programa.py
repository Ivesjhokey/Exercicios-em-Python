"""Adicione ao módulo moedars.py criado nos desafios anteriores, uma
   função chamada resumo(), que mostre na tela algumas informações geradas
   pelas funções que já temos no módulo criado até aqui."""

import Moedarss

n1 = int(input('digite um valor: '))
n3 = int(input('digite o aumento: '))
n4 = int(input('digite a redução: '))
n2 = str(input('quer converter "." para ","? [sim],[nao]: ')).lower()
print(Moedarss.resumo(n1, n2, n3, n4))
