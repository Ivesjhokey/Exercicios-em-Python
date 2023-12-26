'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500'''

soma = 0
contador = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        contador = contador + 1
        soma = soma + c
print(soma)
print(contador)

# alternativa melhor

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(soma)
print(contador)
