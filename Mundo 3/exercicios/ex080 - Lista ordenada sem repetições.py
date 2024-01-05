'''Crie um programa onde o usuário posso digitar cinco valores
   numéricos e cadastre-os em uma lista, ja na posição correta
   de inserção(sem usar o sort()). No final, mostre a lista
   ordenada na tela'''

lista = []

for c in range(0, 5):
    n1 = int(input('digite um valor: '))
    if c == 0 or n1 > lista[-1]:             # se c == 0 ou n1 < que ultimo termo da lista damos um append
        lista.append(n1)
        print(f'adicionado na ultima posição')
    else:                                    # aqui começa a putaria
        pos = 0
        while pos < len(lista):              # enquanto 'pos' for menor que len(lista) que é o numero de termos da lista
            if n1 <= lista[pos]:             # se n1 <= o numero daquela posição, entao n1 assume o seu lugar
                lista.insert(pos, n1)
                print(f'adicionado na posição {pos}')
                break
            pos += 1
print(lista)
