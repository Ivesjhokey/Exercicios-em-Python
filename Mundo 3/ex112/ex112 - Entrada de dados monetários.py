'''Dentro do pacote utilidadescursoemvideo que criamos no desafio 111, temos
   um módulo chamado Dado. Crie uma função chamada leiaDinheiro() que seja capaz
   de funcionar como a funçao input(), mas com uma validação de dados para aceitar
   apenas valores que sejam monetários.'''

from ex111.utilidadescursoemvideo import Dado, Moeda

n1 = Dado.leiadinheiro('digite um valor: ')
Moeda.resumo(n1)
