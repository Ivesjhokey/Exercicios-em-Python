"""Adicione ao módulo moedars.py criado nos desafios anteriores, uma
   função chamada resumo(), que mostre na tela algumas informações geradas
   pelas funções que já temos no módulo criado até aqui."""

from exercicios.ex110 import Moeda4

n1 = float(input('digite o preço: R$'))
Moeda4.resumo(n1, 10, 10)
