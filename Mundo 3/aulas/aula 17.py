"""#  falando sobre listas
#  as listas sao mutaveis e podemos adicionar elementos nela
#  exemplo:

lanche = ['arroz','cocacola', 'feijao', 'carne', 'salada']
lanche[3] = 'cocacola'
print(lanche)

#  para adicionar elementos na lista, e nao apenas substituir, devemos usar o 'append' ou 'insert'

lanche.append('terere')  # adiciona um valor ou string a variavel lanche, porem adiciona no final
print(lanche)

lanche.insert(0, 'cigarro')  # adiciona na posição 0 o cigarro, que é a primeira posição da lista
print(lanche)

# para apagar algum elemento da lista pode-se utilizar:

del lanche[3]
lanche.pop(3)  # se usarmos o pop e nao indicarmos qual é o termo a ser excluido, ele excluira o ultimo da lista
lanche.remove('cocacola')  # o mesmo acontece para o remove se houver mais de um elemento igual na lista

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(0, 10))  # fazendo uma lista ja organizada
print(valores)

valores10 = [8, 12, 41, 3, 23, 6]
valores10.sort()  # sort para organizar
print(valores10)
print(sorted(valores10))  # sorted para classificar

valores = [8, 12, 41, 3, 23, 6]
print(valores10.sort(reverse=True))  # aqui ira dar erro

valores = ['pao', 'mortandela', 'leite', 'queijo']
valores.sort(reverse=True)    # colocou em ordem e depois alinhou de traz para frente, nao da para printar,
print(valores)                # tem que atribuir primeiro

valores = [0, 1, 2, 3, 4]
print(valores)
print(len(valores))

num = [2, 5, 9, 1]  # lista
num[2] = 3          # num[2] recebeu 3 deixando [2,5,3,1]
print(num)

num.append(7)       # adiciona o numero 7 na ultima chave da lista
print(num)

num.sort()          # organiza a lista em ordem
print(num)

num.sort(reverse=True)  # organiza a lista em ordem de traz para frente
print(num)

num.insert(2, 0)    # insere na posição 2 numero 0
print(num)

num.pop()           # apaga o termo da ultima chave
print(num)

num.pop(0)          # apaga o termo selecionado
print(num)

num.remove(2)       # apaga o primeiro elemento 2 que encontrar
print(num)

# num.remove(4)  se o valor nao estiver na lista ira dar erro no codigo, e pra isso utilizamos o if para verificar

if 4 in num:
    num.remove(4)
    print(num)
else:
    print('nao existe esse valor na lista')

# ha duas maneiras de criar uma lista: valores = list() ou valores = []

valores = []
valores.append(4)
valores.append(8)
valores.append(2)
for v in valores:
    print(f'{v}...')

for c, v in enumerate(valores):
    print(f'na posição {c}, encontrei o valor {v}...')
print('cheguei ao final da lista')

# tambem podemos utilizar o for para adicionar termos dentro da lista

valores = []
for c in range(0, 5):
    valores.append(int(input('digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c}, encontrei o valor {v}...')
print('cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a               # b = a, significa que b recebe a, mas tambem que existe uma ligação entre eles
b[2] = 9            # por isto quando demos b[2] = 9, a lista A tambem recebeu o valor 9, pois a e b estao ligados
print(a)
print(b)

a = [2, 3, 4, 7]
b = a[:]               # nesse caso o comando esta pedindo apenas os elementos do inicio ao fim de A
b[2] = 9               # e nao esta ligando eles entre a = b diretamente.
print(a)               # e por isto quando demos b[2] = 9, a lista B recebe o 9, porem a lista A nao.
print(b)"""


