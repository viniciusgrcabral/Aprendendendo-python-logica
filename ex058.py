import random

numeroJogador = 0

contadorTentativa  = 0

numeroComputador = random.randint(1, 10)

while numeroJogador != numeroComputador:
    numeroJogador = int(input('Digite um número: '))
    contadorTentativa += 1
    if numeroJogador == numeroComputador:
        print('Acertou!!')
        print('Seu número de númerode tentativas foi {}'.format(contadorTentativa))
