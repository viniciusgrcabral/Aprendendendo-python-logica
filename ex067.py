numero = multiplicacao = contador = 0


while True:
    contador = 0
    numero = int(input('Digite o número para ver a tabuada: '))
    if numero < 0:
        break
    while contador <= 10:
        multiplicacao = numero * contador
        print(multiplicacao)
        contador += 1