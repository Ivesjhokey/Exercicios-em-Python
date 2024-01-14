def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(a):
    while True:
        try:
            a = int(input(a))
        except (ValueError, TypeError):
            print(f'digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('o usuario preferiu nao digitar o valor')
            break
        else:
            return a


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m = \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32msua opção: \033[m')
    return opc
