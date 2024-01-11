def resumo(n1=0, n2='', n3=0, n4=0):
    dobrado = dobro(n1, n2)
    triplicado = triplo(n1, n2)
    metadinha = metade(n1, n2)
    aum = ((n1/100) * n3)
    aumento = n1 + aum
    aumentocarai = aumentar(aumento, n2)
    dimi = ((n1/100) * n4)
    diminuiu = n1 - dimi
    diminuiucarai = diminuir(diminuiu, n2)

    return f'o dobro = {dobrado}\no triplo = {triplicado}\na metade = {metadinha}\ncom {n3}% de aumento fica {aumentocarai}\n'\
           f'com {n4}% de desconto fica {diminuiucarai}'


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


def metade(n, m=''):
    n1 = n / 2
    metadinha = moeda(n1, m)
    return metadinha


def aumentar(n, m=''):
    n2 = moeda(n, m)
    return n2


def diminuir(n, m=''):
    n2 = moeda(n, m)
    return n2
