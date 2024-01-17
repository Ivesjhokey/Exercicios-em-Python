def moeda(preço=0, moedar='R$'):
    return f'{moedar}{preço:>.2f}'.replace('.', ',')


def aumentar(preço, taxa, formato=False):
    resultado = preço + (preço * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preço, taxa, formato=False):
    resultado = preço - (preço * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def dobro(preço, formato=False):
    resultado = preço * 2
    return resultado if formato is False else moeda(resultado)


def metade(preço, formato=False):
    resultado = preço / 2
    return resultado if formato is False else moeda(resultado)


def resumo(preço=0, taxaa=0, taxar=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')


'''podemos usar muitas maneiras para usar o return, nesse caso vamos usar:
   return resultado if formato is False else moeda(resultado)
   mas poderiamos tambem utilizar:
   return resultado if not formato else Moeda5(resultado)
   nesse caso optei por utilizar todos da primeira maneira pois me convém'''
