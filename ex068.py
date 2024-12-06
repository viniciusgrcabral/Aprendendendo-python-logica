import random

numero = contador = soma = 0

parouimparJogador = 0

parOuIMpar = ['P', 'I']

numeroPC = random.randint(0, 10)

while True:
    while parouimparJogador not in parOuIMpar:
        parouimparJogador = str(input('Digite par ou impar [P/I]: ')).upper()

    numero = int(input('Digite um número de 0 a 10: '))
    numeroPC = random.randint(0, 100)
    soma = numero + numeroPC

    
    if parouimparJogador == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {numero}, o computador jogou {numeroPC} deu Par')
            contador += 1
        else:
            print(f'Você jogou {numero} o computador jogou {numeroPC} deu Ímpar')
            break
    else:
        if soma % 2 != 0:
            print(f'Você jogou {numero}, o computador jogou {numeroPC} deu Ímpar')
            contador += 1
        else:
         print(f'Você jogou {numero} o computador jogou {numeroPC} deu Par')
         break

    

print(f'Você perdeu e obteve {contador} vitórias consecutivas')
    