"""Reescreva a função leiaInt() que fizemos no desafio 104
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


# alternativa 1 jhokey

def leiaint(a):
    while True:
        try:
            a = int(input(a))
        except:
            print(f'infelizmente tivemos um erro')
            continue
        else:
            return print(f'o numero digitado foi {a}')


def leiafloat(msg):
    while True:
        try:
            msg = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO, digite um numero valido')
            continue
        except KeyboardInterrupt:
            print('o usuario preferiu nao digitar os valores')
            break
        else:
            print(f'o valor digitado foi {msg}')
        finally:
            return print('fim de programa, tenha um bom dia')


leiaint('digite um numero: ')
leiafloat('digite um numero: ')

"""
# alternativas guanabara


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
            return print(f'o numero digitado foi {a}')
        finally:
            return print('fim de programa, tenha um bom dia')


leiaint('digite um numero: ')


def leiafloat(msg):
    while True:
        try:
            msg = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO, digite um numero valido')
            continue
        except KeyboardInterrupt:
            print('o usuario preferiu nao digitar os valores')
            break
        else:
            print(f'o valor digitado foi {msg}')
        finally:
            return print('fim de programa, tenha um bom dia')


n1 = (leiafloat('digite um numero: '))
"""
