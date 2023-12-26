'''Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50'''

for c in range(1, 51):
    if c % 2 == 0:
        print(c)

# melhor alternativa para ocupar menos espaço na memoria seria esta de baixo pois ele nao
# tem que comferir valores impares

for c in range(2, 51, 2):
    print(c)
