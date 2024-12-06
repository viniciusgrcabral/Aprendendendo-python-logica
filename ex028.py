import random

numero_aleatorio_do_pc = random.randint(0,5)

numero_do_usuario = int(input('Digite um número de 0 a 5 para adivinhar o número pensado pelo computador: '))

if numero_do_usuario == numero_aleatorio_do_pc:
    print ('Você acertou, venceu! O homem, a máquina, a besta enjaulada com ódio, ele vence, vence e vence')
else:
    print('Você errou, perdeu! Muito burro, filho!')   