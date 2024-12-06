numero = contador = soma = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f'A quantidade de números foi {contador} e a soma é {soma}')