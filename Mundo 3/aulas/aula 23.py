# aula sobre tratamento de erros
# aqui vamos falar sobre oque sao erros e exceçoes

# erros
"""
# erro de sintaxe
por exemplo, se escrevermos algum comando errodo, ele ira dar erro de sintaxe
um erro de escrita no comando, por exemplo primt, quando o correto seria print


# erro semantico
o erro semantico seria um erro de significado, quando voce por exemplo pede
para mostrar ou manipular alguma coisa, que nao esta definido, por exemplo:
print(x).
se nao declararmos a variavel x antes de pedir para escrevela, ele ira nos
mostrar um erro de significado, pois a variavel "x" ainda nao existe
"""


# exceçoes
"""
falando sobre exceçoes que muitas vezes vai ser confundido com erros, devemos sempre lembrar
que: erros sao sintaticos e semanticos, exceçoes sao coisas unicas que acontecem devido
a alguma causa ou consequencia.


como por exemplo se o programa nao deveria dar erro mas esta dando significa que nao temos um erro,
e sim temos um exceção. como por exemplo, n = int(input('digite um numero'))
se digitarmo um numero inteiro ele nao ira dar nenhum erro, mas se por algum acaso escrevermos 'oito'
ele ira dar um erro, pois ele esta definido para ler apenas numeros(int) e nao numeros por extenso(str).
ou seja, o comando nao esta errado, mas temos um problema, temos um exceção


entao podemos afirmar que erros e exceçoes sempre vao acontecer, como por exemplo tentar dividir
um valor por zero, ao tentar fazer isso ele ira dar um erro, mas o programa divide com qualquer valor
menos com o 0, entao podemos dizer que temos uma exceção e nao um erro, é um erro que acontece devido
a uma exceção.
"""


# exemplos de exceçoes
"""
a = b / c
entao c nao pode ser 0 para nao termos esta exceção
e tambem nao podemos pedir tentar = 3 / oito
pois possuem valores diferentes, 3 = int, oito = str, sendo assim daria uma exceção
de nao podermos dividir um numero por uma string


podemos dizer que as linguagens de programação tem diversas e diversas exceçoes
podendo sempre acabarmos nos deparando com diferentes exceçoes durante a execução dos programas.
e todas as exceçoes sao pertencentes a um tipo de exceção maior, que seria o Exception
"""


# exercicios de exceçoes
"""
e agora vamos mostrar como tratar as exceçoes com os comandos try, except.
ou seja: tente alguma coisa, se der erro faça alguma coisa.
exemplo:


try:
    a = int(input('digite o numerador: '))
    b = int(input('digite o denominador: '))
    c = a / b
except:
    print('infelizmente tivemos um erro')
print(c)


alem do try e do except, tambem podemos utilizar o else dentro do codigo
para nos dizer se o que tentamos deu certo. ex:

try:
    a = int(input('digite o numerador: '))
    b = int(input('digite o denominador: '))
    c = a / b
except:
    print('infelizmente tivemos um erro')
else:
    print(f'deu tudo certo, o resultado é {c}')


e para finalizar ainda temos o comando finally, que seria o finalmente
ele ira acontecer independente se deu certo ou errado meu programa
como por exemplo:


try:
    a = int(input('digite o numerador: '))
    b = int(input('digite o denominador: '))
    c = a / b
except:
    print('infelizmente tivemos um erro')
else:
    print(f'deu tudo certo, o resultado é {c}')
finally:
    print('tenha um bom dia')


agora vamos tratar o erro e mostrar o que aconteceu, caso der um erro
com o comando Exception.


try:
    a = int(input('digite o numerador: '))
    b = int(input('digite o denominador: '))
    c = a / b
except Exception as erro:
    print(f'o problema encontrado foi {erro.__class__}')   # aqui estou pedindo para mostrar qual a classe do erro
else:
    print(f'deu tudo certo, o resultado é {c:.1f}')
finally:
    print('tenha um bom dia')


inclusive, podemos ter mais de um except, um mesmo try pode ter varios except,
podemos tratar das exceçoes, analisando o tipo, a causa
e diversas outras coisas para sabermos o que houve com o programa. ex:


try:
    a = int(input('digite o numerador: '))
    b = int(input('digite o denominador: '))
    c = a / b
except ValueError:
    print(f'tivemos um problema de valor')   # aqui estou pedindo para mostrar qual a classe do erro
except ZeroDivisionError:
    print(f'nao podemos dividir por zero')
except KeyboardInterrupt:
    print(f'o usuario preferiu nao informar os dados')
except Exception as error:
    print(f'a causa do erro foi {error.__cause__}')
else:
    print(f'deu tudo certo, o resultado é {c:.1f}')
finally:
    print('tenha um bom dia')
"""
