# todos numeros pares de 1 a 50
for c in range(1, 51):
    if c % 2 == 0:
        print(c)

# melhor alternativa para ocupar menos espaço na memoria seria esta de baixo pois ele nao
# tem que comferir valores impares

for c in range(2, 51, 2):
    print(c)
