def resumo(n1=0, n2=True):
    moedar(metade(n1), n2)
    moedar(dobro(n1), n2)
    moedar(triplo(n1), n2)
    moedar(aumentar(n1), n2)
    moedar(diminuir(n1), n2)


def moedar(n=0, n2=False):
    if n2:
        return print(f'R${n}'.replace('.', ','))
    else:
        return print(f'R${n}')


def dobro(n):
    n1 = n * 2
    return n1


def triplo(n):
    n1 = n * 3
    return n1


def metade(n):
    n1 = n / 2
    return n1


def aumentar(n):
    n1 = (n / 100) * 10
    n2 = n + n1
    return n1


def diminuir(n):
    n1 = (n / 100) * 10
    n2 = n - n1
    return n1


def maior(*n1):
    mai = 0
    for c in range(0, len(n1)):
        if c == 0:
            mai = n1[c]
        elif n1[c] > mai:
            mai = n1[c]
    return mai


def menor(*n1):
    men = 0
    for c in range(0, len(n1)):
        if c == 0:
            men = n1[c]
        elif n1[c] < men:
            men = n1[c]
    return men


def maioremenor(*n1):
    men = 0
    mai = 0
    for c in range(0, len(n1)):
        if c == 0:
            mai = n1[c]
            men = n1[c]
        elif n1[c] > mai:
            mai = n1[c]
        elif n1[c] < men:
            men = n1[c]
    return print(f'o maior valor digitado foi o {mai}\no menor valor digitado foi o {men}')
