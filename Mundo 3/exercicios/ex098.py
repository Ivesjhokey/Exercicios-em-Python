def contador(inicio, fim, passo):
    lista = []
    print('-=' * 15)
    for c in range(inicio, fim, passo):
        lista.append(c)
    if passo < 0:
        print(F'CONTAGEM DE {lista[0]} ATE {lista[-1]} DE {passo*-1} EM {passo*-1}')
    else:
        print(F'CONTAGEM DE {lista[0]} ATE {lista[-1]} DE {passo} EM {passo}')
    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print()
    print('-=' * 15)


contador(1, 11, 1)
contador(10, -1, -2)
print('agora é a sua vez, personaliza ai')
n1 = int(input('INICIO: '))
n2 = int(input('FIM: '))
n3 = int(input('PASSO: '))
if n2 > n1:
    n2 = n2+1
elif n2 < n1:
    n2 = n2-1
contador(n1, n2, n3)

# lendo os comentarios descobria  função abs, que basicamente significa modulo em matematica, ou seja:
# retorna um o valor que vc pediu sem o sinal de positivo ou negativo, logo so retorna valor positivo
# se seu sleep nao estiver funcionando direito, vc usa o comando flush=True para tirar o atraso bugado

"""# alternativa mulekada 1,    porem nessa alternativa, nao da o valor final
                                ou seja de 10 ate 0 de 1 em 1 da 1 no final e deveria dar zero
def contador(a, b, c):
    if c == 0:
        c += 1
        print('O número digitado não é válido. Será realizada a contagem com o PASSO = 1')
    if a > b and c > 0 or b > a and c < 0:
        c *= -1
    for d in range(a, b+1, c):
        print(f'{d}', end=' ')
    print()


contador(1, 10, 1)
contador(10, 0, -2)
contador(int(input('De: ')), int(input('Até: ')), int(input('Passo: ')))


# alternativa 2 mulekada            funciona tambem, porem esta sem as strings de contagem, que é oque da mais
                                    trabalho nessa porra.
                                        
def contador(inicio, fim, passo):       
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end = ' ')
    print()"""

# alternativa guanabara ta mto grande quero copiar nao tnc
