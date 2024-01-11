def moeda(n=0, ativar=''):
    if 'sim' in ativar:
        return f'R${n}'.replace('.', ',')
    else:
        return f'R${n}'


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
