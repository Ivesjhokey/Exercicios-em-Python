'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
   Se o valor digitado for ímpar, desconsidere-o'''

contador = 0
for c in range(1, 7):
    n1 = float(input('digite um valor: '))
    if n1 % 2 == 0:
        contador = contador + n1
print(contador)

# melhor alternativa

contador = 0
for c in range(1, 7):
    n1 = float(input('digite o {} valor: '.format(c)))
    if n1 % 2 == 0:
        contador = contador + n1
print('a soma dos numeros impares é {}'.format(contador))
