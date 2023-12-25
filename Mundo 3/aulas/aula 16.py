'''lanche = 'hamburguer'  # variavel simples
print(lanche)'''

'''lanche1 = ('hamburguer', 'suco')  # variavel composta com 2 ou mais itens
print(lanche1)
print(lanche1[0])
print(lanche1[1])'''

'''lanche2 = ('hamburguer', 'suco', 'pudim', 'tetas')
print(lanche2[-1]), print(lanche2[0])
print(lanche2[-2]), print(lanche2[1])
print(lanche2[-3]), print(lanche2[2])
print(lanche2[-4]), print(lanche2[3])'''

'''lanche3 = ('hamburguer', 'suco', 'pudim', 'tetas')
print((lanche3[-1]), (lanche3[0]))
print((lanche3[-2]), (lanche3[1]))
print((lanche3[-3]), (lanche3[2]))
print((lanche3[-4]), (lanche3[3]))

print(lanche3[0:3])  # no fatiamento sempre o ultimo termo é ignorado
print(lanche3[0:4])  # nesse caso nao tem o termo 4 mas ele ignora o 4 entao vai somente ate o 3
print(lanche3[0:])  #tambem daria pra deixar vago significando que vai ate o fim
print(lanche3[:2])
print(lanche3[-2:])  # segundo termo de traz para frente ate o final'''

'''lanche3 = ('hamburguer', 'suco', 'pudim', 'tetas')
print(len(lanche3))  # vai ler quantos termos tem dentro de lanche3
for c in range(0, len(lanche3)):  # vai de 0 ate 4 que é o numero de termos de 'len(lanche3)'
    print(lanche3)

for c in range(0, len(lanche3)):  # vai de 0 ate 4 que é o numero de termos de 'len(lanche3)' e por ignorar o ultimo termo foi de 0 ate 3 mas apareceu todos pois começa em 0, ficando 0,1,2,3 que tambem da 4 elementos
    print(c)

for c in lanche3:  # vai de 0 ate 4 mas ira printar todos os elementos dentro de lanche3
    print(lanche3)

for c in lanche3:  # vai de 0 ate 4 mas printando 1 elemento por vez dentro de lanche
    print(c)'''

#lanche3 = ('hamburguer', 'suco', 'pudim', 'tetas')
#for c in range(0, len(lanche3)):
    #print(f'eu vou comer {lanche3[c]}')

#for c in lanche3:
#    print(f'eu vou comer {c}')

#for c, comida in enumerate(lanche3):
    #print(comida, c)

'''comida = ('arroz', 'feijão', 'carne', 'farinha')
print(sorted(comida))
print(comida)
n1 = sorted(comida) #sorted serve para colocar em ordem
print(n1)'''

'''a = (7, 5, 4, 6)
b = (1, 3, 5)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5))  # quantos 5 tem em 'c'
print(c.index(5))  # me mostre em que posição esta o 5 dentro de 'c'
print(c.index(5, 2))  # me mostre onde esta o 5, a partir do 2, desconsiderando o termo 0 e o termo 1'''

'''pessoa = 'ives', 22, 'm', 83.0
print(pessoa)'''

'''pessoa = 'ives', 22, 'm', 83.0
del(pessoa)
print(pessoa)'''

'''pessoa = ('ives', 22, 'm', 83.0)
pessoa = 'ivesapenas'
print(pessoa)'''

'''pessoa = ('ives', 22, 'm', 83.0)
del(pessoa)
pessoa = 'ivesapenas'
print(pessoa)'''

"""pessoa = ('ives', 22, 'm', 83.0)
pessoa[2] = 'mn'
print(pessoa) #nao podemos fazer isso pois uma tupla nao pode ser alterada"""
