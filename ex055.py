peso = float(input('Digite o peso: '))

menor = peso

maior = peso

for i in range (4):
    peso = float(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso


print('o maior peso é {} e o menor é {}'.format(maior, menor))