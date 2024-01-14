'''Crie um programa onde o usuário digite uma expressão qualquer
   que use parênteses. Seu aplicativo deverá analisar se a expressão
   passada está com os parênteses abertos e fechados na ordem correta.'''

expre = input('digite sua expressão')
pilha = []
for c in expre:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressao e valida')
else:
    print('sua expressao e invalida')
