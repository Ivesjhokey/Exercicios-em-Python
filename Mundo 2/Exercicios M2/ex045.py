from random import choice

while True:
    jkp = ('pedra', 'papel', 'tesoura')  # poderia usar chave para fazer lista ou parentese para fazer strings#
    maquina = choice(jkp)
    player = input('|escolha pedra, papel ou tesoura para jogar|\n|(sair) para sair do jogo|: ')
    if player == 'sair':
        break
    elif player == maquina:
        print('empate')
    elif player == 'pedra' and maquina == 'tesoura':
        print('player venceu')
    elif player == 'papel' and maquina == 'pedra':
        print('player venceu')
    elif player == 'tesoura' and maquina == 'papel':
        print('player venceu')
    else:
        print('maquina venceu')
