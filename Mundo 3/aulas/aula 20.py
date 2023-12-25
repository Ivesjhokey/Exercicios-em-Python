# ESTUDANDO DEF EM PYTHON, UMA DEF É UMA FUNÇÃO QUE PODEMOS UTILIZAR PARA FACILITAR A VIDA
# INVES DE ESCREVER PRINT ('-' * 30) VARIAS VEZES, BASTA CHAMAR E FUNÇÃO

# METODO SEM DEF
"""print('-' * 30)
print('PROGRAMA PRINCIPAL')
print('-' * 30)
print('-' * 30)
print('IVESJHOKEY')
print('-' * 30)
print('-' * 30)
print('PROGRAMADOH')
print('-' * 30)

linha = str('-' * 30)
print(linha)
print(linha)
print('PROGRAMA PRINCIPAL')
print(linha)
print(linha)
print('IVESJHOKEY')
print(linha)
print(linha)
print('PROGRAMADOH')
print(linha)"""


# UTILIZANDO A DEF
"""def linha():
    print('-' * 30)


linha()
print('PROGRAMA PRINCIPAL')
linha()

linha()
print('IVESJHOKEY')
linha()

linha()
print('PROGRAMADOH')
linha()


def titulo():
    print('-' * 30)
    print('PROGRAMA PRINCIPAL')
    print('-' * 30)


titulo()"""


# ALEM DISSO PODEMOS PASSAR PARAMETROS PARA A DEF PARA FACILITAR MAIS AINDA
"""def titulo(algo):
    print('-' * 30)
    print(algo)
    print('-' * 30)


titulo('aqui dentro da chave escrevemos algo, ou passamos algum parametro')"""


# INCLUSIVE DA PARA PASSAR UMA DEF DENTRO DA OUTRA
"""def linha():
    print('-' * 30)


def titulo(algo):
    linha()
    print(algo)
    linha()


titulo('aqui dentro da chave escrevemos algo, ou passamos algum parametro')"""


# AQUI VAMOS PASSAR ALGUNS PARAMETROS PARA A DEF
"""# AQUI SERIA SEM A DEF
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)


def soma(a, b):
    s = a + b
    print(s)


# AQUI USAMOS A DEF SOMA E PASSAMOS OS PARAMETROS 'A' E 'B'
soma(4, 5)
soma(8, 9)
soma(2, 1)

# MAS PODERIAMOS TAMBEM INFORMAR QUAIS SAO OS VALORES A E B
soma(a=4, b=5)
soma(b=8, a=9)
soma(b=2, a=1)

# OBS COMO PASSAMOS DOIS PARAMETROS PARA A DEF, SE INFORMARMOS APENAS UM PARAMETRO OU MAIS QUE 2, IRA DAR ERRO
soma(a=4)
soma(4)

# OBS SE INFORMARMOS 1 PARAMETRO, TEMOS QUE INFORMAR TODOSO OU TAMBEM DARA ERRO
soma(a=4, 5)"""


# O PYTHON TEM UM CONCEITO DE EMPACOTAR E DESEMPACOTAR PARAMETROS
"""def contador(*numero):   # esse (*numero) quer dizer para desempacotar algo que foi recebido, no caso sao os numeros
    print(numero)           # aqui eu mandei printar o que ele desempacotou que sao os valores de contador


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)


def contador(*numero):
    for c in numero:
        print(c, end=' ')
    print()


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)


def contador(*numero):
    print(f'os numeros digitados foram {numero}, e sao ao todo {len(numero)} numeros')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)


def contador(*numero):
    tam = len(numero)
    print(f'os numeros digitados foram {numero}, e sao ao todo {tam} numeros')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

# OUTRA MANEIRA DE DESEMPACOTAR SERIA:
def contador(*numero):
    soma = 0
    for c in numero:
        soma += c
    print(f'somando os valores {numero} temos {soma}')


contador(5, 7, 3, 1, 4)"""


# AQUI IREMOS UZAR O CONCEITO ANTERIOR, POREM COM LISTAS E IREMOS APRENDER UM COMANDO PARA DOBRAR VALORES DE UMA LISTA
"""def dobra(n1):
    pos = 0
    while pos < len(n1):
        n1[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)

outrosnumero = [13, 3, 0]
dobra(outrosnumero)
print(outrosnumero)"""


# FAZER UM ULTIMO PROGRAMA MAS AGORA COM O WHILE
"""def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('fim')


contador(2, 10, 2)"""
