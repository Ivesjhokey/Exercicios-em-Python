# lendo numeros e descobrindo se sao primos ou nao, alternativa guanabara ou melhor alternativa

n1 = int(input('digite um valor: '))
n2 = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        n2 += 1
if n2 == 2:
    print('é primo')
else:
    print('nao é primo')
