import random

jogadaJogador = str(input('Digite pedra, papel ou tesoura: '))

jogadasPossiveis = ('pedra', 'papel', 'tesoura')

jogadaComputador = random.choice(jogadasPossiveis)

print(jogadaComputador)

while True:
    if jogadaJogador == 'pedra' and jogadaComputador == 'tesoura':
        print('Você ganhou!')
        break
    elif jogadaJogador == 'papel' and jogadaComputador == 'pedra':
        print('Você ganhou!')
        break
    elif jogadaJogador == 'tesoura' and jogadaComputador == 'papel':
        print('Você ganhou!')
        break
    elif jogadaJogador == jogadaJogador:
        print('Niguém ganhou!')
        continue
    else:
        print('Voce perdeu!')