# nesta aula vamos aprender a utilizar o interactive help
# aprender oque sao as docstrings
# funçoes com argumentos opcionais
# escopo de variaveis
# funçoes que retornam resultados


# interactive help
"""primeiro vamos relembrar que todo
nome com parentese no final é uma funçao
ex: help(), print(), etc.

se escrevermos help no console
ele abre um novo pesquisador para
voce digitar o que vc esta procurando
por exemplo, se vc chamar a funçao help
e escrever print em seguida
ele ira mostrar todos os comendos relacionados
com a funçao print e para que servem esses comandos

com isso podemos usar o help para saber
para que serve qualquer coisa dentro do python
e para sairmos do modo interactive help
utilizamos o comando quit, que ele retorna
para o modo normal do console

tambem podemos utilizar o comando help
dentro do quadro negro para pedirmo ajuda
por exemplo, dentro do quadro escrevemos
help(print) e rodamos, e ela mostrara no console
para que serve a funçao que vc esta com dificuldade

outra maneira de descobrir as informaçoes do que vc quer
voce pode usar inves do help o doc
que seria por exemplo, print(input.__doc__)
que seria a mesma coisa help(input)

podemos utilizar o help em praticamente tudo
por exemplo:

def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('fim')


contador(2, 10, 2)

nao sei oque sao esses parametros dentro de contador
entao podemos utilizar help(contador)
mas nao ira mostrar tao bem assim nao
mas ja da uma ajuda.

para ficar mais facil ainda podemos utilizar as docstrings
que seria fazer um documento apos alguma função para
explicar como funciona determinada função
e para isso precisamos utilizar 3 aspas duplas no inicio e no fim
por exemplo:

#def contador(i, f, p):

#    3 aspas duplas aqui
#    faz um contagem e mostra na tela
#    :param i: inicio da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    3 aspas duplas aqui

#    c = i
#    while c <= f:
#        print(f'{c}', end=' ')
#        c += p
#    print('fim')
#
#
#contador(2, 10, 2)
#help(contador)
"""


# agora vamos falar sobre parametros opcionais
"""os parametros opcionais seria dar um valor para algum parametro
caso esse parametro nao receber nenhum valor, por exemplo:

def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('fim')


contador(2, 10)
eu so dei 2 valores e o contador pede 3
entao ira dar erro a nao ser que eu de um valor
para eles, caso eles nao receberem nenhum valor
e seria algo assim:

def contador(i, f, p=0):
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('fim')


contador(2, 10)
nesse caso eu disse que p = 0
ou seja, se nao receber um valor por
parametro, ele ira adicionar o valor 0
a variavel p, fazendo o programa funcionar
e sendo assim poderiamos dar valores opcionais
para todas as variaveis dentro do parametro
por exemplo:

def contador(i=0, f=0, p=0):
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('fim')


contador(2, 10, 2)
sendo assim se nao tiverem valor nenhum
e a função for chamada, ele usara os valores
opcionais
"""


# agora vamos falar sobre escopo de variaveis
"""o escopo de variaveis seria onde uma variavel so existe
dentro de um determinado local e nao no programa inteiro
por exemplo:

n1 = 10 se eu fizer isso fora de qualquer função ou laço
ou o que quer que seja, ela vai ser uma variavel global
mas agora se for mais ou menos assim: 

n1 = 10
def teste():
    x=0
    print(n1)
    print(x)
    

teste()         aqui ela ira chamar a def teste e ira printar
                tanto o n1 quanto o x, porem so printara o x
                pois foi chamada a funçao

print(n1)       aqui ela ira printar n1 normalmente pois ela
                é uma variavel global

print(x)        aqui a variavel nao ira printar pois
                ela so existe dentro da def
                
                
vamos colocar essa merda pra funcionar:
n1 = 10


def teste():
    x = 0
    print(f'na função teste n1 vale {n1}')
    print(f'na função teste x vale {x}')


teste()
print(f'no programa principal n1 vale {n1}')
#print(f'no programa principal x vale {x}') e issso aqui da erro
#porque x nao existe no programa principal, apenas na função


# se por um acaso fizessemos isso
n1 = 10


def teste():
    n1 = 100
    x = 0
    print(f'na função teste n1 vale {n1}')
    print(f'na função teste x vale {x}')


teste()
print(f'no programa principal n1 vale {n1}')
#print(f'no programa principal x vale {x}') e issso aqui da erro
#porque x nao existe no programa principal, apenas na função

#se declararmos uma variavel dentro de uma def
ela so existira la dentro, podendo ser qualquer nome e valor
por exemplo n1 dentro e n1 fora sao variaveis diferentes
pois n1 fora vale n1 normal, e n1 dentro da def pode valer
um outro valor definido, se por algum acaso nao
nada n1 tanto dentro quanto fora sera o mesmo valor
e so para lembrar as variaveis dentro das def que vem do programa
principal, sao apenas copias

#inclusive existe tambem escopo para bibliotecas
podendo por exemplo fazer uma biblioteca funcionar so dentro
de uma determinada def e nao em todo o programa
concluimos que podemos ter importaçao global e local


outra coisa que temos que falar guanabara arrombado
so falou isso agora e tive que voltar aqui fazer as merdas
das anotaçoes, entao:
mesmo com o programa tendo a variavel global e a local
é possivel mudar o valor da variavel global dentro de um local
ou seja mudar o valor global dentro da def
com o comando "global"
vamos por esta merda em pratica

n1 = 10


def teste():
    global n1
    n1 = 100
    x = 0
    print(f'na função teste n1 vale {n1}')
    print(f'na função teste x vale {x}')


teste()
print(f'no programa principal n1 vale {n1}')
# percebesse que agora o valor que retorna é 100
# pois dentro da def alteramos o n1 global e nao apenas
# um valor copiado de n1, que seria o famoso n1 local
"""


# agora vamos falar sobre retorno de valores
"""as funçoes em python podem nao retornar um valor
e imprimir dentro delas mesmas, ou podem 
retornar um valor, e para isso usamos
o comando RETURN por exemplo:


# percebemos nesse codigo que o valor S retorna para
# a variavel que chamou a funçao somar


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(1, 2, 3)
r2 = somar(4, 5, 6)
r3 = somar(7, 8, 9)
print(f'as somas deram {r1}, {r2}, {r3}')"""


# agora vamos fazer exercicios
"""
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c  # ou f = f * c
    return f


f1 = fatorial(5)
f2 = fatorial(6)
f3 = fatorial()
print(f1, f2, f3)
n = int(input('digite um numero: '))
print(f'o fatorial de {n} = {fatorial(n)}')


# aqui vamos pedir para retornar nao apenas numeros
# e sim retornar outras coisas como valores logicos ou
# verdadeiro e falso e etc


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


n1 = par(8)
print(n1)


def par(num=0):
    if num % 2 == 0:
        return 'é par'
    else:
        return 'é impar'


numero = int(input('digite um numero: '))
print(par(numero))

# isso aqui daria a mesma coisa
#numero = int(input('digite um numero: '))
#n1 = par(numero)
#print(n1)

# isso aqui daria a mesma coisa
#n1 = par(int(input('digite um valor: ')))
#print(n1)

#isso aqui seria a mesma coisa
#n1 = int(input('digite um valor: '))
#n1 = par(n1)
#print(n1)

# ou seja podemos usar o return para retornar 
valores logicos, verdadeiros e falsos, strings e etc


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('digite um valor: '))
if par(num):
    print('é par!')
else:
    print('nao é par!')
    
# nesse codigo se ele retorna verdadeiro
# escreve par e se retorna falso, escreve 
# que nao é par"""
