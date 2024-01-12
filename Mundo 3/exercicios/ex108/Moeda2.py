def moeda(preço=0, moedar='R$'):
    return f'{moedar}{preço:>.2f}'.replace('.', ',')


def aumentar(preço, taxa):
    resultado = preço + (preço * taxa / 100)
    return resultado


def diminuir(preço, taxa):
    resultado = preço - (preço * taxa / 100)
    return resultado


def dobro(preço):
    resultado = preço * 2
    return resultado


def metade(preço):
    resultado = preço / 2
    return resultado
