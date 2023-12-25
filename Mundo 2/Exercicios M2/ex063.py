# alternativa 1 jhokey

termo = int(input('digite o termo que voce quer: '))
primeiro = contador = 0
ultimo = 1
while contador < termo:
    primeiro = primeiro + ultimo
    print(primeiro)
    ultimo = ultimo + primeiro
    print(ultimo)
    termo = termo - 2
print('fim')

# alternativa 1 da net

t = int(input('Digite até onde ira o Fibonacci: '))
n = 0
while n < t:
    FN = (pow((1+pow(5, 1/2))/2, n) - pow((1-pow(5, 1/2))/2, n)) / (pow(5, 1/2))
    n = n+1
print('{:.0f}'.format(FN))

# alternativa 2 da net

n = int(input("Digite o n−ésimo termo da serie "))
cont = 0
inicial = 0
final = 1
primeiro = 0
num = 0

print(inicial)
print(final)
while cont <= n - 1:
    inicial = final + inicial
    print(inicial)
    final = inicial + final
    print(final)
    cont += 2
print("Fim")
