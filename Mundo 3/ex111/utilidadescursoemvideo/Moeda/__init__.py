def resumo(n1=0, n2='', n3=0, n4=0):
    dobrado = dobro(n1, n2)
    triplicado = triplo(n1, n2)
    metadinha = metaden(n1, n2)
    aum = ((n1/100) * n3)
    aumento = n1 + aum
    aumentocarai = moeda(aumento, n2)
    dimi = ((n1/100) * n4)
    diminuiu = n1 - dimi
    diminuiucarai = moeda(diminuiu, n2)

    return (f'o dobro = {dobrado}\no triplo = {triplicado}\na metade = {metadinha}\ncom {n3}% de aumento \n'
            f'fica {aumentocarai}\ncom {n4}% de desconto fica {diminuiucarai}')


def moeda(n=0, ativar=''):
    if 'sim' in ativar:
        return f'R${n}'.replace('.', ',')
    else:
        return f'R${n}'


def dobro(n, m=''):
    n1 = n * 2
    dobrado = moeda(n1, m)
    return dobrado


def triplo(n, m=''):
    n1 = n * 3
    triplicado = moeda(n1, m)
    return triplicado


def metaden(n, m=''):
    n1 = n / 2
    metadinha = moeda(n1, m)
    return metadinha

def metade(n, m=''):
    n1 = n / 2
    n1 = moeda(n1, m)
    return n1


def aumentar(n, m=''):
    n1 = (n / 100) * 10
    n2 = n + n1
    n2 = moeda(n2, m)
    return n2


def diminuir(n, m=''):
    n1 = (n / 100) * 10
    n2 = n - n1
    n2 = moeda(n2, m)
    return n2







def moeda(preço=0, moedar='R$', formato=False):
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


def resumo(preço=0, taxaa=0, taxar=0, formato=False):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço, formato)}')
    print(f'Metade do preço: \t{metade(preço, formato)}')
    print(f'Dobro do preço: \t{dobro(preço, formato)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, formato)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, formato)}')


'''podemos usar muitas maneiras para usar o return, nesse caso vamos usar:
   return resultado if formato is False else moeda(resultado)
   mas poderiamos tambem utilizar:
   return resultado if not formato else Moeda(resultado)
   nesse caso optei por utilizar todos da primeira maneira pois me convém'''
