"""Crie um programa que tenha uma função fatorial() que receba
   dois parâmetros: o primeiro que indique o número a calcular
   e o outro chamado show, que será um valor lógico(opcional) indicando
   se será mostrado ou não na tela o processo de cálculo do fatorial."""

def fatorial(num=1, show=False):
    """
    :parametro num: num recebe o valor de n e se nao receber sera = 1
    :parametro show: show recebe falso ou verdadeiro para mostrar o processo do fatorial
    :return: return retorna um valor para o print que pedi mas poderia ser return para uma variavel
    como por exemplo n1 = fatorial(n, show=True) e o valor retornaria para n1
    depois é so printar n1 que ja esta com o valor dentro, obs, apenas o valor, pois o processo
    é mostrado apenas durante o for do local, obs2: posso estar enganado pq to com sono prakaralho
    """
    
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f

n = int(input('digite um numero: '))
print(f'{fatorial(n, show=True)}')
help(fatorial)
