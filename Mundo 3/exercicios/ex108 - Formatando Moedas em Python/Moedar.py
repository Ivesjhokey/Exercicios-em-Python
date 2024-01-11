def moeda(n=0):
    return f'R${n}'.replace('.', ',')


def metade(n):
    n1 = n / 2
    n1 = moeda(n1)
    return n1


def aumentar(n):
    n1 = (n / 100) * 10
    n2 = n + n1
    n2 = moeda(n2)
    return n2


def diminuir(n):
    n1 = (n / 100) * 10
    n2 = n - n1
    n2 = moeda(n2)
    return n2
