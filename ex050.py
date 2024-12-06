somatorio = 0

for i in range (0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        somatorio += numero

print('O somatorio é {}'.format(somatorio))