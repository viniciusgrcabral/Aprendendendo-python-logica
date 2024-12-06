import time


numero1 = int(input('Digite o primeiro número: '))

numero2 = int(input('Digite o segundo número: '))

nova_ação = 0


while nova_ação != 5:
    time.sleep(2)
    print('Digite [1] para somar os números\n[2] para múltiplicar\n[3] para descobrir o maior entre eles\n[4] para digitar novos números\n[5] para sair do programa')
    time.sleep(2)
    nova_ação = int(input())
    time.sleep(2)
    if nova_ação == 1:
        soma = numero1 + numero2
        print(soma)
    elif nova_ação == 2:
        multiplicação = numero1 * numero2
        print(multiplicação)
    elif nova_ação == 3:
        maior = max(numero1, numero2)
        print(maior)
    elif nova_ação == 4:
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))


